"""
summarize_numeric module to to give a basic
summary of a given list of dictionaries based on column name
"""

from statistics import mean


def summarize_numeric(rows: list[dict[str, str]], column: str) -> dict[str, float]:
    """
    Input: rows and a numeric column name
    Output: `{ "min": float, "max": float, "mean": float }`
    """
    column_list = []
    for i in rows:
        for key, value in i.items():
            if key == column:
                column_list.append(float(value))
    return {"min": min(column_list), "max": max(column_list), "mean": mean(column_list)}


print(
    summarize_numeric(
        rows=[
            {"name": "Laptop", "price": "1200.00", "category": "Electronics"},
            {"name": "Mouse", "price": "25.50", "category": "Electronics"},
            {"name": "Desk", "price": "300.00", "category": "Furniture"},
            {"name": "Chair", "price": "150.00", "category": "Furniture"},
        ],
        column="price",
    )
)
