"""
Claw-Morning - Daily Research Briefing Generator
"""
__version__ = "1.1.0"

from .arxiv_search import search_arxiv, get_papers_by_category
from .semantic_scholar import search_papers, get_top_papers_by_field
from .github_trending import get_trending, get_ai_ml_trending
from .huggingface import get_trending_papers
from .news import get_ai_news
from .html_generator import generate_briefing
from .feishu_sender import send_message, send_file

__all__ = [
    "search_arxiv",
    "get_papers_by_category",
    "search_papers", 
    "get_top_papers_by_field",
    "get_trending",
    "get_ai_ml_trending",
    "get_trending_papers",
    "get_ai_news",
    "generate_briefing",
    "send_message",
    "send_file"
]
