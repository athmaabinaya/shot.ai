# Import all individual fetch functions
from .openai import fetch_openai_blog
from .deepmind import fetch_deepmind_blog
from .anthropic import fetch_anthropic_blog
from .huggingface import fetch_huggingface_blog
from .stability import fetch_stability_blog

# Optional: list of all sources for easy iteration
ALL_AI_BLOG_SOURCES = [
    fetch_openai_blog,
    fetch_deepmind_blog,
    fetch_anthropic_blog,
    fetch_huggingface_blog,
    fetch_stability_blog,
]

# Exported names
__all__ = [
    "fetch_openai_blog",
    "fetch_deepmind_blog",
    "fetch_anthropic_blog",
    "fetch_huggingface_blog",
    "fetch_stability_blog",
    "ALL_AI_BLOG_SOURCES",
]
