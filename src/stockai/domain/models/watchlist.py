"""
Domain model representing one watchlist entry.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class WatchlistItem:
    ticker: str
    company_name: str