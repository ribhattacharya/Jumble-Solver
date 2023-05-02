# Jumble-Solver
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/markdown-include/badges/version.svg)](https://anaconda.org/conda-forge/markdown-include)

A solver for the game 'Jumble'. Given a dictionary and any word, this program returns the possible anagrams and sub-anagrams. For any clarifications, contact me (Rishabh Bhattacharya) at [ribhattacharya@ucsd.edu](mailto:ribhattacharya@ucsd.edu). Happy Jumbling!

## Working instructions
### Create conda environment (Optional)
To create a conda environment, run this in the terminal (assuming you have [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system).

    conda env create -f environment.yml

This will create a conda environment named `jupyter_solver` on your system, installing the required packages.

**NOTE**: You could completely skip this step, since this program only uses native python packages, and nothing extra. However, this is recommended to keep things consistent and future proofing.

### Run script
To run the script, enter the following in your command line

    cd ~/path/to/Jumble-Solver
    python3 jumble_solver.py YOUR_DICTIONARY.txt YOUR_WORD

For example, given the (default) dictionary `corncob_lowercase.txt` and the (default) word `dog`, we would run
    
    python3 jumble_solver.py corncob_lowercase.txt dog


Since these are default values, you could also run the same by entering

    python3 jumble_solver.py

Running either of the two commands above would give, this output.

    ------------------------------------------------------------------------------------
    -> Sorting input dictionary since it wasn't already.

    Sub-anagrams found:     16
    Valid sub-anagrams:     4
    Valid sub anagrams are: ['do', 'dog', 'go', 'god']
    Time elapsed:           1.52 ms
    ------------------------------------------------------------------------------------

## Repo structure

- **environment.yml**: Conda environment setup file.
- **constants.py**: Constant values like word file diectory. 
- **jumble_solver.py**: Main interface script for this problem.  
- utils/
    - **utils.py**: Contains various utility functions.
    - **file_utils.py**: File manipulation functions.
- scripts/
    - **binary_search.py**: Binary search algorithm.
    - **sub_anagrams.py**: Compute all possible + valid sub-anagrams.
- word_lists/
    - **mit_10k.txt**: [MIT 10K word list](https://www.mit.edu/~ecprice/wordlist.10000) (10K words)
    - **corncob_lowercase.txt** (default): [Corncob lowercase world list](http://www.mieliestronk.com/corncob_lowercase.txt) (58K words)
    
## Features
1. Checks if dictionary file exists and if input word contains alphabets, else raises error.
2. Checks if the dictionary is sorted, sorts it if it's not already. This helps with the binary search.
3. Handles upper/lower case and combinations by converting the dictionary and input word to lowercase for uniformity across permutations and search.
4. Checks if input word has duplicate alphabets, since this adds duplicate sub-anagrams. Removes duplicates accordingly.
5. Since we are performing binary search across the sorted dictionary, presence of duplicate words in the dictionary does not affect us since we don't care about the order of occurence, but only if a word is present or not. This saves us the computation time for duplicate removal.
## Algorithm and complexity analysis
If dictionary (length $m$) is **sorted** and word (length $n$) contains **no repeated letters**, 
- Power set: $O(2^n)$
- Permutations: $O(n!)$ for each element in the power set. 

Thus we have $O(2^n \times n!)$ for computing all the anagrams. Also, binary search would take $O(\log m)$. Thus we have a final time complexity of 
$$\boxed{O(2^n \times n!) + O(\log m)}$$

If dictionary (length $m$) is **sorted** and word (length $n$) contains **repeated letters**, we use Python's `set()` for duplicate removal. Since it works in $O(1)$ for each element, we have additional $O(2^n) + O(n!)$ complexity for the power set and its permutations. Thus the time complexity in this case is
$$O(2^n \times n!)+ O(2^n) + O(n!) + O(\log m) \approx \boxed{O(2^n \times n!) + O(\log m)}$$

If dictionary (length $m$) is **not sorted** and word (length $n$) contains **no repeated letters**, we use Python's `.sort()` for sorting the dictionary, which works in $O(m \log m)$ (internal implementation based on Timsort). Thus the time complexity in this case is
$$\boxed{O(m \log m) + O(2^n \times n!) + O(\log m)}$$

Finally, if dictionary (length $m$) is **not sorted** and word (length $n$) contains **repeated letters**, we have 
$$O(m \log m) + O(2^n \times n!)+ O(2^n) + O(n!) + O(\log m) \approx \boxed{O(m \log m) + O(2^n \times n!) + O(\log m)}$$

We can summarize the results as follows,

| Case (dictionary, word)   	| Best 	| Average                                      	| Worst 	|
|---------------------------	|------	|----------------------------------------------	|-------	|
| Sorted, non-repeating     	|      	| $O(2^n \times n!) + O(\log m)$               	|       	|
| Sorted, repeating         	|      	| $O(2^n \times n!) + O(\log m)$               	|       	|
| Non-sorted, non-repeating 	|      	| $O(m \log m) + O(2^n \times n!) + O(\log m)$ 	|       	|
| Non-sorted, repeating     	|      	| $O(m \log m) + O(2^n \times n!) + O(\log m)$ 	|       	|

## Future improvements
1. If input dictionary is not sorted, we can sort and save it for future use. Since the dictionary is not supposed to be changed frequently, this would be a one-time computation.

