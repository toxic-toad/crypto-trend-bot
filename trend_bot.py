import os
import requests
import feedparser

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "1237652497"

feeds = [
    "https://feeds.feedburner.com/CoinDesk",
    "https://cointelegraph.com/rss",
    "https://www.theverge.com/rss/index.xml"
]

articles = []

for feed in feeds:
    try:
        parsed = feedparser.parse(feed)

        for entry in parsed.entries[:5]:
            articles.append({
                "title": entry.title,
                "link": entry.link
            })
    except:
        pass

if len(articles) == 0:
    message = "❌ No trends found."
else:
    trend = articles[0]

    headline = trend["title"]

    tweet = f"""
🔥 TREND ALERT

Headline:
{headline}

Tweet Draft:

🚀 {headline}

This story is getting attention right now and could have a major impact on the market and tech ecosystem.

What do you think?

#Trending #Tech #Crypto
"""

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": tweet
        }
    )
