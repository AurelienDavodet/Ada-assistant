from datetime import datetime
from zoneinfo import ZoneInfo

from langchain_core.tools import tool


@tool
def get_date() -> str:
    """Renvoie la date du jour en français, ex: 'mardi 27 juin 2025' (Europe/Paris)."""
    jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
            "août", "septembre", "octobre", "novembre", "décembre"]
    d = datetime.now(ZoneInfo("Europe/Paris")).date()
    return f"{jours[d.weekday()]} {d.day} {mois[d.month - 1]} {d.year}"


@tool
def get_time() -> str:
    """Renvoie l'heure actuelle à Paris en 24h, ex: '07:42'."""
    t = datetime.now(ZoneInfo("Europe/Paris")).time()
    return f"{t.hour:02d}:{t.minute:02d}"
