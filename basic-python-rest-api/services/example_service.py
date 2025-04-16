from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from ..models.example import Example
from ..schemas.example import ExampleCreate, ExampleUpdate

async def get_example(db: AsyncSession, example_id: int) -> Optional[Example]:
    result = await db.execute(select(Example).filter(Example.id == example_id))
    return result.scalars().first()

async def get_examples(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Example]:
    result = await db.execute(select(Example).offset(skip).limit(limit))
    return result.scalars().all()

async def create_example(db: AsyncSession, example: ExampleCreate) -> Example:
    db_example = Example(**example.dict())
    db.add(db_example)
    await db.commit()
    await db.refresh(db_example)
    return db_example

async def update_example(
    db: AsyncSession, 
    example_id: int, 
    example: ExampleUpdate
) -> Optional[Example]:
    db_example = await get_example(db, example_id)
    if db_example:
        update_data = example.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_example, key, value)
        await db.commit()
        await db.refresh(db_example)
    return db_example

async def delete_example(db: AsyncSession, example_id: int) -> bool:
    db_example = await get_example(db, example_id)
    if db_example:
        await db.delete(db_example)
        await db.commit()
        return True
    return False