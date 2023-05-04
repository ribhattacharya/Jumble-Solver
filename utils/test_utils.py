"""
Utilities for testing performance.
"""    
import matplotlib.pyplot as plt
from typing import Union

def get_values(stats: dict, dictionaryName: str, attr: str) -> Union[list[int], list[float]]:
    """
    DESC: Return list of given attribute for all words.
    
    INPUTS:
    stats (type dict): Dictionary of all recorded stats.
    dictionaryName (type str): Dictionary name.
    attr (type str): Attribute to choose from ['wordLen', 'dictLen', 'validLen', 'allLen', 'timeElapsed'].

    OUTPUTS: 
    Union[list[int], list[float]]: List of given attribute from given dictionary for all words.
    """
    # List of all words
    words = [stats[data].keys() for data in stats]
    
    return [stats[dictionaryName][word][attr] for word in words]

def plot_results(stats: dict, dictionaryNames: list[str], words: list[str], attr: str) -> None:
    """
    DESC: Plot results.

    INPUTS:
    stats (type dict): Dictionary of all recorded stats.
    dictionaryNames (type list[str]): List of all dictionary names.
    words (type list[str]): List of all words.
    attr (type str): Attribute to choose from ['wordLen', 'dictLen', 'validLen', 'allLen', 'timeElapsed'].
    """
    # Create title mapping with attr for plotting
    titles = {
        'wordLen': 'word length',
        'dictLen': 'dictionary length',
        'alllen': '# of all possible sub-anagrams',
        'validLen': '# of valid sub-anagrams',
        'timeElapsed': 'Time elapsed (ms)'
    }

    # Create plot for givenb attribute (attr)
    for i, dictionaryName in enumerate(dictionaryNames):
        dictLabel = dictionaryName[:-4] + f" ({get_values(stats, dictionaryName, 'dictLen')[i]/1000:0.0f}K words)"
        x = get_values(stats, dictionaryName, 'wordLen')
        y = get_values(stats, dictionaryName, attr)
        plt.plot(x, y, label=dictLabel) 

    # Custom xticks
    xtick = [f'{word} ({len(word)})' for word in words]
    
    plt.ylabel(titles[attr])
    plt.xlabel(titles['wordLen'])
    plt.xticks(x, xtick)
    plt.title(f"{titles[attr]} vs {titles['wordLen']} for all dictionaries")
    plt.legend()
    plt.savefig(f'./results/{attr}.png')
    plt.show(block=True)