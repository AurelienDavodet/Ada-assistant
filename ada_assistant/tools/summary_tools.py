from langchain_core.tools import tool

from ada_assistant.tools.fun_tools import knowledge_fact
from ada_assistant.tools.time_tools import get_date, get_time
from ada_assistant.tools.transport_tools import ratp_traffic_lines
from ada_assistant.tools.weather_tools import get_weather


@tool
def morning_summary() -> str:
    """Résumé du matin (date, heure, météo, fait culturel)."""
    try:
        date = get_date.invoke("")
        time = get_time.invoke("")
        weather = get_weather.invoke({"city": "Paris", "period": "today"})
        traffic = ratp_traffic_lines.invoke({"lines": ["RER A", "1", "2", "6", "9"]})
        fact = knowledge_fact.invoke("")

        return (
            f"👋 Bonjour Aurélien !\n\n"
            f"🗓️ **Nous sommes le {date}**\n"
            f"⏰ Il est {time} à Paris\n"
            f"🌦️ Météo : {weather}\n\n"
            f"🌦️ Traffic : {traffic}\n\n"
            f"{fact}\n\n"
            "✨ Que cette journée soit pleine d’énergie et de bonnes surprises ! 🚀"
        )
    except Exception as e:
        return f"Impossible de générer le résumé du matin ({e})."
