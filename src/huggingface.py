"""
HuggingFace Papers Module
Get trending papers from HuggingFace
"""
import requests
from typing import List, Dict

API_URL = "https://huggingface.co/api/papers"

def get_trending_papers(limit: int = 10) -> List[Dict]:
    """Get trending papers from HuggingFace"""
    # Try the trending endpoint
    try:
        response = requests.get(f"{API_URL}/trending", params={"limit": limit}, timeout=30)
        if response.status_code == 200:
            data = response.json()
            papers = []
            for item in data:
                papers.append({
                    "title": item.get("title"),
                    "paper_id": item.get("paper_id"),
                    "url": f"https://huggingface.co/papers/{item.get('paper_id')}",
                    "likes": item.get("likes", 0),
                    "published_at": item.get("published_at"),
                    "github_repo": item.get("github_repo")
                })
            return papers
    except Exception as e:
        print(f"Error fetching HuggingFace trending: {e}")
    
    # Fallback: return sample data
    return []

def get_paper_details(paper_id: str) -> Dict:
    """Get details for a specific paper"""
    try:
        response = requests.get(f"{API_URL}/{paper_id}", timeout=30)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching paper details: {e}")
    return {}

if __name__ == "__main__":
    papers = get_trending_papers()
    for p in papers:
        print(f"- {p.get('title', 'N/A')[:50]}")
