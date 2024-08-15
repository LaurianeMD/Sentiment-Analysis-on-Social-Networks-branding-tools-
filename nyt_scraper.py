import requests
import pandas as pd
import os
from dotenv import load_dotenv
import time

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Votre clé API du New York Times
api_key = os.getenv('NYT_API_KEY')

# Fonction pour récupérer les articles avec pagination
def fetch_articles(query, api_key, page=0, max_pages=100):
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    params = {
        'q': query,
        'api-key': api_key,
        'page': page
    }

    all_articles = []
    backoff_time = 60  # Initial backoff time of 1 minute

    while page < max_pages:
        response = requests.get(url, params=params)
        
        if response.status_code == 429:
            print(f"Rate limit exceeded. Waiting for {backoff_time} seconds before retrying...")
            time.sleep(backoff_time)
            backoff_time *= 2  # Exponentially increase the backoff time
            continue
        
        # Reset backoff_time after a successful request
        backoff_time = 60
        
        if response.status_code != 200:
            data = response.json()
            print(f"Error {response.status_code}: {data.get('message', 'Unknown error')}")
            break

        data = response.json()
        articles = data.get('response', {}).get('docs', [])
        if not articles:
            print("No more articles found.")
            break

        all_articles.extend(articles)
        page += 1
        params['page'] = page  # Passer à la page suivante
        
        # Add a delay to avoid hitting rate limits
        time.sleep(1)

    return all_articles

# Récupération des articles
articles = fetch_articles('Kamala Harris elections', api_key)
article_data = []

for article in articles:
    article_data.append([
        article.get('headline', {}).get('main', ''),
        article.get('pub_date', ''),
        article.get('web_url', ''),
        article.get('abstract', ''),
        article.get('byline', {}).get('original', ''),
        article.get('section_name', ''),
        ', '.join([kw.get('value', '') for kw in article.get('keywords', [])])  # Concaténation des mots-clés
    ])

# Stockage des articles dans un DataFrame
df = pd.DataFrame(article_data, columns=['Title', 'Publication Date', 'URL', 'Summary', 'Author', 'Section', 'Tags'])

# Affichage des premiers articles
print(df.head())

# Enregistrement des articles dans un fichier CSV
csv_filename = 'articles.csv'
df.to_csv(csv_filename, index=False, encoding='utf-8')

print(f"Les articles ont été enregistrés dans le fichier {csv_filename}")
