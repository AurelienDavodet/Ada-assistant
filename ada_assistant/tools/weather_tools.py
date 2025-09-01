from datetime import date, timedelta

import requests
from langchain_core.tools import tool

WEATHER_CODES = {
    0: "ciel dégagé ☀️",
    1: "partiellement nuageux 🌤️",
    2: "nuageux ⛅",
    3: "couvert ☁️",
    45: "brouillard 🌫️",
    48: "brouillard givrant ❄️🌫️",
    51: "bruine légère 🌦️",
    61: "pluie faible 🌧️",
    63: "pluie modérée 🌧️🌧️",
    65: "pluie forte ⛈️",
    71: "neige légère 🌨️",
    73: "neige modérée 🌨️❄️",
    75: "fortes chutes de neige ❄️⛄",
    77: "grésil 🌨️💧",
    80: "averses 🌦️",
    81: "averses fortes 🌧️🌧️",
    82: "averses très intenses ⛈️",
    95: "orages ⚡⛈️",
    99: "orages violents 🌩️⚡",
}


@tool
def get_weather(city: str = "Paris", period: str = "today") -> str:
    """
    Renvoie la météo pour une ville donnée.
    period peut être : "today" (actuel), "tomorrow", "week".
    """
    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=fr&format=json"
        g = requests.get(geo_url, timeout=5)
        g.raise_for_status()
        geo_data = g.json()

        if "results" not in geo_data or not geo_data["results"]:
            return f"Ville '{city}' introuvable."

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        city_name = geo_data["results"][0]["name"]

        if period == "today":
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            data = r.json()["current_weather"]
            temp = data["temperature"]
            meteo_code = data["weathercode"]
            description = WEATHER_CODES.get(meteo_code, "conditions météo variées 🌍")
            return f"Actuellement à {city_name}, il fait {temp}°C avec {description}."

        elif period == "tomorrow":
            start = (date.today() + timedelta(days=1)).isoformat()
            end = start
            url = (
                f"https://api.open-meteo.com/v1/forecast"
                f"?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,weathercode"
                f"&start_date={start}&end_date={end}&timezone=auto"
            )
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            d = r.json()["daily"]
            tmin, tmax, code = d["temperature_2m_min"][0], d["temperature_2m_max"][0], d["weathercode"][0]
            description = WEATHER_CODES.get(code, "conditions météo variées 🌍")
            return f"Demain à {city_name} : entre {tmin}°C et {tmax}°C, {description}."

        elif period == "week":
            start = date.today().isoformat()
            end = (date.today() + timedelta(days=6)).isoformat()
            url = (
                f"https://api.open-meteo.com/v1/forecast"
                f"?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,weathercode"
                f"&start_date={start}&end_date={end}&timezone=auto"
            )
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            d = r.json()["daily"]

            res = [f"Prévisions sur 7 jours pour {city_name} :"]
            for i in range(len(d["time"])):
                jour = d["time"][i]
                tmin, tmax, code = d["temperature_2m_min"][i], d["temperature_2m_max"][i], d["weathercode"][i]
                desc = WEATHER_CODES.get(code, "conditions météo variées 🌍")
                res.append(f"- {jour} : {tmin}°C à {tmax}°C, {desc}")
            return "\n".join(res)

        else:
            return "Période invalide. Utilise 'today', 'tomorrow' ou 'week'."

    except Exception as e:
        return f"Impossible de récupérer la météo ({e})."
