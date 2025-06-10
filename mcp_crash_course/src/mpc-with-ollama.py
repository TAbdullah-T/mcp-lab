from praisonaiagents import Agent, MCP, PraisonAIAgents
from llama_index.llms.ollama import Ollama

# it does not work with customed ollama models.
# llm = Ollama(model="gemma3:4b", request_timeout=120.0, base_url="http://localhost:11434")


daily_news_agent = Agent(
    instructions="You are a helpful assistant with access to a tool. Call it when the user asks for it. then give a summary of the news in short terms.",
    llm="gemma3:4b",
    tools=MCP("uv mcp-lab/mcp_crash_course/src/servers/daily_news.py")
)
stock_news_agent = Agent(
    instructions="You are a helpful assistant with access to a tool. Call it when the user asks for it.",
    llm="gemma3:4b",
    tools=MCP("uv src/servers/stock_news.py")
)
# Extrnal tool agent
external_tool_agent = Agent(
    instructions="You are a helpful assistant with access to a tool. Call the tool if the user asks for it.",
    llm="gemma3:4b",
    tools=MCP("npx @openbnb/mcp-server-airbnb")
)

user_input = "Find an apartment in Italy for 25 of September 2025."

multi_tools_agents = PraisonAIAgents(agents=[daily_news_agent,
                                             
                                             stock_news_agent,
                                             external_tool_agent])


user_input = "Call the get_latest_news tool to show headlines from NPR."
response = multi_tools_agents.start(user_input)
print(response)