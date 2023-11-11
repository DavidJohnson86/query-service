from typing import Dict

from pydantic import BaseModel


class CurrencyData(BaseModel):
    date: str
    rates: Dict[str, float]
