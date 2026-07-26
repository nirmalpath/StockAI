"""
Application service for working with the stock watchlist.
"""

from stockai.domain.models import WatchlistItem
from stockai.domain.repositories import WatchlistRepository


class WatchlistService:
    """Provides application-level watchlist operations."""

    def __init__(self, repository: WatchlistRepository):
        self.repository = repository

    def get_watchlist(self) -> list[WatchlistItem]:
        """Return the complete watchlist."""

        return self.repository.get_all()

    def get_tickers(self) -> list[str]:
        """Return ticker symbols from the watchlist."""

        return [item.ticker for item in self.repository.get_all()]
