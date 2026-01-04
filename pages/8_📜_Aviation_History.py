"""
Aviation History Timeline Page
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config import config
from utils.gemini_helper import gemini, render_ai_section

st.set_page_config(
    page_title="Aviation History | Cadet Prep",
    page_icon="📜",
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
    
    .timeline-card {
        background: linear-gradient(145deg, rgba(30, 30, 50, 0.9), rgba(20, 20, 35, 0.95));
        border-left: 4px solid #c8102e;
        border-radius: 0 12px 12px 0;
        padding: 1.5rem;
        margin: 1rem 0;
        position: relative;
    }
    
    .timeline-year {
        font-family: 'Orbitron', monospace;
        font-size: 1.8rem;
        font-weight: 700;
        color: #c8102e;
        margin-bottom: 0.5rem;
    }
    
    .timeline-title {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.3rem;
        font-weight: 600;
        color: #fff;
        margin-bottom: 0.5rem;
    }
    
    .timeline-content {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1rem;
        color: #d0d0d0;
        line-height: 1.6;
    }
    
    .era-header {
        font-family: 'Orbitron', monospace;
        font-size: 1.5rem;
        color: #c8102e;
        border-bottom: 2px solid rgba(200, 16, 46, 0.5);
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
    }
    
    .info-card {
        background: linear-gradient(145deg, rgba(30, 30, 50, 0.9), rgba(20, 20, 35, 0.95));
        border: 1px solid rgba(200, 16, 46, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="page-header">📜 History of Aviation</h1>', unsafe_allow_html=True)
st.markdown("*From the first flight to the modern jet age - major milestones every pilot should know*")

# Timeline data
history_data = [
    # Pioneers Era
    {"year": 1783, "era": "Pioneers", "title": "First Hot Air Balloon Flight", 
     "content": "The Montgolfier brothers launched the first manned hot air balloon flight in Paris, France. Jacques-Étienne and Joseph-Michel Montgolfier demonstrated that humans could fly."},
    
    {"year": 1799, "era": "Pioneers", "title": "George Cayley's Glider Concept", 
     "content": "Sir George Cayley established the concept of the modern airplane with separate systems for lift, propulsion, and control. He is considered the 'Father of Aeronautics.'"},
    
    {"year": 1891, "era": "Pioneers", "title": "Otto Lilienthal's Glider Flights", 
     "content": "German aviation pioneer Otto Lilienthal made over 2,000 glider flights, documenting his research. His work heavily influenced the Wright Brothers."},
    
    {"year": 1903, "era": "Pioneers", "title": "First Powered Flight - Wright Brothers", 
     "content": "On December 17, 1903, Orville and Wilbur Wright achieved the first powered, controlled, sustained heavier-than-air flight at Kitty Hawk, North Carolina. The flight lasted 12 seconds, covering 120 feet."},
    
    {"year": 1909, "era": "Pioneers", "title": "First Flight Across English Channel", 
     "content": "Louis Blériot flew across the English Channel from Calais to Dover in 36 minutes, demonstrating the airplane's potential for international travel."},
    
    # Early Aviation Era
    {"year": 1914, "era": "Early Aviation", "title": "First Scheduled Airline Service", 
     "content": "The St. Petersburg-Tampa Airboat Line became the world's first scheduled commercial airline service, using a Benoist XIV flying boat."},
    
    {"year": 1914, "era": "Early Aviation", "title": "World War I Aviation Begins", 
     "content": "WWI saw rapid development of military aviation. Aircraft evolved from reconnaissance to fighters and bombers. Notable aircraft include the Fokker Dr.I and Sopwith Camel."},
    
    {"year": 1919, "era": "Early Aviation", "title": "First Transatlantic Flight", 
     "content": "John Alcock and Arthur Brown completed the first non-stop transatlantic flight from Newfoundland to Ireland in a modified Vickers Vimy bomber."},
    
    {"year": 1923, "era": "Early Aviation", "title": "First Non-Stop US Transcontinental Flight", 
     "content": "Lt. John Macready and Lt. Oakley Kelly flew non-stop from New York to San Diego in 26 hours and 50 minutes."},
    
    {"year": 1927, "era": "Early Aviation", "title": "Charles Lindbergh's Solo Atlantic Crossing", 
     "content": "Charles Lindbergh flew solo non-stop from New York to Paris in the Spirit of St. Louis, covering 3,600 miles in 33.5 hours. This flight captured worldwide attention and sparked aviation enthusiasm."},
    
    # Golden Age
    {"year": 1930, "era": "Golden Age", "title": "First Flight Attendant", 
     "content": "Ellen Church became the first female flight attendant on a Boeing Air Transport flight. She was also a registered nurse."},
    
    {"year": 1933, "era": "Golden Age", "title": "Turkish Airlines Founded", 
     "content": "Turkish Airlines (Türk Hava Yolları) was established as the State Airlines Administration. It is one of the oldest airlines in the world, celebrating over 90 years of operation."},
    
    {"year": 1933, "era": "Golden Age", "title": "Boeing 247 - First Modern Airliner", 
     "content": "The Boeing 247 introduced all-metal construction, retractable landing gear, and autopilot - features that defined the modern airliner."},
    
    {"year": 1935, "era": "Golden Age", "title": "Douglas DC-3 Introduced", 
     "content": "The Douglas DC-3 revolutionized commercial aviation. It could carry 21 passengers profitably and became the first aircraft to make money solely from passenger service."},
    
    {"year": 1937, "era": "Golden Age", "title": "Amelia Earhart Disappears", 
     "content": "Amelia Earhart, the first woman to fly solo across the Atlantic, disappeared over the Pacific during her attempt to circumnavigate the globe."},
    
    # WWII Era
    {"year": 1939, "era": "World War II", "title": "First Jet Aircraft Flight", 
     "content": "The Heinkel He 178 became the first aircraft to fly powered solely by a jet engine, designed by Hans von Ohain."},
    
    {"year": 1941, "era": "World War II", "title": "First British Jet Flight - Gloster E.28/39", 
     "content": "Britain's first jet aircraft, powered by Frank Whittle's engine, made its first flight."},
    
    {"year": 1942, "era": "World War II", "title": "B-17 Flying Fortress Production", 
     "content": "Mass production of the Boeing B-17 Flying Fortress reached its peak. Over 12,000 were built during the war."},
    
    {"year": 1944, "era": "World War II", "title": "Me 262 - First Jet Fighter in Combat", 
     "content": "The Messerschmitt Me 262 became the world's first operational jet-powered fighter aircraft."},
    
    {"year": 1944, "era": "World War II", "title": "ICAO Convention Signed", 
     "content": "The Chicago Convention established the International Civil Aviation Organization (ICAO), creating standards for international air navigation."},
    
    # Jet Age
    {"year": 1947, "era": "Jet Age", "title": "Sound Barrier Broken", 
     "content": "Chuck Yeager broke the sound barrier in the Bell X-1 'Glamorous Glennis,' reaching Mach 1.06 at 45,000 feet."},
    
    {"year": 1949, "era": "Jet Age", "title": "de Havilland Comet - First Jet Airliner", 
     "content": "The de Havilland Comet became the world's first commercial jet airliner. Initial crashes due to metal fatigue led to crucial advances in aircraft safety engineering."},
    
    {"year": 1952, "era": "Jet Age", "title": "BOAC Begins Jet Service", 
     "content": "British Overseas Airways Corporation (BOAC) began the world's first scheduled jet passenger service using the Comet."},
    
    {"year": 1954, "era": "Jet Age", "title": "Boeing 707 First Flight", 
     "content": "The Boeing 707 prototype (367-80) made its first flight. It would become the aircraft that truly started the jet age for commercial aviation."},
    
    {"year": 1958, "era": "Jet Age", "title": "Boeing 707 Enters Service", 
     "content": "Pan Am introduced the Boeing 707 on the New York to Paris route, beginning the modern jet age of commercial aviation."},
    
    {"year": 1958, "era": "Jet Age", "title": "FAA Established", 
     "content": "The Federal Aviation Agency (later Administration) was created to regulate civil aviation in the United States."},
    
    {"year": 1969, "era": "Jet Age", "title": "Boeing 747 First Flight", 
     "content": "The Boeing 747 'Jumbo Jet' made its first flight. It was the first wide-body commercial aircraft and revolutionized long-haul travel."},
    
    {"year": 1969, "era": "Jet Age", "title": "Concorde First Flight", 
     "content": "The Anglo-French Concorde supersonic airliner made its first flight. It would later operate at Mach 2.04."},
    
    {"year": 1970, "era": "Jet Age", "title": "Boeing 747 Enters Service", 
     "content": "Pan Am introduced the 747 on the New York to London route, making international travel accessible to more people."},
    
    # Modern Era
    {"year": 1978, "era": "Modern Era", "title": "US Airline Deregulation", 
     "content": "The Airline Deregulation Act removed government control over fares, routes, and market entry, leading to increased competition and lower fares."},
    
    {"year": 1981, "era": "Modern Era", "title": "First Glass Cockpit - Boeing 767", 
     "content": "The Boeing 767 introduced digital glass cockpit displays, replacing traditional analog instruments."},
    
    {"year": 1988, "era": "Modern Era", "title": "Airbus A320 First Flight with Fly-By-Wire", 
     "content": "The Airbus A320 became the first commercial aircraft with digital fly-by-wire controls, where computers interpret pilot inputs."},
    
    {"year": 1995, "era": "Modern Era", "title": "Boeing 777 Enters Service", 
     "content": "The Boeing 777, the first aircraft designed entirely using computer-aided design, entered service with United Airlines."},
    
    {"year": 2000, "era": "Modern Era", "title": "Concorde Crash", 
     "content": "Air France Flight 4590 crashed shortly after takeoff from Paris, leading to the eventual retirement of Concorde in 2003."},
    
    {"year": 2005, "era": "Modern Era", "title": "Airbus A380 First Flight", 
     "content": "The Airbus A380, the world's largest passenger aircraft (double-deck, four engines), made its first flight."},
    
    {"year": 2007, "era": "Modern Era", "title": "Boeing 787 Dreamliner First Flight", 
     "content": "The Boeing 787, featuring composite construction and improved fuel efficiency, made its first flight."},
    
    {"year": 2008, "era": "Modern Era", "title": "Turkish Airlines Joins Star Alliance", 
     "content": "Turkish Airlines became a member of Star Alliance, the world's largest airline alliance."},
    
    {"year": 2013, "era": "Modern Era", "title": "Airbus A350 First Flight", 
     "content": "The Airbus A350 XWB made its first flight, featuring composite construction and new Rolls-Royce Trent XWB engines."},
    
    {"year": 2019, "era": "Modern Era", "title": "Istanbul Airport Opens", 
     "content": "Istanbul Airport (IST) fully opened, replacing Atatürk Airport as Turkish Airlines' hub. Designed to be one of the world's largest airports."},
    
    {"year": 2020, "era": "Modern Era", "title": "COVID-19 Pandemic Impact", 
     "content": "The COVID-19 pandemic caused unprecedented disruption to global aviation, with passenger traffic dropping over 60%. The industry has since recovered."},
    
    {"year": 2024, "era": "Modern Era", "title": "Sustainable Aviation Focus", 
     "content": "Airlines increase commitment to Sustainable Aviation Fuel (SAF) and carbon reduction targets. Industry aims for net-zero emissions by 2050."},
]

# Convert to DataFrame
df = pd.DataFrame(history_data)

# Era filter
eras = df['era'].unique().tolist()
selected_era = st.selectbox("Filter by Era", ["All Eras"] + eras)

# Display timeline
if selected_era != "All Eras":
    filtered_df = df[df['era'] == selected_era]
else:
    filtered_df = df

current_era = ""
for _, row in filtered_df.iterrows():
    if row['era'] != current_era:
        current_era = row['era']
        st.markdown(f'<h2 class="era-header">🕐 {current_era}</h2>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="timeline-card">
        <div class="timeline-year">{row['year']}</div>
        <div class="timeline-title">{row['title']}</div>
        <div class="timeline-content">{row['content']}</div>
    </div>
    """, unsafe_allow_html=True)

