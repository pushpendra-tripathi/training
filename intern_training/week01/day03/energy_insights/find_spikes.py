import pandas as pd


def find_spikes(
    rows: list[dict[str, str]], value_col: str, top: int
) -> list[dict[str, str]]:
    df = pd.DataFrame(rows)
    df[value_col] = pd.to_numeric(df[value_col], errors="coerce")

    df = pd.DataFrame(df.nlargest(top, value_col).to_dict(orient="records"))
    df[value_col] = df[value_col].astype(str)

    return df.to_dict(orient="records")
