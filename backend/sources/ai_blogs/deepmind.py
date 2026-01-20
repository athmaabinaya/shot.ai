import feedparser

DEEPMIND_RSS = "https://deepmind.google/blog/rss.xml"

def fetch_deepmind_blog(limit=3):
    feed = feedparser.parse(DEEPMIND_RSS)
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
