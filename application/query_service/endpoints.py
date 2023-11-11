from typing import Dict, Optional, Union

from fastapi import APIRouter, Depends, FastAPI, HTTPException, Query, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from query_service.controller.dto import FxRateRequestDTO
from query_service.core.exceptions import QueryServiceException
from query_service.infrastructure.pipeline_repository import PipelineRepository
from query_service.infrastructure.vendor_repository import VendorRepository
from query_service.service.use_cases import CurrencyUseCase

app = FastAPI()
router = APIRouter()


vendor_repository = VendorRepository()
pipeline_repository = PipelineRepository()


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Welcome to the FX Rates Query Service API"}


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:  # noqa: ARG001
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    return JSONResponse(content={"detail": exc.errors()}, status_code=status_code)


def validate_fx_rate_request(
    currency: Optional[str] = Query(None, description="Currency code"),
    date: Optional[str] = Query(None, description="Date in the format YYYY-MM-DD"),
) -> FxRateRequestDTO:
    return FxRateRequestDTO(currency=currency, date=date)


@router.get("/fx_rates", tags=["FX RATES"])
async def get_fx_rates(
    request: FxRateRequestDTO = Depends(validate_fx_rate_request),
) -> Union[Dict[float,str], Dict[str, Union[float, None]]]:
    """Simple REST API with a single endpoint that returns data to a user based
    on currency and date requests. Data to be fetched once at the start of the process
    and should be kept in the memory"""
    try:
        currency_use_case = CurrencyUseCase(
            vendor_repository=vendor_repository, pipeline_repository=pipeline_repository,
        )
        return currency_use_case.get_fx_rates(request.currency, request.date)
    except QueryServiceException as exc:
        raise HTTPException(status_code=400, detail=exc.message)


app.include_router(router, prefix="/api")
