"""
Tavily Search Tool Module
=========================
DAY 3: This module provides web search capabilities via Tavily.

SOLID Principle: Open/Closed Principle (OCP)
- Open for extension (can add more search tools)
- Closed for modification

Topics to teach:
- Tool integration in LangChain
- Web search augmentation
- When to use web search vs document search
- Tavily API usage
"""

import os
from typing import List, Optional, Literal
from langchain_tavily import TavilySearch

from config.settings import settings


class TavilySearchTool:
    """
    Web search tool using Tavily API.
    
    Use this when:
    - User asks about current events
    - Document search doesn't have relevant information
    - User explicitly asks to search the web
    
    Tavily provides high-quality, AI-optimized search results.
    """
    
    def __init__(
        self,
        max_results: int = 3,
        topic: Literal["general", "news", "finance"] = "general"
    ):
        """
        Initialize the Tavily search tool.
        
        Args:
            max_results: Maximum number of search results
            topic: Search topic - "general", "news", or "finance"
        """
        self.max_results = max_results
        self.topic = topic
        
        # Set Tavily API key in environment (required by langchain-tavily)
        os.environ["TAVILY_API_KEY"] = settings.TAVILY_API_KEY
        
        # Initialize Tavily search
        self._search = TavilySearch(
            max_results=self.max_results,
            topic=self.topic
        )
    
    @property
    def tool(self) -> TavilySearch:
        """Get the Tavily search tool instance."""
        return self._search
    
    def search(self, query: str) -> str:
        """
        Perform a web search and return formatted string.
        
        Args:
            query: Search query
            
        Returns:
            Search results as formatted string
        """
        results = self._search.invoke(query)
        return self._format_results(results)
    
    def _format_results(self, results: dict) -> str:
        """
        Format Tavily results dictionary into readable string.
        
        Args:
            results: Raw Tavily results dictionary
            
        Returns:
            Formatted string of search results
        """
        if not results:
            return "No search results found."
        
        formatted_parts = []
        
        # Add answer if available
        if results.get("answer"):
            formatted_parts.append(f"Summary: {results['answer']}")
        
        # Add individual results
        if results.get("results"):
            for i, result in enumerate(results["results"], 1):
                title = result.get("title", "No title")
                content = result.get("content", "No content")
                url = result.get("url", "")
                formatted_parts.append(f"[{i}] {title}\n{content}\nSource: {url}")
        
        return "\n\n".join(formatted_parts) if formatted_parts else "No results found."
    
    def search_with_context(self, query: str) -> dict:
        """
        Perform a web search and return structured results.
        
        Args:
            query: Search query
            
        Returns:
            Dictionary with search results and metadata
        """
        raw_results = self._search.invoke(query)
        
        return {
            "query": query,
            "results": raw_results,
            "formatted": self._format_results(raw_results),
            "source": "tavily_web_search"
        }

