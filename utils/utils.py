"""
Utilities for valid dictionary and word checks.
"""

import os
from constants import WORD_LIST_DIR

def is_sorted(dictionary: list[str]) -> bool:
    """
    DESC: Checks whether the dictionary is sorted, 
    which is required by binary search.

    INPUTS:
    dictionary (type list[str]): Dictionary as a list of string.

    OUTPUTS:
    True/False (type bool): Is dictionary sorted or not.
    """
    # Sorted if element[i] < element[i+1] (lexicographically) for all i, else unsorted.
    for i in range(len(dictionary)-1):
        if dictionary[i] > dictionary[i+1]:
            return False
    
    return True

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

def check_valid_dict(dictionary: list[str]) -> list[str]:
    """
    DESC: Checks whether the dictionary is valid (no duplicates and sorted). If not, then makes the necessary changes.
    
    INPUTS: 
    dictionary (type list[str]): Dictionary as a list of string.
    """
    
    # Check if dictionary has duplicate elements.
    dictionary_ = set(dictionary)
    if len(dictionary_) < len(dictionary):
        print("-> Removing duplicates from dictionary.")
        dictionary = list(dictionary_)
    
    # Sort dictionary if not already.
    if not is_sorted(dictionary):                           
        print("-> Sorting input dictionary since it wasn't already.")
        dictionary.sort()
    
    return dictionary



