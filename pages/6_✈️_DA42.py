"""
Diamond DA42 Twin Star Training Aircraft Details
"""

import streamlit as st

st.set_page_config(
    page_title="Diamond DA42 | Cadet Prep",
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
    
    .critical-box {
        background: rgba(255, 193, 7, 0.1);
        border: 2px solid rgba(255, 193, 7, 0.5);
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="page-header">✈️ Diamond DA42 Twin Star</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">TAFA Multi-Engine Trainer | Twin Diesel Powerplant</p>', unsafe_allow_html=True)

# Aircraft Image Section
import os

# Check for local image first
local_image_path = "assets/da42.jpg"
local_image_png = "assets/da42.png"

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists(local_image_path):
        st.image(local_image_path, caption="Diamond DA42 Twin Star with Austro AE300 engines", use_container_width=True)
    elif os.path.exists(local_image_png):
        st.image(local_image_png, caption="Diamond DA42 Twin Star with Austro AE300 engines", use_container_width=True)
    else:
        # Display placeholder with instructions
        st.markdown("""
        <div class="spec-card" style="text-align: center; padding: 2rem;">
            <div style="font-size: 6rem; margin-bottom: 1rem;">✈️✈️</div>
            <h3 style="color: #fff; margin-bottom: 0.5rem;">Diamond DA42 Twin Star</h3>
            <p style="color: #888; font-style: italic;">Modern twin-engine trainer with Austro diesel engines and FADEC</p>
            <p style="color: #666; font-size: 0.85rem; margin-top: 1rem;">
                💡 To add an image: Save as <code>assets/da42.jpg</code>
            </p>
        </div>
        """, unsafe_allow_html=True)

# DA42 key features
with st.expander("🔧 DA42 Key Features"):
    st.markdown("""
    **Engine & Propulsion:**
    - 2x Austro Engine AE300 turbo-diesel (168 HP each)
    - FADEC - Single-lever power control
    - Jet-A1 fuel (same as airliners)
    - 3-blade constant-speed feathering propellers
    
    **Airframe:**
    - Full composite construction (carbon fiber/glass)
    - Retractable tricycle landing gear
    - Low-wing cantilever design
    
    **Avionics:**
    - Garmin G1000 NXi integrated flight deck
    - GFC 700 autopilot with flight director
    - Synthetic Vision Technology (SVT)
    """)

# Main specifications
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">📋 General Information</h3>
        <table class="spec-table">
            <tr><td>Manufacturer</td><td class="spec-value">Diamond Aircraft Industries (Austria)</td></tr>
            <tr><td>First Flight</td><td class="spec-value">December 2002</td></tr>
            <tr><td>Type</td><td class="spec-value">Twin-engine, low-wing, retractable gear</td></tr>
            <tr><td>Role</td><td class="spec-value">Multi-engine training, IFR training</td></tr>
            <tr><td>Crew</td><td class="spec-value">1-2 pilots</td></tr>
            <tr><td>Capacity</td><td class="spec-value">2-4 total occupants</td></tr>
            <tr><td>Construction</td><td class="spec-value">Composite (carbon fiber/fiberglass)</td></tr>
            <tr><td>Variant</td><td class="spec-value">DA42 NG (New Generation)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">⚙️ Engine Specifications (DA42 NG)</h3>
        <table class="spec-table">
            <tr><td>Engines</td><td class="spec-value">2x Austro Engine AE300</td></tr>
            <tr><td>Engine Type</td><td class="spec-value">Turbo-diesel, liquid-cooled</td></tr>
            <tr><td>Power Output (each)</td><td class="spec-value">168 HP (125 kW)</td></tr>
            <tr><td>Total Power</td><td class="spec-value">336 HP (250 kW)</td></tr>
            <tr><td>FADEC</td><td class="spec-value">Yes (Full Authority Digital Engine Control)</td></tr>
            <tr><td>Propeller</td><td class="spec-value">MT 3-blade constant speed, feathering</td></tr>
            <tr><td>Fuel Type</td><td class="spec-value">Jet-A1 / Diesel</td></tr>
            <tr><td>Fuel Capacity</td><td class="spec-value">218 L (57.6 US gal)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">📐 Dimensions</h3>
        <table class="spec-table">
            <tr><td>Wingspan</td><td class="spec-value">13.42 m (44 ft 0 in)</td></tr>
            <tr><td>Length</td><td class="spec-value">8.56 m (28 ft 1 in)</td></tr>
            <tr><td>Height</td><td class="spec-value">2.49 m (8 ft 2 in)</td></tr>
            <tr><td>Wing Area</td><td class="spec-value">16.29 m² (175.3 ft²)</td></tr>
            <tr><td>Wing Type</td><td class="spec-value">Low-wing, cantilever</td></tr>
            <tr><td>Engine Nacelles</td><td class="spec-value">Wing-mounted, above wing</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="spec-card">
        <h3 class="spec-title">⚖️ Weights</h3>
        <table class="spec-table">
            <tr><td>Empty Weight</td><td class="spec-value">1,280 kg (2,822 lb)</td></tr>
            <tr><td>Max Takeoff Weight (MTOW)</td><td class="spec-value">1,900 kg (4,189 lb)</td></tr>
            <tr><td>Useful Load</td><td class="spec-value">620 kg (1,367 lb)</td></tr>
            <tr><td>Max Landing Weight</td><td class="spec-value">1,805 kg (3,979 lb)</td></tr>
            <tr><td>Zero Fuel Weight</td><td class="spec-value">1,650 kg (3,638 lb)</td></tr>
            <tr><td>Baggage Capacity</td><td class="spec-value">45 kg (99 lb)</td></tr>
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
        <h4 style="color: #c8102e;">Speed (Both Engines)</h4>
        <table class="spec-table">
            <tr><td>Cruise Speed (75%)</td><td class="spec-value">180 kts (333 km/h)</td></tr>
            <tr><td>Max Speed (VNE)</td><td class="spec-value">223 kts (413 km/h)</td></tr>
            <tr><td>Stall Speed (Clean)</td><td class="spec-value">67 kts (124 km/h)</td></tr>
            <tr><td>Stall Speed (Flaps)</td><td class="spec-value">60 kts (111 km/h)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4 style="color: #c8102e;">Range & Endurance</h4>
        <table class="spec-table">
            <tr><td>Range (75% power)</td><td class="spec-value">920 nm (1,704 km)</td></tr>
            <tr><td>Range (Economy)</td><td class="spec-value">1,200 nm (2,222 km)</td></tr>
            <tr><td>Endurance</td><td class="spec-value">~6-7 hours</td></tr>
            <tr><td>Fuel Consumption</td><td class="spec-value">~32 L/hr total</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="highlight-box">
        <h4 style="color: #c8102e;">Climb & Ceiling</h4>
        <table class="spec-table">
            <tr><td>Rate of Climb (both)</td><td class="spec-value">1,300 ft/min</td></tr>
            <tr><td>Single-Engine ROC</td><td class="spec-value">274 ft/min</td></tr>
            <tr><td>Service Ceiling</td><td class="spec-value">18,000 ft (5,486 m)</td></tr>
            <tr><td>Single-Engine Ceiling</td><td class="spec-value">10,000 ft (3,048 m)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

# V-Speeds - Critical for multi-engine
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">🎯 V-Speeds (CRITICAL FOR MULTI-ENGINE!)</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="critical-box">
        <h4 style="color: #ffc107;">⚠️ Critical Multi-Engine V-Speeds</h4>
        <table class="spec-table">
            <tr><td><strong>VMC</strong> (Min Control Speed)</td><td class="spec-value">68 KIAS</td></tr>
            <tr><td><strong>VYSE</strong> (Best SE Rate of Climb)</td><td class="spec-value">85 KIAS (Blue Line)</td></tr>
            <tr><td><strong>VXSE</strong> (Best SE Angle of Climb)</td><td class="spec-value">80 KIAS</td></tr>
            <tr><td><strong>VSSE</strong> (Safe SE Speed)</td><td class="spec-value">82 KIAS</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <table class="spec-table">
        <tr><td><strong>VR</strong> (Rotation)</td><td class="spec-value">74 KIAS</td></tr>
        <tr><td><strong>VX</strong> (Best Angle of Climb)</td><td class="spec-value">81 KIAS</td></tr>
        <tr><td><strong>VY</strong> (Best Rate of Climb)</td><td class="spec-value">91 KIAS</td></tr>
        <tr><td><strong>VA</strong> (Maneuvering Speed)</td><td class="spec-value">131 KIAS</td></tr>
    </table>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <table class="spec-table">
        <tr><td><strong>VLO</strong> (Gear Operating)</td><td class="spec-value">154 KIAS</td></tr>
        <tr><td><strong>VLE</strong> (Gear Extended)</td><td class="spec-value">154 KIAS</td></tr>
        <tr><td><strong>VFE</strong> (Flaps Extended)</td><td class="spec-value">120 KIAS (Approach), 108 KIAS (Landing)</td></tr>
        <tr><td><strong>VNO</strong> (Max Structural Cruise)</td><td class="spec-value">180 KIAS</td></tr>
        <tr><td><strong>VNE</strong> (Never Exceed)</td><td class="spec-value">223 KIAS</td></tr>
        <tr><td><strong>VSO</strong> (Stall, Landing Config)</td><td class="spec-value">60 KIAS</td></tr>
        <tr><td><strong>VS1</strong> (Stall, Clean)</td><td class="spec-value">67 KIAS</td></tr>
        <tr><td><strong>VREF</strong> (Final Approach)</td><td class="spec-value">80-85 KIAS</td></tr>
    </table>
    """, unsafe_allow_html=True)

# Engine-Out Procedures
st.markdown("""
<div class="spec-card" style="border-color: rgba(255, 193, 7, 0.5);">
    <h3 class="spec-title" style="color: #ffc107;">⚠️ Engine Failure Procedures (Memory Items)</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Engine Failure During Takeoff (Before Liftoff):**
    1. Throttles - **IDLE**
    2. Brakes - **APPLY**
    3. **Abort takeoff**
    """)

with col2:
    st.markdown("""
    **Engine Failure After Liftoff:**
    1. Maintain directional control (**RUDDER**)
    2. Pitch for **VYSE (85 KIAS)** - Blue Line
    3. Identify failed engine ("**Dead Foot = Dead Engine**")
    4. **Verify** - Throttle to idle on suspected engine
    5. **Feather** - Propeller lever to feather
    6. Mixture - Idle cutoff on failed engine
    7. Fuel selector - OFF on failed engine
    8. Complete appropriate checklist
    """)

st.markdown("""
<div style="background: rgba(255, 193, 7, 0.15); border: 2px solid rgba(255, 193, 7, 0.5); border-radius: 8px; padding: 1rem; margin: 1rem 0; text-align: center;">
    <h4 style="color: #ffc107; margin: 0;">🧠 Memory Aid: "Identify, Verify, Feather"</h4>
</div>
""", unsafe_allow_html=True)

# Retractable Gear System
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">⚙️ Retractable Landing Gear System</h3>
    <ul style="color: #d0d0d0; line-height: 2;">
        <li><strong>Type:</strong> Electro-hydraulic tricycle gear</li>
        <li><strong>Extension/Retraction Time:</strong> ~8 seconds</li>
        <li><strong>Emergency Extension:</strong> Gravity free-fall with manual release</li>
        <li><strong>Gear Indicators:</strong> 3 green lights (down and locked)</li>
        <li><strong>Warning Horn:</strong> Activates below 100 KIAS with gear up</li>
        <li><strong>Auto-Extension:</strong> Activates below certain speed thresholds</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# FADEC Diesel Engines
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">🔧 Austro Engine AE300 - Diesel FADEC</h3>
    <ul style="color: #d0d0d0; line-height: 2;">
        <li><strong>FADEC Benefits:</strong> Single-lever power control, automatic mixture, no manual mixture management</li>
        <li><strong>Jet Fuel Advantage:</strong> Jet-A1 is more available worldwide than 100LL Avgas</li>
        <li><strong>Fuel Efficiency:</strong> 30-50% better fuel consumption than gasoline engines</li>
        <li><strong>Gearbox:</strong> Integrated reduction gearbox for propeller</li>
        <li><strong>Liquid Cooling:</strong> Better temperature management than air-cooled engines</li>
        <li><strong>TBO:</strong> 1,800 hours Time Between Overhaul</li>
        <li><strong>ECU:</strong> Dual redundant Electronic Control Units</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Why DA42 for multi-engine training
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">💡 Why DA42 for Multi-Engine Training?</h3>
    <ul style="color: #d0d0d0; line-height: 2;">
        <li><strong>Modern MEP Training:</strong> Centerline thrust awareness not required</li>
        <li><strong>Safe Vmca:</strong> Very manageable minimum control speed</li>
        <li><strong>FADEC Simplicity:</strong> Focus on flying, not mixture management</li>
        <li><strong>Retractable Gear:</strong> Complex aircraft experience</li>
        <li><strong>Fuel Efficiency:</strong> Lower training costs vs older twins</li>
        <li><strong>Glass Cockpit:</strong> G1000 experience continues from single-engine</li>
        <li><strong>Excellent Visibility:</strong> Good for traffic awareness</li>
        <li><strong>Benign Handling:</strong> Forgiving flight characteristics</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Interview Questions
st.markdown("""
<div class="spec-card">
    <h3 class="spec-title">❓ Common Multi-Engine Interview Questions</h3>
    <ul style="color: #d0d0d0; line-height: 2;">
        <li><strong>Q: What is VMC?</strong> A: Minimum controllable airspeed with critical engine inoperative, max power on operating engine.</li>
        <li><strong>Q: What is the blue line?</strong> A: VYSE - Best single-engine rate of climb speed (85 KIAS on DA42).</li>
        <li><strong>Q: Why is VMC marked with a red radial line?</strong> A: To indicate that flight below this speed with engine failure could result in loss of control.</li>
        <li><strong>Q: What factors affect VMC?</strong> A: Altitude (density altitude), weight, CG position, bank angle, gear/flaps configuration.</li>
        <li><strong>Q: What is "Dead Foot = Dead Engine"?</strong> A: The foot with less rudder pressure is on the side of the failed engine.</li>
        <li><strong>Q: Why feather the propeller?</strong> A: To reduce drag by aligning prop blades with the airflow.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Back button
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("← DA40"):
        st.switch_page("pages/5_✈️_DA40.py")
with col2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")
with col3:
    if st.button("Aviation News →"):
        st.switch_page("pages/7_📰_Aviation_News.py")

