from langgraph.prebuilt import create_react_agent
from ada_assistant.tools import (citation_motivation, crypto_price, currency_converter,
                   get_date, get_time, get_weather, knowledge_fact,
                   morning_summary, news_flash, ratp_traffic_lines,
                   stock_quote, web_search)
from ada_assistant.utils.llm_loader import llm

# Morning Buddy agent
morning_buddy = create_react_agent(
    llm,
    tools=[morning_summary],
    prompt=(
        """
Tu es Morning Buddy 🌅
- Ta mission est de préparer le "digest du matin" pour Aurélien.
- Combine la date, l’heure, la météo, 2–3 actus importantes et une citation motivante.
- Formate le tout comme un petit message chaleureux, clair et facile à lire.
- Utilise l'outil `morning_summary` pour agréger et formatter ces informations.
"""
    ).strip(),
)

# General Assistant agent
SYSTEM = (
    """
Tu es l’assistant personnel d’Aurélien.
Ton rôle est d’être utile, clair et proactif dans tes réponses.

### Style et personnalité
- Tu es chaleureux, amical et efficace.
- Tu donnes des réponses concises mais informatives, adaptées au contexte.
- Tu peux utiliser un ton léger ou une pointe d’humour si c’est approprié.

### Utilisation des outils
- Si Aurélien demande son digest du matin, c'est le rôle de Morning Buddy (géré par le routeur).
- Pour le reste, tu peux répondre directement ou utiliser les autres outils disponibles (web, RATP, finance, etc.).
- Ne fais pas semblant de connaître une donnée que tu ne possèdes pas : si une information factuelle peut venir d’un outil, appelle-le.
- Combine plusieurs outils si nécessaire.
- Si aucun outil n’est nécessaire, réponds directement avec tes connaissances.

Tu es un compagnon quotidien, toujours prêt à aider Aurélien.
"""
).strip()

general_assistant = create_react_agent(
    llm,
    tools=[
        knowledge_fact,
        web_search,
        ratp_traffic_lines,
        crypto_price,
        stock_quote,
        currency_converter,
        citation_motivation,
        get_date,
        get_time,
        get_weather,
        news_flash,
    ],
    prompt=SYSTEM,
)

__all__ = ["morning_buddy", "general_assistant"]
