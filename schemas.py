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


# from pydantic import BaseModel
# from typing import Optional

# class ArticleBase(BaseModel):
#     title: str
#     abstract: Optional[str] = None
#     url: Optional[str] = None
#     published_date: Optional[str] = None
#     sentiment: Optional[str] = 'Not analyzed'
#     topic: Optional[str] = 'Not categorized'

# class ArticleCreate(ArticleBase):
#     pass

# class Article(ArticleBase):
#     id: int

#     class Config:
#         orm_mode = True

# from pydantic import BaseModel
# from typing import Optional

# class ArticleCreate(BaseModel):
#     title: str
#     content: str
#     author: Optional[str] = None

# class ArticleResponse(BaseModel):
#     id: int
#     title: str
#     content: str
#     author: Optional[str] = None

    # class Config:
    #     orm_mode = True

