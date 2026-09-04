"""

module to load_csv

"""

from pathlib import Path

import pandas as pd
from rich import print


def load_csv(file_path: str) -> list[dict[str, str]] | str:
    """
    Input: path to CSV
    Output: list of rows as dicts (string values)
    """
    result = []
    if not Path(file_path).exists:
        return "Invalid path"

    df = pd.read_csv(file_path)

    for i in df.index:
        result.append(dict(df.iloc[i]))
    return result


print(load_csv("../../data/energy/hourly_prices.csv"))
