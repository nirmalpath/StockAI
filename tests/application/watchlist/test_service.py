from stockai.application.watchlist import WatchlistService
from stockai.domain.models import WatchlistItem


class FakeWatchlistRepository:
    def get_all(self):
        return [
            WatchlistItem(
                ticker="RELIANCE.NS",
                company_name="Reliance Industries",
            ),
            WatchlistItem(
                ticker="TCS.NS",
                company_name="Tata Consultancy Services",
            ),
        ]


def test_get_watchlist():

    service = WatchlistService(FakeWatchlistRepository())

    watchlist = service.get_watchlist()

    assert len(watchlist) == 2
    assert watchlist[0].ticker == "RELIANCE.NS"


def test_get_tickers():

    service = WatchlistService(FakeWatchlistRepository())

    tickers = service.get_tickers()

    assert tickers == [
        "RELIANCE.NS",
        "TCS.NS",
    ]
