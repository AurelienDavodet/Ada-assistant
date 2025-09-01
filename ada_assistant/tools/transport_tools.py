import requests
from langchain_core.tools import tool


@tool
def ratp_traffic_lines(lines: list[str] = ["RER A", "1", "2", "6", "9"]) -> str:
    """
    Renvoie l'état du trafic RATP pour une liste de lignes précises.
    Exemple: ["RER A", "1", "2", "6", "9"]
    """
    try:
        url = "https://api-ratp.pierre-grimaud.fr/v4/traffic"
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json().get("result", {})

        requested = [l.strip().upper().replace("RER ", "") for l in lines]
        lignes = ["🚦 Infos trafic sélectionnées :"]

        for rer in data.get("rers", []):
            if rer["line"].upper() in requested:
                lignes.append(f"🚆 RER {rer['line']} : {rer['title']} → {rer['message']}")

        for metro in data.get("metros", []):
            if metro["line"].upper() in requested:
                lignes.append(f"🚇 Métro {metro['line']} : {metro['title']} → {metro['message']}")

        if len(lignes) == 1:
            return "Aucune information trafic trouvée pour les lignes demandées."
        return "\n".join(lignes)

    except Exception as e:
        return f"Impossible de récupérer le trafic RATP ({e})."
