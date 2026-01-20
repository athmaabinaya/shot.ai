import feedparser
HF_RSS = "https://huggingface.co/blog/feed.xml"

def fetch_huggingface_blog(limit=3):
    feed = feedparser.parse(HF_RSS)
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