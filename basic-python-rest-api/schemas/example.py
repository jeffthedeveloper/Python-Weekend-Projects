from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class ExampleBase(BaseModel):
    name: str = Field(..., max_length=50, example="Sample Name")
    description: Optional[str] = Field(None, max_length=200)

class ExampleCreate(ExampleBase):
    pass

class ExampleUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = Field(None, max_length=200)

class ExampleInDB(ExampleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ExampleResponse(ExampleInDB):
    pass