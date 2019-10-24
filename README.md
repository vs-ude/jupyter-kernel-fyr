# Fyr kernel for Jupyter

This is a Jupyter notebook kernel for the [Fyr](http://fyr.vs.uni-due.de) language.
It compiles and executes code written in the notebook and prints all generated output.

## Manual installation

### Requirements

* jupyter
* python 3
  * [python-magic](https://pypi.org/project/python-magic/)
* [fyr](https://github.com/vs-ude/fyr)

### Step-by-step

* `git clone` this repo
* `sudo jupyter kernelspec install jupyter-fyr-kernel` (as root, otherwise you have to change path in kernel.json)
* `jupyter notebook`

Enjoy!

## Updating

* Either go to `/usr/local/share/jupyter/kernels/jupyter-fyr-kernel/` and type `git pull` 
* or type `git pull` in the directory where you initially cloned this repo. After that `cd ..` and type `sudo jupyter kernelspec install jupyter-fyr-kernel --replace`

## Credits

The initial implementation of this module was done by [Roman Wagner](https://github.com/rojnwa) as part of his bachelors thesis.

