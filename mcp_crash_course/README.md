# 🧠 MCP Crash Course – News + Stock Agents

This repo contains **two simple MCP servers**:

1. **`news-reader`** — Fetches the latest headlines from major news websites (NPR, BBC).
2. **`stock-news-agent`** — Fetches recent stock-related headlines for a given ticker from [Finviz](https://finviz.com/).

These tools are exposed via the [Model Context Protocol (MCP)](https://modelcontextprotocol.org), allowing integration with AI agents such as Claude Desktop.

---

### 📚 Table of Contents

---

* [MCP Crash Course – News + Stock Agents](#-mcp-crash-course--news--stock-agents)
* [Contents](#-contents)
* [What Is MCP?](#-what-is-mcp)
* [`news_reader.py` – General News Agent](#-news_readerpy--general-news-agent)
* [`stock_news_agent.py` – Stock News Agent](#-stock_news_agentpy--stock-news-agent)
* [Setup Instructions](#️-setup-instructions)
* [How to Use with Claude Desktop](#-how-to-use-with-claude-desktop)
* [Example Prompts](#-example-prompts)
* [Run on Claude Code](#️-run-on-claude-code)
* [Debugging and Running Locally](#-debugging-and-running-locally)
* [Notes](#-notes)

---

## 📦 Project structure

```bash
mcp-crash-course/
├── news_reader.py           # General news reader tool (NPR, BBC)
├── stock_news_agent.py      # Stock news scraping tool (Finviz)
├── requirements.txt
└── README.md
```

---

## 🧠 What Is MCP?

Model Context Protocol (MCP) is an emerging open standard designed to let AI agents talk to local tools securely and naturally. Think of it as letting your LLM "call functions" that you define locally.

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
.venv\Scripts\activate # on Windows or ```source .venv/bin/activate``` on Linux and Mac
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
python src\daily_news_server.py
python src\stock_news_server.py
```

**Using `uv`:**

```bash
uv run src\daily_news_server.py
uv run src\stock_news_server.py
```

Now that the servers are running, we can integrate them into `Claude Desktop` or `OLLAMA`.

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

Update your JSON config to include both the **stock-news agent** and the **daily news reader**:

If you are using `uv`:

```json
{
  "mcpServers": {
    "stock-news": {
      "command": "C:\\Users\\farza\\anaconda3\\envs\\mcp-test\\Scripts\\uv.exe",
      "args": [
        "--directory",
        "D:\\Github\\mcp_lab\\mcp_crash_course\\src",
        "run",
        "stock_news_server.py"
      ],
      "host": "127.0.0.1",
      "port": 5000,
      "timeout": 30000
    },
    "read-daily-news": {
      "command": "C:\\Users\\farza\\anaconda3\\envs\\mcp-test\\Scripts\\uv.exe",
      "args": [
        "--directory",
        "D:\\Github\\mcp_lab\\mcp_crash_course\\src",
        "run",
        "daily_news_server.py"
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

#### 4. Save the File and Restart Claude Desktop

Claude will now be able to detect and run your local tools when prompted.

---

### 💬 Example Prompts

In Claude, you can now simply say:

> “Use the `get_stock_news` tool to get news for Tesla.”

> “Call the `get_latest_news` tool to show headlines from NPR.”

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
