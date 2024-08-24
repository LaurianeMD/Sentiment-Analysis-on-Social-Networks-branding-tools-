# # # import streamlit as st
# # # import requests
# # # import altair as alt
# # # import pandas as pd
# # # from PIL import Image

# # # API_BASE_URL = "http://localhost:8000"

# # # # Charger l'image
# # # background_image = "bgr.jpg"

# # # # Disposition en colonnes pour placer l'image à gauche ou à droite
# # # col1, col2 = st.columns([2, 5])  # Ajustez les valeurs pour modifier la largeur relative des colonnes

# # # with col1:  # Image dans la colonne de gauche
# # #     try:
# # #         img = Image.open(background_image)
# # #         st.image(img, use_column_width=True)
# # #     except FileNotFoundError:
# # #         st.error(f"L'image {background_image} n'a pas été trouvée.")

# # # with col2:  # Contenu de l'application dans la colonne de droite
# # #     # Titre de l'application
# # #     st.title('Sentiment and Topic Analysis')

# # #     # Section pour rechercher des articles
# # #     query = st.text_input('Enter your search query:', 'Windows crash')

# # #     def fetch_articles(query):
# # #         try:
# # #             response = requests.get(f"{API_BASE_URL}/articles", params={"query": query})
# # #             response.raise_for_status()
# # #             return response.json()
# # #         except requests.exceptions.HTTPError as http_err:
# # #             st.error(f"HTTP error occurred: {http_err}")
# # #         except Exception as err:
# # #             st.error(f"An error occurred: {err}")
# # #         return None

# # #     if st.button('Fetch Articles'):
# # #         articles = fetch_articles(query)
# # #         if articles:
# # #             sentiments = []
# # #             topics = []

# # #             for article in articles:
# # #                 st.subheader(article['title'])
# # #                 st.write(f"Abstract: {article['abstract']}")
# # #                 st.write(f"URL: {article['url']}")
# # #                 st.write(f"Published Date: {article['published_date']}")
# # #                 st.write(f"Sentiment: {article['sentiment']}")
# # #                 st.write(f"Topic: {article['topic']}")

# # #                 sentiments.append(article['sentiment'])
# # #                 topics.append(article['topic'])

# # #             # Afficher la distribution des sentiments
# # #             if sentiments:
# # #                 st.subheader("Sentiment Distribution")
# # #                 sentiment_counts = pd.DataFrame({
# # #                     'Sentiment': list(set(sentiments)),
# # #                     'Count': [sentiments.count(sentiment) for sentiment in set(sentiments)]
# # #                 })
# # #                 chart = alt.Chart(sentiment_counts).mark_bar().encode(
# # #                     x='Sentiment',
# # #                     y='Count'
# # #                 )
# # #                 st.altair_chart(chart, use_container_width=True)

# # #             # Afficher la distribution des sujets
# # #             if topics:
# # #                 st.subheader("Topic Distribution")
# # #                 topic_counts = pd.DataFrame({
# # #                     'Topic': list(set(topics)),
# # #                     'Count': [topics.count(topic) for topic in set(topics)]
# # #                 })
# # #                 chart = alt.Chart(topic_counts).mark_bar().encode(
# # #                     x='Topic',
# # #                     y='Count'
# # #                 )
# # #                 st.altair_chart(chart, use_container_width=True)

# # #     # Section pour analyser le texte
# # #     st.subheader("Analyze Text")

# # #     title = st.text_input("Enter the title of the article:")
# # #     content = st.text_area("Enter the content of the article:")

# # #     def analyze_text(title, content):
# # #         try:
# # #             if not title or not content:
# # #                 st.error("Title and content cannot be empty.")
# # #                 return None
# # #             response = requests.post(f"{API_BASE_URL}/analyze", json={"title": title, "content": content})
# # #             response.raise_for_status()
# # #             return response.json()
# # #         except requests.exceptions.HTTPError as http_err:
# # #             st.error(f"HTTP error occurred: {http_err}")
# # #         except Exception as err:
# # #             st.error(f"An error occurred: {err}")
# # #         return None

