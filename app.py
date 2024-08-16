import streamlit as st

# Définir l'application Streamlit
st.title('Analyse des Sentiments et des Sujets des Articles NYT')

# Afficher un aperçu des articles
st.write("Aperçu des articles:")
st.dataframe(df[['Title', 'Sentiment', 'Predicted_Topic']])

# Ajouter un champ de saisie pour la recherche par mot-clé
keyword = st.text_input("Rechercher un mot-clé:")
if keyword:
    results = df[df['Cleaned_Summary'].str.contains(keyword)]
    st.write(f"Résultats pour '{keyword}':")
    st.dataframe(results[['Title', 'Sentiment', 'Predicted_Topic', 'URL']])

# Lancer l'application avec `streamlit run nom_du_fichier.py`
