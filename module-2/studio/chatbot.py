import os
from pathlib import Path
from dotenv import load_dotenv
from rich import print as rprint

from typing import Literal
from langchain_core.messages import HumanMessage, SystemMessage, RemoveMessage
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI

project_root = Path(__file__).parent.parent.parent if '__file__' in globals() else Path.cwd().parent.parent
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)
model_name = os.environ.get("MODEL_NAME")

model = ChatOpenAI(model=model_name, temperature=0) # type: ignore

class State(MessagesState):
    summary: str


def call_model(state: State):
    summary = state.get("summary", "")

    if summary:
        system_message = f"Summary of conversation earlier: {summary}"

        messages = [SystemMessage(content=system_message)] + state["messages"]

    else:
        messages = state["messages"]

    response = model.invoke(messages)
    return {"messages": response}


def should_continue(state: State) -> Literal["summarize_conversation", "__end__"]:

    messages = state["messages"]

    if len(messages) > 6:
        return "summarize_conversation"

    return END


def summarize_conversation(state: State):
    summary = state.get("summary", "")

    if summary:
        summary_message = (
            f"This is summary of the conversation to date: {summary}\n\n"
            "Extend the summary by taking into account the new messages above:"
        )

    else:
        summary_message = "Create a summary of the conversation above:"

    messages = state["messages"] + [HumanMessage(content=summary_message)]
    response = model.invoke(messages)

    delete_messages = [RemoveMessage(id=m.id) for m in state["messages"][:-2]]
    return {"summary": response.content, "messages": delete_messages}


workflow = StateGraph(State)
workflow.add_node("conversation", call_model)
workflow.add_node(summarize_conversation)

workflow.add_edge(START, "conversation")
workflow.add_conditional_edges("conversation", should_continue)
workflow.add_edge("summarize_conversation", END)


graph = workflow.compile()
