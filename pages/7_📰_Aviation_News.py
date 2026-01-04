"""
Aviation News Page - Fetches recent aviation news using Gemini API
"""

import streamlit as st
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config import config
from utils.gemini_helper import gemini, render_ai_section

st.set_page_config(
    page_title="Aviation News | Cadet Prep",
    page_icon="📰",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a1a2e 50%, #16213e 100%);
    }
    
    .page-header {
        font-family: 'Orbitron', monospace;
        font-size: 2.5rem;
        font-weight: 700;
        color: #c8102e;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .news-card {
        background: linear-gradient(145deg, rgba(30, 30, 50, 0.9), rgba(20, 20, 35, 0.95));
        border: 1px solid rgba(200, 16, 46, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .news-card:hover {
        border-color: rgba(200, 16, 46, 0.6);
        box-shadow: 0 8px 30px rgba(200, 16, 46, 0.2);
    }
    
    .news-title {
        font-family: 'Orbitron', monospace;
        font-size: 1.3rem;
        color: #fff;
        margin-bottom: 0.5rem;
    }
    
    .news-date {
        font-family: 'Rajdhani', sans-serif;
        font-size: 0.9rem;
        color: #c8102e;
        margin-bottom: 1rem;
    }
    
    .news-content {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1rem;
        color: #d0d0d0;
        line-height: 1.8;
    }
    
    .news-category {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        background: rgba(200, 16, 46, 0.2);
        border: 1px solid rgba(200, 16, 46, 0.4);
        border-radius: 20px;
        font-size: 0.8rem;
        color: #c8102e;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    .interview-tip {
        background: rgba(255, 193, 7, 0.1);
        border: 1px solid rgba(255, 193, 7, 0.4);
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="page-header">📰 Aviation Industry News</h1>', unsafe_allow_html=True)

# Static news data (can be updated manually or via API)
# In production, you would fetch this from a news API or use OpenAI to summarize recent news

def get_static_news():
    """Static news data - update this periodically or integrate with OpenAI API"""
    return [
        {
            "title": "Boeing 737 MAX Returns to Full Service",
            "date": "2025",
            "category": ["Boeing", "Safety", "Regulatory"],
            "content": """Following extensive regulatory review and safety modifications, the Boeing 737 MAX has returned 
            to service with most major airlines worldwide. The aircraft underwent significant software updates to the 
            MCAS system and pilot training requirements were enhanced. Airlines including Turkish Airlines have 
            reintegrated the aircraft into their fleets with enhanced safety protocols.""",
            "interview_tip": "Be prepared to discuss the MCAS system, the importance of redundancy in flight systems, and how the industry learned from this incident."
        },
        {
            "title": "Sustainable Aviation Fuel (SAF) Adoption Accelerates",
            "date": "2025",
            "category": ["Sustainability", "Environment", "Industry Trend"],
            "content": """Major airlines including Turkish Airlines are increasing their commitment to Sustainable Aviation 
            Fuel. SAF can reduce lifecycle carbon emissions by up to 80% compared to conventional jet fuel. The industry 
            is working towards the goal of carbon-neutral growth, with many carriers committing to net-zero emissions by 2050.""",
            "interview_tip": "Understanding SAF and sustainability initiatives shows awareness of industry challenges. Know that THY has sustainability goals aligned with IATA targets."
        },
        {
            "title": "Airbus Delivers 1000th A350",
            "date": "2025",
            "category": ["Airbus", "Wide-body", "Milestone"],
            "content": """Airbus celebrated the delivery of its 1000th A350 aircraft. The A350 family has become a 
            cornerstone of long-haul fleets worldwide, offering 25% better fuel efficiency than previous-generation 
            aircraft. Turkish Airlines operates A350-900s on its long-haul network and has additional orders pending.""",
            "interview_tip": "Know the A350's key features: composite construction, fuel efficiency, and passenger comfort. THY uses it for ultra-long-haul routes."
        },
        {
            "title": "Electric and Hybrid Aircraft Development Progress",
            "date": "2025",
            "category": ["Technology", "Electric Aviation", "Future"],
            "content": """Several companies are making progress on electric and hybrid-electric aircraft. Regional 
            electric aircraft with ranges of 100-500 nautical miles are expected to enter service within the next 
            5-10 years. This could revolutionize short-haul travel and flight training.""",
            "interview_tip": "Shows awareness of future technology. Acknowledge that while revolutionary, battery technology still limits range for commercial aviation."
        },
        {
            "title": "Global Pilot Shortage Continues",
            "date": "2025",
            "category": ["Industry", "Career", "Training"],
            "content": """The aviation industry continues to face a significant pilot shortage globally. Boeing 
            projects a need for over 600,000 new pilots over the next 20 years. Airlines are investing heavily 
            in training programs - Turkish Airlines' TAFA academy is expanding to meet this demand.""",
            "interview_tip": "This is great context for why you're pursuing this career. Show enthusiasm about being part of the solution to this industry need."
        },
        {
            "title": "Advanced Air Mobility (AAM) / Urban Air Mobility Progress",
            "date": "2025",
            "category": ["Technology", "Future", "Innovation"],
            "content": """Urban Air Mobility vehicles (air taxis) are progressing through certification. Companies 
            like Joby, Lilium, and others are working with regulators on new certification pathways for eVTOL 
            (electric Vertical Take-Off and Landing) aircraft. Commercial operations expected by 2025-2027.""",
            "interview_tip": "Shows awareness of industry innovation. These are separate from traditional commercial aviation but represent future opportunities."
        },
        {
            "title": "Turkish Airlines Expands African Network",
            "date": "2025",
            "category": ["Turkish Airlines", "Network", "Growth"],
            "content": """Turkish Airlines continues to expand its African network, adding new destinations and 
            increasing frequencies. Africa represents a key growth market, with the carrier now serving more 
            African destinations than any other airline. Istanbul serves as a convenient hub for Africa-Europe 
            and Africa-Asia connections.""",
            "interview_tip": "Shows knowledge of THY's strategy. Africa is a growth market and THY's Istanbul hub provides geographic advantage for connections."
        },
        {
            "title": "Single-Pilot Operations Under Study",
            "date": "2025",
            "category": ["Regulatory", "Technology", "Future"],
            "content": """Regulators are studying the feasibility of reduced crew operations (single-pilot) for 
            certain commercial flights, enabled by advanced automation and ground-based monitoring. While 
            controversial, this could address pilot shortages. Full implementation would be years away and 
            would require extensive safety validation.""",
            "interview_tip": "Be aware this is being studied but emphasize that safety is paramount and any changes would require extensive validation."
        },
        {
            "title": "New Istanbul Airport Becomes World's Busiest",
            "date": "2025",
            "category": ["Turkish Airlines", "Infrastructure", "Hub"],
            "content": """Istanbul Airport (IST) has become one of the world's busiest airports, handling over 
            90 million passengers annually. The airport serves as Turkish Airlines' main hub and is designed 
            to eventually handle 200 million passengers. Its strategic location enables efficient connections 
            between Europe, Asia, Africa, and the Americas.""",
            "interview_tip": "Know IST facts: opened 2019, one of world's largest terminals, strategic geographic position is THY's competitive advantage."
        },
        {
            "title": "Recent Aviation Incidents and Safety Lessons",
            "date": "2025",
            "category": ["Safety", "Incidents", "Learning"],
            "content": """The aviation industry continues to maintain an excellent safety record, with 2024 being 
            one of the safest years on record. Each incident is thoroughly investigated with lessons shared 
            industry-wide. Recent focus areas include runway safety, approach stabilization, and automation 
            dependency awareness.""",
            "interview_tip": "If asked about incidents, focus on how the industry learns and improves. Emphasize that safety is the #1 priority in aviation."
        }
    ]

# Display news
st.markdown("### Latest Industry Updates")
st.markdown("*Stay informed about developments that may come up in your interview*")

news_items = get_static_news()

# Filter options
col1, col2 = st.columns([1, 3])
with col1:
    all_categories = set()
    for item in news_items:
        all_categories.update(item["category"])
    
    selected_category = st.selectbox("Filter by Category", ["All"] + sorted(list(all_categories)))

# Display news cards
for item in news_items:
    if selected_category == "All" or selected_category in item["category"]:
        st.markdown(f"""
        <div class="news-card">
            <h3 class="news-title">{item['title']}</h3>
            <p class="news-date">📅 {item['date']}</p>
            <div>
                {''.join([f'<span class="news-category">{cat}</span>' for cat in item['category']])}
            </div>
            <p class="news-content">{item['content']}</p>
            <div class="interview-tip">
                <strong style="color: #ffc107;">💡 Interview Tip:</strong><br>
                <span style="color: #d0d0d0;">{item['interview_tip']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Gemini AI Integration Section
render_ai_section(
    page_name='news',
    card_type='news',
    generate_func=gemini.get_news_updates,
    generate_args=(),
    section_title="🤖 AI-Powered News Updates"
)

# Manual news update section
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("### 📝 Add Your Own News")
st.markdown("*Keep track of news items you find important*")

with st.expander("Add a news item"):
    new_title = st.text_input("News Title")
    new_content = st.text_area("News Content")
    new_tip = st.text_input("Interview Tip")
    
    if st.button("Save to Notes"):
        st.success("News item saved! (Note: In this demo, items are not persisted between sessions)")

# Back button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("← Back to Home"):
    st.switch_page("app.py")

