from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph

from ada_assistant.agents.agents import general_assistant, morning_buddy
from ada_assistant.router import AppState, router

# Build the explicit graph
workflow = StateGraph(AppState)

workflow.add_node("router", router)
workflow.add_node("morning", morning_buddy)
workflow.add_node("general", general_assistant)

workflow.set_entry_point("router")
workflow.add_conditional_edges(
    "router",
    lambda s: s.get("route", "general"),
    {"morning": "morning", "general": "general"},
)
workflow.add_edge("morning", END)
workflow.add_edge("general", END)

# Compile the graph with memory
checkpointer = MemorySaver()
assistant_graph = workflow.compile(checkpointer=checkpointer)

__all__ = ["assistant_graph"]
