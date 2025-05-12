from praisonaiagents import Agent, MCP
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

external_tool_agent = Agent(
    instructions="You are a helpful assistant with access to a tool. Call it when the user asks for it.",
    llm="gpt-4o-mini",
    tools=MCP("npx @openbnb/mcp-server-airbnb --ignore-robots-txt")
)

user_input = "Find an apartment in Italy for 25 of September 2025 for a single person."
response = external_tool_agent.start(user_input)
print(response)
