import feedparser
STABILITY_RSS = "https://stability.ai/blog/rss.xml"

def fetch_stability_blog(limit=3):
    feed = feedparser.parse(STABILITY_RSS)
    items = []

    for entry in feed.entries[:limit]:
        items.append({
            "id": entry.id,
            "title": entry.title,
            "url": entry.link,
            "source": "openai",
            "published_at": entry.get("published"),
            "content": entry.get("summary"),
        })

    return items