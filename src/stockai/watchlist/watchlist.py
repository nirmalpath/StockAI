from pathlib import Path

import pandas as pd

from stockai.config import WATCHLIST_FILE


class Watchlist:
    """
    Manages the investment watchlist.
    """

    REQUIRED_COLUMNS = ["Ticker", "Company"]

    def __init__(self):

        self.df = self._load()

    def _load(self):

        if not Path(WATCHLIST_FILE).exists():
            raise FileNotFoundError(
                f"{WATCHLIST_FILE} not found."
            )

        df = pd.read_csv(WATCHLIST_FILE)

        self._validate_columns(df)

        df = df.drop_duplicates(subset="Ticker")

        df = df.sort_values("Ticker")

        df = df.reset_index(drop=True)

        return df

    def _validate_columns(self, df):

        missing = [
            c for c in self.REQUIRED_COLUMNS
            if c not in df.columns
        ]

        if missing:
            raise ValueError(
                f"Missing columns: {missing}"
            )

    def get_all(self):

        return self.df.copy()

    def tickers(self):

        return self.df["Ticker"].tolist()

    def companies(self):

        return self.df["Company"].tolist()

    def count(self):

        return len(self.df)

    def exists(self, ticker):

        return ticker in self.df["Ticker"].values