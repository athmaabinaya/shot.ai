import os
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY environment variable is not set. "
        "Please set it before running the server. "
        "You can set it with: $env:GEMINI_API_KEY='your-api-key' (PowerShell) "
        "or export GEMINI_API_KEY='your-api-key' (bash). "
        "Get your API key from: https://aistudio.google.com/app/apikey"
    )

genai.configure(api_key=api_key)

# Use a currently supported Gemini model name. The plain "gemini-1.5-flash"
# can return 404 for v1beta; the "-001" suffix is the stable variant.
model = genai.GenerativeModel("gemini-1.5-flash-001")

def summarize_item(title: str, url: str | None):
    prompt = f"""
You are a tech analyst.

Summarize the following tech news item in 3 concise bullet points.
Then explain why it matters for software engineers or product builders.

Title: {title}
URL: {url}
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Fallback so the API still works even if the Gemini model/config
        # is unavailable or misconfigured.
        return (
            "Summary temporarily unavailable due to an AI backend error. "
            f"(details: {type(e).__name__})"
        )
