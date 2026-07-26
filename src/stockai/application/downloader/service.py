"""
Concurrent market data downloader.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date

# from typing import Callable

from loguru import logger

from stockai.domain.models import Quote
from stockai.domain.repositories import MarketDataProvider

from .result import DownloadFailure, DownloadResult


class MarketDataDownloader:
    """
    Downloads market data concurrently for multiple tickers.
    """

    def __init__(
        self,
        provider: MarketDataProvider,
        max_workers: int = 5,
    ):
        if max_workers < 1:
            raise ValueError("max_workers must be at least 1")

        self.provider = provider
        self.max_workers = max_workers

    def download(
        self,
        tickers: list[str],
        trade_date: date | None = None,
    ) -> DownloadResult:
        """
        Download quotes for multiple tickers concurrently.
        """

        if not tickers:
            return DownloadResult()

        quotes: list[Quote] = []
        failures: list[DownloadFailure] = []

        logger.info(
            "Starting market data download for {} tickers",
            len(tickers),
        )

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:

            future_to_ticker = {
                executor.submit(
                    self._download_one,
                    ticker,
                    trade_date,
                ): ticker
                for ticker in tickers
            }

            for future in as_completed(future_to_ticker):

                ticker = future_to_ticker[future]

                try:
                    quote = future.result()

                    quotes.append(quote)

                    logger.info(
                        "Downloaded {}",
                        ticker,
                    )

                except Exception as exc:
                    error_message = str(exc)

                    failures.append(
                        DownloadFailure(
                            ticker=ticker,
                            error=error_message,
                        )
                    )

                    logger.error(
                        "Failed to download {}: {}",
                        ticker,
                        error_message,
                    )

        logger.info(
            "Download completed: {} successful, {} failed",
            len(quotes),
            len(failures),
        )

        return DownloadResult(
            quotes=quotes,
            failures=failures,
        )

    def _download_one(
        self,
        ticker: str,
        trade_date: date | None,
    ) -> Quote:
        """Download a single ticker."""

        return self.provider.get_quote(
            ticker=ticker,
            trade_date=trade_date,
        )
