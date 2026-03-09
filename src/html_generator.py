"""
HTML Generator Module
Generate HTML briefing from templates
"""
import os
import json
from datetime import datetime
from typing import Dict, List
from jinja2 import Template

def load_template(template_path: str) -> Template:
    """Load HTML template"""
    with open(template_path, 'r', encoding='utf-8') as f:
        return Template(f.read())

def generate_arxiv_section(papers: List[Dict], category: str) -> str:
    """Generate ArXiv papers HTML section"""
    html = ""
    for paper in papers:
        html += f'''
<div class="paper-card {category}">
    <div class="title"><a href="{paper.get('link', '#')}" target="_blank">{paper.get('title', 'N/A')}</a></div>
    <div class="meta">{', '.join(paper.get('authors', [])[:3])} | {paper.get('published', 'N/A')}</div>
    <div class="summary"><strong>Summary:</strong> {paper.get('summary', '')[:200]}...</div>
</div>'''
    return html

def generate_semantic_section(papers: List[Dict]) -> str:
    """Generate Semantic Scholar section"""
    html = ""
    for i, paper in enumerate(papers, 1):
        html += f'''
<div class="semantic-card">
    <div class="rank">{i}</div>
    <div class="field">{paper.get('field', 'General')}</div>
    <div class="title"><a href="{paper.get('url', '#')}" target="_blank">{paper.get('title', 'N/A')}</a></div>
    <div class="meta">{paper.get('year', 'N/A')} | {paper.get('venue', 'N/A')}</div>
    <span class="citation">{paper.get('citation_count', 0)} citations</span>
</div>'''
    return html

def generate_news_section(news: List[Dict]) -> str:
    """Generate news section"""
    html = ""
    for item in news:
        html += f'''
<div class="news-item">
    <div class="news-bullet"></div>
    <div class="news-content">
        <div class="news-title"><a href="{item.get('url', '#')}" target="_blank">{item.get('title', 'N/A')}</a></div>
        <div class="news-desc">{item.get('summary', '')}</div>
    </div>
</div>'''
    return html

def generate_github_section(repos: List[Dict]) -> str:
    """Generate GitHub trending section"""
    html = ""
    for i, repo in enumerate(repos, 1):
        html += f'''
<div class="github-card">
    <div class="github-rank">{i}</div>
    <div class="github-info">
        <div class="github-name"><a href="{repo.get('url', '#')}" target="_blank">{repo.get('name', 'N/A')}</a></div>
        <div class="github-desc">{repo.get('description', '')[:100]}</div>
    </div>
    <div class="github-stars">⭐ {repo.get('stars', 0)}</div>
</div>'''
    return html

def generate_briefing(
    template_path: str,
    output_path: str,
    date: str,
    arxiv_papers: Dict[str, List[Dict]],
    semantic_papers: List[Dict],
    news: List[Dict],
    github: List[Dict],
    quote: Dict,
    recommendations: List[Dict]
) -> str:
    """Generate complete HTML briefing"""
    
    template = load_template(template_path)
    
    # Generate sections
    quantum_computing = generate_arxiv_section(arxiv_papers.get("quantum_computing", []), "quantum")
    quantum_satellite = generate_arxiv_section(arxiv_papers.get("quantum_satellite", []), "quantum")
    quantum_ml = generate_arxiv_section(arxiv_papers.get("quantum_ml", []), "quantum")
    ml_papers = generate_arxiv_section(arxiv_papers.get("ml", []), "ml")
    security_papers = generate_arxiv_section(arxiv_papers.get("security", []), "security")
    
    semantic_html = generate_semantic_section(semantic_papers)
    news_html = generate_news_section(news)
    github_html = generate_github_section(github)
    
    # Quote
    quote_html = f'''
<div class="quote-box">
    <div class="quote-text">"{quote.get('text', '')}"</div>
    <div class="quote-author">— {quote.get('author', 'Unknown')}</div>
</div>'''
    
    # Recommendations
    rec_html = ""
    for rec in recommendations:
        rec_html += f'''
<div class="rec-item">
    <div class="rec-title"><a href="{rec.get('url', '#')}" target="_blank">{rec.get('title', 'N/A')}</a></div>
    <div class="rec-why">{rec.get('reason', '')}</div>
</div>'''
    
    # Fill template
    html = template.render(
        DATE=date,
        TIMESTAMP=datetime.now().isoformat(),
        QUANTUM_COMPUTING_PAPERS=quantum_computing,
        QUANTUM_SATELLITE_PAPERS=quantum_satellite,
        QUANTUM_ML_PAPERS=quantum_ml,
        ML_PAPERS=ml_papers,
        SECURITY_PAPERS=security_papers,
        SEMANTIC_SCHOLAR=semantic_html,
        AI_ML_NEWS=news_html,
        GITHUB_TRENDING=github_html,
        QUOTE_TEXT=quote.get('text', ''),
        QUOTE_AUTHOR=quote.get('author', ''),
        RECOMMENDATIONS=rec_html,
        HISTORY=""
    )
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return output_path

if __name__ == "__main__":
    # Test
    print("HTML Generator ready")
