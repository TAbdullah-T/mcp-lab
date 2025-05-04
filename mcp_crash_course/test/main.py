import yfinance as yf
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

mcp = FastMCP("stock_prices")


@mcp.tool()
async def get_stock_price(ticker: str) -> str:
    """Get the current stock price for a given ticker symbol."""
    if not ticker:
        return "No ticker provided"
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        current_price = info.get(
            "currentPrice") or info.get("regularMarketPrice")
        if not current_price:
            return f"Could not retrieve price for {ticker}"
        return f"${current_price:.2f}"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
