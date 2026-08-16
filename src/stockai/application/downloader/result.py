"""
Result models for market data downloads.
"""

from dataclasses import dataclass, field

from stockai.domain.models import Quote


@dataclass(slots=True)
class DownloadFailure:
    """Represents a failed ticker download."""

    ticker: str
    error: str


@dataclass(slots=True)
class DownloadResult:
    """Contains the outcome of a batch market data download."""

    quotes: list[Quote] = field(default_factory=list)
    failures: list[DownloadFailure] = field(default_factory=list)

    @property
    def successful_count(self) -> int:
        """Return the number of successfully downloaded quotes."""

        return len(self.quotes)

    @property
    def failed_count(self) -> int:
        """Return the number of failed downloads."""

        return len(self.failures)
