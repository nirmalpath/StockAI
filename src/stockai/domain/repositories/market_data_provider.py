"""
Interface for external market data providers.
"""

from abc import ABC, abstractmethod
from datetime import date

from stockai.domain.models import Quote


class MarketDataProvider(ABC):
    """Abstract interface for retrieving market data."""

    @abstractmethod
    def get_quote(self, ticker: str, trade_date: date | None = None) -> Quote:
        """Retrieve a quote for a ticker."""
        raise NotImplementedError

    @abstractmethod
    def get_history(
        self,
        ticker: str,
        start_date: date,
        end_date: date,
    ) -> list[Quote]:
        """Retrieve historical quotes."""
        raise NotImplementedError
