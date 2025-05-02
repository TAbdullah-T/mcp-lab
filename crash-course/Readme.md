# 🧠 FastMCP Crash Course – News + Stock Agents

This repo contains **two simple MCP servers** using [FastMCP](https://github.com/jlowin/fastmcp):

1. **`news-reader`** — Fetches the latest headlines from major news websites (NPR, BBC).
2. **`stock-news-agent`** — Fetches recent stock-related headlines for a given ticker from [Finviz](https://finviz.com/).

These tools are exposed via the [Model Context Protocol (MCP)](https://modelcontextprotocol.org), allowing integration with AI agents such as Claude Desktop.

---

## 📦 Contents

```bash
crash-course/
├── news_reader.py           # General news reader tool (NPR, BBC)
├── stock_news_agent.py      # Stock news scraping tool (Finviz)
├── requirements.txt
└── README.md
```

---

## 🧠 What Is MCP?

Model Context Protocol (MCP) is an emerging open standard designed to let AI agents talk to local tools securely and naturally. Think of it as letting your LLM "call functions" that you define locally.

These projects show how to create such tools using [FastMCP](https://github.com/jlowin/fastmcp), a lightweight Python framework to run MCP-compatible servers.

---

## 📰 `news_reader.py` – General News Agent

Fetches the top 10 headlines from either **NPR** or **BBC**.

### 🧪 Sample Output for the LLM Agent

```
- World leaders respond to global tensions
- AI regulations debated at the UN
...
```

---

## 💹 `stock_news_agent.py` – Stock News Agent

Scrapes the latest 5 headlines for a stock ticker from [finviz.com](https://finviz.com).

### 🧪 Sample Output for the LLM Agent

```
08:01AM - Apple launches new iPad (https://...)
07:45AM - Analyst upgrades Apple to Buy (https://...)
```

---

## ⚙️ Setup Instructions

### 1. Clone This Repository

```bash
git clone https://github.com/Farzad-R/mcp-lab.git
cd mcp-lab
```

### 2. Create Environment (recommended: `uv`, `venv`, or `poetry`)

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Start the Servers

```bash
python news_reader.py          # Runs on port 8080
python stock_news_agent.py     # Runs on port 5000
```

---

Sure! Here's the improved and well-formatted version of that section for your `README.md`, with added clarity and formatting for beginners who follow along in your crash course:

---

## 🧠 How to Use with Claude Desktop

Want Claude to use your local news tools? You can expose them to Claude Desktop using [FastMCP](https://github.com/jlowin/fastmcp) and MCP integration.

### ✅ Step-by-Step Setup

#### 1. Install Claude Desktop

Download it from the [official website](https://claude.ai/download).

#### 2. Locate and Edit Your Claude Config

* Open Claude Desktop.
* Go to: **File → Settings → Developer → Edit Config**
* This will open your `claude_desktop_config.json` file.

#### 3. Add Your MCP Servers

Update your JSON config to include both the **stock-news agent** and the **daily news reader**:

```json
{
  "mcpServers": {
    "stock-news": {
      "command": "<absolute path to your python executable>",
      "args": [
        "<absolute path to stock_news_agent.py>"
      ],
      "host": "127.0.0.1",
      "port": 5000,
      "timeout": 30000
    },
    "read-daily-news": {
      "command": "<absolute path to your python executable>",
      "args": [
        "<absolute path to news_reader.py>"
      ],
      "host": "127.0.0.1",
      "port": 8080,
      "timeout": 30000
    }
  }
}
```

> 🔍 **How to find paths:**
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
> * To get the absolute path of your `.py` files, right-click them and copy full path or run:
>
>   ```bash
>   realpath stock_news_agent.py
>   ```

#### 4. Save the File and Restart Claude Desktop

Claude will now be able to detect and run your local tools when prompted.

---

### 💬 Example Prompts

In Claude, you can now simply say:

> “Use the `get_stock_news` tool to get news for Tesla.”

> “Call the `get_latest_news` tool to show headlines from NPR.”

Claude will run the corresponding Python script behind the scenes and return results using MCP.

---

## 🔐 Notes

* These tools are basic demos for educational use.
* Make sure not to abuse web scraping—respect the terms of service of the sites used.

---
