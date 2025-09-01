# app.py
import uuid

import chainlit as cl
from langchain_core.messages import HumanMessage
# IMPORTANT: dans ton fichier LangGraph, tu exportes `agent = app`
from ada_assistant.graph import assistant_graph  # ton graphe compilé


@cl.on_chat_start
async def on_start():
    # Crée un thread_id unique pour ce chat utilisateur
    thread_id = str(uuid.uuid4())
    cl.user_session.set("thread_id", thread_id)

    await cl.Message(content="👋 Salut Aurélien ! Je t'écoute.").send()


@cl.on_message
async def on_message(message: cl.Message):
    user_text = message.content.strip()
    thread_id = cl.user_session.get("thread_id")

    # Passe le thread_id pour que le checkpointer du graphe conserve la mémoire
    config = {"configurable": {"thread_id": thread_id}} if thread_id else {}

    # agent.invoke est synchrone, donc on le rend async
    res = await cl.make_async(assistant_graph.invoke)(
        {"messages": [HumanMessage(user_text)]},
        config=config,
    )

    reply = res["messages"][-1].content
    await cl.Message(content=reply).send()
