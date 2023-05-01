import sys
from utils import *

def main(word_list: str, word: str) -> None:
    """
    DESC:   

    INPUTS: 
            word_list (type str): Dictionary filename.
            word (type str)     : Input word/string.
    """
    raise(NotImplementedError("Program is not implemented!"))

if __name__=='__main__':

    if len(sys.argv) == 3:
        word_list = sys.argv[1]
        word = sys.argv[2]

        checkValidWordList(word_list)
        checkValidWord(word)

    elif len(sys.argv) == 1:
        # Default values
        word_list = 'corncob_lowercase.txt'
        word = 'dog'

        print(f"1 argument passed. Using default word list: {word_list} and word: {word}")
        
    else:
        raise(TypeError(f"Expected 1 or 3 arguments, got {len(sys.argv)}."))

    main(word_list, word)