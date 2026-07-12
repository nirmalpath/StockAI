from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class StockPrice(Base):

    __tablename__ = "stock_prices"

    id = Column(Integer, primary_key=True)

    ticker = Column(String)

    price = Column(Float)

    open = Column(Float)

    high = Column(Float)

    low = Column(Float)

    volume = Column(Float)

    previous_close = Column(Float)

    high52 = Column(Float)

    low52 = Column(Float)

    off_high = Column(Float)

    pe = Column(Float)

    sector = Column(String)

    market_cap = Column(Float)

    download_date = Column(String)