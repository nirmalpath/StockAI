"""
Interface for retrieving the StockAI watchlist.
"""

from abc import ABC, abstractmethod

from stockai.domain.models import WatchlistItem


class WatchlistRepository(ABC):
    """Abstract interface for watchlist storage."""

    @abstractmethod
    def get_all(self) -> list[WatchlistItem]:
        """Return all watchlist entries."""
        raise NotImplementedError
