import requests
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()  # Charger les variables d'environnement

# Configurations PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cur = conn.cursor()

# Configurations de l'API NYT
API_KEY = os.getenv("NYT_API_KEY")
BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

def fetch_articles(query):
    params = {
        'q': query,
        'api-key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def save_article(article):
    cur.execute(
        """
        INSERT INTO articles (title, abstract, url, published_date)
        VALUES (%s, %s, %s, %s) RETURNING id;
        """,
        (article['headline']['main'], article['abstract'], article['web_url'], article['pub_date'])
    )
    article_id = cur.fetchone()[0]
    conn.commit()
    return article_id

# Exemple d'utilisation
query = "Windows crash"  # Exemple de requête
data = fetch_articles(query)
articles = data['response']['docs']

for article in articles:
    save_article(article)

# Fermer la connexion
cur.close()
conn.close()
