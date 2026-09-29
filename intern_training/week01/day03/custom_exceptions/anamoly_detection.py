from statistics import mean, pstdev

import pandas as pd


def anamoly_detection(
    rows: list[dict[str, str]], value_col: str
) -> tuple[bool, pd.DataFrame] | bool:
    """
    function to detect anamoly in the dataset
    """
    average = round(mean([float(i[value_col]) for i in rows]), 2)
    stdv = round(pstdev([float(i[value_col]) for i in rows]), 2)
    # result = {
    #     i["zscore"]: round((float(i[value_col]) - average) / stdv, 2) for i in rows
    # }
    for i in rows:
        i["z-score"] = round((float(i[value_col]) - average) / stdv, 2)

    df = pd.DataFrame(rows)
    outliers = df[df["z-score"].abs() > 3]
    if outliers.empty:
        return False
    return (True, outliers)
