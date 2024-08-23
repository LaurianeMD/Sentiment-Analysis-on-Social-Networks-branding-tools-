# schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional

class ArticleBase(BaseModel):
    title: str
    abstract: Optional[str] = None
    url: str
    published_date: Optional[date] = None
    sentiment: Optional[str] = None
    topic: Optional[str] = None

class ArticleCreate(ArticleBase):
    pass

class ArticleResponse(ArticleBase):
    id: int

    class Config:
        orm_mode = True

class AnalyzeRequest(BaseModel):
    text: str
