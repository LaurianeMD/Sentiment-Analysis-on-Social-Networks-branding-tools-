# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
# import pandas as pd

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')


# df=pd.read_csv("articles.csv")
# def preprocess_text(text):
#     tokens = word_tokenize(text.lower())
#     stop_words = set(stopwords.words('english'))
#     lemmatizer = WordNetLemmatizer()
    
#     cleaned_tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]
#     return ' '.join(cleaned_tokens)

# df['Cleaned Summary'] = df['Summary'].apply(preprocess_text)



# from transformers import pipeline

# # Chargement du modèle pré-entraîné pour la classification des sentiments
# sentiment_pipeline = pipeline('sentiment-analysis')

# # Application du modèle sur les résumés nettoyés
# df['Sentiment'] = df['Cleaned Summary'].apply(lambda x: sentiment_pipeline(x)[0]['label'])


# # Exemple d'application pour la détection des sujets (ce modèle doit être pré-entraîné pour vos catégories spécifiques)
# from transformers import pipeline

# # Chargement du modèle pré-entraîné pour la classification des sujets
# topic_pipeline = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

# # Définir les catégories de sujets
# categories = ['politics', 'health', 'technology', 'sports']

# # Application du modèle sur les résumés nettoyés
# df['Topics'] = df['Cleaned Summary'].apply(lambda x: topic_pipeline(x, candidate_labels=categories)['labels'])



import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import pandas as pd
nltk.download('punkt')
nltk.download('stopwords')

# Charger les données

df = pd.read_csv('articles.csv')

# Fonction de nettoyage des textes
def clean_text(text):
    # Tokenization
    tokens = word_tokenize(text)
    # Conversion en minuscules
    tokens = [word.lower() for word in tokens]
    # Suppression des signes de ponctuation
    tokens = [word for word in tokens if word.isalpha()]
    # Suppression des stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Reconstruire le texte nettoyé
    cleaned_text = ' '.join(tokens)
    return cleaned_text

# Appliquer le nettoyage aux résumés des articles
df['Cleaned_Summary'] = df['Summary'].apply(clean_text)

print(df['Cleaned_Summary'].apply(type).value_counts())

print("espace vide")
print(df['Cleaned_Summary'].apply(lambda x: len(x.strip()) == 0).sum())

missing_values = df['Cleaned_Summary'].isnull().sum()
print(f"Nombre de valeurs manquantes dans 'Cleaned_Summary': {missing_values}")

df['Cleaned_Summary'] = df['Cleaned_Summary'].astype(str)

#Supprimer les espaces vides
df = df[df['Cleaned_Summary'].apply(lambda x: len(x.strip()) != 0)]

print("espace vide")
print(df['Cleaned_Summary'].apply(lambda x: len(x.strip()) == 0).sum())

# Affichage du DataFrame nettoyé
print(df[['Summary', 'Cleaned_Summary']].head())

#Save
df.to_csv('cleaned_articles.csv', index=False, encoding='utf-8')

