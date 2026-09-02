"""
practice module: dictionaries
"""

# 1. `invert_dict(d: dict[str, str]) -> dict[str, str]` - swap keys and values
from typing import Callable


def invert_dict(d: dict[str, str]) -> dict[str, str]:
    """
    function to swap key value pairs of a dictionary
    """
    result: dict[str, str] = {}
    for key, value in d.items():
        result[value] = key
    return result


print(invert_dict({"a": "b", "c": "d", "e": "f"}))

# 2. `merge_dicts(*dicts: dict) -> dict` - merge multiple dicts (later values override)


def merge_dicts(*dicts: dict[str, str]) -> dict[str, str]:
    """
    merge the number of dicts given into a single dict
    """
    result: dict[str, str] = {}
    for i in dicts:
        for j in i:
            result[j] = i[j]
    return result


# 3. `filter_dict(d: dict, predicate) -> dict` - keep only items where predicate(key, value) is True


def predicate(x: str | int, y: int) -> bool:
    """
    predicate function for filter dict fucntion
    checks if the given element is in the list
    """
    return x in ["a", "b", "c"]


def filter_dict(
    d: dict[int | str, int], predicate: Callable[[str | int, int], bool]
) -> dict[str | int, int]:
    """
    function to filter dict on the basis for given predicate
    """
    return {key: value for key, value in d.items() if predicate(key, value)}


print(filter_dict({"a": "b", "c": "d", "e": "f"}, predicate))
