import os
from constants import WORD_LIST_DIR

def checkValidWord(s: str) -> None:
    """
    DESC:   Checks whether the input word is valid (only contains alphabets) and isn't empty.
    
    INPUTS: 
            s (type str): Input word/string.
    """

    if not s.isalpha():
        raise(ValueError(f"Received invalid word input: {s}. Should be only alphabets."))
    
def checkValidWordList(s: str) -> None:
    """
    DESC:   Checks whether the input word list file exists.
    
    INPUTS: 
            s (type str): Input word/string.
    """

    if not os.path.exists(os.path.join(WORD_LIST_DIR, s)):
        raise(FileNotFoundError(f"Received invalid word list file name: {s}."))