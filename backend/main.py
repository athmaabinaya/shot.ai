import os
import json
from datetime import date
from fastapi import FastAPI
from ai import summarize_item
from sources import hackernews, github, ai_blogs
from sources.ai_blogs import ALL_AI_BLOG_SOURCES
from ranking import select_top_ai_blog_items

app = FastAPI()

CACHE_FILE = "cache/summaries.json"


def generate_daily_digest():
    daily_items = []

    # --- AI blogs ---
    all_blogs = []
    for fetch_fn in ALL_AI_BLOG_SOURCES:
        all_blogs.extend(fetch_fn(limit=3))

    top_ai_blogs = select_top_ai_blog_items(all_blogs, k=2)

    for item in top_ai_blogs:
        item["summary"] = summarize_item(title=item["title"], url=item["url"])
        item["score"] = item.get("score", 0)

    # --- HackerNews ---
    hn_items = hackernews.fetch_top_hn(n=2)
    for item in hn_items:
        item["summary"] = summarize_item(title=item["title"], url=item["url"])
        item["score"] = item.get("score", 0)

    # --- GitHub ---
    github_items = github.fetch_github_trending(n=1)
    for item in github_items:
        item["summary"] = summarize_item(title=item["title"], url=item["url"])
 #       item["score"] = item.get("score", 0)
        item["stars"] = item.get("stars", 0)

    # --- Combine all ---
    daily_items.extend(hn_items)
    daily_items.extend(github_items)
    daily_items.extend(top_ai_blogs)   # <-- extend the top AI blogs

    # Ensure exactly 5 items
    daily_items = daily_items[:5]

    return {"date": str(date.today()), "items": daily_items}



@app.get("/digest")
def daily_digest():
    # Check if cache exists and is for today
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r") as f:
                cached = json.load(f)
        except json.JSONDecodeError:
            print("Cache file corrupted or incomplete. Regenerating digest...")
            cached = None

        if cached and cached.get("date") == str(date.today()):
            return cached

    # Generate fresh digest
    digest = generate_daily_digest()

    # Save to cache
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(digest, f, indent=2)

    return digest
