import os.path as op
import tempfile
import subprocess
from subprocess import run, PIPE
import magic
import base64


def exec_fyr(code):
    """Compile, execute Fyr code, and return the standard output."""

    # Create temp folder which gets deleted afterwards
    with tempfile.TemporaryDirectory() as tmpdir:

        # Define source and executable filenames
        source_path = op.join(tmpdir, "temp.fyr")
        program_path = op.join(tmpdir, "temp")

        # Write code to the Fyr file
        with open(source_path, "w") as f:
            f.write(code)

        # Compile the Fyr code into an executable and save stdout/stderr
        res = run(["fyrc", "-n", source_path], stdout=PIPE, stderr=subprocess.STDOUT)

        # Execute program depending on returncode and return output or stdout+stderr
        # Check if Image in Mimetype, if yes: convert to png (because Jupyter can display PNG)
        # And return base64 encoded png
        # 0 = text, 1 = error, 2 = image
        if res.returncode == 0:
            output = run([program_path], stdout=PIPE)
            if ("image" in magic.from_buffer(output.stdout, mime=True)):
                png = run(["convert", "-", "png:-"], input=output.stdout, stdout=PIPE)
                return [base64.b64encode(png.stdout), 2]
            else:
                return [output.stdout, 0]
        else:
            return [res.stdout.decode("utf-8"), 1]


"""Fyr wrapper kernel"""
from ipykernel.kernelbase import Kernel


class FyrKernel(Kernel):

    # Kernel information
    implementation = "Fyr"
    implementation_version = "1.1"
    language = "fyr"
    language_version = "0.1.4"
    language_info = {
        "name": "fyr",
        "mimetype": "text/plain",
        "file_extension": ".fyr",
        "codemirror_mode": "go",
    }
    banner = "Fyr kernel"

    def do_execute(
        self, code, silent, store_history=True, user_expressions=None, allow_stdin=False
    ):
        """Function which is run when a code cell is executed"""
        
        # Run Fyr code and get output
        output = exec_fyr(code)

        if not silent:
            # Send back result to frontend depending on returnvalue of exec_fyr
            # 0 = text, 1 = error, 2 = image
            if output[1] == 0:
                stream_content = {"name": "stdout", "text": output[0]}
                msg_type = "stream"
            elif output[1] == 2:
                stream_content = {"data": {"image/png": output[0]}}
                msg_type = "display_data"
            else:
                stream_content = {"name": "stderr", "text": output[0]}
                msg_type = "stream"

            self.send_response(self.iopub_socket, msg_type, stream_content)

        return {
            "status": "ok",
            # Base class increments execution count
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }


if __name__ == "__main__":
    from ipykernel.kernelapp import IPKernelApp

    IPKernelApp.launch_instance(kernel_class=FyrKernel)
