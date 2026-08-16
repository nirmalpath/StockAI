from pathlib import Path

from stockai.infrastructure.watchlist import CsvWatchlistRepository


def test_load_watchlist(tmp_path: Path):

    file_path = tmp_path / "stocks.csv"

    file_path.write_text(
        "Ticker,Company\n" "RELIANCE.NS,Reliance Industries\n" "TCS.NS,Tata Consultancy Services\n",
        encoding="utf-8",
    )

    repository = CsvWatchlistRepository(file_path)

    items = repository.get_all()

    assert len(items) == 2
    assert items[0].ticker == "RELIANCE.NS"
    assert items[1].company_name == "Tata Consultancy Services"
