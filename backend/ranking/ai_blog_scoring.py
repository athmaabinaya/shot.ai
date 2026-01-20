KEYWORD_SCORES = {
    "llm": 4,
    "agent": 4,
    "inference": 3,
    "training": 3,
    "open source": 3,
    "api": 2,
    "developer": 2,
    "safety": 2,
    "release": 2,
    "launch": 2,
    "benchmark": 2,
}

SOURCE_BONUS = {
    "openai": 2,
    "anthropic": 2,
    "deepmind": 2,
    "huggingface": 2,
}

def score_ai_blog_item(item: dict) -> int:
    score = 0
    text = f"{item.get('title','')} {item.get('content','')}".lower()

    for keyword, points in KEYWORD_SCORES.items():
        if keyword in text:
            score += points

    score += SOURCE_BONUS.get(item.get("source"), 0)
    print(f"score for {item.get('title')} is: {score}")
    return score
