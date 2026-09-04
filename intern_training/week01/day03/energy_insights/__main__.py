"""
main file for package
cli tool for analysing csv files
"""

import argparse
import sys
from pathlib import Path
from typing import Protocol

import pandas as pd
from rich import print

from energy_insights.daily_average import compute_daily_averages
from energy_insights.find_spikes import find_spikes


def help():
    print("""
   A cli tool which gives basic stats of a csv file

     Arguments of cli:

     --file: name of the file to be analyzed (not optional)
     --top: for view only top n files,by default it will return all the rows (type:int, optional)
     --column: name of the column to be analyzed (not optional)

     use case:

     - python3 tools/csv_stats.py --file="hourly_prices.csv" --column=price --top=5  #default arguments

     """)


for i in sys.argv:
    if i == "--help" or i == "-h":
        help()
        sys.exit(0)


class CLIargs(Protocol):
    """
    type interface for cli args
    """

    file: str
    top: int
    column: str


parser = argparse.ArgumentParser()
file = str(parser.add_argument("--file", default="../hourly_prices.csv"))
n = parser.add_argument("--top", type=int, default=5)
column_name = parser.add_argument("--column", default="price")
ts_column = parser.add_argument("--tscolumn", default="timestamp")
args: CLIargs = parser.parse_args()  # pyright: ignore
base_dir = Path("../../")


try:
    file_path = ""
    for path in base_dir.rglob(args.file):
        file_path = path
    with open(file_path, encoding="utf-8") as file:
        df: pd.DataFrame = pd.read_csv(file)
        df_dict = df.to_dict(orient="records")
        print(
            "daily_average_price: ",
            compute_daily_averages(
                rows=df_dict, ts_col=args.tscolumn, value_col=args.column
            ),
        )
        print(
            "spikes_report: ",
            find_spikes(rows=df_dict, value_col=args.column, top=args.top),
        )
except FileNotFoundError:
    print("invalid file name")
