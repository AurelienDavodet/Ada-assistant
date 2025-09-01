import requests
from langchain_core.tools import tool


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
