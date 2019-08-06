# Fyr kernel for Jupyter

## Manual installation

Make sure you have the following requirements installed:
  * jupyter
  * python 3
  * fyr (https://github.com/vs-ude/fyr)

### Step-by-step:

 * `git clone` this repo
 * `jupyter kernelspec install jupyter-fyr-kernel` (as root, otherwise you have to change path in kernel.json)
 * `jupyter notebook`. Enjoy!

## Updating

* Either go to `/usr/local/share/jupyter/kernels/jupyter-fyr-kernel/` and type `git pull` 
* or type `git pull` in the directory where you initially cloned this repo. After that `cd ..` and type `jupyter kernelspec install jupyter-fyr-kernel --replace`

## Contributing

I'm still struggling with the path inside of kernel.json. I don't really wanna have the need of installing the
kernel as root but I cannot get it to work otherwise. People would have to add
$HOME/.local/share/jupyter/kernels/jupyter-fyr-kernel to their path.

In addition I have to say that this is still a very bare boned kernel. It's just a wrapper kernel around python so some
stuff is not supported (like links between different cells). This is just a prototype to show that Fyr can have
it's own Jupyter Kernel!

This is also part of my bachelors thesis.
