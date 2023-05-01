"""
Implement binary search for strings.
"""

def binary_search(dictionary: list[str], target: str) -> bool:
    low, high = 0, len(dictionary)-1

    while (low<=high):
        mid = (low+high)//2

        if target == dictionary[mid]:
            return True

        if target > dictionary[mid]:
            low = mid + 1
        else:
            high = mid - 1
        
    return False