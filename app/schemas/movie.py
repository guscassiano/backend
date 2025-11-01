from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class MovieBase(BaseModel):
    title: str
    genre: str
    release_year: int
    director: str
    rating: float = Field(..., ge=0, le=10)


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    release_year: Optional[int] = None
    director: Optional[str] = None
    rating: Optional[float] = Field(None, ge=0, le=10)


class MovieResponse(MovieBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
