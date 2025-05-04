from mcp.server.fastmcp import FastMCP
import httpx
from bs4 import BeautifulSoup
import signal
import sys

mcp = FastMCP(name="stock-news-agent", host="127.0.0.1", port=5000, timeout=30)


def signal_handler(sig, frame):
    print("Shutting down...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


@mcp.tool()
async def get_stock_news(ticker: str) -> str:
    """
    Asynchronously scrapes the latest 5 news headlines from Finviz for a given stock ticker.
    """
    try:
        url = f"https://finviz.com/quote.ashx?t={ticker}"
        headers = {'User-Agent': 'Mozilla/5.0'}

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)

        soup = BeautifulSoup(response.content, 'html.parser')
        news_table = soup.find('table', class_='fullview-news-outer')
        rows = news_table.find_all('tr')

        news = []
        for row in rows[:5]:
            time_tag = row.td.text.strip()
            headline = row.a.text.strip()
            link = row.a['href']
            news.append(f"{time_tag} - {headline} ({link})")

        return "\n".join(news)

    except Exception as e:
        return f"Error fetching news: {e}"

if __name__ == "__main__":
    print("Starting stock-news MCP server at PORT 5000...")
    mcp.run()
