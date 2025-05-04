from praisonaiagents import Agent, MCP

external_agent = Agent(
    instructions="test",
    llm="ollama/llama3.2",
    tools=MCP(
        "python src/stock_news_server.py")
)
external_agent.start("Use the `get_stock_news` tool to get news for Tesla.")
