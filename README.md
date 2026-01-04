# ✈️ THY Cadet Pilot Interview Preparation Dashboard

A comprehensive Streamlit-based web application to help cadet pilot candidates prepare for their Turkish Airlines interview.

## 📊 Data Sources

Fleet and destination data sourced from official Turkish Airlines Investor Relations:
- [Fleet Data](https://investor.turkishairlines.com/en/financial-and-operational/fleet)
- [Flight Network](https://investor.turkishairlines.com/en/financial-and-operational/flight-network)

**Current Statistics (January 2026):**
| Metric | Value |
|--------|-------|
| Total Aircraft | 516 |
| Wide-body | 142 |
| Narrow-body | 347 |
| Cargo | 27 |
| Countries Served | 132 |
| Total Destinations | 356 |

## Features

### 🏢 Turkish Airlines Overview
- Company history, mission, and vision
- Fleet statistics with interactive charts
- Global destination map with flight frequencies
- Near future goals and strategic initiatives

### 🛩️ Fleet Information
- **516 total aircraft** breakdown by manufacturer (Airbus/Boeing)
- Detailed aircraft counts by model
- Interactive pie charts and bar graphs
- Upcoming fleet orders
- Source-verified data from THY Investor Relations
- **🤖 AI Insights**: Get fleet strategy insights, aircraft comparisons, and operational efficiency analysis
- **📜 Cache History**: View previous AI-generated fleet insights

### 🌍 Destinations
- Interactive world map with destination coverage
- **132 countries** with destination counts
- **356 destinations** (53 domestic + 303 international)
- Sortable and filterable destination list
- Regional breakdown statistics
- **🤖 AI Insights**: Get route network insights, hub strategy analysis, and market positioning
- **📜 Cache History**: View previous AI-generated destination insights

### ✈️ TAFA Training Aircraft
Detailed specifications for all training aircraft:
- **Cessna 172 NavIII** - Primary trainer
- **Diamond DA40** - Advanced single-engine
- **Diamond DA42** - Multi-engine trainer

Each includes:
- Complete specifications (dimensions, weights, performance)
- **V-speeds** (critical for interviews!)
- Engine details and systems
- Avionics information (G1000/G1000 NXi)
- **Multi-engine procedures** (DA42 engine failure memory items)
- Interview-relevant key points
- Custom image support

### 📖 Aviation Dictionary
Comprehensive glossary with **260+ terms** including:
- **Abbreviations**: VOR, ILS, TCAS, EGPWS, FADEC, and 150+ more
- **Aviation Terms**: Stall, Spin, Lift, Drag, Aileron, Rudder, and 80+ more
- **V-Speeds**: V1, VR, V2, VMC, VYSE, VA, VNE, and all critical speeds
- **Categories**: Aerodynamics, Navigation, Meteorology, Aircraft Systems, ATC, Human Factors, and more

**Study Features:**
- 🔍 Search functionality
- 📁 Category filtering
- 📊 Difficulty levels (Basic/Intermediate/Advanced)
- 🎴 **Flashcard Mode** with shuffle and navigation
- 📋 Compact table view
- **🤖 AI Suggestions**: Get additional aviation terms suggested by Gemini AI
- **📜 Cache History**: View previous AI-suggested terms

### 📰 Aviation News
- Curated industry news relevant to interviews
- Interview tips for each news item
- **🤖 AI-Powered Updates**: Get fresh aviation news analyzed by Gemini AI
- **📜 Cache History**: View last 5 AI-generated news summaries

### 📜 Aviation History
- Comprehensive timeline from 1783 to present
- **40+ major milestones** including THY founding (1933)
- Filterable by era (Pioneers, Golden Age, Jet Age, Modern)
- Interactive timeline visualization
- Key interview topics highlighted
- **🤖 AI Additions**: Get additional historical events suggested by AI
- **📜 Cache History**: View previous AI-suggested events

### 🔮 Future of Aviation
- Sustainable aviation (SAF, electric, hydrogen)
- Technology advances (AI, automation, eVTOL)
- Future aircraft concepts
- Operational changes and trends
- **🤖 AI Insights**: Get emerging trends and technologies from AI
- **📜 Cache History**: View previous AI insights

## Installation

> **Quick Start?** See [QUICK_START.md](QUICK_START.md) for a 5-minute setup guide!

### Prerequisites
- Python 3.9+
- pip package manager

### Setup

1. **Navigate to the project directory:**
```bash
cd /path/to/aviation
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **(Optional) Configure Gemini AI:**
   - See [Configuring Gemini AI](#-gemini-ai-integration) section below
   - Or set environment variable: `export GEMINI_API_KEY=your_api_key_here`

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 🌐 Deploying Online

Want to access your app from anywhere? Deploy it online for free!

**Quick Start:**
1. Push your code to GitHub
2. Go to https://share.streamlit.io
3. Connect your repository
4. Deploy!

**Full Guide:** See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions including:
- Step-by-step Streamlit Cloud deployment
- Setting up API keys securely
- Alternative deployment platforms
- Troubleshooting tips

Your app will be accessible via a simple web link like: `https://your-app-name.streamlit.app`

## Project Structure

```
aviation/
├── app.py                          # Main application entry point
├── config.yaml                     # Configuration file (AI settings)
├── config.yaml.example             # Example config (safe to commit)
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── DEPLOYMENT.md                   # Deployment guide
├── .gitignore                      # Git ignore rules
├── .streamlit/                     # Streamlit configuration
│   └── config.toml                 # Theme and server settings
├── .cache/                         # AI response cache (auto-created)
│   └── history_*.json              # Per-page cache history (last 5)
├── assets/                          # Custom images folder
│   ├── README.md                   # Image instructions
│   ├── cessna172.jpg              # (add your own)
│   ├── da40.jpg                   # (add your own)
│   └── da42.jpg                   # (add your own)
├── utils/                          # Utility modules
│   ├── __init__.py
│   ├── config.py                   # Configuration manager
│   └── gemini_helper.py            # Gemini AI integration + caching
└── pages/
    ├── 1_🏠_Home.py                # Home redirect
    ├── 2_🛩️_Fleet.py              # Fleet information + AI insights
    ├── 3_🌍_Destinations.py        # Destination map + AI insights
    ├── 4_✈️_Cessna_172.py          # Cessna 172 NavIII specs
    ├── 5_✈️_DA40.py                # Diamond DA40 specs
    ├── 6_✈️_DA42.py                # Diamond DA42 specs + procedures
    ├── 7_📰_Aviation_News.py       # Industry news + AI updates
    ├── 8_📜_Aviation_History.py    # Historical timeline + AI additions
    ├── 9_🔮_Future_of_Aviation.py  # Future trends + AI insights
    └── 10_📖_Aviation_Dictionary.py # 260+ terms + AI suggestions
```

## Customization

### Adding Aircraft Images

Save images to the `assets/` folder:
- `cessna172.jpg` or `cessna172.png` - Cessna 172 Skyhawk
- `da40.jpg` or `da40.png` - Diamond DA40 Diamond Star
- `da42.jpg` or `da42.png` - Diamond DA42 Twin Star

**Recommended sources:**
- [Diamond Aircraft](https://www.diamondaircraft.com)
- [Textron Aviation/Cessna](https://cessna.txtav.com)
- [AOPA](https://www.aopa.org)

### Adding Your Own Content

1. **Aviation Dictionary:** Edit `pages/10_📖_Aviation_Dictionary.py` to add terms
2. **Aviation News:** Edit `pages/7_📰_Aviation_News.py` to add/update news items
3. **Fleet Data:** Update fleet numbers in `pages/2_🛩️_Fleet.py`
4. **Destinations:** Modify destination data in `pages/3_🌍_Destinations.py`
5. **History:** Add historical events in `pages/8_📜_Aviation_History.py`

### 🤖 Gemini AI Integration

The app supports **Gemini AI** for enhancing content across multiple pages with intelligent insights and suggestions.

#### Features

**AI-Enhanced Pages:**
- **📖 Dictionary**: Get additional aviation terms and abbreviations
- **📰 News**: Fetch and analyze recent aviation industry news
- **📜 History**: Discover additional historical aviation events
- **🔮 Future**: Get insights on emerging technologies and trends
- **🛩️ Fleet**: Receive fleet strategy insights and comparisons
- **🌍 Destinations**: Get route network and hub strategy analysis

**AI UI Controls:**
- **🔄 Get Fresh AI Response**: Always makes a new API call (uses tokens)
- **📜 Show Previous Responses**: View last 5 cached AI responses with timestamps
- **📦 Cache Counter**: See how many responses are saved

**Cache System:**
- Each page maintains its own cache history (last 5 responses)
- Responses are saved with timestamps
- View previous AI answers without using API tokens
- Fresh responses always bypass cache

#### Step 1: Get a Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key

#### Step 2: Configure config.yaml
Edit `config.yaml` in the project root:

```yaml
gemini:
  api_key: "your-api-key-here"  # Or use GEMINI_API_KEY env var
  model: "gemini-1.5-flash"      # Preferred model (auto-fallback if unavailable)
  enabled: true                   # Global enable/disable

# Enable AI for specific pages
ai_enhancements:
  dictionary: true      # AI suggests additional terms
  news: true            # AI fetches recent news
  history: true         # AI suggests historical events
  future: true          # AI adds future trends
  fleet: true           # AI provides fleet insights
  destinations: true    # AI provides destination insights
  training_aircraft: false  # AI tips for training aircraft (optional)
```

**Note:** If your preferred model isn't available, the app will prompt you to select from available models.

#### Step 3: Run the Application
```bash
streamlit run app.py
```

The sidebar will show "🤖 Gemini AI: Enabled" when configured correctly.

#### AI Content Indicators
- **🤖 Badge**: All AI-generated content is marked with a purple 🤖 badge
- **Purple Borders**: AI content cards have distinct purple styling
- **Disclaimer**: A disclaimer appears above AI sections noting content is AI-generated
- **Timestamp**: Cached responses show when they were generated

#### Using AI Features

1. **Get Fresh Content**: Click "🔄 Get Fresh AI Response" on any AI-enabled page
   - Makes a new API call
   - Saves response to cache history
   - Uses API tokens

2. **View History**: Click "📜 Show Previous Responses"
   - Expands to show last 5 cached responses
   - No API calls needed
   - Each entry shows timestamp

3. **Page-Specific AI**:
   - Each page has its own AI section at the bottom
   - Enable/disable per page in `config.yaml`
   - Cache is maintained separately per page

#### Alternative: Environment Variable
You can also set the API key via environment variable:
```bash
export GEMINI_API_KEY=your-api-key-here
streamlit run app.py
```

#### Model Selection
- The app automatically detects available models for your API key
- If your preferred model isn't available, you'll be prompted to select one
- Model selection is saved for the session

## Technologies Used

- **Streamlit** - Web application framework
- **Plotly** - Interactive visualizations and maps
- **Pandas** - Data manipulation
- **Google Gemini AI** (optional) - AI-powered content enhancements with caching
- **Pillow** - Image handling
- **PyYAML** - Configuration management
- **JSON** - Cache storage for AI responses

## Interview Preparation Tips

1. **Review Daily:** Open the dashboard each day to refresh your knowledge
2. **Use Flashcards:** Study the Aviation Dictionary in Flashcard Mode
3. **Memorize V-Speeds:** Critical for all three training aircraft
4. **Know THY Facts:** 
   - Founded: May 20, 1933
   - Fleet: 516 aircraft
   - Destinations: 356 in 132 countries
   - Alliance: Star Alliance (since 2008)
   - Hub: Istanbul Airport (IST)
5. **Multi-Engine Procedures:** Know the DA42 engine failure memory items
6. **Stay Updated:** Check the news section regularly (use AI for fresh updates)
7. **Understand History:** Know major aviation milestones (use AI for additional events)
8. **Think Future:** Be aware of SAF, sustainability, and technology trends (use AI insights)
9. **Use AI Wisely:** 
   - Get fresh AI responses when you need current information
   - Review cached responses to save API tokens
   - AI content is marked with 🤖 - always verify critical facts
10. **Fleet & Network Insights:** Use AI to get deeper understanding of THY's strategy

## Key Interview Topics

### V-Speeds to Memorize
| Speed | Cessna 172 | DA40 | DA42 |
|-------|------------|------|------|
| VR | 55 KIAS | 59 KIAS | 74 KIAS |
| VX | 62 KIAS | 66 KIAS | 81 KIAS |
| VY | 74 KIAS | 78 KIAS | 91 KIAS |
| VA | 99 KIAS | 108 KIAS | 131 KIAS |
| VS0 | 47 KIAS | 49 KIAS | 60 KIAS |
| VMC | - | - | 68 KIAS |
| VYSE | - | - | 85 KIAS (Blue Line) |

### DA42 Engine Failure Memory Items
1. Maintain directional control (RUDDER)
2. Pitch for VYSE (85 KIAS) - Blue Line
3. **Identify** failed engine ("Dead Foot = Dead Engine")
4. **Verify** - Throttle to idle on suspected engine
5. **Feather** - Propeller lever to feather

**Memory Aid: "Identify, Verify, Feather"**

## Good Luck! 🍀

Best wishes for your Turkish Airlines cadet pilot interview in March/April 2026!

---

*Built for interview preparation purposes*

**Data Sources:**
- Turkish Airlines Investor Relations: https://investor.turkishairlines.com
- Fleet: https://investor.turkishairlines.com/en/financial-and-operational/fleet
- Network: https://investor.turkishairlines.com/en/financial-and-operational/flight-network
