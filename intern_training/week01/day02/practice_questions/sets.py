"""
practice  module: sets
"""

# 1. `common_elements(list1: list, list2: list) -> set` - intersection of two lists


def common_elements(list1: list[int], list2: list[int]) -> set[int]:
    """
    function to return the common elements between two sets
    """
    return set(list1).intersection(set(list2))


print(common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7]))

# 2. `unique_chars(s: str) -> set[str]` - unique characters in a string


def unique_chars(s: str) -> set[str]:
    """
    function to return unique chars of a string
    """
    return set(s)


print(unique_chars("hello"))

# 3. `is_subset(set1: set, set2: set) -> bool` - check if set1 ⊆ set2


def is_subset(set1: set[int], set2: set[int]) -> bool:
    """
    function to check if a given set is a subset of other given set
    """
    return set1.issubset(set2)


print(is_subset(set1={1, 2, 3}, set2={1, 2, 3, 4, 5, 6}))
