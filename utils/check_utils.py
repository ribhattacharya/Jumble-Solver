"""
Utilities for valid dictionary and word checks.
"""

import os
from constants import WORD_LIST_DIR

def check_valid_word(s: str) -> None:
    """
    DESC: Checks whether the input word is valid (only contains alphabets) and isn't empty.
    
    INPUTS: 
    s (type str): Input word/string.
    """

    if not s.isalpha():
        raise(ValueError(f"Received invalid word input: {s}. Should be only alphabets."))
    
def check_valid_dictionary(s: str) -> None:
    """
    DESC: Checks whether the input dictionary file exists.
    
    INPUTS: 
    s (type str): Dictionary filename.
    """

    if not os.path.exists(os.path.join(WORD_LIST_DIR, s)):
        raise(FileNotFoundError(f"Received invalid dictionary filename: {s}."))

def check_sorted(dictionary: list[str]) -> bool:
    """
    DESC: Checks whether the dictionary is sorted, which would simplify searching.

    INPUTS:
    lst (type list[str]): Dictionary as a list of string.

    OUTPUTS:
    True/False (type bool): Is dictionary sorted or not.
    """
    for i in range(len(dictionary)-1):
        if dictionary[i] > dictionary[i+1]:
            return False
    
    return True



