"""
module to calcualte daily average
"""

from collections import defaultdict
from statistics import mean


def compute_daily_averages(
    rows: list[dict[str, str]], ts_col: str, value_col: str
) -> dict[str, float]:
    """
    function to calculate daily average based on the given dataset

    -- input type:
        rows -> list[dict[str, str]]
        ts_col -> str
        value_col -> str

    -- output type:
        dict[str,float]
    """
    tmp_dict = {}
    result = defaultdict(list)
    for i in rows:
        for key, value in i.items():
            if key == ts_col:
                tmp_dict[value] = i[value_col]

    for i, j in tmp_dict.items():
        year = i[:10]
        result[year].append(float(j))
    result = dict(result)

    for key, value in result.items():
        result[key] = round(mean(value), 2)

    return result
