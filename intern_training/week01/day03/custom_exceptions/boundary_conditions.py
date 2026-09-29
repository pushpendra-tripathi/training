"""
test module for checking boundary conditions
"""

import string


def single_item(rows: list[dict[str, str]]):
    """
    function to check for single rows
    """
    if len(rows) == 1:
        return True


def very_long_string(value_col: str, tscol: str):
    """
    function to check for very long string
    """
    if len(value_col) > 20 or len(tscol) > 20:
        return True


def special_characters(value_col: str, tscol: str):
    """
    function to check for special characters
    """
    return any(char in string.punctuation for char in value_col) or any(
        char in string.punctuation for char in tscol
    )
