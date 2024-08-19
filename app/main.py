# from fastapi import FastAPI, HTTPException
# from typing import List
# from pydantic import BaseModel

# app = FastAPI()

# # Votre modèle
# class ArticleBase(BaseModel):
#     title: str
#     abstract: str
#     url: str
#     published_date: str
#     sentiment: str
#     topic: str

# class ArticleCreate(ArticleBase):
#     pass

# class ArticleResponse(ArticleBase):
#     id: int

#     class Config:
#         orm_mode = True

# # Simulez une base de données pour les exemples
# fake_db = []

# @app.post("/articles/", response_model=ArticleResponse)
# async def create_article(article: ArticleCreate):
#     article_data = article.dict()
#     article_data['id'] = len(fake_db) + 1
#     fake_db.append(article_data)
#     return article_data

# @app.get("/articles/{article_id}", response_model=ArticleResponse)
# async def read_article(article_id: int):
#     for article in fake_db:
#         if article['id'] == article_id:
#             return article
#     raise HTTPException(status_code=404, detail="Article not found")

from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI()

# Inclure les routes
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment and Topic Analysis API!"}
