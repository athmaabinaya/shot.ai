from ranking.ai_blog_scoring import score_ai_blog_item

def select_top_ai_blog_items(items: list[dict], k: int = 2) -> list[dict]:
    for item in items:
        item["score"] = score_ai_blog_item(item)

    items.sort(key=lambda x: x["score"], reverse=True)
    return items[:k]
