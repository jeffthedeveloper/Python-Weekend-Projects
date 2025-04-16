from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field, validator
from typing import Optional
import logging
from ..dependencies.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/examples",
    tags=["examples"]
)

logger = logging.getLogger(__name__)

class Example(BaseModel):
    """Validation for Example using Pydantic"""
    id: int = Field(..., description="ID of the example", gt=0)
    name: str = Field(..., max_length=5, description="Name of the example")

    @validator('name')
    def name_must_be_short(cls, v):
        if len(v) > 5:
            logger.warning(f"Name length validation failed: {v}")
            raise ValueError("Name must be 5 characters or less")
        return v

@router.get("/{example_id}", response_model=Example)
async def get_example(
    example_id: int,
    db: Session = Depends(get_db)
):
    """
    Get one example's details
    
    Args:
        example_id: ID of the example to retrieve (must be positive integer)
    
    Returns:
        Example: The requested example data
        
    Raises:
        HTTPException: 404 if example not found, 422 if validation fails
    """
    try:
        # Simulação de dados - substituir por busca real no banco de dados
        example_data = {
            'id': example_id,
            'name': 'test'  # Alterado para passar na validação
        }
        
        # Validação com Pydantic
        example = Example(**example_data)
        
        logger.info(f"Successfully retrieved example {example_id}")
        return example
        
    except ValueError as ve:
        logger.error(f"Validation error for example {example_id}: {str(ve)}")
        raise HTTPException(
            status_code=422,
            detail={"message": "Validation error", "errors": str(ve)}
        )
        
    except Exception as e:
        logger.exception(f"Unexpected error retrieving example {example_id}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )