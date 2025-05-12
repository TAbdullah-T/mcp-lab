from praisonaiagents import Agent, MCP, PraisonAIAgents

# LLM choices: llama3.2 (3B), falcon3 (7B)

daily_news_agent = Agent(
    instructions="You are a helpful assistant with access to a tool. Call it when the user asks for it.",
    llm="ollama/falcon3",
    tools=MCP("python src/servers/daily_news.py")
)
stock_news_agent = Agent(
    instructions="You are a helpful assistant with access to a tool. Call it when the user asks for it.",
    llm="ollama/falcon3",
    tools=MCP("python src/servers/stock_news.py")
)
multi_tools_agents = PraisonAIAgents(
    agents=[daily_news_agent, stock_news_agent])


print("🔧 Agent initialized. You can now chat with it (type 'exit' to quit).")
print("--------------------------------------------------------------")

# Interactive loop
while True:
    try:
        user_input = input("🧑 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting chat.")
            break
        response = multi_tools_agents.start(user_input)
        print(f"🤖 Agent: {response}\n")
    except KeyboardInterrupt:
        print("\n👋 Interrupted. Exiting chat.")
        break
    except Exception as e:
        print(f"⚠️ Error: {e}")
