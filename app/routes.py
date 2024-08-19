# from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.orm import Session
# from app.models import Article
# from app.database import get_db
# from app.schemas import ArticleCreate, ArticleResponse

# router = APIRouter()

# @router.get("/articles/{article_id}", response_model=ArticleResponse)
# def read_article(article_id: int, db: Session = Depends(get_db)):
#     article = db.query(Article).filter(Article.id == article_id).first()
#     if article is None:
#         raise HTTPException(status_code=404, detail="Article not found")
#     return article

# @router.post("/articles/", response_model=ArticleResponse)
# def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
#     db_article = Article(**article.dict())
#     db.add(db_article)
#     db.commit()
#     db.refresh(db_article)
#     return db_article


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List
from app import models, schemas, database

router = APIRouter()

@router.post("/articles/", response_model=schemas.ArticleResponse)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(database.get_db)):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@router.get("/articles/{article_id}", response_model=schemas.ArticleResponse)
def read_article(article_id: int, db: Session = Depends(database.get_db)):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article

@router.get("/articles/search/", response_model=List[schemas.ArticleResponse])
def search_articles(query: str, db: Session = Depends(database.get_db)):
    articles = db.query(models.Article).filter(
        or_(
            models.Article.title.contains(query),
            models.Article.abstract.contains(query),
            models.Article.url.contains(query)
        )
    ).all()
    
    return articles
