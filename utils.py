# utils.py

import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Télécharger les ressources nécessaires de NLTK lors de la première exécution
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def clean_text(text: str) -> str:
    if not text:
        return ""

    # Mettre en minuscule
    text = text.lower()

    # Retirer la ponctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenizer le texte
    tokens = word_tokenize(text)

    # Retirer les stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Rejoindre les tokens nettoyés
    cleaned_text = " ".join(tokens)

    return cleaned_text
