"""
Database lifecycle management.
"""

from sqlalchemy import Engine

from .base import Base


class DatabaseManager:
    """Creates and manages the StockAI database schema."""

    def __init__(self, engine: Engine):
        self.engine = engine

    def create_tables(self) -> None:
        """Create all registered database tables."""

        Base.metadata.create_all(self.engine)
