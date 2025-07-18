from pydantic import BaseModel
from typing import Optional

class BookSchema(BaseModel):
    id: Optional[int]
    title: str
    author: str
    year: Optional[int] = None
    isbn: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    rating: Optional[int] = None

    class Config:
        from_attributes = True