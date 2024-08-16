from transformers import pipeline
import pandas as pd
# from cleaning import clean_text
TF_ENABLE_ONEDNN_OPTS=0

# Utilisation d'un modèle pré-entraîné de Hugging Face pour l'analyse des sentiments
sentiment_analyzer = pipeline('sentiment-analysis')

#importation des données nettoyées
df = pd.read_csv('cleaned_articles.csv')

# Application du modèle aux résumés nettoyés
df['Sentiment'] = df['Cleaned_Summary'].apply(lambda x: sentiment_analyzer(x)[0]['label'])

# Affichage des résultats
print(df[['Cleaned_Summary', 'Sentiment']].head())


# Pour la classification des sujets

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Exemple de pipeline pour classifier les articles par sujet
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Exemple de données d'entraînement pour la classification des sujets
# Vous devrez ajuster cette partie avec des données spécifiques pour entraîner le modèle.
X_train = df['Cleaned_Summary']
y_train = df['Section']  # Utilisation de la section comme label pour les sujets
model.fit(X_train, y_train)

# Prédiction des sujets pour les articles
df['Predicted_Topic'] = model.predict(df['Cleaned_Summary'])

# Affichage des prédictions
print(df[['Cleaned_Summary', 'Predicted_Topic']].head())


# ##---------------------------
# from transformers import pipeline
# import pandas as pd

# # Charger le DataFrame nettoyé
# df = pd.read_csv('cleaned_articles.csv')
# print("les colonnes:",df.columns)

# # Liste des modèles à comparer
# models = [
#     "distilbert-base-uncased-finetuned-sst-2-english",
#     "bert-base-uncased",
#     "roberta-base"
# ]

# results = {}

# for model_name in models:
#     print(f"Évaluation du modèle: {model_name}")
#     # Créer un pipeline pour le modèle actuel
#     sentiment_analyzer = pipeline('sentiment-analysis', model=model_name)
    
#     # Appliquer le modèle aux résumés nettoyés
#     df[f'Sentiment_{model_name}'] = df['Cleaned_Summary'].apply(lambda x: sentiment_analyzer(x)[0]['label'])
    
#     # Calcul des performances (exemple avec l'accuracy)
#     # Vous devez avoir des étiquettes de vérité pour calculer les métriques de manière correcte
#     accuracy = (df[f'Sentiment_{model_name}'] == df['True_Sentiment']).mean()
#     results[model_name] = accuracy
#     print(f"Précision pour {model_name}: {accuracy}\n")

# # Comparaison des modèles
# best_model = max(results, key=results.get)
# print(f"Le meilleur modèle est {best_model} avec une précision de {results[best_model]}")


