"""
Utilities for read/write external files.
"""

import os
from constants import WORD_LIST_DIR

def load_words(s: str) -> list[str]:
    """
    DESC:   Loads data from dictionary into Python list.
    
    INPUTS: 
    s (type str): Dictionary filename.
    
    OUTPUTS:
    word_list (type list[str]): List of words in the dictionary.
    """
    with open(os.path.join(WORD_LIST_DIR, s), 'r') as file:
        word_list = [line.strip().lower() for line in file]
    
    return word_list