# # #     if st.button("Analyze"):
# # #         result = analyze_text(title, content)
# # #         if result:
# # #             st.write("Sentiment:", result['sentiment'])
# # #             st.write("Predicted Topic:", result['topic'])



# # import streamlit as st
# # import requests
# # import altair as alt
# # import pandas as pd
# # from PIL import Image

# # API_BASE_URL = "http://localhost:8000"

# # # Charger l'image
# # background_image = "bgr.jpg"

# # # Disposition en colonnes pour placer l'image à gauche ou à droite
# # col1, col2 = st.columns([2, 5])  # Ajustez les valeurs pour modifier la largeur relative des colonnes

# # with col1:  # Image dans la colonne de gauche
# #     try:
# #         img = Image.open(background_image)
# #         st.image(img, use_column_width=True)
# #     except FileNotFoundError:
# #         st.error(f"L'image {background_image} n'a pas été trouvée.")

# # with col2:  # Contenu de l'application dans la colonne de droite
# #     # Titre de l'application
# #     st.title('Sentiment and Topic Analysis')

# #     # Section pour rechercher des articles
# #     query = st.text_input('Enter your search query:', 'Windows crash')

# #     def fetch_articles(query):
# #         try:
# #             response = requests.get(f"{API_BASE_URL}/articles", params={"query": query})
# #             response.raise_for_status()
# #             return response.json()
# #         except requests.exceptions.HTTPError as http_err:
# #             st.error(f"HTTP error occurred: {http_err}")
# #         except Exception as err:
# #             st.error(f"An error occurred: {err}")
# #         return None

# #     if st.button('Fetch Articles'):
# #         articles = fetch_articles(query)
# #         if articles:
# #             sentiments = []
# #             topics = []

# #             for article in articles:
# #                 st.subheader(article['title'])
# #                 st.write(f"Abstract: {article['abstract']}")
# #                 st.write(f"URL: {article['url']}")
# #                 st.write(f"Published Date: {article['published_date']}")
# #                 st.write(f"Sentiment: {article['sentiment']}")
# #                 st.write(f"Topic: {article['topic']}")

# #                 sentiments.append(article['sentiment'])
# #                 topics.append(article['topic'])

# #             # Afficher la distribution des sentiments
# #             if sentiments:
# #                 st.subheader("Sentiment Distribution")
# #                 sentiment_counts = pd.DataFrame({
# #                     'Sentiment': list(set(sentiments)),
# #                     'Count': [sentiments.count(sentiment) for sentiment in set(sentiments)]
# #                 })
# #                 chart = alt.Chart(sentiment_counts).mark_bar().encode(
# #                     x='Sentiment',
# #                     y='Count'
# #                 )
# #                 st.altair_chart(chart, use_container_width=True)

# #             # Afficher la distribution des sujets
# #             if topics:
# #                 st.subheader("Topic Distribution")
# #                 topic_counts = pd.DataFrame({
# #                     'Topic': list(set(topics)),
# #                     'Count': [topics.count(topic) for topic in set(topics)]
# #                 })
# #                 chart = alt.Chart(topic_counts).mark_bar().encode(
# #                     x='Topic',
# #                     y='Count'
# #                 )
# #                 st.altair_chart(chart, use_container_width=True)

# #     # Section pour analyser le texte
# #     st.subheader("Analyze Text")

# #     title = st.text_input("Enter the title of the article:")
# #     content = st.text_area("Enter the content of the article:")

# #     def analyze_text(title, content):
# #         try:
# #             if not title or not content:
# #                 st.error("Title and content cannot be empty.")
# #                 return None
# #             response = requests.post(f"{API_BASE_URL}/analyze", json={"title": title, "content": content})
# #             response.raise_for_status()
# #             return response.json()
# #         except requests.exceptions.HTTPError as http_err:
# #             st.error(f"HTTP error occurred: {http_err}")
# #         except Exception as err:
# #             st.error(f"An error occurred: {err}")
# #         return None

