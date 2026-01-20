import feedparser
ANTHROPIC_RSS = "https://www.anthropic.com/rss.xml"

def fetch_anthropic_blog(limit=3):
    feed = feedparser.parse(ANTHROPIC_RSS)
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
