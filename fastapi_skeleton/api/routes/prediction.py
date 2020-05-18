from fastapi import APIRouter, Depends
from starlette.requests import Request

from fastapi_skeleton.core import security
from fastapi_skeleton.models.payload import HousePredictionPayload
from fastapi_skeleton.models.prediction import HousePredictionResult
from fastapi_skeleton.services.models import HousePriceModel
from fastapi_skeleton.core import config

router = APIRouter()


@router.post("/predict", response_model=HousePredictionResult, name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request) if config.API_KEY_AUTH else True,
    block_data: HousePredictionPayload = None
) -> HousePredictionResult:

    model: HousePriceModel = request.app.state.model
    prediction: HousePredictionResult = model.predict(block_data)

    return prediction
