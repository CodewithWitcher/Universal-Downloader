from flask import Flask, request, render_template, jsonify
import os
import tempfile
import requests
import json
import re
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'vercel-deployment-key-2025')

# For Vercel, use temp directory for downloads
DOWNLOAD_DIR = tempfile.mkdtemp()

class BasicDownloader:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def detect_platform(self, url):
        """Detect the platform from URL"""
        url = url.lower()
        if 'youtube.com' in url or 'youtu.be' in url:
            return 'youtube'
        elif 'instagram.com' in url:
            return 'instagram'
        elif 'facebook.com' in url or 'fb.watch' in url:
            return 'facebook'
        elif 'twitter.com' in url or 'x.com' in url:
            return 'twitter'
        elif 'tiktok.com' in url:
            return 'tiktok'
        elif 'reddit.com' in url:
            return 'reddit'
        else:
            return 'unknown'
    
    def download_content(self, url):
        """Basic download function - placeholder for now"""
        platform = self.detect_platform(url)
        
        # For initial deployment, just return success with platform detection
        return {
            'status': 'success',
            'message': f'Platform detected: {platform}. Full download functionality requires yt-dlp and instaloader packages.',
            'platform': platform,
            'type': 'detection',
            'note': 'This is a demo response. Install yt-dlp and instaloader for full functionality.'
        }

# Initialize downloader
downloader = BasicDownloader()

@app.route('/')
def index():
    """Main page"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Universal Social Media Downloader</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #0a0a0a; color: white; }
            .container { max-width: 800px; margin: 0 auto; }
            h1 { color: #8b5cf6; text-align: center; }
            .form-group { margin: 20px 0; }
            input[type="url"] { width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #333; background: #1a1a1a; color: white; border-radius: 8px; }
            button { background: #8b5cf6; color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; width: 100%; }
            button:hover { background: #7c3aed; }
            .status { margin: 20px 0; padding: 12px; border-radius: 8px; }
            .success { background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); color: #10b981; }
            .error { background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); color: #ef4444; }
            .platforms { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 20px 0; }
            .platform { background: #1a1a1a; padding: 16px; border-radius: 8px; border: 1px solid #333; }
            .badge { background: #8b5cf6; color: white; padding: 4px 8px; border-radius: 12px; font-size: 0.8em; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌐 Universal Social Media Downloader</h1>
            <div class="badge">🚀 Deployed on Vercel</div>
            
            <div class="form-group">
                <label for="url">Enter social media URL:</label>
                <input type="url" id="url" placeholder="https://www.youtube.com/watch?v=..." />
                <button onclick="downloadContent()">Detect Platform & Download</button>
                <div id="status"></div>
            </div>

            <div class="platforms">
                <div class="platform">
                    <h3>📺 Supported Platforms</h3>
                    <ul>
                        <li>YouTube</li>
                        <li>Instagram</li>
                        <li>TikTok</li>
                        <li>Twitter/X</li>
                        <li>Facebook</li>
                        <li>Reddit</li>
                    </ul>
                </div>
                <div class="platform">
                    <h3>⚡ Features</h3>
                    <ul>
                        <li>Auto-platform detection</li>
                        <li>Bulk downloads</li>
                        <li>High quality videos</li>
                        <li>Metadata preservation</li>
                        <li>Subtitle support</li>
                    </ul>
                </div>
            </div>

            <p style="text-align: center; color: #666;">
                Made with ❤️ by Witcher | Deployed on Vercel
            </p>
        </div>

        <script>
        async function downloadContent() {
            const url = document.getElementById('url').value;
            const status = document.getElementById('status');
            
            if (!url) {
                status.innerHTML = '<div class="status error">Please enter a URL</div>';
                return;
            }
            
            status.innerHTML = '<div class="status">Processing...</div>';
            
            try {
                const response = await fetch('/download', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ url: url })
                });
                
                const result = await response.json();
                
                if (result.status === 'success') {
                    status.innerHTML = `<div class="status success">
                        ✅ ${result.message}<br>
                        🌐 Platform: ${result.platform}<br>
                        ${result.note ? `📝 Note: ${result.note}` : ''}
                    </div>`;
                } else {
                    status.innerHTML = `<div class="status error">❌ ${result.message}</div>`;
                }
            } catch (error) {
                status.innerHTML = `<div class="status error">❌ Network error: ${error.message}</div>`;
            }
        }
        </script>
    </body>
    </html>
    '''

@app.route('/download', methods=['POST'])
def download():
    """Handle download requests"""
    try:
        data = request.get_json()
        url = data.get('url', '').strip()
        
        if not url:
            return jsonify({'status': 'error', 'message': 'URL is required'})
        
        # Start download
        result = downloader.download_content(url)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Server error: {str(e)}'})

@app.route('/supported-platforms')
def supported_platforms():
    """List supported platforms"""
    platforms = {
        'video_platforms': [
            'YouTube (videos, shorts, playlists)',
            'TikTok',
            'Twitter/X',
            'Facebook',
            'Instagram (Reels, IGTV)',
            'Reddit'
        ],
        'features': [
            'Auto-platform detection',
            'Bulk downloads',
            'High quality downloads',
            'Metadata preservation',
            'Subtitle downloads'
        ],
        'status': 'Demo version - Install yt-dlp and instaloader for full functionality'
    }
    return jsonify(platforms)

@app.route('/health')
def health_check():
    """Health check endpoint for Vercel"""
    return jsonify({
        'status': 'healthy',
        'service': 'Universal Social Media Downloader',
        'version': '1.0.0',
        'environment': 'vercel',
        'note': 'Demo version - requires yt-dlp and instaloader for full functionality'
    })

# For Vercel
if __name__ == '__main__':
    app.run(debug=False)
