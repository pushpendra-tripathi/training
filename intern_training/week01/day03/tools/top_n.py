"""
module to sort the given top n rows in descending order
"""

import pandas as pd


def top_n(rows: list[dict[str, str]], column: str, n: int) -> list[dict[str, str]]:
    """
    Input: rows, numeric column, number N
    Output: top N rows sorted descending by the column
    """

    return (
        pd.DataFrame(rows)[column]  # pyright: ignore
        .sort_values(ignore_index=True, ascending=False)
        .head(n)
    )  # pyright: ignore


print(
    top_n(
        [
            {"name": "Laptop", "price": "1200.00", "category": "Electronics"},
            {"name": "Mouse", "price": "25.50", "category": "Electronics"},
            {"name": "Desk", "price": "300.00", "category": "Furniture"},
            {"name": "Chair", "price": "150.00", "category": "Furniture"},
        ],
        column="price",
        n=5,
    )
)
