from unittest.mock import MagicMock, patch

import pandas as pd

from stockai.infrastructure.market_data import YahooFinanceProvider


def test_get_quote():

    history = pd.DataFrame(
        {
            "Open": [100.0],
            "High": [110.0],
            "Low": [95.0],
            "Close": [105.0],
            "Volume": [100000],
        },
        index=pd.to_datetime(["2026-07-24"]),
    )

    mock_ticker = MagicMock()
    mock_ticker.history.return_value = history

    with patch(
        "stockai.infrastructure.market_data.yahoo_finance_provider.yf.Ticker",
        return_value=mock_ticker,
    ):
        provider = YahooFinanceProvider()

        quote = provider.get_quote("RELIANCE.NS")

    assert quote.ticker == "RELIANCE.NS"
    assert quote.close_price == 105.0
    assert quote.high_price == 110.0
    assert quote.volume == 100000
