"""Domain exceptions."""

from enum import Enum
from typing import Optional


class FxRatesErrorCode(Enum):
    FX_RATES_RETRIEVAL_ERROR = "Unable to retrieve data"


class QueryServiceException(BaseException):
    def __init__(
        self,
        message: str,
        error_code: FxRatesErrorCode,
        error_cause: Optional[BaseException] = None,
    ) -> None:
        super().__init__(message, error_code, error_cause)
        self.message = message
        self.error_code = error_code
        self.error_cause = error_cause
