"""
Turkish Airlines Fleet Page
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
    page_title="THY Fleet | Cadet Prep",
    page_icon="🛩️",
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
    
    .fleet-card {
        background: linear-gradient(145deg, rgba(30, 30, 50, 0.9), rgba(20, 20, 35, 0.95));
        border: 1px solid rgba(200, 16, 46, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
    }
    
    .manufacturer-header {
        font-family: 'Orbitron', monospace;
        font-size: 1.5rem;
        color: #fff;
        border-bottom: 2px solid #c8102e;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="page-header">🛩️ Turkish Airlines Fleet</h1>', unsafe_allow_html=True)

# Source info
st.markdown("""
<div style="text-align: center; padding: 0.5rem; background: rgba(200, 16, 46, 0.1); border-radius: 8px; margin-bottom: 1rem;">
    <span style="color: #888; font-size: 0.9rem;">
        📊 Official data from <a href="https://investor.turkishairlines.com/en/financial-and-operational/fleet" target="_blank" style="color: #c8102e;">THY Investor Relations</a> | Total: <strong style="color: #fff;">516 aircraft</strong>
    </span>
</div>
""", unsafe_allow_html=True)

# Fleet data - Updated from THY Investor Relations (January 2026)
# Source: https://investor.turkishairlines.com/en/financial-and-operational/fleet
# Total: 516 aircraft (142 Wide-body + 347 Narrow-body + 27 Cargo)

fleet_data = {
    "Manufacturer": ["Airbus", "Airbus", "Airbus", "Airbus", "Airbus",
                     "Boeing", "Boeing", "Boeing", "Boeing", "Boeing", "Boeing"],
    "Model": ["A319/A320/A321 (Classic)", "A320neo/A321neo", "A330-200/300", "A350-900", "A350F",
              "737-800/900", "737 MAX 8/9", "777-300ER", "787-9", "777F", "747-400F"],
    "Type": ["Narrow-body", "Narrow-body", "Wide-body", "Wide-body", "Freighter",
             "Narrow-body", "Narrow-body", "Wide-body", "Wide-body", "Freighter", "Freighter"],
    "Count": [101, 105, 49, 33, 4,
              99, 42, 34, 26, 17, 6],
    "Passengers": ["132-220", "165-240", "264-330", "329", "Cargo",
                   "151-189", "151-188", "349-377", "270-300", "Cargo", "Cargo"],
    "Range_km": [6100, 7400, 12500, 15000, 8700,
                 5700, 6500, 13650, 14000, 9200, 8230],
    "Status": ["Active", "Active", "Active", "Active", "Active",
               "Active", "Active", "Active", "Active", "Active", "Active"]
}

df = pd.DataFrame(fleet_data)

# Summary statistics
total_aircraft = df['Count'].sum()
narrow_body = df[df['Type'] == 'Narrow-body']['Count'].sum()
wide_body = df[df['Type'] == 'Wide-body']['Count'].sum()
freighter = df[df['Type'] == 'Freighter']['Count'].sum()

# Display summary cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Fleet", f"{total_aircraft}")
with col2:
    st.metric("Narrow-body", f"{narrow_body}")
with col3:
    st.metric("Wide-body", f"{wide_body}")
with col4:
    st.metric("Freighters", f"{freighter}")

st.markdown("<br>", unsafe_allow_html=True)

# Tabs for different views
tab1, tab2, tab3 = st.tabs(["📊 Fleet Overview", "📈 Charts", "📋 Detailed Table"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="fleet-card">
            <h3 class="manufacturer-header">✈️ Airbus Fleet</h3>
        </div>
        """, unsafe_allow_html=True)
        
        airbus_df = df[df['Manufacturer'] == 'Airbus'][['Model', 'Count', 'Type', 'Passengers']]
        st.dataframe(airbus_df, use_container_width=True, hide_index=True)
        
        airbus_total = df[df['Manufacturer'] == 'Airbus']['Count'].sum()
        st.info(f"**Total Airbus Aircraft: {airbus_total}**")
    
    with col2:
        st.markdown("""
        <div class="fleet-card">
            <h3 class="manufacturer-header">✈️ Boeing Fleet</h3>
        </div>
        """, unsafe_allow_html=True)
        
        boeing_df = df[df['Manufacturer'] == 'Boeing'][['Model', 'Count', 'Type', 'Passengers']]
        st.dataframe(boeing_df, use_container_width=True, hide_index=True)
        
        boeing_total = df[df['Manufacturer'] == 'Boeing']['Count'].sum()
        st.info(f"**Total Boeing Aircraft: {boeing_total}**")

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        # Pie chart by manufacturer
        manufacturer_counts = df.groupby('Manufacturer')['Count'].sum().reset_index()
        fig1 = px.pie(
            manufacturer_counts, 
            values='Count', 
            names='Manufacturer',
            title='Fleet by Manufacturer',
            color_discrete_sequence=['#c8102e', '#1e3a5f']
        )
        fig1.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            title_font_size=18
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Pie chart by type
        type_counts = df.groupby('Type')['Count'].sum().reset_index()
        fig2 = px.pie(
            type_counts, 
            values='Count', 
            names='Type',
            title='Fleet by Aircraft Type',
            color_discrete_sequence=['#c8102e', '#4a90d9', '#2ecc71']
        )
        fig2.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            title_font_size=18
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Bar chart of all models
    fig3 = px.bar(
        df.sort_values('Count', ascending=True), 
        x='Count', 
        y='Model',
        orientation='h',
        color='Manufacturer',
        title='Aircraft Count by Model',
        color_discrete_map={'Airbus': '#c8102e', 'Boeing': '#1e3a5f'}
    )
    fig3.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        title_font_size=18,
        height=500
    )
    st.plotly_chart(fig3, use_container_width=True)

