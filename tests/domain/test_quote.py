from datetime import date

from stockai.domain.models import Quote


def test_quote_creation():
    quote = Quote(
        ticker="RELIANCE.NS",
        ##trade_date=date.today(),
        trade_date=date(2026, 7, 24),
        open_price=100,
        high_price=105,
        low_price=99,
        close_price=104,
        volume=1000,
    )

    assert quote.ticker == "RELIANCE.NS"
