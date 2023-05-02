"""
Utilities for valid dictionary and word checks.
"""

import os
from constants import WORD_LIST_DIR

def check_dict_exists(s: str) -> None:
    """
    DESC: Checks whether the input dictionary file exists.
    
    INPUTS: 
    s (type str): Dictionary filename.
    """

    if not os.path.exists(os.path.join(WORD_LIST_DIR, s)):
        raise(FileNotFoundError(f"Received invalid dictionary filename: {s}."))

def check_valid_word(s: str) -> None:
    """
    DESC: Checks whether the input word is valid (only contains alphabets) and isn't empty.
    
    INPUTS: 
    s (type str): Input word/string.
    """

    if not s.isalpha():
        raise(ValueError(f"Received invalid word input: {s}. Should be only alphabets."))

def return_sorted_dict(dictionary: list[str]) -> list[str]:
    """
    DESC: Checks whether the dictionary is sorted. If not, then sorts it.
    
    INPUTS: 
    dictionary (type list[str]): Dictionary as a list of string.
    """
    # Sorted if element[i] < element[i+1] (lexicographically) for all i.
    isSorted = True
    for i in range(len(dictionary)-1):
        if dictionary[i] > dictionary[i+1]:
            isSorted = False
    
    # Sort dictionary if not already.
    if not isSorted:                           
        print("-> Sorting input dictionary since it wasn't already.")
        dictionary.sort()
    
    return dictionary



