from abc import ABC, abstractmethod
from typing import Dict

from pandas import DataFrame


class IPipelineRepository(ABC):
    @abstractmethod
    def filter_currency(self, currency: str, data: DataFrame) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def filter_date(self, date: str, data: DataFrame) -> Dict:
        raise NotImplementedError
