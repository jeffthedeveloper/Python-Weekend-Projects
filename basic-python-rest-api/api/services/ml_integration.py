import httpx
from fastapi import HTTPException
from .config import settings
from typing import Optional

class MLService:
    def __init__(self):
        self.base_url = settings.ML_SERVICE_URL
        self.enabled = settings.ENABLE_AI_FEATURES
    
    async def predict(self, data: dict) -> Optional[dict]:
        if not self.enabled or not self.base_url:
            return None
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/predict",
                    json=data,
                    timeout=10.0
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=503,
                detail=f"ML Service unavailable: {str(e)}"
            )

ml_service = MLService()