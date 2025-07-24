# Vercel Deployment Guide

## 🚀 Deploy to Vercel

This Universal Social Media Downloader is optimized for deployment on Vercel's serverless platform.

### Prerequisites
- A Vercel account (free at [vercel.com](https://vercel.com))
- Git repository (GitHub, GitLab, or Bitbucket)

### Deployment Steps

#### 1. Prepare Repository
```bash
# Ensure all files are committed
git add .
git commit -m "Prepare for Vercel deployment"
git push origin main
```

#### 2. Deploy to Vercel

**Option A: Using Vercel Dashboard**
1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "New Project"
3. Import your GitHub repository
4. Vercel will automatically detect the configuration from `vercel.json`
5. Click "Deploy"

**Option B: Using Vercel CLI**
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy from project directory
vercel

# Follow the prompts:
# - Set up and deploy? Y
# - Which scope? (your account)
# - Link to existing project? N
# - Project name: universal-downloader
# - Directory: ./
# - Override settings? N
```

#### 3. Configure Environment Variables (Optional)
In Vercel Dashboard → Project → Settings → Environment Variables:
- `SECRET_KEY`: Your custom secret key for Flask

### 🔧 Configuration Files

#### `vercel.json`
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/app.py"
    }
  ],
  "functions": {
    "api/app.py": {
      "maxDuration": 300
    }
  }
}
```

#### `requirements.txt`
```
Flask==2.3.3
requests==2.31.0
yt-dlp==2023.10.13
instaloader==4.10.3
Werkzeug==2.3.7
```

### 📁 Project Structure for Vercel
```
project/
├── api/
│   ├── app.py              # Main Flask application
│   └── templates/
│       └── index.html      # Web interface
├── vercel.json             # Vercel configuration
├── requirements.txt        # Python dependencies
├── package.json           # Project metadata
├── index.html             # Static landing page (optional)
└── README.md
```

### ⚠️ Important Considerations

#### Serverless Limitations
- **Execution Time**: Max 300 seconds per request
- **Memory**: 1GB RAM limit
- **Storage**: Temporary filesystem only
- **File Persistence**: Downloaded files are temporary

#### Optimizations Applied
- Lower video quality (720p max) for faster processing
- Bulk download limit (5 URLs max)
- Temporary file storage using `tempfile`
- Reduced Instagram posts limit (5 instead of 10)

### 🔍 Testing Deployment

After deployment, test these endpoints:
- `https://your-app.vercel.app/` - Main interface
- `https://your-app.vercel.app/health` - Health check
- `https://your-app.vercel.app/supported-platforms` - Platform info

### 🐛 Troubleshooting

#### Common Issues:

1. **Build Failures**
   ```bash
   # Check Python dependencies
   vercel logs
   ```

2. **Function Timeout**
   - Large videos may timeout (300s limit)
   - Use shorter videos for testing
   - Consider chunked downloads

3. **Memory Issues**
   - Lower video quality helps
   - Limit concurrent downloads

4. **Missing Dependencies**
   ```bash
   # Verify requirements.txt
   pip install -r requirements.txt
   ```

### 📊 Performance Tips

1. **Optimize for Speed**
   - Use lower quality formats
   - Implement download queues
   - Cache frequently accessed data

2. **Monitor Usage**
   - Check Vercel function logs
   - Monitor execution time
   - Track memory usage

### 🔒 Security

1. **Environment Variables**
   ```bash
   # Set in Vercel Dashboard
   SECRET_KEY=your-secret-key-here
   ```

2. **Rate Limiting**
   - Consider implementing rate limits
   - Add CORS headers if needed

### 📈 Scaling Considerations

For high-traffic scenarios:
- Consider upgrading to Vercel Pro
- Implement caching strategies
- Use CDN for static assets
- Consider microservices architecture

### 🆘 Support

If you encounter issues:
1. Check Vercel logs in dashboard
2. Review function execution time
3. Test locally first: `python api/app.py`
4. Check dependency versions

### 🎯 Next Steps

After successful deployment:
- [ ] Test all download functions
- [ ] Set up monitoring
- [ ] Configure custom domain (optional)
- [ ] Add analytics (optional)
- [ ] Set up CI/CD (optional)

---

**Happy Deploying! 🚀**
