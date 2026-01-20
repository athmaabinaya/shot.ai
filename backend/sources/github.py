import requests
from bs4 import BeautifulSoup

def fetch_github_trending(n=1):
    url = "https://github.com/trending?since=daily"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    
    items = []
    for repo in soup.select("article.Box-row")[:n]:
        repo_name = repo.h2.a.get_text(strip=True).replace("\n", "").replace(" ", "")
        repo_url = "https://github.com" + repo.h2.a['href']
        description_tag = repo.p
        description = description_tag.get_text(strip=True) if description_tag else ""
        stars_text = repo.find("a", class_="Link--muted").text
        stars = int(stars_text.replace(",", "").replace("k", "000"))
        
        items.append({
            "title": f"{repo_name} – {description}",
            "url": repo_url,
            "source": "GitHub Trending",
            "category": "Open Source / Tools",
            "summary": None,
            "stars": stars
        })
    return items