# #     if st.button("Analyze"):
# #         result = analyze_text(title, content)
# #         if result:
# #             st.write("Sentiment:", result['sentiment'])
# #             st.write("Predicted Topic:", result['topic'])



# import streamlit as st
# import requests
# import altair as alt
# import pandas as pd
# from PIL import Image
# import os
# from dotenv import load_dotenv

# # Charger les variables d'environnement depuis le fichier .env
# load_dotenv()

# # Récupérer les variables d'environnement
# NYT_API_KEY = os.getenv('NYT_API_KEY')

# # Définir l'URL de l'API du New York Times
# NYT_API_BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

# # Charger l'image
# background_image = "bgr.jpg"

# # Disposition en colonnes pour placer l'image à gauche ou à droite
# col1, col2 = st.columns([2, 5])  # Ajustez les valeurs pour modifier la largeur relative des colonnes

# with col1:  # Image dans la colonne de gauche
#     try:
#         img = Image.open(background_image)
#         st.image(img, use_column_width=True)
#     except FileNotFoundError:
#         st.error(f"L'image {background_image} n'a pas été trouvée.")

# with col2:  # Contenu de l'application dans la colonne de droite
#     # Titre de l'application
#     st.title('Sentiment and Topic Analysis')

#     # Section pour rechercher des articles
#     query = st.text_input('Enter your search query:', 'Windows crash')

#     def fetch_articles(query):
#         try:
#             params = {
#                 'q': query,
#                 'api-key': NYT_API_KEY
#             }
#             response = requests.get(NYT_API_BASE_URL, params=params)
#             response.raise_for_status()
#             data = response.json()
#             articles = data['response']['docs']
#             return articles
#         except requests.exceptions.HTTPError as http_err:
#             st.error(f"HTTP error occurred: {http_err}")
#         except Exception as err:
#             st.error(f"An error occurred: {err}")
#         return None

#     if st.button('Fetch Articles'):
#         articles = fetch_articles(query)
#         if articles:
#             sentiments = []
#             topics = []

#             for article in articles:
#                 st.subheader(article['headline']['main'])
#                 st.write(f"Abstract: {article['abstract']}")
#                 st.write(f"URL: {article['web_url']}")
#                 st.write(f"Published Date: {article['pub_date']}")
#                 st.write(f"Sentiment: {article.get('sentiment', 'Not analyzed')}")
#                 st.write(f"Topic: {article.get('topic', 'Not categorized')}")

#                 # Sentiments and topics need to be processed separately
#                 sentiments.append(article.get('sentiment', 'Not analyzed'))
#                 topics.append(article.get('topic', 'Not categorized'))

#             # Afficher la distribution des sentiments
#             if sentiments:
#                 st.subheader("Sentiment Distribution")
#                 sentiment_counts = pd.DataFrame({
#                     'Sentiment': list(set(sentiments)),
#                     'Count': [sentiments.count(sentiment) for sentiment in set(sentiments)]
#                 })
#                 chart = alt.Chart(sentiment_counts).mark_bar().encode(
#                     x='Sentiment',
#                     y='Count'
#                 )
#                 st.altair_chart(chart, use_container_width=True)

#             # Afficher la distribution des sujets
#             if topics:
#                 st.subheader("Topic Distribution")
#                 topic_counts = pd.DataFrame({
#                     'Topic': list(set(topics)),
#                     'Count': [topics.count(topic) for topic in set(topics)]
#                 })
#                 chart = alt.Chart(topic_counts).mark_bar().encode(
#                     x='Topic',
#                     y='Count'
#                 )
#                 st.altair_chart(chart, use_container_width=True)

#     # Section pour analyser le texte
#     st.subheader("Analyze Text")

#     title = st.text_input("Enter the title of the article:")
#     content = st.text_area("Enter the content of the article:")

