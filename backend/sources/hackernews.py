import requests

HACKERNEWS_TOP_STORIES = "https://hacker-news.firebaseio.com/v0/topstories.json"

def fetch_top_hn(n=2):
    ids = requests.get(HACKERNEWS_TOP_STORIES).json()[:50]  # fetch first 50, filter later
    items = []

    for id in ids:
        story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json").json()
        if story and story.get("type") == "story" and story.get("title"):
            url = story.get("url") or f"https://news.ycombinator.com/item?id={id}"
            items.append({
                "title": story.get("title"),
                "url": url,
                "source": "Hacker News",
                "category": "Community / Startups",
                "score": story.get("score", 0),
                "summary": None
            })
        if len(items) >= n:
            break
    return items
