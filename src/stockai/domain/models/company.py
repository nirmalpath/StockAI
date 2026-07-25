"""
Domain model representing a company.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class Company:
    ticker: str
    name: str
    sector: Optional[str] = None
    industry: Optional[str] = None
    market_cap: Optional[int] = None
    pe_ratio: Optional[float] = None
