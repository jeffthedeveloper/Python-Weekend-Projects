from fastapi import APIRouter, Depends
from ..services.ml_integration import ml_service
from ..schemas.ai import PredictionRequest, PredictionResponse

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/predict", response_model=PredictionResponse)
async def make_prediction(request: PredictionRequest):
    result = await ml_service.predict(request.dict())
    if result is None:
        return {"message": "AI features are disabled"}
    return result