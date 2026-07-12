from dataclasses import dataclass
from typing import Optional


@dataclass
class Quote:

    ticker: str

    current_price: float

    previous_close: float

    open_price: float

    high: float

    low: float

    volume: int

    high_52: float

    low_52: float

    market_cap: Optional[int]

    pe_ratio: Optional[float]

    sector: Optional[str]    