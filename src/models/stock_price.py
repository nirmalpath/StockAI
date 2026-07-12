from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float, Date


class Base(DeclarativeBase):
    pass


class StockPrice(Base):
    __tablename__ = "stock_prices"

    id = Column(Integer, primary_key=True)

    ticker = Column(String, index=True)

    trade_date = Column(Date, index=True)

    open_price = Column(Float)

    high_price = Column(Float)

    low_price = Column(Float)

    close_price = Column(Float)

    previous_close = Column(Float)

    volume = Column(Float)

    high_52 = Column(Float)

    low_52 = Column(Float)

class CompanyProfile(Base):

    __tablename__ = "company_profiles"

    ticker = Column(String, primary_key=True)

    company = Column(String)

    sector = Column(String)

    industry = Column(String)

    market_cap = Column(Float)

    pe_ratio = Column(Float)

    dividend_yield = Column(Float)

    last_updated = Column(Date)