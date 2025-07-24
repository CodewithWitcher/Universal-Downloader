#!/bin/bash

# Universal Social Media Downloader - Local Launch Script
# Optimized for highest quality downloads

echo "🚀 Starting Universal Social Media Downloader..."
echo "📱 Optimized for HIGHEST QUALITY local downloads"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "🔧 Please run: python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment and start the app
source .venv/bin/activate

echo "🔍 Checking dependencies..."
python -c "import flask, yt_dlp, instaloader; print('✅ All dependencies available')" || {
    echo "❌ Dependencies missing. Installing..."
    pip install flask requests yt-dlp instaloader werkzeug
}

echo ""
echo "🌐 Starting server on http://localhost:8080"
echo "📁 Downloads will be saved to ./downloads/"
echo ""
echo "🎯 Configured for MAXIMUM QUALITY:"
echo "   • YouTube: Best video+audio (4K/8K if available)"
echo "   • Instagram: Original resolution + metadata"
echo "   • TikTok: Original quality"
echo "   • All platforms: Thumbnails, subtitles, metadata"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=" * 60

python app.py
