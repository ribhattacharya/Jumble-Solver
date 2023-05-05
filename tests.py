from utils import *
from scripts import *
from time import time
from itertools import product
import pandas as pd

def main(dictionaryName: str, word: str) -> dict:
    """
    DESC: Main method which calls all other methods for the jumble problem, 
    and prints the results.

    INPUTS: 
    dictionaryName (type str): Dictionary filename.
    word (type str): Input word/string.

    OUTPUTS:
    stat (type dict): Dictionary of various stats to evaluate performance against.
    """
    # Load and save dictionary
    dictionary = load_dict(dictionaryName)                 

    # Get valid sub anagrams, and additional data
    _, lenValid, lenAll = sub_anagrams(dictionary, word)

    # Return stats for current test
    stat = {
        'wordLen': len(word),
        'dictLen': len(dictionary),
        'allLen': lenAll,
        'validLen': lenValid
    }
    return stat

if __name__=='__main__':

    dictionaryNames = ['mit_10k.txt', 'corncob_lowercase.txt', 'english3.txt', 'words_alpha.txt']
    words = ['cat', 'lion', 'tiger', 'pangol', 'leopard', 'flamingo']
    attributes = ['wordLen', 'dictLen', 'validLen', 'allLen', 'timeElapsed']
    
    # Store all stats here
    stats = pd.DataFrame(
        columns=['dictionaryName', 'word', *attributes], 
        index=pd.MultiIndex.from_tuples(product(dictionaryNames, words))
    )

    for i, prod in enumerate(product(dictionaryNames, words)):
        stats.loc[prod, ['dictionaryName', 'word']] = prod


    # Compute and store stats for all test cases in the DataFrame
    for dictionaryName in dictionaryNames:
        for word in words:

            tic = time()
            stat = main(dictionaryName, word)
            stats.loc[(dictionaryName, word), 'timeElapsed'] = 1000*(time()-tic)
            
            for attr in attributes:
                if attr != 'timeElapsed':
                    stats.loc[(dictionaryName, word), attr] = stat[attr]

    # Plot results
    plot_results(stats, dictionaryNames, words, 'timeElapsed')
    plot_results(stats, dictionaryNames, words, 'validLen')
 