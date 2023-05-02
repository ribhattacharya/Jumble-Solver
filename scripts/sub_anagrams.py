from itertools import permutations
from .binary_search import binary_search

class computeAllSubAnagrams:
    def __init__(self, word: str) -> None:
        """
        DESC: Helper class containing methods to return all possible sub-anagrams for a word.

        INPUTS: 
        word (type str): Input word/string.
        """
        self.word = word

        # Check for duplicates in the input word, as it causes duplicate permutations.
        self.hasDuplicate = len(set(word)) < len(word)

    def __powerset(self) -> list[str]:
        """
        DESC: Computes the powerset of a given string.

        OUTPUTS: 
        wordPowerSet (type list[str]): Power set of the input word.

        EXAMPLE: For input word 'dog', power set is ['', 'd', 'o', 'do', 'g', 'dg', 'og', 'dog'].
        """

        wordPowerSet = ['']

        # Take each character one-by-one in the word, then append it to each element in the power set.
        for c in self.word:
            for i in range(len(wordPowerSet)):
                wordPowerSet.append(wordPowerSet[i]+c)
        
        if self.hasDuplicate:       # Only return unique anagrams
            wordPowerSet = list(set(wordPowerSet))
        
        return wordPowerSet
    
    def __permutations(self, wordPowerSet) -> list[str]:
        """
        DESC: Computes the sub anagrams for the given word, using its power set.

        INPUTS: 
        wordPowerSet (type list[str]): Power set of the input word.

        OUTPUTS:
        allSubAnagramsList (type list[str]): All possible sub-anagrams of the input word.

        EXAMPLE: For input word 'dog', permutations of all anagrams are 
        ['', 'd', 'o', 'do', 'od', 'g', 'dg', 'gd', 'og', 'go', 'dog', 'dgo', 'odg', 'ogd', 'gdo', 'god'].
        """
        
        allSubAnagramsList = []

        # Permute each word in the power set.
        for i in range(len(wordPowerSet)):
            
            # Compute all permutations of the word.
            perms = permutations(wordPowerSet[i])

            # Append the permutations to the list.
            for perm in perms:
                allSubAnagramsList.append(''.join(perm))
        
        if self.hasDuplicate:       # Only return unique anagrams
            allSubAnagramsList = list(set(allSubAnagramsList))
        
        return allSubAnagramsList
    
    def compute(self) -> list[str]:
        """
        DESC: Calls the required functions for computing the sub-anagrams.

        OUTPUTS:
        (type list[str]): All possible sub-anagrams of the input word.
        
        EXAMPLE: For input word 'dog', sub-anagrams are ['', 'd', 'o', 'do', 'od', 
        'g', 'dg', 'gd', 'og', 'go', 'dog', 'dgo', 'odg', 'ogd', 'gdo', 'god'].
        """
        return self.__permutations(self.__powerset())

class returnValidSubAnagrams:
    def __init__(self, dictionary: list[str], allSubAnagramsList: list[str]) -> None:
        """
        DESC: Helper class to search for the sub-anagrams in the given dictionary, and only return the valid words.

        INPUTS:
        dictionary (type list[str]): Word list/dictionary.
        allSubAnagramsList (type list[str]): All possible sub anagrams of the input word.
        """
        self.allSubAnagramsList = allSubAnagramsList
        self.dictionary = dictionary

    def compute(self) -> list[str]:
        """
        DESC: Computes the valid sub-anagrams by calling binary-search for each sub-anagram on the dictionary.

        OUTPUTS:
        validSubAnagramsList (type list[str]): Valid sub-anagrams of the input word that are present in the dictionary.

        EXAMPLE: For input word 'dog', valid sub-anagrams are ['do', 'dog', 'go', 'god'].
        """
        validSubAnagramsList = []

        # Search each possible sub-anagram in dictionary, and append if found.
        for wordInAnagram in self.allSubAnagramsList:
            if binary_search(self.dictionary, wordInAnagram):
                validSubAnagramsList.append(wordInAnagram)

        validSubAnagramsList.sort()
        
        return validSubAnagramsList