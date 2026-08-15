"""
Domain model representing a market quote.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class Quote:
    ticker: str
    trade_date: date
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: int
    previous_close: float | None = None
    high_52_week: float | None = None
    low_52_week: float | None = None
