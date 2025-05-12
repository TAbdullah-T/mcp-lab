# 🧠 MCP Crash Course – (Claude desktop - Ollama - OpenAI)

This repo demonstrates how to run local and remote [Model Context Protocol (MCP)](https://modelcontextprotocol.org) servers with claude desktop, Ollama, and OpenAI. 

---

### 📚 Table of Contents

---

* [MCP Crash Course – News + Stock Agents](#-mcp-crash-course--news--stock-agents)
* [Contents](#-contents)
* [What Is MCP?](#-what-is-mcp)
* [Setup Instructions](#️-setup-instructions)
* [How to Use with Claude Desktop](#-how-to-use-with-claude-desktop)
* [Example Prompts](#-example-prompts)
* [Run on Claude Code](#️-run-on-claude-code)
* [Debugging and Running Locally](#-debugging-and-running-locally)
* [Notes](#-notes)
* [How to Use MCP with Ollama](#-how-to-use-mcp-with-ollama)
* [Run MCP with Ollama (Local Tools)](#-run-mcp-with-ollama-(Local-Tools))
* [Run MCP with Ollama (Remote/Public Tools)](#-run-mcp-with-ollama-(remote/public-tools))
* [How to Use MCP with OpenAI](#-how-to-use-mcp-with-openai)

---

## 🧠 What Is MCP?

Model Context Protocol (MCP) is an emerging open standard designed to let AI agents talk to local tools securely and naturally. Think of it as letting your LLMs "call functions" that you define.

---

## ⚙️ Setup Instructions

### 1. Clone This Repository

```bash
git clone https://github.com/Farzad-R/mcp-lab.git
cd mcp-lab/mcp-crash-course
```

### 2. Create a Python Environment

```bash
python -m venv .venv
.venv\Scripts\activate # on Windows or ```source .venv/bin/activate``` on Linux and Mac
```
**Using `uv`:**
```bash
uv venv
```

### 3. Install the dependencies

**Using `pip`:**

```bash
pip install mcp beautifulsoup4 ipykernel requests mcp[cli]
```

**Using `uv`:**

```bash
uv add mcp beautifulsoup4 ipykernel requests mcp[cli]
```

### 4. Start the Servers

**Using `pip`:**

```bash
python src\servers\daily_news.py
python src\servers\stock_news.py
python src\servers\wikipedia_summary.py
```

**Using `uv`:**

```bash
uv run src\servers\daily_news.py
uv run src\servers\stock_news.py
uv run src\servers\wikipedia_summary.py
```

Now that the servers are running, we can integrate them into `Claude Desktop`, `OLLAMA`, or `OpenAI` models.

---

## 🧠 How to Use with Claude Desktop

### ✅ Step-by-Step Setup

#### 1. Install Claude Desktop

Download it from the [official website](https://claude.ai/download).

#### 2. Locate and Edit Your Claude Config

* Open Claude Desktop.
* Go to: **File → Settings → Developer → Edit Config**
* This will open your `claude_desktop_config.json` file.

#### 3. Add Your MCP Servers

##### Local servers

Update your JSON config to include both the **stock-news agent** and the **daily news reader**:

If you are using `uv`:

```json
{
    "mcpServers": {
      "stock-news": {
        "command": "C:\\Users\\farza\\anaconda3\\envs\\mcp-test\\python.exe",
        "args": [
          "D:\\Github\\mcp_lab\\mcp_crash_course\\src\\servers\\stock_news.py"
        ],
        "host": "127.0.0.1",
        "port": 5000,
        "timeout": 30000
      },
      "daily-news": {
        "command": "C:\\Users\\farza\\anaconda3\\envs\\mcp-test\\python.exe",
        "args": [
          "D:\\Github\\mcp_lab\\mcp_crash_course\\src\\servers\\daily_news.py"
        ],
        "host": "127.0.0.1",
        "port": 8080,
        "timeout": 30000
      }
    }
  }
```

You can fine more examples for both `pip` and `uv` in `anthropic_developer_config_templates` folder.

```
> 🔍 **How to find absolute paths:**
>
> * On **Mac/Linux**, activate your environment and run:
>
>   ```bash
>   which python
>   ```
> * On **Windows** (Git Bash or Command Prompt):
>
>   ```bash
>   where python
>   ```
> * To get the absolute path of your `.py` files, right-click them and copy path.
```

##### Remote/Public servers

You can find a list of available MCP servers in this [repository](https://github.com/punkpeye/awesome-mcp-servers?tab=readme-ov-file).

Example config for connecting to [airbnb-server](https://github.com/openbnb-org/mcp-server-airbnb):

```json
{
  "mcpServers": {
    "airbnb": {
      "command": "npx",
      "args": [
        "-y",
        "@openbnb/mcp-server-airbnb"
      ]
    }
  }
}
```

#### 4. Save the File and Restart Claude Desktop

Claude will now be able to detect and run your local tools when prompted.

---

### 💬 Example Prompts

In Claude, you can now simply say:

> “Use the `stock_news` tool to get news for Tesla.”

> “Call the `daily_news` tool to show headlines from NPR.”

> “Use my airbnb tool and find an apartment in Italy for 25 of September 2025.”

Claude will run the corresponding Python script behind the scenes and return results using MCP.

---

## 🐞 Debugging and Running Locally

Follow the steps below to get started with debugging and running your tools.

### 1. Install the MCP CLI

```bash
pip install mcp[cli]
or
uv add mcp[cli]
```

### 2. Check if Node.js, npm, and npx are installed

Open your terminal and type:

```bash
node -v
npm -v
npx -v
```

If you see version numbers (like `v18.16.1`), you're good to go.
If it says "command not found" or something similar, continue to the next step.

### 3. Install Node.js

#### On **Windows** or **Mac**:

* Visit: [https://nodejs.org](https://nodejs.org)
* Download the **LTS version**
* During installation, **check "Add to PATH"**
* After installation, **restart your terminal**
* Verify again with `node -v` and `npx -v`

#### On **Linux**:

Run the following commands in your terminal:

```bash
sudo apt update
sudo apt install nodejs npm
```

Then check versions ad verify the installation:

```bash
node -v
npm -v
npx -v
```

---

### 4. Start Debugging

Run the following command (replace with the actual path to your module):

```bash
mcp dev <path-to-your-module>/get_latest_news.py
```

You’ll be prompted:

```bash
Need to install the following packages:
@modelcontextprotocol/inspector@0.11.0
Ok to proceed? (y)
```

Type `y` and press **Enter**.

After that, you’ll see something like:

```bash
Starting MCP inspector...
⚙️ Proxy server listening on port 6277
🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
```

Click the link or open it in your browser to use the tool inspector.
There you can **list, run, and debug** your tools.

---

## 🔐 Notes

* These tools are basic demos for educational use.
* Make sure not to abuse web scraping—respect the terms of service of the sites used.

---

## 🧠 How to Use MCP with Ollama

### ✅ Step-by-Step Setup (Linux / WSL)

To run MCP with Ollama, you'll need a **Linux environment**. If you're using Windows, I recommend setting up **WSL (Windows Subsystem for Linux)**.

#### 1. Set Up Environment

* If you haven't already, install WSL:
  [Install WSL Guide](https://learn.microsoft.com/en-us/windows/wsl/install)

* Follow the steps in the previous sections to install **Node.js** and **npm**.

* Set up a Python environment and install the required libraries.

#### 2. Install Ollama

* Download and install Ollama from the official site:
  [https://ollama.com](https://ollama.com)

* Open a terminal and pull your desired models (make sure they support **tool calling**):

```bash
ollama pull llama3.2
ollama pull falcon3
```

#### 3. Run MCP with Ollama (Local Tools)

There are a few framework that would allow you to use the MCP servers with OLLAMA. I am using `praisonaiagents` due to its bigger community. 

Install it using
```bash
pip install praisonaiagents
```

Use this template to connect Ollama to a **local MCP tool**:

```python
from praisonaiagents import Agent, MCP

single_agent = Agent(
    instructions="You are a helpful assistant. Only call the tool if the user asks for it.",
    llm="ollama/falcon3",
    tools=MCP("python src/servers/daily_news.py")
)

user_input = "Call the get_latest_news tool to show headlines from NPR."
response = single_agent.start(user_input)
print(response)
```

#### 4. Run MCP with Ollama (Remote/Public Tools)

To connect to a **public MCP server**, use the following template:

```python
from praisonaiagents import Agent, MCP

external_agent = Agent(
    instructions="test",
    llm="ollama/llama3.2",
    tools=MCP("npx @openbnb/mcp-server-airbnb")
)

user_input = "Find an apartment in Italy for 25 of September 2025."
response = external_agent.start(user_input)
print(response)
```

---


## 🧠 How to Use MCP with OpenAI

You can use the same library `praisonaiagents` to run MCP servers with OpenAI models. Sample code:

```python
from praisonaiagents import Agent, MCP

external_agent = Agent(
    instructions="test",
    llm="gpt-4o-mini",
    tools=MCP("npx @openbnb/mcp-server-airbnb")
)

user_input = "Find an apartment in Italy for 25 of September 2025."
response = external_agent.start(user_input)
print(response)
```

---