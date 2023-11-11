from typing import Optional

from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, validator


class FxRateRequestDTO(BaseModel):
    currency: Optional[str]
    date: Optional[str]

    @validator("date")
    def check_currency_or_date(cls: object, date: str, values: object) -> str:  # noqa: N805
        if not values.get("currency") and not date:
            msg = "Currency or Date required."
            raise RequestValidationError(msg)
        return date