with tab3:
    st.subheader("Complete Fleet Details")
    
    # Sortable complete table
    st.dataframe(
        df.sort_values('Count', ascending=False),
        use_container_width=True,
        hide_index=True,
        column_config={
            "Count": st.column_config.NumberColumn("Aircraft Count", format="%d"),
            "Range_km": st.column_config.NumberColumn("Range (km)", format="%d km"),
        }
    )

# Fleet Orders Section
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="fleet-card">
    <h3 class="manufacturer-header">📦 Upcoming Fleet Orders</h3>
</div>
""", unsafe_allow_html=True)

orders_data = {
    "Aircraft": ["Boeing 787-9", "Airbus A350-900", "Boeing 737 MAX 8", "Boeing 737 MAX 10", "Airbus A321neo"],
    "On Order": [25, 15, 40, 20, 20],
    "Expected Delivery": ["2024-2028", "2024-2027", "2024-2028", "2025-2028", "2024-2027"],
    "Notes": [
        "Long-haul expansion", 
        "Fleet modernization", 
        "Narrow-body refresh", 
        "Largest MAX variant",
        "Fuel-efficient single-aisle"
    ]
}
orders_df = pd.DataFrame(orders_data)
st.dataframe(orders_df, use_container_width=True, hide_index=True)

# Key Points for Interview
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="fleet-card">
    <h3 class="manufacturer-header">💡 Key Points for Interview</h3>
    <ul style="color: #d0d0d0; font-family: 'Rajdhani', sans-serif; line-height: 2;">
        <li><strong>Total Fleet:</strong> 516 aircraft (142 wide-body + 347 narrow-body + 27 cargo)</li>
        <li><strong>Fleet Strategy:</strong> Turkish Airlines operates a mixed Airbus/Boeing fleet for operational flexibility</li>
        <li><strong>Wide-body Fleet:</strong> 142 aircraft including 34 B777-300ER, 33 A350-900, 26 B787-9, 49 A330</li>
        <li><strong>Narrow-body Fleet:</strong> 347 aircraft - strong A320/A321neo family (206) and Boeing 737 family (141)</li>
        <li><strong>Fuel Efficiency:</strong> New deliveries focus on fuel-efficient aircraft (A321neo, 787, A350)</li>
        <li><strong>Cargo Operations:</strong> 27 dedicated freighters including 777F, 747-400F, and A350F for Turkish Cargo</li>
        <li><strong>Hub Advantage:</strong> Istanbul's geographic position enables one-stop connections to 60% of the world</li>
        <li><strong>Average Fleet Age:</strong> Approximately 8-9 years (relatively young fleet)</li>
    </ul>
    <p style="color: #888; font-size: 0.9rem; margin-top: 1rem;">
        📊 Source: <a href="https://investor.turkishairlines.com/en/financial-and-operational/fleet" target="_blank" style="color: #c8102e;">THY Investor Relations</a>
    </p>
</div>
""", unsafe_allow_html=True)

# AI Insights Section
fleet_summary = """
- Total Fleet: 516 aircraft
- Wide-body: 142 (B777-300ER: 34, A350-900: 33, B787-9: 26, A330: 49)
- Narrow-body: 347 (A321neo: 108, A321: 68, A320: 30, B737 MAX 8/9: 76, B737-800/900: 65)
- Cargo: 27 freighters (B777F: 7, A350F: 3, B747-400F: 4, A330-200F: 10, A321F: 3)
- Hub: Istanbul Airport (IST)
"""

render_ai_section(
    page_name='fleet',
    card_type='insight',
    generate_func=gemini.get_fleet_insights,
    generate_args=(fleet_summary,),
    section_title="🤖 AI Fleet Insights"
)

# Back button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("← Back to Home"):
    st.switch_page("app.py")

