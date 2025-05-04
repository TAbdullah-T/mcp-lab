# You can find an interesting list of mcp servers here: https://github.com/punkpeye/awesome-mcp-servers
from praisonaiagents import Agent, MCP

# LLM choices: llama3.2 (3B), falcon3 (7B)

external_agent = Agent(
    instructions="test",
    llm="ollama/llama3.2",
    tools=MCP(
        "npx @openbnb/mcp-server-airbnb")
)

print("🔧 Agent initialized. You can now chat with it (type 'exit' to quit).")
print("--------------------------------------------------------------")

# Interactive loop
while True:
    try:
        user_input = input("🧑 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting chat.")
            break
        response = external_agent.start(user_input)
        print(f"🤖 Agent: {response}\n")
    except KeyboardInterrupt:
        print("\n👋 Interrupted. Exiting chat.")
        break
    except Exception as e:
        print(f"⚠️ Error: {e}")
