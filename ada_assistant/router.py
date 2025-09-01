import operator
from typing import Annotated, Literal, Optional, Sequence, TypedDict

from langchain_core.messages import BaseMessage


# Shared state for the LangGraph
class AppState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    route: Optional[Literal["morning", "general"]]


# Simple rule-based router
def router(state: AppState) -> AppState:
    text = (state["messages"][-1].content or "").lower()

    triggers = (
        "digest du matin",
        "résumé du matin",
        "briefing du matin",
        "morning buddy",
        "morning summary",
        "morning digest"
    )

    route = "morning" if any(t in text for t in triggers) else "general"
    return {"route": route}


__all__ = ["AppState", "router"]
