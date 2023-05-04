from utils import *
from scripts import *
from time import time


def main(dictionaryName: str, word: str) -> dict:
    """
    DESC: Main method which calls all other methods for the jumble problem, 
    and prints the results.

    INPUTS: 
    dictionaryName (type str): Dictionary filename.
    word (type str): Input word/string.
    """
    # Load and save dictionary
    dictionary = load_dict(dictionaryName)                 

    # Create an object to compute anagrams.
    jumbleSolver = computeSubAnagrams(dictionary, word)
    jumbleSolver.compute()

    # Return stats for current test
    stat = {
        'wordLen': len(word),
        'dictLen': len(dictionary),
        'allLen': jumbleSolver.size('all'),
        'validLen': jumbleSolver.size('valid')
    }
    return stat

if __name__=='__main__':

    dictionaryNames = ['mit_10k.txt', 'corncob_lowercase.txt', 'english3.txt', 'words_alpha.txt']
    words = ['cat', 'lion', 'tiger', 'pangol', 'leopard', 'flamingo']

    stats = {}  # Store all stats here

    # Compute stats for all test cases
    for dictionaryName in dictionaryNames:
        stats[dictionaryName] = {}

        for word in words:
            tic = time()
            stats[dictionaryName][word] = main(dictionaryName, word)
            stats[dictionaryName][word]['timeElapsed'] = 1000*(time()-tic)

    # Plot results
    plot_results(stats, dictionaryNames, words, 'timeElapsed')
    plot_results(stats, dictionaryNames, words, 'validLen')