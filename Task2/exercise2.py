import requests
import feedparser
import urllib3

# Suppress the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_headlines(rss_url):
    response = requests.get(rss_url, verify=False)  # Disable SSL verification
    feed = feedparser.parse(response.content)
    
    headlines = []
    for entry in feed.entries:
        headlines.append(entry.title)
    
    return headlines

google_news_url = "https://news.google.com/news/rss"
print(get_headlines(google_news_url))