import requests
from langchain_core.tools import tool


@tool
def get_joke() -> str:
    """Renvoie une blague aléatoire en français via une API externe."""
    try:
        url = "https://v2.jokeapi.dev/joke/Any?type=single&blacklistFlags=nsfw,racist,sexist,explicit"
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()
        return data.get("joke", "Je n’ai pas trouvé de blague 😅.")
    except Exception as e:
        return f"Impossible de récupérer une blague ({e})."


@tool
def knowledge_fact() -> str:
    """Renvoie une anecdote insolite via l'API Useless Facts."""
    try:
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        headers = {"User-Agent": "MorningBuddy/1.0"}
        r = requests.get(url, headers=headers, timeout=5)
        r.raise_for_status()
        data = r.json()
        fact = data.get("text", "Pas d'anecdote trouvée.")
        source = data.get("source_url", "")
        return f"💡 {fact}\n(Source : {source})" if source else f"💡 {fact}"
    except Exception as e:
        return f"Impossible de récupérer une anecdote ({e})."


@tool
def citation_motivation() -> str:
    """Renvoie une citation motivante aléatoire."""
    try:
        url = "https://zenquotes.io/api/random"
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()[0]
        return f"💡 « {data.get('q')} » — *{data.get('a')}*"
    except Exception as e:
        return f"Impossible de récupérer une citation ({e})."
