# %%
import csv
import os
from newsapi.newsapi_client import NewsApiClient

# Get the NewsAPI key from the environment variables
api_key = os.getenv("NEWSAPI_KEY")

# Initialize the NewsAPI client
newsapi = NewsApiClient(api_key=api_key)

# Fetch the top headlines from the US and the UK in the general category, wieghting more towards the US
top_headlines_us = newsapi.get_top_headlines(country='us', category='general', page_size=8)
# Include just a couple of articles from the UK to limit less relevant articles & ensure we only get top headlines
top_headlines_uk = newsapi.get_top_headlines(country='gb', category='general', page_size=2)

# Combine the US and UK headlines
top_headlines = top_headlines_us['articles'] + top_headlines_uk['articles']

# Save the title, source, URL, and published date of each article to a CSV file
with open('newslog.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Source', 'PublishedAt', 'Url'])
    
    for article in top_headlines:
        writer.writerow([article['title'], article['source']['name'], article['publishedAt'], article['url']])

# %%



