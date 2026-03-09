#!/bin/bash
# Claw-Morning Local Runner

# Default values
DATE=$(date +%Y-%m-%d)
OUTPUT="claw-morning-${DATE}.html"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --date)
            DATE="$2"
            shift 2
            ;;
        --output)
            OUTPUT="$2"
            shift 2
            ;;
        --help|-h)
            echo "Usage: ./run.sh [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --date DATE     Date for briefing (default: today)"
            echo "  --output FILE   Output HTML file"
            echo "  --help          Show this help"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

echo "🤖 Running Claw-Morning..."
echo "📅 Date: $DATE"
echo "📄 Output: $OUTPUT"

# Run Python script
python3 main.py --date "$DATE" --output "$OUTPUT"

echo "✅ Done! Output: $OUTPUT"
