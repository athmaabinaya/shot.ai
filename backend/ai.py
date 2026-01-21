import os
import json
from pathlib import Path
import google.generativeai as genai
from datetime import date

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY environment variable is not set. "
        "Please set it before running the server. "
        "or export GEMINI_API_KEY='your-api-key' (bash). "
        "Get your API key from: https://aistudio.google.com/app/apikey"
    )

genai.configure(api_key=api_key)

# Use a currently supported Gemini model name. The plain "gemini-1.5-flash"
# can return 404 for v1beta; the "-001" suffix is the stable variant.
model = genai.GenerativeModel("gemini-2.5-flash-lite") #gemini-1.5-flash-001

# ------------------------
# Summary cache setup
# ------------------------

SUMMARY_CACHE_FILE = Path("cache/summaries.json")
SUMMARY_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)

def load_summary_cache():
    if SUMMARY_CACHE_FILE.exists():
        return json.loads(SUMMARY_CACHE_FILE.read_text())
    return {}

def save_summary_cache(cache: dict):
    SUMMARY_CACHE_FILE.write_text(json.dumps(cache, indent=2))

def summarize_item(title: str, url: str | None):
    if not url:
        return "Summary unavailable."

    cache = load_summary_cache()

    # 🔒 HARD RULE: never resummarize the same URL
    if url in cache:
        print(f"[SUMMARY CACHE HIT] {url}")
        return cache[url]["summary"]

    prompt = f"""
You are a tech analyst.

Return the response in EXACTLY this format:

SUMMARY:
• <bullet 1>
• <bullet 2>
• <bullet 3>

WHY THIS MATTERS:
2–3 sentences explaining relevance to software engineers, product builders, or the tech industry.

Title: {title}
URL: {url}
"""

    try:
        response = model.generate_content(prompt)
        summary_text = response.text

        cache[url] = {
            "summary": summary_text,
            "created_at": str(date.today()),
        }
        save_summary_cache(cache)

        return summary_text

    except Exception as e:
        return (
            "Summary temporarily unavailable due to an AI backend error. "
            f"(details: {type(e).__name__})"
        )
    
