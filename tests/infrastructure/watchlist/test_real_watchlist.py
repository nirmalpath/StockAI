from pathlib import Path

from stockai.application.watchlist import WatchlistService
from stockai.infrastructure.watchlist import CsvWatchlistRepository


def test_real_watchlist():

    repository = CsvWatchlistRepository(Path("config/stocks.csv"))

    service = WatchlistService(repository)

    tickers = service.get_tickers()

    assert len(tickers) > 0
    assert "RELIANCE.NS" in tickers
