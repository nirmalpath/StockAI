"""
Database connection management.
"""

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def create_sqlite_engine(database_path: str | Path) -> Engine:
    """
    Create a SQLAlchemy engine for SQLite.
    """

    path = Path(database_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    database_url = f"sqlite:///{path}"

    return create_engine(
        database_url,
        future=True,
    )
