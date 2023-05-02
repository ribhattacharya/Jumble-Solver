"""
Implement binary search for strings.
"""

def binary_search(dictionary: list[str], word: str) -> bool:
    """
    DESC: Searches the given word in the dictionary using binary search. 
    Dictionary NEEDS to be sorted.

    OUTPUTS:
    (type bool): Is word found in dictionary?
    """
    low, high = 0, len(dictionary)-1

    while (low<=high):
        mid = (low+high)//2

        if word == dictionary[mid]:
            return True     # word is found

        if word > dictionary[mid]:
            low = mid + 1
        else:
            high = mid - 1
        
    return False            # word is not found