#     def analyze_text(title, content):
#         # Implémente la logique d'analyse du texte ici ou appelle ton API locale pour analyse
#         try:
#             if not title or not content:
#                 st.error("Title and content cannot be empty.")
#                 return None
#             response = requests.post(f"{API_BASE_URL}/analyze", json={"title": title, "content": content})
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.HTTPError as http_err:
#             st.error(f"HTTP error occurred: {http_err}")
#         except Exception as err:
#             st.error(f"An error occurred: {err}")
#         return None

#     if st.button("Analyze"):
#         result = analyze_text(title, content)
#         if result:
#             st.write("Sentiment:", result['sentiment'])
#             st.write("Predicted Topic:", result['topic'])


import streamlit as st
import requests
import altair as alt
import pandas as pd
from PIL import Image
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les variables d'environnement
NYT_API_KEY = os.getenv('NYT_API_KEY')

# Définir l'URL de l'API du New York Times
NYT_API_BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

# Charger l'image
background_image = "bgr.jpg"

# Disposition en colonnes pour placer l'image à gauche ou à droite
col1, col2 = st.columns([2, 5])  # Ajustez les valeurs pour modifier la largeur relative des colonnes

with col1:  # Image dans la colonne de gauche
    try:
        img = Image.open(background_image)
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.error(f"L'image {background_image} n'a pas été trouvée.")

with col2:  # Contenu de l'application dans la colonne de droite
    # Titre de l'application
    st.title('Sentiment and Topic Analysis')

    # Section pour rechercher des articles
    query = st.text_input('Enter your search query:', 'Windows crash')

    def fetch_articles(query):
        try:
            params = {
                'q': query,
                'api-key': NYT_API_KEY
            }
            response = requests.get(NYT_API_BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            articles = data['response']['docs']
            return articles
        except requests.exceptions.HTTPError as http_err:
            st.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            st.error(f"An error occurred: {err}")
        return None

    if st.button('Fetch Articles'):
        articles = fetch_articles(query)
        if articles:
            sentiments = []
            topics = []

            for article in articles:
                st.subheader(article['headline']['main'])
                st.write(f"Abstract: {article['abstract']}")
                st.write(f"URL: {article['web_url']}")
                st.write(f"Published Date: {article['pub_date']}")
                st.write(f"Sentiment: {article.get('sentiment', 'Not analyzed')}")
                st.write(f"Topic: {article.get('topic', 'Not categorized')}")

                sentiments.append(article.get('sentiment', 'Not analyzed'))
                topics.append(article.get('topic', 'Not categorized'))

            # Afficher la distribution des sentiments
            if sentiments:
                st.subheader("Sentiment Distribution")
                sentiment_counts = pd.DataFrame({
                    'Sentiment': list(set(sentiments)),
                    'Count': [sentiments.count(sentiment) for sentiment in set(sentiments)]
                })
                chart = alt.Chart(sentiment_counts).mark_bar().encode(
                    x='Sentiment',
                    y='Count'
                )
                st.altair_chart(chart, use_container_width=True)

            # Afficher la distribution des sujets
            if topics:
                st.subheader("Topic Distribution")
                topic_counts = pd.DataFrame({
                    'Topic': list(set(topics)),
                    'Count': [topics.count(topic) for topic in set(topics)]
                })
                chart = alt.Chart(topic_counts).mark_bar().encode(
                    x='Topic',
                    y='Count'
                )
                st.altair_chart(chart, use_container_width=True)

    # Section pour analyser le texte
    st.subheader("Analyze Text")

    title = st.text_input("Enter the title of the article:")
    content = st.text_area("Enter the content of the article:")

    def analyze_text(title, content):
        try:
            if not title or not content:
                st.error("Title and content cannot be empty.")
                return None
            response = requests.post(f"{API_BASE_URL}/analyze", json={"title": title, "content": content})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            st.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            st.error(f"An error occurred: {err}")
        return None

    if st.button("Analyze"):
        result = analyze_text(title, content)
        if result:
            st.write("Sentiment:", result['sentiment'])
            st.write("Predicted Topic:", result['topic'])
