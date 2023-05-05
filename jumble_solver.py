import sys
from utils import *
from scripts import *
from time import time

def main(dictionaryName: str, word: str) -> None:
    """
    DESC: Main method which calls all other methods for the jumble problem, 
    and prints the results.

    INPUTS: 
    dictionaryName (type str): Dictionary filename.
    word (type str): Input word/string.
    """
    # Load and save dictionary
    dictionary = load_dict(dictionaryName)                 

    # Get valid sub anagrams, and additional data
    validSubAnagrams, lenValid, lenAll = sub_anagrams(dictionary, word)
    
    print(f"# of all possible sub-anagrams:\t{lenAll}")
    print(f"# of valid sub-anagrams:\t{lenValid}")
    print('Valid sub-anagrams are:\t\t',validSubAnagrams)



if __name__=='__main__':

    if len(sys.argv) == 3:
        # Store dictionary filename and word if provided as arguments
        dictionaryName = sys.argv[1]
        word = sys.argv[2]

        # Run checks for invalid dictionary file and invalid word
        check_dict_exists(dictionaryName)
        check_valid_word(word)

    elif len(sys.argv) == 1:
        # Default values if no argument given
        dictionaryName = 'corncob_lowercase.txt'
        word = 'dog'

        print(f"1 argument passed. Using default word list: {dictionaryName} and word: {word}")
        
    else:
        raise(TypeError(f"Expected 1 or 3 arguments, got {len(sys.argv)}."))

    tic = time()
    
    # For correct matching, convert word to lowercase, since dictionary is also converted to lowercase.
    word = word.lower()  
    
    print("------------------------------------------------------------------------------------")
    main(dictionaryName, word)
    print(f'Time elapsed:\t\t\t{1000*(time()-tic):0.2f} ms')
    print("------------------------------------------------------------------------------------")