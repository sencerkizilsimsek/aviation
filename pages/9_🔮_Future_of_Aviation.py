"""
Future of Aviation Page
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config import config
from utils.gemini_helper import gemini, render_ai_section

st.set_page_config(
    page_title="Future of Aviation | Cadet Prep",
    page_icon="🔮",
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
    
    .future-card {
        background: linear-gradient(145deg, rgba(30, 30, 50, 0.9), rgba(20, 20, 35, 0.95));
        border: 1px solid rgba(200, 16, 46, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .future-card:hover {
        border-color: rgba(200, 16, 46, 0.6);
        box-shadow: 0 8px 30px rgba(200, 16, 46, 0.2);
    }
    
    .section-title {
        font-family: 'Orbitron', monospace;
        font-size: 1.5rem;
        color: #c8102e;
        margin-bottom: 1rem;
    }
    
    .content-text {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1rem;
        color: #d0d0d0;
        line-height: 1.8;
    }
    
    .timeline-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        background: rgba(200, 16, 46, 0.2);
        border: 1px solid rgba(200, 16, 46, 0.4);
        border-radius: 20px;
        font-size: 0.9rem;
        color: #c8102e;
        margin-bottom: 1rem;
    }
    
    .impact-high {
        border-left: 4px solid #ff4757;
    }
    
    .impact-medium {
        border-left: 4px solid #ffa502;
    }
    
    .impact-emerging {
        border-left: 4px solid #2ed573;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="page-header">🔮 Future of Aviation</h1>', unsafe_allow_html=True)
st.markdown("*Emerging technologies and trends shaping tomorrow's aviation industry*")

# Tab organization
tab1, tab2, tab3, tab4 = st.tabs(["🌱 Sustainability", "🤖 Technology", "✈️ Aircraft", "👨‍✈️ Operations"])

with tab1:
    st.markdown('<h2 class="section-title">🌱 Sustainable Aviation</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-high">
        <span class="timeline-badge">2024-2050</span>
        <h3 style="color: #fff;">Sustainable Aviation Fuel (SAF)</h3>
        <p class="content-text">
            <strong>What it is:</strong> SAF is produced from sustainable feedstocks like used cooking oil, 
            agricultural residues, municipal waste, and even captured CO2. It can reduce lifecycle carbon 
            emissions by up to 80% compared to conventional jet fuel.
        </p>
        <p class="content-text">
            <strong>Current Status:</strong> SAF currently makes up less than 1% of global jet fuel consumption. 
            Airlines are committed to increasing this to 10% by 2030 and achieving net-zero emissions by 2050.
        </p>
        <p class="content-text">
            <strong>Challenges:</strong> Limited production capacity, higher cost (2-4x conventional fuel), 
            feedstock availability, and infrastructure requirements.
        </p>
        <p class="content-text">
            <strong>Turkish Airlines:</strong> THY has committed to sustainability goals aligned with IATA targets 
            and is increasing SAF usage on select routes.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-high">
        <span class="timeline-badge">2025-2040</span>
        <h3 style="color: #fff;">Electric & Hybrid-Electric Aircraft</h3>
        <p class="content-text">
            <strong>Electric Aircraft:</strong> Battery-powered aircraft are being developed for short-range 
            regional flights (up to 500 nm). Companies like Heart Aerospace, Eviation, and others are developing 
            9-30 seat electric aircraft.
        </p>
        <p class="content-text">
            <strong>Hybrid-Electric:</strong> Combines conventional engines with electric motors. Could reduce 
            fuel consumption by 30-50%. Airbus and Boeing are exploring hybrid concepts.
        </p>
        <p class="content-text">
            <strong>Limitations:</strong> Battery energy density is currently ~50x lower than jet fuel. This limits 
            range and payload. Significant improvements needed for larger aircraft.
        </p>
        <p class="content-text">
            <strong>Timeline:</strong> Regional electric aircraft expected by 2028-2030. Hybrid aircraft for 
            larger operations expected 2035-2040.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-medium">
        <span class="timeline-badge">2030-2050</span>
        <h3 style="color: #fff;">Hydrogen-Powered Aviation</h3>
        <p class="content-text">
            <strong>Concept:</strong> Hydrogen can be burned in modified turbine engines or used in fuel cells. 
            Produces zero CO2 emissions at point of use (only water vapor).
        </p>
        <p class="content-text">
            <strong>Airbus ZEROe:</strong> Airbus is developing hydrogen aircraft concepts targeting entry into 
            service by 2035. Designs include turboprop, turbofan, and blended-wing-body configurations.
        </p>
        <p class="content-text">
            <strong>Challenges:</strong> Hydrogen requires 4x the volume of jet fuel for the same energy. 
            Requires new airport infrastructure, storage systems, and safety protocols. Green hydrogen 
            production must scale up.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-medium">
        <span class="timeline-badge">2024-2030</span>
        <h3 style="color: #fff;">Carbon Offsetting & Net-Zero Targets</h3>
        <p class="content-text">
            <strong>CORSIA:</strong> Carbon Offsetting and Reduction Scheme for International Aviation (ICAO) 
            requires airlines to offset emissions growth above 2019 levels.
        </p>
        <p class="content-text">
            <strong>Industry Commitment:</strong> IATA airlines committed to net-zero carbon emissions by 2050. 
            This requires combination of new technology, SAF, operational improvements, and carbon offsets.
        </p>
        <p class="content-text">
            <strong>EU Regulations:</strong> European Green Deal includes aviation in emissions trading scheme (ETS) 
            and mandates increasing SAF blending percentages.
        </p>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown('<h2 class="section-title">🤖 Technology Advances</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-high">
        <span class="timeline-badge">Now-2030</span>
        <h3 style="color: #fff;">Artificial Intelligence in Aviation</h3>
        <p class="content-text">
            <strong>Flight Operations:</strong> AI is being used for flight planning optimization, fuel efficiency, 
            predictive maintenance, and weather routing. Can reduce fuel consumption by 5-10%.
        </p>
        <p class="content-text">
            <strong>Air Traffic Management:</strong> AI-enhanced ATC systems can optimize airspace usage, 
            reduce delays, and improve safety through better conflict detection.
        </p>
        <p class="content-text">
            <strong>Maintenance:</strong> Predictive maintenance using AI analyzes sensor data to predict 
            component failures before they occur, reducing unscheduled maintenance.
        </p>
        <p class="content-text">
            <strong>Pilot Assistance:</strong> AI co-pilot systems can assist with workload management, 
            provide decision support, and enhance situational awareness.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-high">
        <span class="timeline-badge">Now-2035</span>
        <h3 style="color: #fff;">Advanced Automation & Autonomy</h3>
        <p class="content-text">
            <strong>Enhanced Autopilot:</strong> Modern autopilots can handle all phases of flight. 
            Future systems will have better decision-making capabilities in complex situations.
        </p>
        <p class="content-text">
            <strong>Single-Pilot Operations (SPO):</strong> Regulators are studying reduced crew operations 
            for certain flights. Would require ground-based monitoring and advanced automation.
        </p>
        <p class="content-text">
            <strong>Autonomous Cargo:</strong> Unmanned cargo aircraft are being developed and tested. 
            Could enter service before passenger autonomy.
        </p>
        <p class="content-text">
            <strong>Note:</strong> Full passenger autonomy remains distant. Safety certification requires 
            extensive validation, and public acceptance is a major factor.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-medium">
        <span class="timeline-badge">Now-2030</span>
        <h3 style="color: #fff;">Connected Aircraft & Digital Operations</h3>
        <p class="content-text">
            <strong>Real-time Connectivity:</strong> High-speed satellite internet enables real-time data 
            transmission for operations, maintenance, and passenger connectivity.
        </p>
        <p class="content-text">
            <strong>Electronic Flight Bag (EFB):</strong> Tablets and digital systems replace paper charts 
            and manuals. Enables dynamic updates and integration with airline systems.
        </p>
        <p class="content-text">
            <strong>Digital Twin:</strong> Virtual replicas of aircraft that simulate real-world conditions 
            for maintenance prediction and operational optimization.
        </p>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown('<h2 class="section-title">✈️ Future Aircraft</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-emerging">
        <span class="timeline-badge">2025-2030</span>
        <h3 style="color: #fff;">Urban Air Mobility (UAM) / eVTOL</h3>
        <p class="content-text">
            <strong>What it is:</strong> Electric Vertical Take-Off and Landing (eVTOL) aircraft designed 
            for urban transportation. Think "air taxis" for city transport.
        </p>
        <p class="content-text">
            <strong>Key Players:</strong> Joby Aviation, Lilium, Archer, Volocopter, Wisk, and others. 
            Many are backed by major aerospace companies and airlines.
        </p>
        <p class="content-text">
            <strong>Characteristics:</strong> 2-6 passengers, 20-100 mile range, speed ~150 mph, 
            quiet operation, zero emissions at point of use.
        </p>
        <p class="content-text">
            <strong>Timeline:</strong> First commercial operations expected 2025-2027 in select cities. 
            Scale-up through 2030s.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-medium">
        <span class="timeline-badge">2030-2040</span>
        <h3 style="color: #fff;">Next-Generation Narrowbody Aircraft</h3>
        <p class="content-text">
            <strong>A320/737 Replacements:</strong> Both Airbus and Boeing are studying clean-sheet 
            narrowbody aircraft to replace the A320 family and 737 MAX.
        </p>
        <p class="content-text">
            <strong>Expected Features:</strong> 20-30% better fuel efficiency, possibly new engine types 
            (open rotor, ultra-high bypass), advanced composites, and enhanced automation.
        </p>
        <p class="content-text">
            <strong>Timeline:</strong> Development decisions expected mid-2020s, entry into service 
            potentially early-to-mid 2030s.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-medium">
        <span class="timeline-badge">2035+</span>
        <h3 style="color: #fff;">Supersonic & Hypersonic Travel</h3>
        <p class="content-text">
            <strong>Boom Overture:</strong> Boom Supersonic is developing a Mach 1.7 supersonic airliner 
            for 65-80 passengers. Designed to be sustainable with SAF.
        </p>
        <p class="content-text">
            <strong>Challenges:</strong> Sonic boom restrictions over land, fuel efficiency, noise regulations, 
            and certification requirements.
        </p>
        <p class="content-text">
            <strong>Hypersonic:</strong> Research into Mach 5+ passenger travel continues but remains 
            decades away from commercial reality.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-emerging">
        <span class="timeline-badge">2030-2040</span>
        <h3 style="color: #fff;">Blended Wing Body (BWB) Aircraft</h3>
        <p class="content-text">
            <strong>Concept:</strong> Aircraft where the wings blend seamlessly into the body, 
            creating a more efficient aerodynamic shape.
        </p>
        <p class="content-text">
            <strong>Benefits:</strong> 20-30% better fuel efficiency, reduced noise, more interior 
            space, potential for distributed propulsion.
        </p>
        <p class="content-text">
            <strong>Challenges:</strong> Passenger acceptance (no windows in some seats), emergency 
            evacuation certification, airport compatibility.
        </p>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown('<h2 class="section-title">👨‍✈️ Future Operations</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-high">
        <span class="timeline-badge">Now-2030</span>
        <h3 style="color: #fff;">Single European Sky & NextGen</h3>
        <p class="content-text">
            <strong>Single European Sky (SES):</strong> Initiative to modernize European air traffic 
            management, reduce fragmentation, and improve efficiency.
        </p>
        <p class="content-text">
            <strong>NextGen (US):</strong> FAA's Next Generation Air Transportation System. Transitions 
            from radar to satellite-based navigation and surveillance.
        </p>
        <p class="content-text">
            <strong>Benefits:</strong> Reduced delays, more efficient routes, lower fuel consumption, 
            and improved safety through better situational awareness.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-medium">
        <span class="timeline-badge">2025-2035</span>
        <h3 style="color: #fff;">Reduced Crew Operations</h3>
        <p class="content-text">
            <strong>Extended Minimum Crew (eMCO):</strong> Studies into allowing single-pilot cruise 
            phases for long-haul flights, with second pilot resting.
        </p>
        <p class="content-text">
            <strong>Single-Pilot Operations (SPO):</strong> Research into solo-pilot commercial 
            operations with ground-based support.
        </p>
        <p class="content-text">
            <strong>Requirements:</strong> Enhanced automation, ground monitoring systems, 
            pilot incapacitation detection, and extensive safety validation.
        </p>
        <p class="content-text">
            <strong>Note:</strong> Any changes will be gradual, heavily regulated, and prioritize safety. 
            Pilots remain essential for the foreseeable future.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="future-card impact-high">
        <span class="timeline-badge">Now-2030</span>
        <h3 style="color: #fff;">Training Evolution</h3>
        <p class="content-text">
            <strong>Evidence-Based Training (EBT):</strong> Modern training approach focusing on 
            competencies rather than just maneuvers. Based on data analysis of real operations.
        </p>
        <p class="content-text">
            <strong>Virtual Reality (VR):</strong> VR training for procedures, emergency scenarios, 
            and cockpit familiarization. Supplements traditional simulator training.
        </p>
        <p class="content-text">
            <strong>MPL:</strong> Multi-Crew Pilot Licence focuses on airline operations from the start, 
            with extensive simulator training. THY's TAFA program incorporates modern training methods.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Key Interview Points
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="future-card">
    <h3 class="section-title">💡 Key Points for Interview</h3>
    <ul class="content-text">
        <li><strong>Sustainability Awareness:</strong> Know about SAF, carbon targets, and airline commitments</li>
        <li><strong>Technology Understanding:</strong> Be familiar with automation trends but emphasize pilot importance</li>
        <li><strong>Balanced View:</strong> Acknowledge challenges as well as opportunities</li>
        <li><strong>Career Relevance:</strong> Show you understand how these trends affect your future career</li>
        <li><strong>Safety Priority:</strong> Always emphasize that safety drives all aviation decisions</li>
        <li><strong>Enthusiasm:</strong> Express excitement about being part of aviation's future</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# AI Insights Section
existing_topics = [
    "Electric Aircraft", "Sustainable Aviation Fuel", "Urban Air Mobility",
    "Autonomous Flight", "Advanced Air Mobility", "Hydrogen Aircraft",
    "Next-Gen ATC", "Supersonic Revival", "Space Tourism"
]

render_ai_section(
    page_name='future',
    card_type='insight',
    generate_func=gemini.get_future_insights,
    generate_args=(existing_topics,),
    section_title="🤖 AI Future Aviation Insights"
)

# Back button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("← Back to Home"):
    st.switch_page("app.py")

