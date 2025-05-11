from praisonaiagents import Agent, MCP

external_agent = Agent(
    instructions="test",
    llm="gpt-4o-mini",
    tools=MCP("npx @openbnb/mcp-server-airbnb")
)

user_input = "Find an apartment in Italy for 25 of September 2025."
response = external_agent.start(user_input)
print(response)
