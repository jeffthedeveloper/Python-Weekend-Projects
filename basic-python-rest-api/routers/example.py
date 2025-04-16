from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..schemas.example import ExampleIn, ExampleOut, ExampleUpdate
from ..services.example_service import (
    create_example,
    get_example_by_id,
    get_all_examples,
    update_example,
    delete_example
)
from ..dependencies.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/examples",
    tags=["examples"]
)

@router.get("/", response_model=List[ExampleOut])
async def read_all_examples(
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Retrieve all examples with pagination"""
    return await get_all_examples(db, skip=skip, limit=limit)

@router.post("/", response_model=ExampleOut, status_code=status.HTTP_201_CREATED)
async def create_new_example(
    example: ExampleIn, 
    db: Session = Depends(get_db)
):
    """Create a new example"""
    return await create_example(db, example)

@router.put("/{example_id}", response_model=ExampleOut)
async def update_existing_example(
    example_id: int, 
    example: ExampleUpdate,
    db: Session = Depends(get_db)
):
    """Update an existing example"""
    updated = await update_example(db, example_id, example)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Example not found"
        )
    return updated

@router.delete("/{example_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_example(
    example_id: int,
    db: Session = Depends(get_db)
):
    """Delete an example"""
    if not await delete_example(db, example_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Example not found"
        )