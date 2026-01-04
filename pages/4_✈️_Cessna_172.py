"""
Cessna 172 NavIII Training Aircraft Details
"""

import streamlit as st

st.set_page_config(
    page_title="Cessna 172 NavIII | Cadet Prep",
    page_icon="✈️",
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
        margin-bottom: 0.5rem;
    }
    
    .sub-header {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.2rem;
        color: #888;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .spec-card {
        background: linear-gradient(145deg, rgba(30, 30, 50, 0.9), rgba(20, 20, 35, 0.95));
        border: 1px solid rgba(200, 16, 46, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
    }
    
    .spec-title {
        font-family: 'Orbitron', monospace;
        font-size: 1.3rem;
        color: #c8102e;
        margin-bottom: 1rem;
    }
    
    .spec-table {
        width: 100%;
        color: #d0d0d0;
        font-family: 'Rajdhani', sans-serif;
    }
    
    .spec-table td {
        padding: 10px 5px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    
    .spec-value {
        font-weight: 600;
        color: #fff;
    }
    
    .highlight-box {
        background: rgba(200, 16, 46, 0.1);
        border: 1px solid rgba(200, 16, 46, 0.4);
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="page-header">✈️ Cessna 172 Skyhawk NavIII</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">TAFA Primary Training Aircraft | Single Engine Piston</p>', unsafe_allow_html=True)

# Aircraft Image Section
import os

# Check for local image first
local_image_path = "assets/cessna172.jpg"
local_image_png = "assets/cessna172.png"

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists(local_image_path):
        st.image(local_image_path, caption="Cessna 172 Skyhawk with G1000 glass cockpit", use_container_width=True)
    elif os.path.exists(local_image_png):
        st.image(local_image_png, caption="Cessna 172 Skyhawk with G1000 glass cockpit", use_container_width=True)
    else:
        # Display placeholder with instructions
        st.markdown("""
        <div class="spec-card" style="text-align: center; padding: 2rem;">
            <div style="font-size: 6rem; margin-bottom: 1rem;">🛩️</div>
            <h3 style="color: #fff; margin-bottom: 0.5rem;">Cessna 172 Skyhawk</h3>
            <p style="color: #888; font-style: italic;">The world's most popular training aircraft - Over 45,000 built since 1956</p>
            <p style="color: #666; font-size: 0.85rem; margin-top: 1rem;">
                💡 To add an image: Save as <code>assets/cessna172.jpg</code>
            </p>
        </div>
        """, unsafe_allow_html=True)

# G1000 cockpit description
with st.expander("🖥️ About the G1000 Glass Cockpit"):
    st.markdown("""
    The Garmin G1000 NavIII features:
    - **PFD (Primary Flight Display)** - Left screen showing attitude, airspeed, altitude
    - **MFD (Multi-Function Display)** - Right screen for navigation, engine data, weather
    - **Integrated GPS/NAV/COM** - Full navigation capability
    - **Engine Monitoring** - Real-time engine parameters on MFD
    - **Synthetic Vision** (optional) - Terrain display on PFD
    """)

# Main specifications
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">📋 General Information</h3>
        <table class="spec-table">
            <tr><td>Manufacturer</td><td class="spec-value">Cessna Aircraft Company (Textron Aviation)</td></tr>
            <tr><td>First Flight</td><td class="spec-value">June 12, 1955</td></tr>
            <tr><td>Type</td><td class="spec-value">Single-engine, high-wing, fixed-gear</td></tr>
            <tr><td>Role</td><td class="spec-value">Primary flight training, personal aviation</td></tr>
            <tr><td>Crew</td><td class="spec-value">1 pilot</td></tr>
            <tr><td>Capacity</td><td class="spec-value">3 passengers (4 total occupants)</td></tr>
            <tr><td>NavIII Variant</td><td class="spec-value">Garmin G1000 glass cockpit</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">⚙️ Engine Specifications</h3>
        <table class="spec-table">
            <tr><td>Engine</td><td class="spec-value">Lycoming IO-360-L2A</td></tr>
            <tr><td>Engine Type</td><td class="spec-value">4-cylinder, horizontally opposed</td></tr>
            <tr><td>Power Output</td><td class="spec-value">180 HP (134 kW)</td></tr>
            <tr><td>Fuel Injection</td><td class="spec-value">Yes (IO = Injected, Opposed)</td></tr>
            <tr><td>Propeller</td><td class="spec-value">2-blade, fixed-pitch</td></tr>
            <tr><td>Fuel Type</td><td class="spec-value">100LL Avgas</td></tr>
            <tr><td>Fuel Capacity</td><td class="spec-value">212 L (56 US gal)</td></tr>
            <tr><td>Usable Fuel</td><td class="spec-value">204 L (53 US gal)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">📐 Dimensions</h3>
        <table class="spec-table">
            <tr><td>Wingspan</td><td class="spec-value">11.0 m (36 ft 1 in)</td></tr>
            <tr><td>Length</td><td class="spec-value">8.28 m (27 ft 2 in)</td></tr>
            <tr><td>Height</td><td class="spec-value">2.72 m (8 ft 11 in)</td></tr>
            <tr><td>Wing Area</td><td class="spec-value">16.2 m² (174 ft²)</td></tr>
            <tr><td>Wing Type</td><td class="spec-value">High-wing, semi-cantilever</td></tr>
            <tr><td>Aspect Ratio</td><td class="spec-value">7.5</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">⚖️ Weights</h3>
        <table class="spec-table">
            <tr><td>Empty Weight</td><td class="spec-value">767 kg (1,691 lb)</td></tr>
            <tr><td>Max Takeoff Weight (MTOW)</td><td class="spec-value">1,111 kg (2,450 lb)</td></tr>
            <tr><td>Useful Load</td><td class="spec-value">344 kg (759 lb)</td></tr>
            <tr><td>Max Landing Weight</td><td class="spec-value">1,111 kg (2,450 lb)</td></tr>
            <tr><td>Baggage Capacity</td><td class="spec-value">54 kg (120 lb)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

# Performance specifications
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">📈 Performance Specifications</h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4 style="color: #c8102e;">Speed</h4>
        <table class="spec-table">
            <tr><td>Cruise Speed (75%)</td><td class="spec-value">122 kts (226 km/h)</td></tr>
            <tr><td>Max Speed (VNE)</td><td class="spec-value">163 kts (302 km/h)</td></tr>
            <tr><td>Stall Speed (Clean)</td><td class="spec-value">51 kts (94 km/h)</td></tr>
            <tr><td>Stall Speed (Flaps)</td><td class="spec-value">47 kts (87 km/h)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4 style="color: #c8102e;">Range & Endurance</h4>
        <table class="spec-table">
            <tr><td>Range (75% power)</td><td class="spec-value">640 nm (1,185 km)</td></tr>
            <tr><td>Endurance</td><td class="spec-value">~5 hours</td></tr>
            <tr><td>Fuel Consumption</td><td class="spec-value">~36 L/hr (9.5 gal/hr)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="highlight-box">
        <h4 style="color: #c8102e;">Climb & Ceiling</h4>
        <table class="spec-table">
            <tr><td>Rate of Climb</td><td class="spec-value">730 ft/min (3.7 m/s)</td></tr>
            <tr><td>Service Ceiling</td><td class="spec-value">13,500 ft (4,100 m)</td></tr>
            <tr><td>Takeoff Distance</td><td class="spec-value">960 ft (293 m)</td></tr>
            <tr><td>Landing Distance</td><td class="spec-value">575 ft (175 m)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

# V-Speeds
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">🎯 V-Speeds (Critical for Interview!)</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <table class="spec-table">
        <tr><td><strong>VR</strong> (Rotation)</td><td class="spec-value">55 KIAS</td></tr>
        <tr><td><strong>VX</strong> (Best Angle of Climb)</td><td class="spec-value">62 KIAS</td></tr>
        <tr><td><strong>VY</strong> (Best Rate of Climb)</td><td class="spec-value">74 KIAS</td></tr>
        <tr><td><strong>VA</strong> (Maneuvering Speed @ MTOW)</td><td class="spec-value">99 KIAS</td></tr>
        <tr><td><strong>VFE</strong> (Max Flap Extended)</td><td class="spec-value">110 KIAS (10°), 85 KIAS (10-30°)</td></tr>
    </table>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <table class="spec-table">
        <tr><td><strong>VNO</strong> (Max Structural Cruise)</td><td class="spec-value">129 KIAS</td></tr>
        <tr><td><strong>VNE</strong> (Never Exceed)</td><td class="spec-value">163 KIAS</td></tr>
        <tr><td><strong>VSO</strong> (Stall, Landing Config)</td><td class="spec-value">47 KIAS</td></tr>
        <tr><td><strong>VS1</strong> (Stall, Clean)</td><td class="spec-value">51 KIAS</td></tr>
        <tr><td><strong>VREF</strong> (Final Approach)</td><td class="spec-value">60-70 KIAS</td></tr>
    </table>
    """, unsafe_allow_html=True)

# Avionics - NavIII
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">🖥️ Garmin G1000 NavIII Avionics</h3>
    <p style="color: #d0d0d0; line-height: 1.8;">
        The NavIII variant features the Garmin G1000 integrated flight deck, a glass cockpit system that includes:
    </p>
    <ul style="color: #d0d0d0; line-height: 2;">
        <li><strong>PFD (Primary Flight Display):</strong> 10.4" LCD showing attitude, airspeed, altitude, heading, vertical speed</li>
        <li><strong>MFD (Multi-Function Display):</strong> 10.4" LCD for navigation, engine monitoring, traffic, terrain</li>
        <li><strong>GIA 63 Integrated Avionics Units:</strong> GPS, VHF COM/NAV, engine/airframe interface</li>
        <li><strong>GDC 74A Air Data Computer:</strong> Computes airspeed, altitude, vertical speed</li>
        <li><strong>GRS 77 AHRS:</strong> Attitude and Heading Reference System</li>
        <li><strong>GTX 33 Transponder:</strong> Mode S with TIS traffic display</li>
        <li><strong>GMA 1347 Audio Panel:</strong> Integrated audio management</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Why Cessna 172 for training
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">💡 Why Cessna 172 for Training?</h3>
    <ul style="color: #d0d0d0; line-height: 2;">
        <li><strong>Most Produced Aircraft:</strong> Over 45,000 units built - proven design</li>
        <li><strong>High Wing Design:</strong> Excellent visibility for ground reference maneuvers</li>
        <li><strong>Forgiving Flight Characteristics:</strong> Stable, predictable behavior</li>
        <li><strong>Fixed Tricycle Gear:</strong> Easy ground handling for students</li>
        <li><strong>Docile Stall Behavior:</strong> Safe stall recovery characteristics</li>
        <li><strong>Glass Cockpit Training:</strong> G1000 prepares students for modern airline cockpits</li>
        <li><strong>Abundant Parts & Support:</strong> Excellent maintenance infrastructure worldwide</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Back button
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("← Back to Home"):
        st.switch_page("app.py")
with col2:
    if st.button("Next: DA40 →"):
        st.switch_page("pages/5_✈️_DA40.py")

