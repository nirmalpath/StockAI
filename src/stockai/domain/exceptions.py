"""Domain-specific exceptions for market data operations."""

from __future__ import annotations


class MarketDataError(Exception):
    """
    Raised when the market data provider fails to return a valid quote
    (network errors, parse errors, provider-specific errors, etc.).

    Provider implementations should wrap lower-level exceptions in this
    type so callers can handle provider failures explicitly.
    """

    pass
