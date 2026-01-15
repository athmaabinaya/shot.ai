import os
import json
from datetime import date
from fastapi import FastAPI
from ai import summarize_item
from sources import hackernews, github, ai_blogs

app = FastAPI()

CACHE_FILE = "cache/daily_digest.json"

def generate_daily_digest():
    daily_items = []

    # 1-2 top HN stories
    hn_items = hackernews.fetch_top_hn(n=2)
    for item in hn_items:
        item["summary"] = summarize_item(title=item["title"], url=item["url"])
        item["score"] = item.get("score", 0)
    daily_items += hn_items

    # 1 GitHub trending
    github_items = github.fetch_github_trending(n=1)
    for item in github_items:
        item["summary"] = summarize_item(title=item["title"], url=item["url"])
        item["score"] = item.get("score", 0)
    daily_items += github_items

    # 1 AI blog post
    ai_item = ai_blogs.fetch_ai_blog_post()
    if ai_item:
        ai_item["summary"] = summarize_item(title=ai_item["title"], url=ai_item["url"])
        ai_item["score"] = ai_item.get("score", 0)
        daily_items.append(ai_item)

    # 1 wildcard
    daily_items.append({
        "title": "Wildcard tech story",
        "url": None,
        "source": "Wildcard",
        "category": "Misc",
        "summary": "Summary temporarily unavailable.",
        "score": 0
    })

    # Ensure exactly 5 items
    daily_items = daily_items[:5]

    return {"date": str(date.today()), "items": daily_items}


@app.get("/digest")
def daily_digest():
    # Check if cache exists and is for today
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            cached = json.load(f)
            if cached.get("date") == str(date.today()):
                return cached

    # Generate fresh digest
    digest = generate_daily_digest()

    # Save to cache
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(digest, f)

    return digest
