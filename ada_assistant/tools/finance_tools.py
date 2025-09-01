import requests
from langchain_core.tools import tool


@tool
def currency_converter(amount: float, from_cur: str, to_cur: str) -> str:
    """Convertit un montant d'une devise vers une autre."""
    try:
        url = f"https://api.exchangerate.host/convert?from={from_cur}&to={to_cur}&amount={amount}"
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()
        result = data.get("result")
        if result is None:
            return "Conversion impossible."
        return f"{amount} {from_cur.upper()} = {result:.2f} {to_cur.upper()}"
    except Exception as e:
        return f"Impossible de convertir ({e})."


@tool
def stock_quote(symbol: str = "AAPL") -> str:
    """Renvoie le dernier cours d'une action donnée (ex: AAPL, TSLA)."""
    try:
        url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()["quoteResponse"]["result"][0]
        price = data.get("regularMarketPrice")
        currency = data.get("currency", "")
        name = data.get("shortName", symbol)
        return f"📊 {name} ({symbol}) : {price} {currency}"
    except Exception as e:
        return f"Impossible de récupérer le cours de {symbol} ({e})."


@tool
def crypto_price(symbol: str = "bitcoin") -> str:
    """Renvoie le prix actuel d'une cryptomonnaie (par défaut Bitcoin)."""
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=eur,usd"
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()[symbol]
        eur, usd = data.get("eur"), data.get("usd")
        return f"₿ {symbol.capitalize()} : {eur} € | {usd} $"
    except Exception as e:
        return f"Impossible de récupérer le prix de {symbol} ({e})."
