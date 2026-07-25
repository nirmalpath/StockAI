"""
Yahoo Finance implementation of the market data provider.
"""

from datetime import date

import yfinance as yf

from stockai.domain.models import Quote
from stockai.domain.repositories import MarketDataProvider


class YahooFinanceProvider(MarketDataProvider):
    """Market data provider backed by Yahoo Finance."""

    def get_quote(
        self,
        ticker: str,
        trade_date: date | None = None,
    ) -> Quote:
        """Retrieve the latest available quote."""

        symbol = yf.Ticker(ticker)

        history = symbol.history(period="5d")

        if history.empty:
            raise ValueError(f"No market data found for {ticker}")

        row = history.iloc[-1]

        actual_date = history.index[-1].date()

        return Quote(
            ticker=ticker,
            trade_date=actual_date,
            open_price=float(row["Open"]),
            high_price=float(row["High"]),
            low_price=float(row["Low"]),
            close_price=float(row["Close"]),
            volume=int(row["Volume"]),
        )

    def get_history(
        self,
        ticker: str,
        start_date: date,
        end_date: date,
    ) -> list[Quote]:
        """Retrieve historical daily quotes."""

        symbol = yf.Ticker(ticker)

        history = symbol.history(
            start=start_date,
            end=end_date,
        )

        if history.empty:
            return []

        quotes = []

        for timestamp, row in history.iterrows():
            quotes.append(
                Quote(
                    ticker=ticker,
                    trade_date=timestamp.date(),
                    open_price=float(row["Open"]),
                    high_price=float(row["High"]),
                    low_price=float(row["Low"]),
                    close_price=float(row["Close"]),
                    volume=int(row["Volume"]),
                )
            )

        return quotes
