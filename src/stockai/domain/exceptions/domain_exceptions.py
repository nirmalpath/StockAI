class StockAIError(Exception):
    """Base exception."""


class InvalidTickerError(StockAIError):
    """Ticker is invalid."""


class QuoteNotFoundError(StockAIError):
    """Quote not found."""