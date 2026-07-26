"""
Application dependency composition.
"""

from pathlib import Path

from stockai.application.downloader import MarketDataDownloader
from stockai.application.market_data import MarketDataService
from stockai.application.watchlist import WatchlistService
from stockai.infrastructure.database import (
    DatabaseManager,
    SQLitePriceRepository,
    create_session_factory,
    create_sqlite_engine,
)
from stockai.infrastructure.market_data import (
    YahooFinanceProvider,
)
from stockai.infrastructure.watchlist import (
    CsvWatchlistRepository,
)


def create_market_data_service(
    database_path: str | Path,
) -> MarketDataService:
    """Create the fully configured market data service."""

    provider = YahooFinanceProvider()

    downloader = MarketDataDownloader(
        provider=provider,
        max_workers=5,
    )

    engine = create_sqlite_engine(database_path)

    DatabaseManager(engine).create_tables()

    session_factory = create_session_factory(engine)

    repository = SQLitePriceRepository(session_factory)

    return MarketDataService(
        downloader=downloader,
        price_repository=repository,
    )


def create_watchlist_service(
    watchlist_path: str | Path,
) -> WatchlistService:
    """Create the watchlist service."""

    repository = CsvWatchlistRepository(watchlist_path)

    return WatchlistService(repository)
