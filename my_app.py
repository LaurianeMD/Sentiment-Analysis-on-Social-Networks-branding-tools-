import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Télécharger les ressources nécessaires de NLTK
nltk.download('punkt')
nltk.download('stopwords')

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

# CSS pour ajouter une image de fond à l'application Streamlit
page_bg_img = '''
<style>
.stApp {
    background-image: url("bgr.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''


# Appliquer le CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Interface utilisateur avec Streamlit
st.title("Sentiment and Topic Analysis")

# Input text area
input_text = st.text_area("Enter text for analysis:", "")

if st.button("Analyze"):
    if input_text:
        sentiment = analyze_sentiment(input_text)
        topic = classify_topic(input_text)
        st.write(f"Sentiment: {sentiment}")
        st.write(f"Topic: {topic}")
    else:
        st.write("Please enter some text to analyze.")
