import json
from typing import Dict

from pandas import DataFrame
from query_service.core.repository.pipeline_repository import IPipelineRepository


class PipelineRepository(IPipelineRepository):
    def filter_currency(self, currency: str, data: DataFrame) -> Dict:
        if currency not in data:
            msg = "Currency not exists in database: {currency}."
            raise RuntimeError(msg)
        return dict(zip(data[currency], data["Date"]))

    def filter_date(self, date: str, data: DataFrame) -> Dict:
        if date not in data["Date"].values:
            msg = f"Date not exists in database: {date}. "
            raise RuntimeError(msg)
        result_dict = json.loads(
            data[(data["Date"] == date)]
            .filter(regex="^(?!Unnamed)")
            .to_json(orient="index", default_handler=str),
        )["0"]
        del result_dict[next(iter(result_dict))]
        return result_dict
