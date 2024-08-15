import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


df=pd.read_csv("articles.csv")
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    cleaned_tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]
    return ' '.join(cleaned_tokens)

df['Cleaned Summary'] = df['Summary'].apply(preprocess_text)



from transformers import pipeline

# Chargement du modèle pré-entraîné pour la classification des sentiments
sentiment_pipeline = pipeline('sentiment-analysis')

# Application du modèle sur les résumés nettoyés
df['Sentiment'] = df['Cleaned Summary'].apply(lambda x: sentiment_pipeline(x)[0]['label'])


# Exemple d'application pour la détection des sujets (ce modèle doit être pré-entraîné pour vos catégories spécifiques)
from transformers import pipeline

# Chargement du modèle pré-entraîné pour la classification des sujets
topic_pipeline = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

# Définir les catégories de sujets
categories = ['politics', 'health', 'technology', 'sports']

# Application du modèle sur les résumés nettoyés
df['Topics'] = df['Cleaned Summary'].apply(lambda x: topic_pipeline(x, candidate_labels=categories)['labels'])
