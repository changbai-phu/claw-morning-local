"""
ArXiv Search Module
Search for papers on ArXiv
"""
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from typing import List, Dict

ARXIV_API = "http://export.arxiv.org/api/query"

CATEGORIES = {
    "quantum_computing": "cat:cs.QC OR cat:quant-ph",
    "quantum_satellite": "all:quantum AND (satellite OR communication)",
    "quantum_ml": "all:quantum AND machine learning",
    "ml": "cat:cs.LG OR cat:stat.ML",
    "security": "cat:cs.CR"
}

def search_arxiv(query: str, max_results: int = 5, days_back: int = 7) -> List[Dict]:
    """Search ArXiv for papers"""
    # Calculate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back)
    
    # Build query
    search_query = f"{query} AND submittedDate:[{start_date.strftime('%Y%m%d')}000000 TO {end_date.strftime('%Y%m%d')}235959]"
    
    params = {
        "search_query": search_query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }
    
    try:
        response = requests.get(ARXIV_API, params=params, timeout=30)
        response.raise_for_status()
        
        # Parse XML
        root = ET.fromstring(response.content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        
        papers = []
        for entry in root.findall(".//atom:entry", ns):
            paper = {
                "title": entry.find("atom:title", ns).text.strip(),
                "authors": [a.text for a in entry.findall("atom:author/atom:name", ns)],
                "summary": entry.find("atom:summary", ns).text.strip(),
                "published": entry.find("atom:published", ns).text[:10],
                "id": entry.find("atom:id", ns).text.split("/")[-1],
                "link": entry.find("atom:id", ns).text
            }
            papers.append(paper)
        
        return papers
    except Exception as e:
        print(f"Error searching ArXiv: {e}")
        return []

def get_papers_by_category(category: str, max_results: int = 3) -> List[Dict]:
    """Get papers by category"""
    query = CATEGORIES.get(category, category)
    return search_arxiv(query, max_results)

if __name__ == "__main__":
    # Test
    papers = get_papers_by_category("quantum_computing")
    for p in papers:
        print(f"- {p['title'][:50]}...")
