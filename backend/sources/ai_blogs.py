import feedparser

AI_BLOG_FEEDS = [
    "https://openai.com/blog/rss/",
    "https://ai.googleblog.com/feeds/posts/default",
]

def fetch_ai_blog_post():
    for feed in AI_BLOG_FEEDS:
        parsed = feedparser.parse(feed)
        if parsed.entries:
            entry = parsed.entries[0]
            return {
                "title": entry.title,
                "url": entry.link,
                "source": "AI Blog",
                "category": "AI / Platform",
                "summary": None
            }
    return None
