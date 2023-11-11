from functools import wraps
from typing import Callable, Dict, Union

from query_service.core.exceptions import FxRatesErrorCode, QueryServiceException
from query_service.core.repository.vendor_repository import VendorRepository
from query_service.infrastructure.pipeline_repository import PipelineRepository


def query_service_exception_handler(
    exception_type: tuple,
    error_indicator: FxRatesErrorCode,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: str, **kwargs: dict) -> Union[Callable, Exception]:
            try:
                return func(*args, **kwargs)
            except exception_type as e:
                raise QueryServiceException(message=str(e), error_code=error_indicator) from e

        return wrapper

    return decorator


class CurrencyUseCase:
    def __init__(self, vendor_repository: VendorRepository, pipeline_repository: PipelineRepository) -> None:
        self.vendor_repository = vendor_repository
        self.pipeline_repository = pipeline_repository

    @query_service_exception_handler(
        (RuntimeError),
        FxRatesErrorCode.FX_RATES_RETRIEVAL_ERROR,
    )
    def get_fx_rates(self, currency: str, date: str) -> Dict[Union[str, float], Union[str, float]]:
        if currency is not None:
            filtered_data = self.pipeline_repository.filter_currency(
                currency=currency, data=self.vendor_repository.fetched_data,
            )
        if date is not None:
            filtered_data = self.pipeline_repository.filter_date(date=date, data=self.vendor_repository.fetched_data)
        return filtered_data
