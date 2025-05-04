from praisonaiagents import Agent, MCP
import os
from dotenv import load_dotenv
from openai import OpenAI

print(load_dotenv())

client = OpenAI(api_key="sk-proj-Clib8BxUNm6VjQU8yI9oT3BlbkFJ6ckrtNFRBjU0gHGNXCs0")
agent = Agent(
    instructions="""You are a helpful assistant that can check stock prices and perform other tasks.
    Use the available tools when relevant to answer user questions.""",
    llm="ollama/llama3.2",
    tools=MCP("python test/main.py"),
)
agent.start("What is the stock price of AAPL?")
