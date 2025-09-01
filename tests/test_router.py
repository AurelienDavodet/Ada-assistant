import pytest
from langchain_core.messages import HumanMessage
from ada_assistant.router import AppState, router


def make_state(text: str) -> AppState:
    return {"messages": [HumanMessage(content=text)], "route": None}

def test_router_morning():
    state = make_state("Peux-tu me faire le digest du matin ?")
    result = router(state)
    assert result["route"] == "morning"

def test_router_general():
    state = make_state("Donne-moi le cours du bitcoin")
    result = router(state)
    assert result["route"] == "general"
