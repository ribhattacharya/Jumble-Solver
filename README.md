# Jumble-Solver
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/markdown-include/badges/version.svg)](https://anaconda.org/conda-forge/markdown-include)

A solver for the game 'Jumble'. Given a dictionary and any word, this program returns the possible anagrams and sub-anagrams. 

## TODO (update finally before submitting) Create conda environment 
To create a conda environment, run this in the terminal (assuming you have [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system).

    conda env create -f environment.yml

This will create a conda environment named `jupyter_solver` on your system, installing the required packages.

## Run script
To run the script, enter the following in your command line

    python3 jumble_solver.py YOUR_WORD_LIST.txt YOUR_WORD

For example, given the (default) word list `corncob_lowercase.txt` and the (default) word `dog`, we would run
    
    python3 jumble_solver.py corncob_lowercase.txt dog


Since these are default values, you could also run the same by entering

    python3 jumble_solver.py

## TODO File info


For any clarifications, contact me (Rishabh Bhattacharya) at [ribhattacharya@ucsd.edu](mailto:ribhattacharya@ucsd.edu). Happy Jumbling!
