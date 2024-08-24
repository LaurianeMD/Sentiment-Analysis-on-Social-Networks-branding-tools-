# # main.py

# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# import requests
# from datetime import datetime
# from dotenv import load_dotenv
# import os

# from database import SessionLocal, engine
# import models
# import schemas
# from sentiment_topic_analysis import analyze_sentiment, classify_topic

# # Charger les variables d'environnement
# load_dotenv()

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="Sentiment and Topic Analysis API",
#     description="API for analyzing sentiment and topics of articles",
#     version="1.0.0"
# )

# # Dépendance pour obtenir une session de base de données
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Endpoint racine pour vérifier que l'API fonctionne
# @app.get("/", tags=["Root"])
# def read_root():
#     return {"message": "Welcome to the Sentiment and Topic Analysis API!"}

# # Endpoint pour récupérer tous les articles ou filtrer par requête
# @app.get("/articles/", response_model=List[schemas.ArticleResponse], tags=["Articles"])
# def get_articles(query: str = None, db: Session = Depends(get_db)):
#     if query:
#         articles = db.query(models.Article).filter(models.Article.title.ilike(f"%{query}%")).all()
#     else:
#         articles = db.query(models.Article).all()
#     return articles

# # Endpoint pour récupérer des articles depuis l'API NYT et les stocker dans la base de données
# @app.post("/articles/fetch/", response_model=List[schemas.ArticleResponse], tags=["Articles"])
# def fetch_and_store_articles(query: str, db: Session = Depends(get_db)):
#     nyt_api_key = os.getenv("NYT_API_KEY")
#     if not nyt_api_key:
#         raise HTTPException(status_code=500, detail="NYT API key not configured.")
    
#     url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
#     params = {
#         "q": query,
#         "api-key": nyt_api_key
#     }
#     response = requests.get(url, params=params)
#     if response.status_code != 200:
#         raise HTTPException(status_code=response.status_code, detail="Error fetching articles from NYT API.")
    
#     data = response.json()
#     articles = data.get("response", {}).get("docs", [])
#     if not articles:
#         raise HTTPException(status_code=404, detail="No articles found for the given query.")
    
#     stored_articles = []
#     for article in articles:
#         title = article.get("headline", {}).get("main")
#         abstract = article.get("abstract")
#         url = article.get("web_url")
#         published_date_str = article.get("pub_date")

#         # Convertir la date en format date
#         try:
#             published_date = datetime.fromisoformat(published_date_str).date()
#         except:
#             published_date = None

#         sentiment = analyze_sentiment(abstract or "")
#         topic = classify_topic(abstract or "")

#         article_obj = models.Article(
#             title=title,
#             abstract=abstract,
#             url=url,
#             published_date=published_date,
#             sentiment=sentiment,
#             topic=topic
#         )

#         # Vérifier si l'article existe déjà
#         existing_article = db.query(models.Article).filter(models.Article.url == url).first()
#         if not existing_article:
#             db.add(article_obj)
#             db.commit()
#             db.refresh(article_obj)
#             stored_articles.append(article_obj)
    
#     return stored_articles

# # Endpoint pour analyser un texte fourni par l'utilisateur
# @app.post("/analyze/", tags=["Analysis"])
# def analyze_text(request: schemas.AnalyzeRequest):
#     sentiment = analyze_sentiment(request.text)
#     topic = classify_topic(request.text)
#     return {
#         "sentiment": sentiment,
#         "topic": topic
#     }


# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

from database import SessionLocal, engine
import models
import schemas
from sentiment_topic_analysis import analyze_sentiment, classify_topic

# Charger les variables d'environnement
load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sentiment and Topic Analysis API",
    description="API for analyzing sentiment and topics of articles",
    version="1.0.0"
)

# Dépendance pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint racine pour vérifier que l'API fonctionne
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Sentiment and Topic Analysis API!"}

# Endpoint pour récupérer tous les articles ou filtrer par requête
@app.get("/articles/", response_model=List[schemas.ArticleResponse], tags=["Articles"])
def get_articles(query: str = None, db: Session = Depends(get_db)):
    if query:
        articles = db.query(models.Article).filter(models.Article.title.ilike(f"%{query}%")).all()
    else:
        articles = db.query(models.Article).all()
    return articles

# Endpoint pour récupérer des articles depuis l'API NYT et les stocker dans la base de données
@app.post("/articles/fetch/", response_model=List[schemas.ArticleResponse], tags=["Articles"])
def fetch_and_store_articles(query: str, db: Session = Depends(get_db)):
    nyt_api_key = os.getenv("NYT_API_KEY")
    if not nyt_api_key:
        raise HTTPException(status_code=500, detail="NYT API key not configured.")
    
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params = {
        "q": query,
        "api-key": nyt_api_key
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching articles from NYT API.")
    
    data = response.json()
    articles = data.get("response", {}).get("docs", [])
    if not articles:
        raise HTTPException(status_code=404, detail="No articles found for the given query.")
    
    stored_articles = []
    for article in articles:
        title = article.get("headline", {}).get("main")
        abstract = article.get("abstract")
        url = article.get("web_url")
        published_date_str = article.get("pub_date")

        # Convertir la date en format date
        try:
            published_date = datetime.fromisoformat(published_date_str).date()
        except:
            published_date = None

        sentiment = analyze_sentiment(abstract or "")
        topic = classify_topic(abstract or "")

        article_obj = models.Article(
            title=title,
            abstract=abstract,
            url=url,
            published_date=published_date,
            sentiment=sentiment,
            topic=topic
        )

        # Vérifier si l'article existe déjà
        existing_article = db.query(models.Article).filter(models.Article.url == url).first()
        if not existing_article:
            db.add(article_obj)
            db.commit()
            db.refresh(article_obj)
            stored_articles.append(article_obj)
    
    return stored_articles

# Endpoint pour analyser un texte fourni par l'utilisateur
@app.post("/analyze/", tags=["Analysis"])
def analyze_text(request: schemas.AnalyzeRequest):
    sentiment = analyze_sentiment(request.text)
    topic = classify_topic(request.text)
    return {
        "sentiment": sentiment,
        "topic": topic
    }

