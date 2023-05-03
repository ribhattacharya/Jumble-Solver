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
    - **sub_anagrams.py**: Compute all possible + valid sub-anagrams.
- word_lists/
    - **mit_10k.txt**: [MIT 10K word list](https://www.mit.edu/~ecprice/wordlist.10000) (10K words)
    - **corncob_lowercase.txt** (default): [Corncob lowercase world list](http://www.mieliestronk.com/corncob_lowercase.txt) (58K words)
    
## Features
1. Checks if dictionary file exists and if input word contains alphabets, else raises error.
2. Dictionary is implemented as a hashset, so sorting is not needed and duplicate elements are rejected inherently.
3. Handles upper/lower case and combinations by converting the dictionary and input word to lowercase for uniformity across permutations and search.
4. The sub-anagrams are also stored as hashsets. Thus even if input word has duplicate alphabets, the sub-anagrams are unique.
5. Search takes $O(1)$ complexity on average due to the `set` inplementation.

## Algorithm and complexity analysis
I used Python's hashset `set()` for this implementation. Insertion in both `set()` and `List[]` take $O(1)$ time. However, the current implementation (using `set()`) improves upon the previous build (using `List[]` and binary search) majorly due to two factors,

1. Search in a `set()` takes $O(1)$ time, and it is not required to be sorted. In contrast, binary-search in a sorted `List[]` takes $O(\log m)$ time, and the sorting (if dictionary is unsorted) itself takes $O(m\log m)$ time. Both end up taking the same space $O(m)$.
2. If the input word has repeated characters, there would be duplicate permutations when adding in a `List[]`. Rather than trying to remove duplicates seperately, adding elements in a `set()` ensures that no duplicates are added. Both methods take $O(1)$ time to append each element, but we achieve duplicate removal as a bonus by using `set()`.

If dictionary has $m$ words and input word has $n$ characters, then 
- **Creating dictionary**: Time: $O(m)$, Space: $O(m)$
    - Traversal over dictionary.txt file: $O(m)$
    - Adding to set: $O(1)$ for each element in dictionary
    - **Total time**: $O(m \times 1) = O(m)$
    - **Total space**: $O(m)$
- **Computing all possible sub-anagrams**:Time: $O(\lfloor n! \times e\rfloor)$, Space: $O(\lfloor n! \times e\rfloor)$
    - Permuting _r_ letters at a time: $O({}^n P_r)$
    - Adding to set: $O(1)$ for each element
    - **Total time**: $O({}^n P_n + {}^n P_{n-1} + \cdots {}^n P_1 + {}^n P_0) = O(\sum_{r=0}^n {}^n P_r) = O(\lfloor n! \times e\rfloor)$. See this [link](https://math.stackexchange.com/questions/161314/what-is-the-sum-of-following-permutation-series-np0-np1-np2-cdots-npn) for the derivation.
    - **Total space**: $O(\lfloor n! \times e\rfloor)$. 
- **Search for valid sub-anagrams**: Time: $O(1)$, Space: $O(k)$ where $k$ is the number of valid matches in the dictionary.
    - Search for a sub-anagram in set of words (dictionary): $O(1)$
    - **Total time**: $O(1)$
    - **Total space**: $O(k)$

Thus given $m$ words in the dictionary, input word of length $n$, and $k$ sub-anagram matches in the dictionary, we have
| Step # 	| Step description                    	| Time complexity                               	| Space complexity                              	|
|--------	|-------------------------------------	|-----------------------------------------------	|-----------------------------------------------	|
| 1      	| Creating dictionary                 	| $O(m)$                                        	| $O(m)$                                        	|
| 2      	| Computing all possible sub-anagrams 	| $O(\lfloor n! \times e\rfloor)$               	| $O(\lfloor n! \times e\rfloor)$               	|
| 3      	| Search for valid sub-anagrams       	| $O(1)$                                        	| $O(k)$                                        	|
|        	| **Total**                           	| $O(m) + O(\lfloor n! \times e\rfloor) + O(1)$ 	| $O(m) + O(\lfloor n! \times e\rfloor) + O(k)$ 	|

## Future functionality improvements
1. If we have repeating characters in the input word, the duplicate permutations are currently computed before attempting to add into the `set()`. A further optimization could be to skip this computation itself.