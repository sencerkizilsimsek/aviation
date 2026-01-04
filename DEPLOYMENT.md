# 🚀 Deployment Guide

This guide will help you deploy your THY Cadet Pilot Prep app online so it can be accessed from anywhere via a web link.

## Option 1: Streamlit Community Cloud (Recommended - FREE)

Streamlit Community Cloud is the easiest and free way to deploy your app.

### Prerequisites
- A GitHub account
- Your code pushed to a GitHub repository

### Step-by-Step Deployment

#### 1. Prepare Your Repository

Make sure your code is on GitHub:

```bash
# If not already a git repository
git init
git add .
git commit -m "Initial commit"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

#### 2. Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**: https://share.streamlit.io/
2. **Sign in** with your GitHub account
3. **Click "New app"**
4. **Select your repository** and branch (usually `main`)
5. **Set the main file path**: `app.py`
6. **Click "Deploy"**

Your app will be available at: `https://YOUR_APP_NAME.streamlit.app`

#### 3. Configure Secrets (API Keys)

**Important**: Never commit your API keys to GitHub!

Instead, use Streamlit Secrets:

1. In your Streamlit Cloud app dashboard, go to **Settings** → **Secrets**
2. Add your secrets in TOML format:

```toml
[gemini]
api_key = "your-gemini-api-key-here"
```

3. The app will automatically use these secrets in production.

#### 4. Update config.yaml for Production

For production, you can leave the API key empty in `config.yaml` since it will use secrets:

```yaml
gemini:
  api_key: ""  # Leave empty - will use Streamlit secrets
  model: "gemini-1.5-flash"
  enabled: true

ai_enhancements:
  dictionary: true
  news: true
  history: true
  future: true
  fleet: true
  destinations: true
```

### Automatic Updates

- Every time you push to GitHub, Streamlit Cloud automatically redeploys your app
- Changes go live in 1-2 minutes

---

## Option 2: Other Deployment Platforms

### Railway

1. Sign up at https://railway.app
2. Create new project → Deploy from GitHub
3. Select your repository
4. Add environment variable: `GEMINI_API_KEY=your-key`
5. Railway auto-detects Streamlit and deploys

### Render

1. Sign up at https://render.com
2. Create new Web Service
3. Connect GitHub repository
4. Build command: `pip install -r requirements.txt`
5. Start command: `streamlit run app.py`
6. Add environment variable: `GEMINI_API_KEY=your-key`

### Fly.io

1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Run: `fly launch`
3. Follow prompts
4. Add secrets: `fly secrets set GEMINI_API_KEY=your-key`

---

## Security Best Practices

### ✅ DO:
- Use Streamlit Secrets for API keys
- Keep `config.yaml` with empty API key in repository
- Use environment variables in other platforms
- Regularly rotate API keys

### ❌ DON'T:
- Commit API keys to GitHub
- Share your secrets publicly
- Use the same API key for development and production

---

## Troubleshooting

### App Won't Deploy

1. **Check requirements.txt**: All dependencies must be listed
2. **Check Python version**: Streamlit Cloud uses Python 3.9+
3. **Check file paths**: Make sure `app.py` is in the root directory
4. **Check logs**: Streamlit Cloud shows deployment logs

### API Keys Not Working

1. **Verify secrets**: Check that secrets are set correctly in Streamlit Cloud
2. **Check format**: Secrets must be in TOML format
3. **Restart app**: Sometimes a restart is needed after adding secrets

### Import Errors

1. **Check imports**: All imports must be from installed packages
2. **Check file structure**: Make sure `utils/` folder is included
3. **Check Python path**: Imports should use relative paths

---

## Custom Domain (Optional)

Streamlit Community Cloud doesn't support custom domains, but you can:
- Use a URL shortener (bit.ly, tinyurl.com)
- Use a redirect service
- Deploy to a platform that supports custom domains (Railway, Render)

---

## Monitoring

- **Streamlit Cloud**: Built-in analytics in dashboard
- **Logs**: View real-time logs in Streamlit Cloud dashboard
- **Usage**: Monitor API usage in Google AI Studio

---

## Quick Checklist

Before deploying:
- [ ] Code is on GitHub
- [ ] `requirements.txt` is up to date
- [ ] `config.yaml` has empty API key (or uses secrets)
- [ ] All dependencies are listed
- [ ] `app.py` is in root directory
- [ ] Tested locally first

After deploying:
- [ ] App loads successfully
- [ ] Secrets are configured
- [ ] AI features work (if enabled)
- [ ] All pages load correctly
- [ ] Images display (if using assets/)

---

## Need Help?

- **Streamlit Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **Streamlit Forum**: https://discuss.streamlit.io
- **GitHub Issues**: Create an issue in your repository

Good luck with your deployment! 🚀

