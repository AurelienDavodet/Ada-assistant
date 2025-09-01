import os

import requests
from langchain_core.tools import tool


@tool
def news_flash() -> str:
    """Renvoie les 3 actualités principales en France (via GNews API)."""
    GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
    try:
        url = f"https://gnews.io/api/v4/top-headlines?country=fr&max=5&lang=fr&apikey={GNEWS_API_KEY}"
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        articles = r.json().get("articles", [])
        if not articles:
            return "Aucune actu trouvée."

        lignes = ["📰 Actus du jour :"]
        for art in articles:
            lignes.append(f"- {art['title']} ➡️ {art['url']}")
        return "\n".join(lignes)
    except Exception as e:
        return f"Impossible de récupérer les actualités ({e})."


@tool
def web_search(query: str) -> str:
    """Fait une recherche Internet avec DuckDuckGo et renvoie un résumé des premiers résultats."""
    try:
        url = "https://api.duckduckgo.com/"
        params = {"q": query, "format": "json", "no_html": 1, "skip_disambig": 1}
        headers = {"User-Agent": "MorningBuddy/1.0 (https://example.com)"}
        r = requests.get(url, params=params, headers=headers, timeout=5)
        r.raise_for_status()
        data = r.json()

        if data.get("AbstractText"):
            return f"🔎 Résultat : {data['AbstractText']}"

        if data.get("RelatedTopics"):
            topic = data["RelatedTopics"][0]
            if isinstance(topic, dict) and "Text" in topic and "FirstURL" in topic:
                return f"🔎 {topic['Text']}\n➡️ {topic['FirstURL']}"

        return "Je n’ai trouvé aucun résultat pertinent."
    except Exception as e:
        return f"Impossible de faire la recherche ({e})."
