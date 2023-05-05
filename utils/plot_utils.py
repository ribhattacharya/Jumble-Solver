"""
Utilities for plotting.
"""    
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_theme()

def plot_results(stats: pd.DataFrame, dictionaryNames: list[str], words: list[str], attr: str) -> None:
    """
    DESC: Plot results.

    INPUTS:
    stats (type pd.DataFrame): Pandas DataFrame of all data.
    dictionaryNames (type list[str]): List of all dictionary names.
    words (type list[str]): List of all words.
    attr (type str): Attribute to choose from ['wordLen', 'dictLen', 'validLen', 'allLen', 'timeElapsed'].
    """
    # Create title mapping with attr for plotting
    titles = {
        'wordLen': 'word length',
        'dictLen': 'dictionary length',
        'allLen': '# of all possible sub-anagrams',
        'validLen': '# of valid sub-anagrams',
        'timeElapsed': 'Time elapsed (ms)'
    }

    data = stats.pivot(index="word", columns='dictionaryName', values=attr).loc[words, dictionaryNames]
    sns.lineplot(data)
    
    # Custom xticks
    xticks = [f'{word} ({len(word)})' for word in words]
    
    plt.ylabel(titles[attr])
    plt.xticks(range(len(xticks)), xticks)
    plt.title(f"{titles[attr]} vs {titles['wordLen']} for all dictionaries")
    plt.legend()
    plt.savefig(f'./results/{attr}.png')
    plt.show(block=True)