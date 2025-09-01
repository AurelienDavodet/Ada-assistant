from langchain_core.messages import HumanMessage

from ada_assistant.graph import assistant_graph


def test_graph_morning():
    state_in = {"messages": [HumanMessage(content="Fais-moi le digest du matin")]}
    result = assistant_graph.invoke(
        state_in,
        config={"configurable": {"thread_id": "test-thread"}}
    )
    reply = result["messages"][-1].content
    assert isinstance(reply, str)
    assert len(reply) > 0


def test_graph_general():
    state_in = {"messages": [HumanMessage(content="Quel est le prix du bitcoin ?")]}
    result = assistant_graph.invoke(
        state_in,
        config={"configurable": {"thread_id": "test-thread"}}
    )
    reply = result["messages"][-1].content
    assert isinstance(reply, str)
    assert len(reply) > 0
