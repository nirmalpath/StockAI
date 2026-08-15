"""
Domain model representing a company.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Company:
    ticker: str
    name: str
    sector: str | None = None
    industry: str | None = None
    market_cap: int | None = None
    pe_ratio: float | None = None
