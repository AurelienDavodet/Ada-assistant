import pytest

from ada_assistant.tools import (citation_motivation, crypto_price,
                                 currency_converter, get_date, get_joke,
                                 get_time, get_weather, knowledge_fact,
                                 morning_summary, news_flash,
                                 ratp_traffic_lines, stock_quote, web_search)


def test_get_date():
    result = get_date.invoke("")
    assert isinstance(result, str)
    assert len(result) > 0


def test_get_time():
    result = get_time.invoke("")
    assert isinstance(result, str)
    assert ":" in result  # format HH:MM attendu


def test_get_joke():
    result = get_joke.invoke("")
    assert isinstance(result, str)


def test_get_weather():
    result = get_weather.invoke({"city": "Paris", "period": "today"})
    assert isinstance(result, str)
    assert "Paris" in result or "Impossible" in result


def test_knowledge_fact():
    result = knowledge_fact.invoke("")
    assert isinstance(result, str)


def test_web_search():
    result = web_search.invoke("LangGraph")
    assert isinstance(result, str)


def test_citation_motivation():
    result = citation_motivation.invoke("")
    assert isinstance(result, str)


def test_news_flash():
    result = news_flash.invoke("")
    assert isinstance(result, str)


def test_currency_converter():
    result = currency_converter.invoke({"amount": 10, "from_cur": "EUR", "to_cur": "USD"})
    assert isinstance(result, str)
    assert any(word in result for word in ["EUR", "Impossible", "Conversion"])


def test_stock_quote():
    result = stock_quote.invoke("AAPL")
    assert isinstance(result, str)


def test_crypto_price():
    result = crypto_price.invoke("bitcoin")
    assert isinstance(result, str)


def test_ratp_traffic_lines():
    result = ratp_traffic_lines.invoke({"lines": ["1"]})
    assert isinstance(result, str)


def test_morning_summary():
    result = morning_summary.invoke("")
    assert isinstance(result, str)
