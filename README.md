# :city_sunset: Fyr kernel for Jupyter

## Manual installation

Make sure you have the following requirements installed:
* jupyter
* python 3
  * [python-magic](https://pypi.org/project/python-magic/)
* [fyr](https://github.com/vs-ude/fyr)

### Step-by-step:

* `git clone` this repo
* `sudo jupyter kernelspec install jupyter-fyr-kernel` (as root, otherwise you have to change path in kernel.json)
* `jupyter notebook`. Enjoy!

## Updating

* Either go to `/usr/local/share/jupyter/kernels/jupyter-fyr-kernel/` and type `git pull` 
* or type `git pull` in the directory where you initially cloned this repo. After that `cd ..` and type `sudo jupyter kernelspec install jupyter-fyr-kernel --replace`

---

This is part of my bachelors thesis.
