"""
cli tool for analysing csv files
put your csv file in the directory: intern_training/data/energy/hourly_prices.csv
"""

import argparse
from pathlib import Path
from typing import Protocol

import pandas as pd


class CLIargs(Protocol):
    """
    type interface for cli args
    """

    file: str
    top: int
    column: str


parser = argparse.ArgumentParser()
file = str(parser.add_argument("--file", required=True))
n = parser.add_argument("--top", type=int)
column_name = parser.add_argument("--column", required=True)
args: CLIargs = parser.parse_args()  # pyright: ignore
base_dir = Path("../../")

try:
    file_name: str = args.file
    column: str = args.column
    top_n: int = args.top
    file_path = ""
    for path in base_dir.rglob(file_name):
        file_path = path
    with open(file_path, encoding="utf-8") as file:
        df: pd.DataFrame = pd.read_csv(file)
        # print(tabulate(df[column].head(top_n), tablefmt="fancy_grid"))
        print("\n")
        print("number of rows:", len(df))
        print("\n")
        print(f"top {top_n} rows of column {column}")
        print("\n")
        print(df[column].head(top_n))
        print("\n")
        print(f"{column} summary")
        print("\n")
        print("mean: ", df[column].mean())
        print("max: ", df[column].max())
        print("min: ", df[column].min())
except FileNotFoundError:
    print("invalid file name,check if the file is present in the given data directory")
