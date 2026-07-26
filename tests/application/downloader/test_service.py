from datetime import date

from stockai.application.downloader import MarketDataDownloader
from stockai.domain.models import Quote

import pytest


class FakeMarketDataProvider:
    def get_quote(self, ticker, trade_date=None):
        return Quote(
            ticker=ticker,
            trade_date=date(2026, 7, 24),
            open_price=100.0,
            high_price=110.0,
            low_price=95.0,
            close_price=105.0,
            volume=100000,
        )


def test_download_multiple_tickers():

    downloader = MarketDataDownloader(
        provider=FakeMarketDataProvider(),
        max_workers=3,
    )

    result = downloader.download(
        [
            "RELIANCE.NS",
            "TCS.NS",
            "INFY.NS",
        ]
    )

    assert result.successful_count == 3
    assert result.failed_count == 0

    tickers = {quote.ticker for quote in result.quotes}

    assert tickers == {
        "RELIANCE.NS",
        "TCS.NS",
        "INFY.NS",
    }


def test_one_failure_does_not_stop_other_downloads():

    class PartiallyFailingProvider:

        def get_quote(self, ticker, trade_date=None):

            if ticker == "BAD.NS":
                raise RuntimeError("Market data unavailable")

            return Quote(
                ticker=ticker,
                trade_date=date(2026, 7, 24),
                open_price=100.0,
                high_price=110.0,
                low_price=95.0,
                close_price=105.0,
                volume=100000,
            )

    downloader = MarketDataDownloader(
        provider=PartiallyFailingProvider(),
        max_workers=3,
    )

    result = downloader.download(
        [
            "RELIANCE.NS",
            "BAD.NS",
            "TCS.NS",
        ]
    )

    assert result.successful_count == 2
    assert result.failed_count == 1

    assert result.failures[0].ticker == "BAD.NS"
    assert "Market data unavailable" in result.failures[0].error


def test_empty_watchlist():

    downloader = MarketDataDownloader(provider=FakeMarketDataProvider())

    result = downloader.download([])

    assert result.successful_count == 0
    assert result.failed_count == 0
    assert result.quotes == []
    assert result.failures == []


def test_invalid_worker_count():

    with pytest.raises(ValueError):

        MarketDataDownloader(
            provider=FakeMarketDataProvider(),
            max_workers=0,
        )
