# Claw-Morning Local

> Standalone version of Claw-Morning that runs **WITHOUT AI dependency**. (Local version of one of skills used in my openclaw - if interested, checkout my `claw-skills` for AI version)

## Overview

Claw-Morning Local is a CLI tool that generates daily research briefings by fetching data from public APIs (ArXiv, GitHub, Semantic Scholar, HuggingFace) and generating HTML reports.

## Short Demo
![Claw-Morning-Short-Demo-gif](claw-morning-short-demo.gif)

![Claw-Morning-Research-Short-Demo-gif](claw-morning-research-short-demo.gif)

## Features

- **ArXiv Papers** - Quantum Computing, Quantum Satellite, Quantum+ML, ML, Security
- **Semantic Scholar** - Top cited papers by field
- **GitHub Trending** - Hot repositories
- **AI/ML News** - Industry updates
- **Beautiful HTML** - Responsive design with dark theme
- **Mobile Friendly** - Works on desktop and mobile
- **Feishu Support** - Send directly to Feishu (optional)

## Structure

```
claw-morning-local/
├── main.py              # CLI entry point
├── src/                 # Source modules
│   ├── arxiv_search.py       # ArXiv API
│   ├── semantic_scholar.py   # Semantic Scholar API
│   ├── github_trending.py    # GitHub API
│   ├── huggingface.py        # HuggingFace API
│   ├── news.py               # News fetcher
│   ├── html_generator.py     # HTML generator
│   └── feishu_sender.py     # Feishu integration
├── templates/
│   └── template-v5.html     # HTML template
├── data/
│   ├── history.json          # Recommendation history
│   └── recommendations.json  # Cached recommendations
├── requirements.txt       # Python dependencies
├── .env.example         # Environment template
├── run.sh              # Shell runner
└── README.md           # This file
```

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure (Optional)

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings (optional)
# - FEISHU credentials for sending to Feishu
# - CDN settings for uploading
```

### 3. Run

```bash
# Generate today's briefing
python main.py

# Generate for specific date
python main.py --date 2026-03-09

# Custom output file
python main.py --output my-briefing.html

# Send to Feishu
python main.py --send-feishu
```

Or use the shell script:

```bash
chmod +x run.sh
./run.sh --date 2026-03-09
```

## API Modules

### src/arxiv_search.py
```python
from src.arxiv_search import get_papers_by_category

# Get papers by category
papers = get_papers_by_category("quantum_computing", max_results=3)
```

Categories: `quantum_computing`, `quantum_satellite`, `quantum_ml`, `ml`, `security`

### src/semantic_scholar.py
```python
from src.semantic_scholar import get_top_papers_by_field

# Get top papers by field
papers = get_top_papers_by_field("ml")
```

Fields: `quantum`, `security`, `ml`

### src/github_trending.py
```python
from src.github_trending import get_ai_ml_trending

# Get trending AI/ML repos
repos = get_ai_ml_trending(limit=5)
```

### src/huggingface.py
```python
from src.huggingface import get_trending_papers

# Get trending papers
papers = get_trending_papers(limit=10)
```

### src/html_generator.py
```python
from src.html_generator import generate_briefing

# Generate HTML
generate_briefing(
    template_path="templates/template-v5.html",
    output_path="output.html",
    date="2026-03-09",
    arxiv_papers={...},
    semantic_papers=[...],
    news=[...],
    github=[...],
    quote={...},
    recommendations=[...]
)
```

### src/feishu_sender.py
```python
from src.feishu_sender import send_message, send_file, get_tenant_access_token

# Get token
token = get_tenant_access_token(app_id, app_secret)

# Send message
send_message(token, user_id, "Hello!")

# Send file
send_file(token, user_id, "report.html")
```

## Configuration

### Environment Variables (.env)

```bash
# ArXiv API (public, no key needed)
ARXIV_API_URL=https://export.arxiv.org/api/query

# Semantic Scholar API (public, rate limited)
SEMANTIC_SCHOLAR_API=https://api.semanticscholar.org

# GitHub API (public)
GITHUB_API=https://api.github.com

# HuggingFace (public)
HUGGINGFACE_API=https://huggingface.co/api

# CDN Upload (optional)
CDN_UPLOAD_URL=

# Feishu Configuration (optional)
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_app_secret
FEISHU_USER_ID=your_user_id

# Output directory
OUTPUT_DIR=./output
```

## HTML Template

The template uses:
- Responsive grid layout
- Dark theme with gradient accents
- Mobile-friendly design
- Navigation bar for quick jumps

Template file: `templates/template-v5.html`

## Output

Generates an HTML file with:
- ArXiv papers by category
- Semantic Scholar top papers
- AI/ML news
- GitHub trending repos
- Daily quote
- Recommendations

## Updating

To get the latest version:
1. Download new release from GitHub
2. Replace local files
3. Update `requirements.txt` if needed

## License

MIT

## Contributing

Pull requests welcome! Please ensure tests pass before submitting.

## Support

For issues, please open an issue on GitHub.
