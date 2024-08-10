import feedparser

def get_headlines(rss_url):
    feed = feedparser.parse(rss_url)
    titles = [entry.title for entry in feed.entries]
    return titles

google_news_url="https://news.google.com/news/rss"
titles = get_headlines(google_news_url)
print(titles)