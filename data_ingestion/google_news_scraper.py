import requests
from bs4 import BeautifulSoup
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def scrape_google_news():
    url = 'https://news.google.com/search?q=cryptocurrency'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')
    for article in articles:
        news = {
            'title': article.find('h3').text,
            'link': article.find('a')['href'],
            'source': article.find('div', class_='SVJrMe').text,
        }
        producer.send('google_news_stream', json.dumps(news).encode('utf-8'))
    time.sleep(60)

while True:
    scrape_google_news()
