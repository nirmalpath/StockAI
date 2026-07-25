from abc import ABC, abstractmethod


class CompanyRepository(ABC):

    @abstractmethod
    def get_company(self, symbol: str):
        """Return company information for the given symbol."""
        pass

    @abstractmethod
    def save_company(self, company) -> None:
        """Save company information."""
        pass
