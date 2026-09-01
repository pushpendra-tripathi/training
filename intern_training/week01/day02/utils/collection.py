"""
utility collections

frequencies(): takes list of strings as an input

returns dictionary containing the elements frequencies

dedupe(): takes list of strings as an input

returns a list of unique elements in the given list

groupby(): takes list of dictionary and a string key as input

returns a dict mapping key values ot list of items

"""

from typing import TypedDict


def frequencies(items: list[str]) -> dict[str, int]:
    """
    - Input: list of strings
    - Output: dict mapping item -> count
    - Example: ["a","b","a"] -> {"a": 2, "b": 1}
    """

    return {i: items.count(i) for i in items}


print(frequencies(["a", "b", "b"]))
print("\n")


def dedupe(items: list[str]) -> list[str]:
    """
    - Input: list with duplicates
     - Output: list preserving first occurrence order
     - Example: ["a","b","a"] -> ["a","b"]
    """

    return list(set(items))


print(dedupe(["a", "b", "b"]))
print("\n")


class Todo(TypedDict):
    """
    interface for dictionary element in list
    """

    status: str
    id: int


def groupby(items: list[Todo], key: str) -> dict[str, list[Todo]] | None:
    """
    - Input: list of dicts, key to group by
     - Output: dict mapping key values to lists of items
     - Example: `[{"status":"todo","id":1},
     {"status":"done","id":2}]` grouped by "status"
    """
    result: dict[str, list[Todo]] = {}
    for i in items:
        if i[key] not in result:
            result[i[key]] = []
        result[i[key]].append(i)
    return result


print(
    groupby(
        items=[
            {"status": "todo", "id": 1},
            {"status": "done", "id": 2},
            {"status": "todo", "id": 3},
            {"status": "done", "id": 4},
        ],
        key="status",
    )
)
