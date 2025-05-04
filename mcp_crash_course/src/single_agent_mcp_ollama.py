from praisonaiagents import Agent, MCP
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv("../.env")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

single_agent = Agent(
    instructions="You are a helpful assistant.",
    # llm="ollama/llama3.2",
    llm="gpt-4o-mini",
    tools=MCP("C:\\Users\\farza\\anaconda3\\envs\\mcp-test\\python.exe servers\\daily_news_server.py")
)
single_agent.start(
    "Do you have access to any tools that I provided to you? Specifically get_stock_news")
