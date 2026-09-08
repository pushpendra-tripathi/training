from custom_exceptions.boundary_conditions import (
    single_item,
    special_characters,
    very_long_string,
)
from custom_exceptions.malformed_data_check import malformed_check


class Malformed_data(Exception):
    """
    custom exception for malformed data
    """

    pass


class boundary_conditions(Exception):
    """
    custom exception for boundary conditions
        - very long column names
        - single row dataset
        - column names containing special characters
    """

    pass


def boundary_case_checks(rows: list[dict[str, str]], valuecol: str, ts_col: str):
    if single_item(rows):
        raise (boundary_conditions("The dataset has a single row"))
    elif special_characters(value_col=valuecol, tscol=ts_col):
        raise (boundary_conditions("The column name contains special characters"))
    elif very_long_string(value_col=valuecol, tscol=ts_col):
        raise (boundary_conditions("too long column name"))


def data_analysis(file: str, val_col: str, tscol: str):
    if malformed_check(file_path=file, value_col=val_col, ts_col=tscol):
        raise Malformed_data("Bad data, please clean the data")
