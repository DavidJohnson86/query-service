from abc import ABC, abstractmethod

import requests
from pandas import DataFrame


class VendorRepository(ABC):
    @abstractmethod
    def fetch_data(self, endpoint: str) -> requests.Response.content:
        raise NotImplementedError

    @abstractmethod
    def unzip_and_get_data(self, content: requests.Response.content) -> DataFrame:
        raise NotImplementedError
