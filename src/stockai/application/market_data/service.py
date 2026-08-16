"""
Application service for downloading and persisting market data.
"""

from datetime import date

from loguru import logger

from stockai.application.downloader import (
    DownloadResult,
    MarketDataDownloader,
)
from stockai.domain.repositories import PriceRepository


class MarketDataService:
    """Coordinates downloading and persistence of market data."""

    def __init__(
        self,
        downloader: MarketDataDownloader,
        price_repository: PriceRepository,
    ):
        self.downloader = downloader
        self.price_repository = price_repository

    def download_and_store(
        self,
        tickers: list[str],
        trade_date: date | None = None,
    ) -> DownloadResult:
        """
        Download market data and persist successful quotes.
        """

        logger.info(
            "Starting market data pipeline for {} tickers",
            len(tickers),
        )

        result = self.downloader.download(
            tickers=tickers,
            trade_date=trade_date,
        )

        if result.quotes:
            self.price_repository.save_all(result.quotes)

            logger.info(
                "Persisted {} quotes",
                len(result.quotes),
            )

        logger.info(
            "Market data pipeline completed: " "{} successful, {} failed",
            result.successful_count,
            result.failed_count,
        )

        return result
