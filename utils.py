# # utils.py

# import nltk
# import string
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# nltk.download('punkt')


# # Télécharger les ressources nécessaires de NLTK lors de la première exécution
# nltk.download('punkt', quiet=True)
# nltk.download('stopwords', quiet=True)

# def clean_text(text: str) -> str:
#     if not text:
#         return ""

#     # Mettre en minuscule
#     text = text.lower()

#     # Retirer la ponctuation
#     text = text.translate(str.maketrans("", "", string.punctuation))

#     # Tokenizer le texte
#     tokens = word_tokenize(text)

#     # Retirer les stopwords
#     stop_words = set(stopwords.words('english'))
#     tokens = [word for word in tokens if word not in stop_words]

#     # Rejoindre les tokens nettoyés
#     cleaned_text = " ".join(tokens)

#     return cleaned_text

import requests
from typing import List, Dict
from transformers import pipeline

def fetch_articles(query: str, api_key: str) -> List[Dict]:
    try:
        response = requests.get(
            "https://api.nytimes.com/svc/search/v2/articlesearch.json",
            params={"q": query, "api-key": api_key}
        )
        response.raise_for_status()
        data = response.json()
        return data['response']['docs']
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except Exception as err:
        print(f"An error occurred: {err}")
        return []

def analyze_text(title: str, content: str, sentiment_pipeline, topic_pipeline) -> Dict[str, str]:
    result = {
        "sentiment": sentiment_pipeline(content),
        "topic": topic_pipeline(content)
    }
    return result
