"""
Return valid sub-anagrams from the dictionary.
"""

from itertools import permutations
    
def sub_anagrams(dictionary: set[str], word: str) -> None:
    """
    DESC: Returns the valid sub-anagrams by computing each possible sub-anagram and checking it in the dictionary.

    INPUTS: 
    dictionary (type set[str]): Word list/dictionary.
    word (type str): Input word/string.

    OUTPUTS:
    subAnagrams (type set[str]): Valid sub-anagrams of the input word that are present in the given dictionary.

    EXAMPLE: For input word 'dog' and dictionary 'corncob_lowercase.txt', output is {'do', 'dog', 'go', 'god'}.
    """
    
    _validSubAnagrams = set()    # Store valid sub-anagrams here
    
    # No. of all possible permutations/anagrams = floor(n! x e)
    # https://math.stackexchange.com/questions/161314/what-is-the-sum-of-following-permutation-series-np0-np1-np2-cdots-npn
    _len_allSubAnagrams = 0
    
    # Permute the word by taking 0,1,2...n letters at a time.
    for i in range(len(word)+1):
        perms = permutations(word, i)

        # Store permutations only if they are in dictionary.
        for perm in perms:
            _len_allSubAnagrams += 1
            
            subAnagram =  ''.join(perm)
            if subAnagram in dictionary:
                _validSubAnagrams.add(subAnagram)
    
    return _validSubAnagrams, len(_validSubAnagrams), _len_allSubAnagrams