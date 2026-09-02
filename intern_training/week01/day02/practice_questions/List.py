"""
practice module: list
"""

# 1. `merge_sorted(list1: list[int], list2: list[int]) -> list[int]` - merge two sorted lists


def merge_sorted(list1: list[int], list2: list[int]) -> list[int]:
    """
    function to merge two sorted list
    """
    return list1 + list2


print(merge_sorted([1, 2, 3, 4, 5], [6, 7, 8]))

# 2. `chunk_list(items: list, size: int) -> list[list]` - split into chunks: `[1,2,3,4,5], 2` → `[[1,2],[3,4],[5]]`

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def chunk_list(items: list[int], size: int) -> list[list[int]]:
    """
    funciton to divide the list into chunks based on given argument
    """
    lst: list[list[int]] = []
    i = 0
    while i + size < len(items):
        lst.append(items[i : i + size])
        i += size
    lst.append(items[i::])

    return lst


print(chunk_list(lst, 4))

# 3. `flatten(nested: list[list]) -> list` - flatten one level: `[[1,2],[3,4]]` → `[1,2,3,4]`


def flatten(nested: list[list[int]]) -> list[int]:
    """
    function to flatten a nested list
    """
    lst: list[int] = []
    for i in nested:
        for j in i:
            lst.append(j)
    return lst


print(flatten([[1, 2, 4, 4], [5, 6]]))
