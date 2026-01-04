"""
Diamond DA40 Training Aircraft Details
"""

import streamlit as st

st.set_page_config(
    page_title="Diamond DA40 | Cadet Prep",
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

st.markdown('<h1 class="page-header">✈️ Diamond DA40 Diamond Star</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">TAFA Advanced Single-Engine Trainer | Modern Composite Design</p>', unsafe_allow_html=True)

# Aircraft Image Section
import os

# Check for local image first
local_image_path = "assets/da40.jpg"
local_image_png = "assets/da40.png"

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists(local_image_path):
        st.image(local_image_path, caption="Diamond DA40 Diamond Star with G1000 NXi", use_container_width=True)
    elif os.path.exists(local_image_png):
        st.image(local_image_png, caption="Diamond DA40 Diamond Star with G1000 NXi", use_container_width=True)
    else:
        # Display placeholder with instructions
        st.markdown("""
        <div class="spec-card" style="text-align: center; padding: 2rem;">
            <div style="font-size: 6rem; margin-bottom: 1rem;">🛩️</div>
            <h3 style="color: #fff; margin-bottom: 0.5rem;">Diamond DA40 Diamond Star</h3>
            <p style="color: #888; font-style: italic;">Modern composite single-engine trainer with center stick control</p>
            <p style="color: #666; font-size: 0.85rem; margin-top: 1rem;">
                💡 To add an image: Save as <code>assets/da40.jpg</code>
            </p>
        </div>
        """, unsafe_allow_html=True)

# G1000 NXi description
with st.expander("🖥️ About the G1000 NXi Avionics"):
    st.markdown("""
    The Garmin G1000 NXi in DA40 features:
    - **Faster Processors** - Improved boot time and responsiveness
    - **Wireless Database Updates** - Connext Bluetooth connectivity  
    - **Synthetic Vision** - 3D terrain display on PFD
    - **GFC 700 Autopilot** - Three-axis autopilot with flight director
    - **ADS-B In/Out** - Traffic and weather information
    - **Integrated Engine Monitoring** - Austro/Lycoming engine data
    """)

# Main specifications
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">📋 General Information</h3>
        <table class="spec-table">
            <tr><td>Manufacturer</td><td class="spec-value">Diamond Aircraft Industries (Austria)</td></tr>
            <tr><td>First Flight</td><td class="spec-value">1997</td></tr>
            <tr><td>Type</td><td class="spec-value">Single-engine, low-wing, fixed-gear</td></tr>
            <tr><td>Role</td><td class="spec-value">Advanced flight training, touring</td></tr>
            <tr><td>Crew</td><td class="spec-value">1 pilot</td></tr>
            <tr><td>Capacity</td><td class="spec-value">3 passengers (4 total occupants)</td></tr>
            <tr><td>Construction</td><td class="spec-value">Composite (carbon fiber/fiberglass)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">⚙️ Engine Specifications</h3>
        <table class="spec-table">
            <tr><td>Engine</td><td class="spec-value">Lycoming IO-360-M1A</td></tr>
            <tr><td>Engine Type</td><td class="spec-value">4-cylinder, horizontally opposed</td></tr>
            <tr><td>Power Output</td><td class="spec-value">180 HP (134 kW)</td></tr>
            <tr><td>Fuel Injection</td><td class="spec-value">Yes</td></tr>
            <tr><td>Propeller</td><td class="spec-value">MT 3-blade constant speed</td></tr>
            <tr><td>Fuel Type</td><td class="spec-value">100LL Avgas</td></tr>
            <tr><td>Fuel Capacity</td><td class="spec-value">148 L (39 US gal)</td></tr>
            <tr><td>Usable Fuel</td><td class="spec-value">145 L (38.3 US gal)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">📐 Dimensions</h3>
        <table class="spec-table">
            <tr><td>Wingspan</td><td class="spec-value">11.94 m (39 ft 2 in)</td></tr>
            <tr><td>Length</td><td class="spec-value">8.06 m (26 ft 5 in)</td></tr>
            <tr><td>Height</td><td class="spec-value">1.97 m (6 ft 6 in)</td></tr>
            <tr><td>Wing Area</td><td class="spec-value">13.54 m² (145.7 ft²)</td></tr>
            <tr><td>Wing Type</td><td class="spec-value">Low-wing, cantilever</td></tr>
            <tr><td>Aspect Ratio</td><td class="spec-value">10.5 (high efficiency)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">⚖️ Weights</h3>
        <table class="spec-table">
            <tr><td>Empty Weight</td><td class="spec-value">800 kg (1,764 lb)</td></tr>
            <tr><td>Max Takeoff Weight (MTOW)</td><td class="spec-value">1,200 kg (2,646 lb)</td></tr>
            <tr><td>Useful Load</td><td class="spec-value">400 kg (882 lb)</td></tr>
            <tr><td>Max Landing Weight</td><td class="spec-value">1,200 kg (2,646 lb)</td></tr>
            <tr><td>Baggage Capacity</td><td class="spec-value">30 kg (66 lb)</td></tr>
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
            <tr><td>Cruise Speed (75%)</td><td class="spec-value">147 kts (272 km/h)</td></tr>
            <tr><td>Max Speed (VNE)</td><td class="spec-value">178 kts (330 km/h)</td></tr>
            <tr><td>Stall Speed (Clean)</td><td class="spec-value">57 kts (106 km/h)</td></tr>
            <tr><td>Stall Speed (Flaps)</td><td class="spec-value">49 kts (91 km/h)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4 style="color: #c8102e;">Range & Endurance</h4>
        <table class="spec-table">
            <tr><td>Range (75% power)</td><td class="spec-value">720 nm (1,333 km)</td></tr>
            <tr><td>Endurance</td><td class="spec-value">~5 hours</td></tr>
            <tr><td>Fuel Consumption</td><td class="spec-value">~34 L/hr (9 gal/hr)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="highlight-box">
        <h4 style="color: #c8102e;">Climb & Ceiling</h4>
        <table class="spec-table">
            <tr><td>Rate of Climb</td><td class="spec-value">1,070 ft/min (5.4 m/s)</td></tr>
            <tr><td>Service Ceiling</td><td class="spec-value">16,400 ft (5,000 m)</td></tr>
            <tr><td>Takeoff Distance</td><td class="spec-value">1,232 ft (376 m)</td></tr>
            <tr><td>Landing Distance</td><td class="spec-value">1,148 ft (350 m)</td></tr>
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
        <tr><td><strong>VR</strong> (Rotation)</td><td class="spec-value">59 KIAS</td></tr>
        <tr><td><strong>VX</strong> (Best Angle of Climb)</td><td class="spec-value">66 KIAS</td></tr>
        <tr><td><strong>VY</strong> (Best Rate of Climb)</td><td class="spec-value">78 KIAS</td></tr>
        <tr><td><strong>VA</strong> (Maneuvering Speed @ MTOW)</td><td class="spec-value">108 KIAS</td></tr>
        <tr><td><strong>VFE</strong> (Max Flap Extended)</td><td class="spec-value">108 KIAS (TO), 91 KIAS (LDG)</td></tr>
    </table>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <table class="spec-table">
        <tr><td><strong>VNO</strong> (Max Structural Cruise)</td><td class="spec-value">135 KIAS</td></tr>
        <tr><td><strong>VNE</strong> (Never Exceed)</td><td class="spec-value">178 KIAS</td></tr>
        <tr><td><strong>VSO</strong> (Stall, Landing Config)</td><td class="spec-value">49 KIAS</td></tr>
        <tr><td><strong>VS1</strong> (Stall, Clean)</td><td class="spec-value">57 KIAS</td></tr>
        <tr><td><strong>VREF</strong> (Final Approach)</td><td class="spec-value">67-73 KIAS</td></tr>
    </table>
    """, unsafe_allow_html=True)

# Avionics
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">🖥️ Garmin G1000 NXi Avionics</h3>
    <p style="color: #d0d0d0; line-height: 1.8;">
        The DA40 features the Garmin G1000 NXi integrated flight deck:
    </p>
    <ul style="color: #d0d0d0; line-height: 2;">
        <li><strong>PFD (Primary Flight Display):</strong> High-resolution LCD with synthetic vision</li>
        <li><strong>MFD (Multi-Function Display):</strong> Engine monitoring, moving map, weather</li>
        <li><strong>GFC 700 Autopilot:</strong> Three-axis autopilot with flight director</li>
        <li><strong>Wireless Database Updates:</strong> Connext wireless connectivity</li>
        <li><strong>Faster Processors:</strong> Improved boot time and responsiveness</li>
        <li><strong>ADS-B In/Out:</strong> Traffic and weather information</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# DA40 vs Cessna 172 Comparison
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">🔄 DA40 vs Cessna 172 - Key Differences</h3>
    <table class="spec-table">
        <tr style="background: rgba(200, 16, 46, 0.2);">
            <td><strong>Feature</strong></td>
            <td><strong>DA40</strong></td>
            <td><strong>Cessna 172</strong></td>
        </tr>
        <tr><td>Wing Position</td><td class="spec-value">Low-wing</td><td>High-wing</td></tr>
        <tr><td>Construction</td><td class="spec-value">Composite</td><td>Aluminum</td></tr>
        <tr><td>Propeller</td><td class="spec-value">Constant-speed (3-blade)</td><td>Fixed-pitch (2-blade)</td></tr>
        <tr><td>Cruise Speed</td><td class="spec-value">147 kts (faster)</td><td>122 kts</td></tr>
        <tr><td>Rate of Climb</td><td class="spec-value">1,070 ft/min (better)</td><td>730 ft/min</td></tr>
        <tr><td>Fuel Efficiency</td><td class="spec-value">Better (composite, aerodynamics)</td><td>Standard</td></tr>
        <tr><td>Visibility</td><td class="spec-value">Forward/sides (low-wing)</td><td>Better upward (high-wing)</td></tr>
        <tr><td>Stick vs Yoke</td><td class="spec-value">Center stick</td><td>Yoke</td></tr>
        <tr><td>Castering Nose Wheel</td><td class="spec-value">Yes (differential braking)</td><td>No (steerable)</td></tr>
    </table>
</div>
""", unsafe_allow_html=True)

# Why DA40 for training
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">💡 Why DA40 for Advanced Training?</h3>
    <ul style="color: #d0d0d0; line-height: 2;">
        <li><strong>Constant-Speed Propeller:</strong> Introduces complex aircraft operations</li>
        <li><strong>Higher Performance:</strong> Better climb rate and cruise speed</li>
        <li><strong>Low-Wing Aerodynamics:</strong> Different handling characteristics from C172</li>
        <li><strong>Center Stick:</strong> Develops fine motor control for future airline sidestick</li>
        <li><strong>Castering Nose Wheel:</strong> Teaches differential braking technique</li>
        <li><strong>Modern Design:</strong> Latest avionics and safety features</li>
        <li><strong>Excellent Safety Record:</strong> Spin-resistant design</li>
        <li><strong>Fuel Efficiency:</strong> Lower operating costs per hour</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Back button
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("← Cessna 172"):
        st.switch_page("pages/4_✈️_Cessna_172.py")
with col2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")
with col3:
    if st.button("DA42 →"):
        st.switch_page("pages/6_✈️_DA42.py")

