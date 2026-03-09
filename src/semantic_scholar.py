"""
Semantic Scholar API Module
Get top cited papers
"""
import requests
from typing import List, Dict, Optional

API_BASE = "https://api.semanticscholar.org/graph/v1"

FIELDS = {
    "quantum": "quantum computing OR quantum communication",
    "security": "cryptography OR cybersecurity OR security",
    "ml": "machine learning OR deep learning OR transformer"
}

def search_papers(query: str, limit: int = 5, year_min: int = 2022) -> List[Dict]:
    """Search Semantic Scholar for papers"""
    params = {
        "query": query,
        "limit": limit,
        "year": f"{year_min}-",
        "fields": "title,authors,year,venue,citationCount,externalIds,abstract",
        "sort": "-citationCount"
    }
    
    headers = {"Accept": "application/json"}
    
    try:
        response = requests.get(
            f"{API_BASE}/paper/search",
            params=params,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        
        papers = []
        for paper in data.get("data", []):
            external = paper.get("externalIds", {})
            papers.append({
                "title": paper.get("title"),
                "authors": [a.get("name") for a in paper.get("authors", [])],
                "year": paper.get("year"),
                "venue": paper.get("venue"),
                "citation_count": paper.get("citationCount", 0),
                "doi": external.get("DOI"),
                "arxiv": external.get("ArXiv"),
                "abstract": paper.get("abstract")
            })
        
        return papers
    except Exception as e:
        print(f"Error searching Semantic Scholar: {e}")
        return []

def get_top_papers_by_field(field: str) -> List[Dict]:
    """Get top papers for a specific field"""
    query = FIELDS.get(field, field)
    return search_papers(query, limit=3)

if __name__ == "__main__":
    # Test
    papers = get_top_papers_by_field("ml")
    for p in papers:
        print(f"- {p['title'][:50]}... ({p.get('citation_count', 0)} cites)")
