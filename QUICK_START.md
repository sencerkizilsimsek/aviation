# ⚡ Quick Start Guide

Get your THY Cadet Pilot Prep app running in 5 minutes!

## Local Setup

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure (optional - for AI features):**
   ```bash
   # Copy example config
   cp config.yaml.example config.yaml
   
   # Edit config.yaml and add your Gemini API key (if you want AI features)
   # Or leave it empty to use without AI
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser:** http://localhost:8501

## Deploy Online (5 minutes)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 2: Deploy to Streamlit Cloud
1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file: `app.py`
6. Click "Deploy"

### Step 3: Add API Key (Optional)
1. In Streamlit Cloud dashboard → Settings → Secrets
2. Add:
   ```toml
   [gemini]
   api_key = "your-key-here"
   ```
3. App restarts automatically

**Done!** Your app is live at: `https://your-app-name.streamlit.app`

## Need Help?

- **Full deployment guide:** See [DEPLOYMENT.md](DEPLOYMENT.md)
- **Configuration help:** See [README.md](README.md#-gemini-ai-integration)

