import os
import os.path as op
import tempfile

# Import 'getouput()' function provided by IPython
# Allows to do system calls from Python
from IPython.utils.process import getoutput


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

        # Compile the Fyr code into an executable
        os.system("fyrc -n {}".format(source_path))

        # Execute program and return output
        return getoutput(program_path)


"""Fyr wrapper kernel"""
from ipykernel.kernelbase import Kernel


class FyrKernel(Kernel):

    # Kernel information
    implementation = "Fyr"
    implementation_version = "1.0"
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

        if not silent:
            # Run Fyr code and get output
            output = exec_fyr(code)

            # Send back result to frontend
            stream_content = {"name": "stdout", "text": output}
            self.send_response(self.iopub_socket, "stream", stream_content)

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
