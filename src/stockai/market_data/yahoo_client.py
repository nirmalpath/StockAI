import yfinance as yf

from stockai.models.quote import Quote


class YahooFinanceClient:

    def get_quote(self, ticker: str) -> Quote:

        stock = yf.Ticker(ticker)

        history = stock.history(period="1y")

        if history.empty:
            raise ValueError(f"No data returned for {ticker}")

        latest = history.iloc[-1]

        info = stock.info

        return Quote(

            ticker=ticker,

            current_price=float(latest["Close"]),

            previous_close=float(history.iloc[-2]["Close"]),

            open_price=float(latest["Open"]),

            high=float(latest["High"]),

            low=float(latest["Low"]),

            volume=int(latest["Volume"]),

            high_52=float(history["High"].max()),

            low_52=float(history["Low"].min()),

            market_cap=info.get("marketCap"),

            pe_ratio=info.get("trailingPE"),

            sector=info.get("sector")

        )