"""
StockAI application entry point.
"""

from pathlib import Path

from loguru import logger

from stockai.application.bootstrap import (
    create_market_data_service,
    create_watchlist_service,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

WATCHLIST_PATH = PROJECT_ROOT / "config" / "stocks.csv"

DATABASE_PATH = PROJECT_ROOT / "database" / "stocks.db"


def main() -> None:
    """Run the StockAI market data pipeline."""

    logger.info("Starting StockAI")

    watchlist_service = create_watchlist_service(WATCHLIST_PATH)

    tickers = watchlist_service.get_tickers()

    logger.info(
        "Loaded {} stocks from watchlist",
        len(tickers),
    )

    market_data_service = create_market_data_service(DATABASE_PATH)

    result = market_data_service.download_and_store(tickers)

    logger.info(
        "Completed: {} successful, {} failed",
        result.successful_count,
        result.failed_count,
    )


if __name__ == "__main__":
    main()
