"""
Compute all possible sub-anagrams and valid sub-anagrams from the dictionary.
"""

from itertools import permutations
from typing import Any

class computeSubAnagrams:
    def __init__(self, dictionary: set[str], word: str) -> None:
        """
        DESC: Helper class containing methods to return sub-anagrams for a word.

        INPUTS: 
        word (type str): Input word/string.
        dictionary (type set[str]): Word list/dictionary.
        """
        self.word = word
        self.dictionary = dictionary
        self._allSubAnagrams = set()
        self._validSubAnagrams = set()
    
    def _all_sub_anagrams(self) -> None:
        """
        DESC: Computes the sub-anagrams for the given word.

        EXAMPLE: For input word 'dog', permutations of all anagrams are 
        {'', 'dg', 'odg', 'dgo', 'god', 'g', 'do', 'gdo', 'ogd', 'gd', 'od', 'o', 'd', 'og', 'go', 'dog'}.
        """

        # Permute the word by taking 0,1,2...n letters at a time.
        for i in range(len(self.word)+1):
            perms = permutations(self.word, i)

            # Append the permutations to the list.
            for perm in perms:
                self._allSubAnagrams.add(''.join(perm))

    def _valid_sub_anagrams(self) -> None:
        """
        DESC: Computes the valid sub-anagrams by searching each sub-anagram in the dictionary.

        OUTPUTS:
        validSubAnagrams (type set[str]): Valid sub-anagrams of the input word that are present in the chosen dictionary.

        EXAMPLE: For input {'', 'dg', 'odg', 'dgo', 'god', 'g', 'do', 'gdo', 'ogd', 'gd', 'od', 'o', 'd', 'og', 'go', 'dog'},
        valid sub-anagrams are {'do', 'dog', 'go', 'god'}.
        """

        # Search each possible sub-anagram in dictionary, and append if found.
        for subAnagram in self._allSubAnagrams:
            if subAnagram in self.dictionary:
                self._validSubAnagrams.add(subAnagram)
        
        return self._validSubAnagrams

    def compute(self) -> set[str]:
        """
        DESC: Returns the valid sub-anagrams by calling required methods.

        OUTPUTS:
        (type set[str]): Valid sub-anagrams of the input word that are present in the dictionary.

        EXAMPLE: For input word 'dog', valid sub-anagrams are {'do', 'dog', 'go', 'god'}.
        """
        self._all_sub_anagrams()
        return self._valid_sub_anagrams()
    
    def size(self, identifier: str = 'valid') -> int:
        """
        DESC: Returns the number of all sub-anagrams or only valid sub-anagrams.

        INPUT:
        indentifier (type str): 'all' or 'valid' (default).
        
        OUTPUTS:
        (type int): Number of sub-anagrams for chosen identifier.
        """
        assert identifier in ['all', 'valid'], AssertionError(f"identifier should be 'all' or 'valid', got:{identifier}")
        
        if identifier == 'all':
            return len(self._allSubAnagrams) 
        
        return len(self._validSubAnagrams)
    
    def get_sub_anagrams(self, identifier: str = 'valid') -> set[str]:
        """
        DESC: Returns all sub-anagrams or only valid sub-anagrams.

        INPUT:
        indentifier (type str): 'all' or 'valid' (default).
        
        OUTPUTS:
        (type set[str]): Sub-anagrams for chosen identifier.
        """
        assert identifier in ['all', 'valid'], AssertionError(f"identifier should be 'all' or 'valid', got:{identifier}")
        
        if identifier == 'all':
            return self._allSubAnagrams
        
        return self._validSubAnagrams