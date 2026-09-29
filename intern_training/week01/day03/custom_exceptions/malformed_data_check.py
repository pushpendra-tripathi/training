"""
module for dataset check
"""

import pandas as pd


def malformed_check(file_path: str, value_col: str, ts_col: str):
    """
    function for checking malformed data
    """
    missing_values = ["n/a", "na", "--"]
    df = pd.read_csv(file_path, na_values=missing_values)
    for value in df[value_col].isnull():
        if value is True or value:
            return True


# print(
#     malformed_check(
#         file_path="./malformed_temperature_dataset.csv",
#         value_col="temperature",
#         ts_col="timestamp",
#     )
# )
