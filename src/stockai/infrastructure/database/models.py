"""
SQLAlchemy persistence models.
"""

from datetime import date

from sqlalchemy import Date, Float, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class StockPriceModel(Base):
    """
    Database representation of a daily stock price.
    """

    __tablename__ = "stock_prices"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    ticker: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True,
    )

    trade_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    open_price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    high_price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    low_price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    close_price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    volume: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    previous_close: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    high_52_week: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    low_52_week: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    __table_args__ = (
        UniqueConstraint(
            "ticker",
            "trade_date",
            name="uq_stock_price_ticker_date",
        ),
    )
