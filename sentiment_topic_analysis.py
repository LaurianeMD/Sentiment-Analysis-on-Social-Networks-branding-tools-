# from transformers import pipeline
# import requests
# from dotenv import load_dotenv
# import os
# import psycopg2
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# import string

# # Télécharger les ressources nécessaires de NLTK
# nltk.download('punkt')
# nltk.download('stopwords')

# # Charger les variables d'environnement
# load_dotenv()

# # Connexion à la base de données PostgreSQL
# try:
#     conn = psycopg2.connect(
#         dbname=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         host=os.getenv("DB_HOST"),
#         port=os.getenv("DB_PORT")
#     )
#     cur = conn.cursor()

#     # Configurations de l'API NYT
#     API_KEY = os.getenv("NYT_API_KEY")
#     BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

#     # Charger les modèles de traitement du langage
#     sentiment_analyzer = pipeline(
#         "sentiment-analysis",
#         model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
#     )
#     topic_classifier = pipeline(
#         "zero-shot-classification",
#         model="facebook/bart-large-mnli"
#     )

#     # Fonction de nettoyage du texte
#     def clean_text(text):
#         if not text:
#             return text

#         # Mettre en minuscule et retirer la ponctuation
#         text = text.lower()
#         text = text.translate(str.maketrans("", "", string.punctuation))

#         # Tokenization et suppression des stopwords
#         words = word_tokenize(text)
#         stop_words = set(stopwords.words('english'))
#         words = [word for word in words if word not in stop_words]

#         # Reconstruire le texte nettoyé
#         cleaned_text = " ".join(words)
#         return cleaned_text

#     # Fonction pour récupérer des articles via l'API du NYT
#     def fetch_articles(query):
#         params = {
#             'q': query,
#             'api-key': API_KEY
#         }
#         try:
#             response = requests.get(BASE_URL, params=params)
#             response.raise_for_status()
#         except requests.RequestException as e:
#             print(f"Error fetching articles: {e}")
#             return {}
#         return response.json()

#     # Fonction pour analyser le sentiment d'un texte
#     def analyze_sentiment(text):
#         cleaned_text = clean_text(text)
#         if not cleaned_text:
#             return "NEUTRAL"
#         try:
#             result = sentiment_analyzer(cleaned_text)
#         except Exception as e:
#             print(f"Error analyzing sentiment: {e}")
#             return "NEUTRAL"
#         return result[0]['label']

#     # Fonction pour classer le sujet d'un texte
#     def classify_topic(text):
#         cleaned_text = clean_text(text)
#         if not cleaned_text:
#             return "unknown"

#         candidate_labels = ['politics', 'health', 'business', 'technology', 'sports', 'entertainment']
#         try:
#             result = topic_classifier(cleaned_text, candidate_labels)
#         except Exception as e:
#             print(f"Error classifying topic: {e}")
#             return "unknown"

#         if 'labels' not in result or not result['labels']:
#             return "unknown"

#         return result['labels'][0]

#     # Fonction pour sauvegarder un article dans la base de données
#     def save_article(article):
#         title = article['headline']['main']
#         abstract = article['abstract']
#         url = article['web_url']
#         published_date = article['pub_date']

#         sentiment = analyze_sentiment(abstract)
#         try:
#             topic = classify_topic(abstract)
#         except ValueError as e:
#             print(f"Error in classifying topic: {e}")
#             topic = "unknown"

#         try:
#             cur.execute(
#                 """
#                 INSERT INTO articles (title, abstract, url, published_date, sentiment, topic)
#                 VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
#                 """,
#                 (title, abstract, url, published_date, sentiment, topic)
#             )
#             article_id = cur.fetchone()[0]
#             conn.commit()
#             print(f"Article '{title}' saved with ID {article_id}")
#         except psycopg2.Error as e:
#             print(f"Error saving article to database: {e}")
#             conn.rollback()
#             raise
#         return article_id

#     # Exemple d'utilisation
#     query = "Windows crash"
#     data = fetch_articles(query)
#     articles = data.get('response', {}).get('docs', [])

#     for i, article in enumerate(articles):
#         print(f"Processing article {i + 1} of {len(articles)}...")
#         try:
#             save_article(article)
#         except Exception as e:
#             print(f"Failed to save article {i + 1}: {e}")

# finally:
#     if conn:
#         cur.close()
#         conn.close()

from transformers import pipeline
import requests
from dotenv import load_dotenv
import os
import psycopg2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from datetime import datetime

# Télécharger les ressources nécessaires de NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Charger les variables d'environnement
load_dotenv()

# Connexion à la base de données PostgreSQL
try:
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

    # Charger les modèles de traitement du langage
    sentiment_analyzer = pipeline(
        "sentiment-analysis",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )
    topic_classifier = pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli"
    )

    # Fonction de nettoyage du texte
    def clean_text(text):
        if not text:
            return text

        # Mettre en minuscule et retirer la ponctuation
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Tokenization et suppression des stopwords
        words = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]

        # Reconstruire le texte nettoyé
        cleaned_text = " ".join(words)
        return cleaned_text

    # Fonction pour récupérer des articles via l'API du NYT
    def fetch_articles(query):
        params = {
            'q': query,
            'api-key': API_KEY
        }
        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching articles: {e}")
            return {}

    # Fonction pour analyser le sentiment d'un texte
    def analyze_sentiment(text):
        cleaned_text = clean_text(text)
        if not cleaned_text:
            return "NEUTRAL"
        try:
            result = sentiment_analyzer(cleaned_text)
            return result[0]['label']
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return "NEUTRAL"

    # Fonction pour classer le sujet d'un texte
    def classify_topic(text):
        cleaned_text = clean_text(text)
        if not cleaned_text:
            return "unknown"

        candidate_labels = ['politics', 'health', 'business', 'technology', 'sports', 'entertainment']
        try:
            result = topic_classifier(cleaned_text, candidate_labels)
            return result['labels'][0] if 'labels' in result and result['labels'] else "unknown"
        except Exception as e:
            print(f"Error classifying topic: {e}")
            return "unknown"

    # Fonction pour sauvegarder un article dans la base de données
    def save_article(article):
        title = article.get('headline', {}).get('main', 'No Title')
        abstract = article.get('abstract', 'No Abstract')
        url = article.get('web_url', 'No URL')
        published_date_str = article.get('pub_date', '1900-01-01')
        
        try:
            published_date = datetime.strptime(published_date_str, '%Y-%m-%d').date()
        except ValueError:
            published_date = None

        sentiment = analyze_sentiment(abstract)
        topic = classify_topic(abstract)

        try:
            cur.execute(
                """
                INSERT INTO articles (title, abstract, url, published_date, sentiment, topic)
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
                """,
                (title, abstract, url, published_date, sentiment, topic)
            )
            article_id = cur.fetchone()[0]
            conn.commit()
            print(f"Article '{title}' saved with ID {article_id}")
        except psycopg2.Error as e:
            print(f"Error saving article to database: {e}")
            conn.rollback()
            raise
        return article_id

    # Exemple d'utilisation
    query = "Windows crash"
    data = fetch_articles(query)
    articles = data.get('response', {}).get('docs', [])

    for i, article in enumerate(articles):
        print(f"Processing article {i + 1} of {len(articles)}...")
        try:
            save_article(article)
        except Exception as e:
            print(f"Failed to save article {i + 1}: {e}")

finally:
    if conn:
        cur.close()
        conn.close()

