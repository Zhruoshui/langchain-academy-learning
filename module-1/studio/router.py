import os
from pathlib import Path
from dotenv import load_dotenv
from rich import print as rprint

# 获取项目根目录（当前文件在 module-1/studio/，需要向上两级到达项目根目录）
project_root = Path(__file__).parent.parent.parent if '__file__' in globals() else Path.cwd().parent.parent
env_path = project_root / '.env'

# 加载 .env 文件
load_dotenv(dotenv_path=env_path)


required_vars = ['OPENAI_API_KEY', 'OPENAI_API_BASE', 'MODEL_NAME', "LANGSMITH_API_KEY", "LANGSMITH_TRACING", "LANGSMITH_PROJECT"]
missing_vars = [var for var in required_vars if not os.environ.get(var)]

if missing_vars:
    rprint(f"[red]警告: 以下环境变量未在 .env 文件中配置: {', '.join(missing_vars)}[/red]")
else:
    rprint(f"[green]✓ 环境变量已从 {env_path} 成功加载[/green]")

from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition


# Tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

# LLM with bound tool
llm = ChatOpenAI(model="MODEL_NAME",temperature=0)
llm_with_tools = llm.bind_tools([multiply])

# Node
def tool_calling_llm(state: MessagesState):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# Build graph
builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode([multiply]))
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", END)

# Compile graph
graph = builder.compile()