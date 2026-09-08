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

from custom_exceptions.anamoly_detection import anamoly_detection
from custom_exceptions.exceptions import (
    Malformed_data,
    boundary_case_checks,
    data_analysis,
)
from custom_exceptions.malformed_data_check import malformed_check
from energy_insights.daily_average import compute_daily_averages
from energy_insights.find_spikes import find_spikes

for i in sys.argv:
    if i in ("--help", "-h"):
        print("""
           A cli tool which gives basic stats of a csv file

             Arguments of cli:

             --file: name of the file to be analyzed (not optional)
             --top: for view only top n files,by default it will return all the rows (type:int, optional)
             --column: name of the column to be analyzed (not optional)
             --tscolum: name of the time series column

             use case:

             - python3 tools/csv_stats.py --file="hourly_prices.csv" --column=price --top=5  #default arguments

             Note:
                 Avoid usign data containing:
                    - very long column name
                    - only one row
                    - column names having special characters

             """)

        sys.exit(0)


class CLIargs(Protocol):
    """
    type interface for cli args
    """

    file: str
    top: int
    column: str


parser = argparse.ArgumentParser()
base_dir = Path(__file__).resolve().parent.parent
fileName = str(
    parser.add_argument(
        "--file", default="test/test_databases/hourly_prices.csv", type=Path
    )
)
n = parser.add_argument("--top", type=int, default=5)
column_name = parser.add_argument("--column", default="price")
ts_column = parser.add_argument("--tscolumn", default="timestamp")
args: CLIargs = parser.parse_args()  # pyright: ignore


def main(
    file_path: str = args.file,
    column: str = args.column,
    top: int = args.top,
    tscolumn: str = args.tscolumn,
):
    """
    main function for cli
    """
    try:
        with open(file=rf"{file_path}", encoding="utf-8") as f:
            df: pd.DataFrame = pd.read_csv(f)
            df_dict: list[dict[str, str]] = df.to_dict(orient="records")
            boundary_case_checks(valuecol=column, ts_col=tscolumn, rows=df_dict)
            data_analysis(file=file_path, val_col=column, tscol=tscolumn)
    except IsADirectoryError:
        print("Is a directory,please provide a correct path of the file")
    except FileNotFoundError:
        print("invalid file name")
    except Malformed_data as e:
        print(e)
    except KeyError:
        print("enter valid column name")
    except boundary_case_checks as e:
        print(e)
    except data_analysis as e:
        print(e)
    else:
        print(
            f"daily_average_{column}: ",
            compute_daily_averages(rows=df_dict, ts_col=tscolumn, value_col=column),
        )
        print("\n")
        print(
            f"Top {top} {column} spikes report: ",
            find_spikes(rows=df_dict, value_col=column, top=top),
        )
        if anamoly := anamoly_detection(
            rows=df_dict,
            value_col=column,
        ):
            print("anamoly detected: ", anamoly[0])
            print("\n")
            print(anamoly[1])
        else:
            print("anamoly detected: ", False)


if __name__ == "__main__":
    main()
