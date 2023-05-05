"""
Utilities for read/write external files.
"""

import os
from constants import WORD_LIST_DIR

def load_dict(s: str) -> set[str]:
    """
    DESC:   Loads data from dictionary into Python list.
    
    INPUTS: 
    s (type str): Dictionary filename.
    
    OUTPUTS:
    dictionary (type set[str]): Set of lowercased words in the dictionary. Lowercased dictionary and input word ensures consistent matches. 
    """
    dictionary = set()

    with open(os.path.join(WORD_LIST_DIR, s), 'r') as file:
        for line in file:
            dictionary.add(line.strip().lower())
    
    return dictionary
