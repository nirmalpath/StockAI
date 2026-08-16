from datetime import date

from stockai.domain.models import Quote
from stockai.infrastructure.database import (
    DatabaseManager,
    SQLitePriceRepository,
    create_session_factory,
    create_sqlite_engine,
)


def create_repository():
    engine = create_sqlite_engine(":memory:")

    DatabaseManager(engine).create_tables()

    session_factory = create_session_factory(engine)

    return SQLitePriceRepository(session_factory)


def create_quote(
    ticker: str = "RELIANCE.NS",
) -> Quote:

    return Quote(
        ticker=ticker,
        trade_date=date(2026, 7, 24),
        open_price=100.0,
        high_price=110.0,
        low_price=95.0,
        close_price=105.0,
        volume=100000,
    )


def test_save_and_get_latest():

    repository = create_repository()

    quote = create_quote()

    repository.save(quote)

    result = repository.get_latest("RELIANCE.NS")

    assert result is not None
    assert result.ticker == "RELIANCE.NS"
    assert result.close_price == 105.0


def test_save_same_ticker_and_date_updates_existing_record():

    repository = create_repository()

    original = create_quote()

    repository.save(original)

    updated = Quote(
        ticker="RELIANCE.NS",
        trade_date=date(2026, 7, 24),
        open_price=101.0,
        high_price=111.0,
        low_price=96.0,
        close_price=106.0,
        volume=200000,
    )

    repository.save(updated)

    result = repository.get_latest("RELIANCE.NS")

    assert result is not None
    assert result.close_price == 106.0
    assert result.volume == 200000


def test_get_history():

    repository = create_repository()

    repository.save(
        Quote(
            ticker="TCS.NS",
            trade_date=date(2026, 7, 22),
            open_price=100.0,
            high_price=110.0,
            low_price=95.0,
            close_price=105.0,
            volume=100000,
        )
    )

    repository.save(
        Quote(
            ticker="TCS.NS",
            trade_date=date(2026, 7, 23),
            open_price=105.0,
            high_price=115.0,
            low_price=100.0,
            close_price=112.0,
            volume=120000,
        )
    )

    history = repository.get_history(
        ticker="TCS.NS",
        start_date=date(2026, 7, 22),
        end_date=date(2026, 7, 23),
    )

    assert len(history) == 2
    assert history[0].trade_date == date(2026, 7, 22)
    assert history[1].trade_date == date(2026, 7, 23)
