#!/usr/bin/env python3
"""
Test script for Universal Social Media Downloader
Tests the downloader functionality locally
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import UniversalDownloader

def test_platform_detection():
    """Test platform detection functionality"""
    downloader = UniversalDownloader()
    
    test_urls = {
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ': 'youtube',
        'https://youtu.be/dQw4w9WgXcQ': 'youtube',
        'https://www.instagram.com/p/ABC123/': 'instagram',
        'https://www.tiktok.com/@user/video/123': 'tiktok',
        'https://twitter.com/user/status/123': 'twitter',
        'https://x.com/user/status/123': 'twitter',
        'https://www.facebook.com/video/123': 'facebook',
        'https://www.reddit.com/r/videos/comments/123': 'reddit',
    }
    
    print("🔍 Testing Platform Detection:")
    print("-" * 50)
    
    for url, expected in test_urls.items():
        detected = downloader.detect_platform(url)
        status = "✅" if detected == expected else "❌"
        print(f"{status} {url[:40]}... → {detected}")
    
    print()

def main():
    print("🚀 Universal Social Media Downloader - Local Test")
    print("=" * 60)
    
    # Test platform detection
    test_platform_detection()
    
    print("📁 Downloads will be saved to: ./downloads/")
    print("🌐 Ready to start! Run: python app.py")
    print("📱 Then visit: http://localhost:5000")
    print()
    print("🎯 Optimized for HIGHEST QUALITY downloads:")
    print("   • YouTube: Best video+audio quality available")
    print("   • Instagram: Full resolution with metadata")
    print("   • TikTok: Original quality")
    print("   • Twitter: Best available format")
    print("   • Facebook: Highest quality")
    print("   • Reddit: Best available")
    print("   • All platforms: Thumbnails, metadata, subtitles")

if __name__ == "__main__":
    main()
