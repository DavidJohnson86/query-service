import logging
from io import BytesIO
from zipfile import ZipFile

import requests
from pandas import DataFrame, read_csv
from query_service.app_config import ENDPOINT

logger = logging.getLogger(__name__)

class VendorRepository:
    def __init__(self) -> None:
        self.fetched_data = self.unzip_and_get_data(content=self.fetch_data(endpoint=ENDPOINT))

    def fetch_data(self, endpoint: str) -> requests.Response.content:
        logger.info("Fetch data from remote.")
        return requests.get(endpoint).content

    def unzip_and_get_data(self, content: requests.Response.content) -> DataFrame:
        with ZipFile(BytesIO(content)) as file:
            with file.open("eurofxref-hist.csv") as csv_file:
                logger.info("Reading File.")
                return read_csv(csv_file)
