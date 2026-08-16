"""
CSV implementation of the watchlist repository.
"""

import csv
from pathlib import Path

from stockai.domain.models import WatchlistItem
from stockai.domain.repositories import WatchlistRepository


class CsvWatchlistRepository(WatchlistRepository):
    """Loads watchlist entries from a CSV file."""

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

    def get_all(self) -> list[WatchlistItem]:
        """Load all watchlist entries from CSV."""

        if not self.file_path.exists():
            raise FileNotFoundError(f"Watchlist file not found: {self.file_path}")

        items: list[WatchlistItem] = []

        with self.file_path.open(
            mode="r",
            encoding="utf-8",
            newline="",
        ) as file:

            reader = csv.DictReader(file)

            for row_number, row in enumerate(reader, start=2):
                ticker = (row.get("Ticker") or "").strip()
                company = (row.get("Company") or "").strip()

                if not ticker:
                    raise ValueError(f"Missing ticker at row {row_number}")

                if not company:
                    raise ValueError(f"Missing company at row {row_number}")

                items.append(
                    WatchlistItem(
                        ticker=ticker,
                        company_name=company,
                    )
                )

        return items
