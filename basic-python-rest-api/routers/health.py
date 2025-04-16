from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..utils.health_check import check_database_connection

router = APIRouter(
    prefix="/health",
    tags=["health"]
)

@router.get("/")
async def health_check(db: Session = Depends(get_db)):
    """
    Health check endpoint
    
    Returns:
        dict: Status of the API and its dependencies
    """
    db_status = await check_database_connection(db)
    
    return {
        "status": "healthy",
        "database": db_status,
        "version": "1.0.0",
        "services": {
            "cache": "enabled",
            "ml_service": "disabled"
        }
    }