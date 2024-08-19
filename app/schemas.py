from pydantic import BaseModel

class ArticleBase(BaseModel):
    title: str
    abstract: str
    url: str
    published_date: str
    sentiment: str
    topic: str

class ArticleCreate(ArticleBase):
    pass

class ArticleResponse(ArticleBase):
    id: int

    class Config:
        orm_mode = True
