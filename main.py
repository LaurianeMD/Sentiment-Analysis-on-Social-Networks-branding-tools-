import streamlit as st

# Exemple de code Streamlit pour visualiser les résultats
st.title('Analyse des Sentiments des Articles NYT')

# Formulaire pour entrer un mot-clé
keyword = st.text_input('Entrez un mot-clé pour rechercher des articles', 'windows crash')

# Filtrer les données en fonction du mot-clé
filtered_df = df[df['Title'].str.contains(keyword, case=False, na=False)]

# Affichage des résultats
st.write(filtered_df[['Title', 'Publication Date', 'Sentiment', 'Topics']])
