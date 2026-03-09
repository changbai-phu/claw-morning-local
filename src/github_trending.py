"""
GitHub Trending Module
Get trending repositories
"""
import requests
from datetime import datetime, timedelta
from typing import List, Dict

API_URL = "https://api.github.com/search/repositories"

LANGUAGES = ["Python", "JavaScript", "TypeScript"]

def get_trending(days: int = 1, language: str = None, limit: int = 10) -> List[Dict]:
    """Get trending GitHub repos"""
    since = datetime.now() - timedelta(days=days)
    date_str = since.strftime("%Y-%m-%d")
    
    query = f"created:>{date_str}"
    if language:
        query += f" language:{language}"
    
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }
    
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    try:
        response = requests.get(API_URL, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        repos = []
        for item in data.get("items", []):
            repo = {
                "name": item.get("full_name"),
                "description": item.get("description"),
                "stars": item.get("stargazers_count", 0),
                "language": item.get("language"),
                "url": item.get("html_url"),
                "created": item.get("created_at")[:10]
            }
            repos.append(repo)
        
        return repos
    except Exception as e:
        print(f"Error fetching GitHub trending: {e}")
        return []

def get_ai_ml_trending(limit: int = 5) -> List[Dict]:
    """Get AI/ML trending repos"""
    # Search for AI/ML related repos
    repos = get_trending(days=7, limit=limit)
    return repos

if __name__ == "__main__":
    repos = get_ai_ml_trending()
    for r in repos:
        print(f"- {r['name']}: ⭐ {r['stars']}")
