"""
Turkish Airlines Cadet Pilot Interview Preparation Dashboard
Main Application Entry Point
"""

import streamlit as st
from utils.config import config

st.set_page_config(
    page_title="THY Cadet Pilot Prep",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar - AI Status
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    if config.gemini_enabled:
        st.markdown("""
        <div style="padding: 0.5rem; background: rgba(46, 213, 115, 0.15); border: 1px solid rgba(46, 213, 115, 0.4); border-radius: 8px; margin-bottom: 1rem;">
            <span style="color: #2ed573;">🤖 Gemini AI: <strong>Enabled</strong></span>
        </div>
        """, unsafe_allow_html=True)
        
        # Show which pages have AI enabled
        enabled_pages = []
        if config.is_ai_enabled_for('dictionary'):
            enabled_pages.append("Dictionary")
        if config.is_ai_enabled_for('news'):
            enabled_pages.append("News")
        if config.is_ai_enabled_for('history'):
            enabled_pages.append("History")
        if config.is_ai_enabled_for('future'):
            enabled_pages.append("Future")
        
        if enabled_pages:
            st.caption(f"AI enabled for: {', '.join(enabled_pages)}")
    else:
        st.markdown("""
        <div style="padding: 0.5rem; background: rgba(100, 100, 100, 0.15); border: 1px solid rgba(100, 100, 100, 0.4); border-radius: 8px; margin-bottom: 1rem;">
            <span style="color: #888;">🤖 Gemini AI: <strong>Disabled</strong></span>
        </div>
        """, unsafe_allow_html=True)
        st.caption("Configure in config.yaml")
    
    st.markdown("---")

# Custom CSS for beautiful styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a1a2e 50%, #16213e 100%);
    }
    
    .main-header {
        font-family: 'Orbitron', monospace;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #c8102e 0%, #ff4757 50%, #c8102e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 30px rgba(200, 16, 46, 0.5);
    }
    
    .sub-header {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.3rem;
        color: #a0a0a0;
        text-align: center;
        margin-bottom: 2rem;
        letter-spacing: 3px;
    }
    
    .info-card {
        background: linear-gradient(145deg, rgba(30, 30, 50, 0.9), rgba(20, 20, 35, 0.95));
        border: 1px solid rgba(200, 16, 46, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        transition: all 0.3s ease;
    }
    
    .info-card:hover {
        border-color: rgba(200, 16, 46, 0.6);
        box-shadow: 0 12px 40px rgba(200, 16, 46, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transform: translateY(-2px);
    }
    
    .stat-number {
        font-family: 'Orbitron', monospace;
        font-size: 2.8rem;
        font-weight: 700;
        color: #c8102e;
        text-shadow: 0 0 20px rgba(200, 16, 46, 0.4);
    }
    
    .stat-label {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1rem;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .section-title {
        font-family: 'Orbitron', monospace;
        font-size: 1.8rem;
        color: #fff;
        border-left: 4px solid #c8102e;
        padding-left: 1rem;
        margin: 2rem 0 1rem 0;
    }
    
    .aircraft-card {
        background: linear-gradient(145deg, rgba(25, 25, 45, 0.95), rgba(15, 15, 30, 0.98));
        border: 1px solid rgba(100, 100, 150, 0.2);
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .aircraft-card:hover {
        border-color: #c8102e;
        box-shadow: 0 0 30px rgba(200, 16, 46, 0.3);
        transform: scale(1.02);
    }
    
    .motto-text {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.5rem;
        font-style: italic;
        color: #c8102e;
        text-align: center;
        padding: 1rem;
        border: 1px solid rgba(200, 16, 46, 0.3);
        border-radius: 8px;
        background: rgba(200, 16, 46, 0.05);
    }
    
    .nav-button {
        display: inline-block;
        padding: 0.8rem 1.5rem;
        background: linear-gradient(135deg, #c8102e, #a00d25);
        color: white !important;
        border-radius: 8px;
        text-decoration: none;
        font-family: 'Rajdhani', sans-serif;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    
    .nav-button:hover {
        background: linear-gradient(135deg, #ff4757, #c8102e);
        box-shadow: 0 0 20px rgba(200, 16, 46, 0.5);
    }
    
    .stButton > button {
        font-family: 'Rajdhani', sans-serif;
        font-weight: 600;
        letter-spacing: 1px;
        background: linear-gradient(135deg, #c8102e, #a00d25);
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #ff4757, #c8102e);
        box-shadow: 0 0 20px rgba(200, 16, 46, 0.5);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a15 0%, #1a1a2e 100%);
        border-right: 1px solid rgba(200, 16, 46, 0.2);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #d0d0d0;
    }
</style>
""", unsafe_allow_html=True)


def main():
    # Header
    st.markdown('<h1 class="main-header">✈️ THY CADET PILOT PREP</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">TURKISH AIRLINES INTERVIEW PREPARATION DASHBOARD</p>', unsafe_allow_html=True)
    
    # Turkish Airlines Info Section
    st.markdown('<h2 class="section-title">🏢 Turkish Airlines Overview</h2>', unsafe_allow_html=True)
    
    # Motto
    st.markdown("""
    <div class="motto-text">
        "Widen Your World" | "Daha Büyük Düşün"
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Key Statistics in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <div class="stat-number">1933</div>
            <div class="stat-label">Founded</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("🛩️ 516 Aircraft", key="fleet_btn", use_container_width=True):
            st.switch_page("pages/2_🛩️_Fleet.py")
        st.markdown("""
        <div style="text-align: center; color: #888; font-size: 0.9rem;">
            Click to view fleet details
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.button("🌍 356 Destinations", key="dest_btn", use_container_width=True):
            st.switch_page("pages/3_🌍_Destinations.py")
        st.markdown("""
        <div style="text-align: center; color: #888; font-size: 0.9rem;">
            Click to explore destinations
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <div class="stat-number">132</div>
            <div class="stat-label">Countries Served</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Company Details
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3 style="color: #c8102e; font-family: 'Orbitron', monospace;">📋 Company Details</h3>
            <table style="width: 100%; color: #d0d0d0; font-family: 'Rajdhani', sans-serif;">
                <tr><td style="padding: 8px 0;"><strong>Official Name:</strong></td><td>Türk Hava Yolları A.O.</td></tr>
                <tr><td style="padding: 8px 0;"><strong>Founded:</strong></td><td>20 May 1933</td></tr>
                <tr><td style="padding: 8px 0;"><strong>Founder:</strong></td><td>Turkish Government (State Airlines Administration)</td></tr>
                <tr><td style="padding: 8px 0;"><strong>Headquarters:</strong></td><td>Istanbul, Turkey</td></tr>
                <tr><td style="padding: 8px 0;"><strong>Main Hub:</strong></td><td>Istanbul Airport (IST)</td></tr>
                <tr><td style="padding: 8px 0;"><strong>Alliance:</strong></td><td>Star Alliance (since 2008)</td></tr>
                <tr><td style="padding: 8px 0;"><strong>CEO:</strong></td><td>Bilal Ekşi</td></tr>
                <tr><td style="padding: 8px 0;"><strong>IATA Code:</strong></td><td>TK</td></tr>
                <tr><td style="padding: 8px 0;"><strong>ICAO Code:</strong></td><td>THY</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h3 style="color: #c8102e; font-family: 'Orbitron', monospace;">🎯 Mission & Vision</h3>
            <p style="color: #d0d0d0; font-family: 'Rajdhani', sans-serif; line-height: 1.8;">
                <strong style="color: #c8102e;">Mission:</strong><br>
                To be the preferred leading airline by providing sustainable profitable growth 
                while maintaining the highest standards of safety and customer satisfaction.
            </p>
            <p style="color: #d0d0d0; font-family: 'Rajdhani', sans-serif; line-height: 1.8;">
                <strong style="color: #c8102e;">Vision:</strong><br>
                To be the airline that flies to most countries in the world and that is preferred 
                for its hospitality, reliability, and competitive pricing.
            </p>
            <p style="color: #d0d0d0; font-family: 'Rajdhani', sans-serif; line-height: 1.8;">
                <strong style="color: #c8102e;">Core Values:</strong><br>
                Safety First • Customer Focus • Excellence • Innovation • Sustainability
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Near Future Goals
    st.markdown("""
    <div class="info-card">
        <h3 style="color: #c8102e; font-family: 'Orbitron', monospace;">🚀 Near Future Goals (2025-2030)</h3>
        <ul style="color: #d0d0d0; font-family: 'Rajdhani', sans-serif; line-height: 2;">
            <li><strong>Fleet Expansion:</strong> Reach 600+ aircraft by 2028 with new Boeing 787 and Airbus A350 orders</li>
            <li><strong>Sustainability:</strong> Achieve carbon neutrality goals, increase SAF (Sustainable Aviation Fuel) usage</li>
            <li><strong>Digital Transformation:</strong> AI-powered customer service, enhanced mobile experience</li>
            <li><strong>Network Growth:</strong> Expand to 400+ destinations, new routes to Africa and South America</li>
            <li><strong>Training:</strong> Expand TAFA (Turkish Airlines Flight Academy) capacity to train more pilots</li>
            <li><strong>New Hub Development:</strong> Maximize Istanbul Airport capacity, potential for second hub</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # TAFA Training Aircraft Section
    st.markdown('<h2 class="section-title">🎓 TAFA Training Aircraft</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="aircraft-card">
            <h3 style="color: #fff; font-family: 'Orbitron', monospace;">Cessna 172 NavIII</h3>
            <p style="color: #888;">Single Engine Trainer</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Details", key="cessna_btn", use_container_width=True):
            st.switch_page("pages/4_✈️_Cessna_172.py")
    
    with col2:
        st.markdown("""
        <div class="aircraft-card">
            <h3 style="color: #fff; font-family: 'Orbitron', monospace;">Diamond DA40</h3>
            <p style="color: #888;">Single Engine Advanced</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Details", key="da40_btn", use_container_width=True):
            st.switch_page("pages/5_✈️_DA40.py")
    
    with col3:
        st.markdown("""
        <div class="aircraft-card">
            <h3 style="color: #fff; font-family: 'Orbitron', monospace;">Diamond DA42</h3>
            <p style="color: #888;">Multi-Engine Trainer</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Details", key="da42_btn", use_container_width=True):
            st.switch_page("pages/6_✈️_DA42.py")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Navigation Section
    st.markdown('<h2 class="section-title">📚 Study Resources</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3 style="color: #c8102e; font-family: 'Orbitron', monospace;">📰 Aviation News</h3>
            <p style="color: #888; font-family: 'Rajdhani', sans-serif;">
                Stay updated with recent aviation industry news, incidents, and developments 
                that might come up in your interview.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Read News", key="news_btn", use_container_width=True):
            st.switch_page("pages/7_📰_Aviation_News.py")
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h3 style="color: #c8102e; font-family: 'Orbitron', monospace;">📜 Aviation History</h3>
            <p style="color: #888; font-family: 'Rajdhani', sans-serif;">
                Explore the major milestones in aviation history from the Wright Brothers 
                to modern commercial aviation.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore History", key="history_btn", use_container_width=True):
            st.switch_page("pages/8_📜_Aviation_History.py")
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <h3 style="color: #c8102e; font-family: 'Orbitron', monospace;">🔮 Future of Aviation</h3>
            <p style="color: #888; font-family: 'Rajdhani', sans-serif;">
                Learn about emerging technologies, sustainable aviation, 
                and what the future holds for the industry.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Discover Future", key="future_btn", use_container_width=True):
            st.switch_page("pages/9_🔮_Future_of_Aviation.py")
    
    # Aviation Dictionary - Full width featured section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-card" style="border: 2px solid rgba(200, 16, 46, 0.5); background: linear-gradient(145deg, rgba(40, 20, 30, 0.9), rgba(25, 15, 25, 0.95));">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 300px;">
                <h3 style="color: #c8102e; font-family: 'Orbitron', monospace; font-size: 1.5rem;">📖 Aviation Dictionary</h3>
                <p style="color: #d0d0d0; font-family: 'Rajdhani', sans-serif; line-height: 1.8; margin-top: 0.5rem;">
                    <strong>180+ terms</strong> covering V-speeds, navigation, meteorology, aircraft systems, 
                    ATC procedures, human factors, and more. Features <strong>flashcard mode</strong> for effective studying 
                    and filters by category and difficulty level.
                </p>
            </div>
            <div style="text-align: center; padding: 1rem;">
                <span style="font-size: 4rem;">📖</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📖 Open Aviation Dictionary", key="dict_btn", use_container_width=True):
        st.switch_page("pages/10_📖_Aviation_Dictionary.py")
    
    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; color: #555; font-family: 'Rajdhani', sans-serif; padding: 2rem; border-top: 1px solid rgba(200, 16, 46, 0.2);">
        <p>🎯 Interview Date: March/April 2026 | Good luck with your cadet pilot interview!</p>
        <p style="font-size: 0.9rem;">Built for interview preparation purposes</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

