from itertools import permutations
from .binary_search import binary_search

class computeAllSubAnagrams:
    def __init__(self, word: str) -> None:
        self.word = word

    def __powerset(self) -> list[str]:
        __wordPowerSet = ['']
        for c in self.word:
            for i in range(len(__wordPowerSet)):
                __wordPowerSet.append(__wordPowerSet[i]+c)
        
        return __wordPowerSet
    
    def __permutations(self, __wordPowerSet) -> list[str]:
        
        subAnagramsList = []
        for i in range(len(__wordPowerSet)):
            perms = permutations(__wordPowerSet[i])

            for perm in perms:
                subAnagramsList.append(''.join(perm))
        
        return subAnagramsList
    
    def compute(self) -> list[str]:
        
        __wordPowerSet = self.__powerset()
        subAnagramsList = self.__permutations(__wordPowerSet)
        return subAnagramsList

class returnValidSubAnagrams:
    def __init__(self, dictionary: list[str], allSubAnagrams: list[str]) -> None:
        self.allSubAnagrams = allSubAnagrams
        self.dictionary = dictionary

    def compute(self) -> list[str]:
        
        validSubAnagrams = []
        for wordInAnagram in self.allSubAnagrams:
            if binary_search(self.dictionary, wordInAnagram):
                validSubAnagrams.append(wordInAnagram)

        return validSubAnagrams