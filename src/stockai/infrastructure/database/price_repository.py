"""
SQLite implementation of the price repository.
"""

from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from stockai.domain.models import Quote
from stockai.domain.repositories import PriceRepository

from .models import StockPriceModel


class SQLitePriceRepository(PriceRepository):
    """Stores and retrieves quotes using SQLite."""

    def __init__(
        self,
        session_factory: sessionmaker[Session],
    ):
        self.session_factory = session_factory

    def save(self, quote: Quote) -> None:
        """Save one quote."""

        with self.session_factory() as session:

            existing = session.scalar(
                select(StockPriceModel).where(
                    StockPriceModel.ticker == quote.ticker,
                    StockPriceModel.trade_date == quote.trade_date,
                )
            )

            if existing:
                self._update_model(existing, quote)
            else:
                session.add(self._to_model(quote))

            session.commit()

    def save_all(
        self,
        quotes: list[Quote],
    ) -> None:
        """Save multiple quotes."""

        if not quotes:
            return

        with self.session_factory() as session:

            for quote in quotes:

                existing = session.scalar(
                    select(StockPriceModel).where(
                        StockPriceModel.ticker == quote.ticker,
                        StockPriceModel.trade_date == quote.trade_date,
                    )
                )

                if existing:
                    self._update_model(
                        existing,
                        quote,
                    )
                else:
                    session.add(self._to_model(quote))

            session.commit()

    def get_latest(
        self,
        ticker: str,
    ) -> Quote | None:
        """Return the latest available quote for a ticker."""

        with self.session_factory() as session:

            model = session.scalar(
                select(StockPriceModel)
                .where(StockPriceModel.ticker == ticker)
                .order_by(StockPriceModel.trade_date.desc())
            )

            if model is None:
                return None

            return self._to_domain(model)

    def get_history(
        self,
        ticker: str,
        start_date: date,
        end_date: date,
    ) -> list[Quote]:
        """Return historical quotes for a ticker."""

        with self.session_factory() as session:

            models = session.scalars(
                select(StockPriceModel)
                .where(
                    StockPriceModel.ticker == ticker,
                    StockPriceModel.trade_date >= start_date,
                    StockPriceModel.trade_date <= end_date,
                )
                .order_by(StockPriceModel.trade_date)
            ).all()

            return [self._to_domain(model) for model in models]

    @staticmethod
    def _to_model(
        quote: Quote,
    ) -> StockPriceModel:
        """Convert a domain quote to a database model."""

        return StockPriceModel(
            ticker=quote.ticker,
            trade_date=quote.trade_date,
            open_price=quote.open_price,
            high_price=quote.high_price,
            low_price=quote.low_price,
            close_price=quote.close_price,
            volume=quote.volume,
            previous_close=quote.previous_close,
            high_52_week=quote.high_52_week,
            low_52_week=quote.low_52_week,
        )

    @staticmethod
    def _to_domain(
        model: StockPriceModel,
    ) -> Quote:
        """Convert a database model to a domain quote."""

        return Quote(
            ticker=model.ticker,
            trade_date=model.trade_date,
            open_price=model.open_price,
            high_price=model.high_price,
            low_price=model.low_price,
            close_price=model.close_price,
            volume=model.volume,
            previous_close=model.previous_close,
            high_52_week=model.high_52_week,
            low_52_week=model.low_52_week,
        )

    @staticmethod
    def _update_model(
        model: StockPriceModel,
        quote: Quote,
    ) -> None:
        """Update an existing database model."""

        model.open_price = quote.open_price
        model.high_price = quote.high_price
        model.low_price = quote.low_price
        model.close_price = quote.close_price
        model.volume = quote.volume
        model.previous_close = quote.previous_close
        model.high_52_week = quote.high_52_week
        model.low_52_week = quote.low_52_week
