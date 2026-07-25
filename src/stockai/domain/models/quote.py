"""
Domain model representing a market quote.
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(slots=True)
class Quote:
    ticker: str
    trade_date: date
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: int
    previous_close: Optional[float] = None
    high_52_week: Optional[float] = None
    low_52_week: Optional[float] = None
