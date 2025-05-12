# You can find an interesting list of mcp servers here: https://github.com/punkpeye/awesome-mcp-servers
from praisonaiagents import Agent, MCP

# LLM choices: llama3.2 (3B), falcon3 (7B)

external_tool_agent = Agent(
    instructions="You are a helpful assistant with access to a tool. Call it when the user asks for it.",
    llm="ollama/falcon3",
    tools=MCP(
        "npx @openbnb/mcp-server-airbnb --ignore-robots-txt")
)
user_input = "Find an apartment in Italy for 25 of September 2025."
response = external_tool_agent.start(user_input)
