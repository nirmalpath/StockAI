from datetime import date

from stockai.application.downloader import DownloadResult
from stockai.application.market_data import MarketDataService
from stockai.domain.models import Quote

from stockai.application.downloader import DownloadFailure


class FakeDownloader:
    def download(self, tickers, trade_date=None):
        return DownloadResult(
            quotes=[
                Quote(
                    ticker="RELIANCE.NS",
                    trade_date=date(2026, 7, 24),
                    open_price=100.0,
                    high_price=110.0,
                    low_price=95.0,
                    close_price=105.0,
                    volume=100000,
                ),
            ],
        )


class FakePriceRepository:
    def __init__(self):
        self.saved_quotes = []

    def save_all(self, quotes):
        self.saved_quotes.extend(quotes)


def test_download_and_store():
    downloader = FakeDownloader()
    repository = FakePriceRepository()

    service = MarketDataService(
        downloader=downloader,
        price_repository=repository,
    )

    result = service.download_and_store(["RELIANCE.NS"])

    assert result.successful_count == 1
    assert len(repository.saved_quotes) == 1
    assert repository.saved_quotes[0].ticker == "RELIANCE.NS"


def test_empty_download_does_not_save():
    class EmptyDownloader:
        def download(self, tickers, trade_date=None):
            return DownloadResult()

    repository = FakePriceRepository()

    service = MarketDataService(
        downloader=EmptyDownloader(),
        price_repository=repository,
    )

    result = service.download_and_store([])

    assert result.successful_count == 0
    assert repository.saved_quotes == []


def test_failed_downloads_are_not_persisted():
    class FailingDownloader:
        def download(self, tickers, trade_date=None):
            return DownloadResult(
                failures=[
                    DownloadFailure(
                        ticker="BAD.NS",
                        error="Data unavailable",
                    ),
                ],
            )

    repository = FakePriceRepository()

    service = MarketDataService(
        downloader=FailingDownloader(),
        price_repository=repository,
    )

    result = service.download_and_store(["BAD.NS"])

    assert result.failed_count == 1
    assert repository.saved_quotes == []