# Interactive timeline chart
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📊 Visual Timeline")

fig = px.scatter(
    df,
    x="year",
    y="era",
    hover_name="title",
    hover_data={"year": True, "era": False},
    color="era",
    size_max=20,
    title="Aviation History Timeline"
)

fig.update_traces(marker=dict(size=15))
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white',
    height=400,
    xaxis=dict(
        title="Year",
        gridcolor='rgba(255,255,255,0.1)',
        range=[1775, 2030]
    ),
    yaxis=dict(
        title="Era",
        gridcolor='rgba(255,255,255,0.1)'
    ),
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# Gemini AI Additions Section
existing_years = df['year'].tolist()

render_ai_section(
    page_name='history',
    card_type='history',
    generate_func=gemini.get_history_additions,
    generate_args=(existing_years,),
    section_title="🤖 AI-Suggested Historical Events"
)

# Key interview topics
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="info-card">
    <h3 style="color: #c8102e; font-family: 'Orbitron', monospace;">💡 Key Topics for Interview</h3>
    <ul style="color: #d0d0d0; font-family: 'Rajdhani', sans-serif; line-height: 2;">
        <li><strong>Wright Brothers (1903):</strong> First powered, controlled flight - know the date and location</li>
        <li><strong>Turkish Airlines (1933):</strong> Founded as State Airlines Administration - one of the oldest airlines</li>
        <li><strong>DC-3 (1935):</strong> First commercially successful airliner</li>
        <li><strong>Jet Age (1958):</strong> Boeing 707 introduced modern jet travel</li>
        <li><strong>Boeing 747 (1970):</strong> First wide-body, democratized air travel</li>
        <li><strong>Fly-by-Wire (1988):</strong> A320 introduced digital flight controls</li>
        <li><strong>Composites (2007-2013):</strong> 787 and A350 brought composite construction</li>
        <li><strong>Istanbul Airport (2019):</strong> THY's new mega-hub</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Back button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("← Back to Home"):
    st.switch_page("app.py")

