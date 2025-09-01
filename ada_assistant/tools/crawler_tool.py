import asyncio
import json
from typing import Any, Dict

from crawl4ai import AsyncWebCrawler
from langchain_core.tools import tool


async def _crawl(url: str, max_depth: int = 1, max_links: int = 10) -> Dict[str, Any]:
    """Asynchronous crawling with configurable depth and link limit."""
    async with AsyncWebCrawler() as crawler:
        try:
            result = await crawler.arun(
                url=url, max_depth=max_depth, max_links=max_links, timeout=30
            )
            return {
                "markdown": result.markdown,
                "links": result.links,
                "status_code": result.status_code,
                "error": None,
            }
        except Exception as e:
            return {"markdown": "", "links": [], "status_code": None, "error": str(e)}


@tool("crawl_website", return_direct=True)
def crawl_website(url: str, params: str = "") -> str:
    """
    Crawl a website and return cleaned markdown + metadata.

    Args:
        url: URL to crawl (must start with http:// or https://)
        params: Optional JSON string, e.g. {"max_depth": 2, "max_links": 15}
    """
    if not (url.startswith("http://") or url.startswith("https://")):
        return "Error: URL must start with http:// or https://"

    config = {"max_depth": 1, "max_links": 10}
    if params:
        try:
            user_config = json.loads(params)
            config.update(user_config)
        except json.JSONDecodeError:
            pass

    result = asyncio.run(
        _crawl(url, max_depth=config["max_depth"], max_links=config["max_links"])
    )

    if result["error"]:
        return f"❌ Error crawling {url}: {result['error']}"

    return f"""
    🌍 URL: {url}
    📡 Status: {result['status_code']}
    🔗 Links found: {len(result['links'])}
    📏 Crawl depth: {config['max_depth']}

    📄 CONTENT:
    {result['markdown']}
    """

print(crawl_website.invoke({"url": "https://www.amazon.fr/"}))
