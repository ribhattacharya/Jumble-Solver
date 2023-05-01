import sys
from utils import *
from scripts import *

def main(dictionaryName: str, word: str) -> None:
    """
    DESC:   

    INPUTS: 
    dictionaryName (type str): Dictionary filename.
    word (type str): Input word/string.
    """
    
    dictionary = load_words(dictionaryName)                 # Save dictionary as list
    if not check_sorted(dictionary):
        print("Sorting input dictionary since it wasn't already.")
        dictionary.sort()
    
    allSubAnagrams = computeAllSubAnagrams(word).compute()        # Save all sub-anagrams of input word
    print(f'Total sub-anagrams found: {len(allSubAnagrams)}\n')

    validSubAnagrams = returnValidSubAnagrams(dictionary, allSubAnagrams).compute()
    print(f'Total valid sub-anagrams found in dictionary: {len(validSubAnagrams)}\n')



if __name__=='__main__':

    if len(sys.argv) == 3:
        # Store dictionary filename and word if provided as arguments
        dictionaryName = sys.argv[1]
        word = sys.argv[2]

        # Run checks for invalid dictionary file and invalid word
        check_valid_dictionary(dictionaryName)
        check_valid_word(word)

    elif len(sys.argv) == 1:
        # Default values if no argument given
        dictionaryName = 'corncob_lowercase.txt'
        word = 'dog'

        print(f"1 argument passed. Using default word list: {dictionaryName} and word: {word}")
        
    else:
        raise(TypeError(f"Expected 1 or 3 arguments, got {len(sys.argv)}."))

    word = word.lower()
    main(dictionaryName, word)