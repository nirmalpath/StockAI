from abc import ABC, abstractmethod

from stockai.domain.models.quote import Quote


class PriceRepository(ABC):

    @abstractmethod
    def save(self, quote: Quote) -> None:
        ...

    @abstractmethod
    def save_all(self, quotes: list[Quote]) -> None:
        ...

    @abstractmethod
    def get_latest(self, ticker: str) -> Quote | None:
        ...