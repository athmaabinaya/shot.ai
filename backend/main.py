from fastapi import FastAPI
import httpx
from ai import summarize_item


app = FastAPI(title="shot.ai API")

HN_TOP_STORIES = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM = "https://hacker-news.firebaseio.com/v0/item/{}.json"


@app.get("/")
def health():
    return {"status": "ok", "app": "shot.ai"}


@app.get("/digest")
async def get_digest():
    async with httpx.AsyncClient() as client:
        # get top story IDs
        ids_response = await client.get(HN_TOP_STORIES)
        ids = ids_response.json()[:5]  # top 10 for now

        items = []
        for story_id in ids:
            item_resp = await client.get(HN_ITEM.format(story_id))
            data = item_resp.json()

            if data and data.get("type") == "story":
                item = {
                "id": data["id"],
                "title": data.get("title"),
                "url": data.get("url"),
                "by": data.get("by"),
                "score": data.get("score"),
                }

                summary = summarize_item(
                title=data.get("title"),
                url=data.get("url")
            ) or "Summary unavailable."
            
            item["summary"] = summary
            items.append(item)

        return {
            "date": "today",
            "items": items
        }
