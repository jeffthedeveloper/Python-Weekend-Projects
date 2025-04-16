from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from ..schemas.example import ExampleOut
from ..services.example_service import get_example_by_id
from ..dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/examples",
    tags=["examples"]
)

@router.get("/{example_id}", response_model=ExampleOut)
async def get_example(
    example_id: int, 
    db: Session = Depends(get_db)
):
    """
    Get a specific example by ID
    
    - **example_id**: ID of the example to retrieve
    - Returns: Example data if found
    """
    example = await get_example_by_id(db, example_id)
    if not example:
        raise HTTPException(
            status_code=404,
            detail="Example not found"
        )
    return example