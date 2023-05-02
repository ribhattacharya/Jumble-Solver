"""
Utilities for read/write external files.
"""

import os
from constants import WORD_LIST_DIR

def load_dict(s: str) -> list[str]:
    """
    DESC:   Loads data from dictionary into Python list.
    
    INPUTS: 
    s (type str): Dictionary filename.
    
    OUTPUTS:
    dictionary (type list[str]): List of lowercased words in the dictionary. 
    Lowercased dictionary and input word ensures consistent matches. 
    """
    with open(os.path.join(WORD_LIST_DIR, s), 'r') as file:
        dictionary = [line.strip().lower() for line in file]
    
    return dictionary
