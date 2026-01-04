"""
Turkish Airlines Destinations Page with Interactive World Map
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
    page_title="THY Destinations | Cadet Prep",
    page_icon="🌍",
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
    
    .info-card {
        background: linear-gradient(145deg, rgba(30, 30, 50, 0.9), rgba(20, 20, 35, 0.95));
        border: 1px solid rgba(200, 16, 46, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="page-header">🌍 Turkish Airlines Destinations</h1>', unsafe_allow_html=True)

# Official stats from THY Investor Relations (January 2026)
# Source: https://investor.turkishairlines.com/en/financial-and-operational/flight-network
st.markdown("""
<div style="text-align: center; padding: 0.5rem; background: rgba(200, 16, 46, 0.1); border-radius: 8px; margin-bottom: 1rem;">
    <span style="color: #888; font-size: 0.9rem;">
        📊 Official data from <a href="https://investor.turkishairlines.com/en/financial-and-operational/flight-network" target="_blank" style="color: #c8102e;">THY Investor Relations</a>
    </span>
</div>
""", unsafe_allow_html=True)

# Destination data by country with ISO codes for map (sample of major countries)
destinations_data = {
    "Country": ["Turkey", "Germany", "United States", "United Kingdom", "France", "Italy", 
                "Russia", "Saudi Arabia", "UAE", "Netherlands", "Spain", "Switzerland",
                "Austria", "Belgium", "Poland", "Ukraine", "Greece", "Morocco", "Egypt",
                "South Africa", "Nigeria", "Kenya", "Ethiopia", "Algeria", "Tunisia",
                "India", "Pakistan", "China", "Japan", "South Korea", "Thailand",
                "Indonesia", "Malaysia", "Singapore", "Australia", "Brazil", "Argentina",
                "Mexico", "Canada", "Iran", "Iraq", "Kazakhstan", "Azerbaijan", "Georgia",
                "Israel", "Jordan", "Lebanon", "Kuwait", "Qatar", "Bahrain", "Oman",
                "Libya", "Senegal", "Ghana", "Tanzania", "Rwanda", "Uganda", "Mozambique",
                "Mauritius", "Madagascar", "Seychelles", "Maldives", "Sri Lanka", "Bangladesh",
                "Vietnam", "Philippines", "Hong Kong", "Taiwan", "Mongolia", "Uzbekistan",
                "Turkmenistan", "Tajikistan", "Kyrgyzstan", "Afghanistan", "Nepal",
                "Colombia", "Chile", "Peru", "Panama", "Cuba", "Dominican Republic",
                "Portugal", "Ireland", "Norway", "Sweden", "Denmark", "Finland",
                "Czech Republic", "Hungary", "Romania", "Bulgaria", "Serbia", "Croatia",
                "Slovenia", "Bosnia", "Montenegro", "Albania", "North Macedonia", "Kosovo",
                "Cyprus", "Malta", "Luxembourg", "Iceland"],
    "ISO": ["TUR", "DEU", "USA", "GBR", "FRA", "ITA", 
            "RUS", "SAU", "ARE", "NLD", "ESP", "CHE",
            "AUT", "BEL", "POL", "UKR", "GRC", "MAR", "EGY",
            "ZAF", "NGA", "KEN", "ETH", "DZA", "TUN",
            "IND", "PAK", "CHN", "JPN", "KOR", "THA",
            "IDN", "MYS", "SGP", "AUS", "BRA", "ARG",
            "MEX", "CAN", "IRN", "IRQ", "KAZ", "AZE", "GEO",
            "ISR", "JOR", "LBN", "KWT", "QAT", "BHR", "OMN",
            "LBY", "SEN", "GHA", "TZA", "RWA", "UGA", "MOZ",
            "MUS", "MDG", "SYC", "MDV", "LKA", "BGD",
            "VNM", "PHL", "HKG", "TWN", "MNG", "UZB",
            "TKM", "TJK", "KGZ", "AFG", "NPL",
            "COL", "CHL", "PER", "PAN", "CUB", "DOM",
            "PRT", "IRL", "NOR", "SWE", "DNK", "FIN",
            "CZE", "HUN", "ROU", "BGR", "SRB", "HRV",
            "SVN", "BIH", "MNE", "ALB", "MKD", "XKX",
            "CYP", "MLT", "LUX", "ISL"],
    "Destinations": [53, 12, 13, 6, 5, 8, 
                     8, 6, 3, 2, 4, 4,
                     2, 2, 3, 4, 4, 5, 3,
                     3, 3, 2, 2, 3, 2,
                     10, 5, 7, 4, 2, 2,
                     4, 2, 1, 2, 3, 2,
                     3, 4, 5, 5, 4, 2, 2,
                     2, 1, 1, 1, 1, 1, 1,
                     2, 1, 1, 2, 1, 1, 1,
                     1, 1, 1, 1, 1, 2,
                     2, 2, 1, 1, 1, 2,
                     1, 1, 1, 1, 1,
                     2, 1, 1, 1, 1, 1,
                     2, 1, 2, 2, 2, 1,
                     1, 1, 2, 2, 1, 2,
                     1, 1, 1, 1, 1, 1,
                     2, 1, 1, 1],
    "Region": ["Europe", "Europe", "Americas", "Europe", "Europe", "Europe",
               "Europe", "Middle East", "Middle East", "Europe", "Europe", "Europe",
               "Europe", "Europe", "Europe", "Europe", "Europe", "Africa", "Africa",
               "Africa", "Africa", "Africa", "Africa", "Africa", "Africa",
               "Asia", "Asia", "Asia", "Asia", "Asia", "Asia",
               "Asia", "Asia", "Asia", "Oceania", "Americas", "Americas",
               "Americas", "Americas", "Middle East", "Middle East", "Asia", "Europe", "Europe",
               "Middle East", "Middle East", "Middle East", "Middle East", "Middle East", "Middle East", "Middle East",
               "Africa", "Africa", "Africa", "Africa", "Africa", "Africa", "Africa",
               "Africa", "Africa", "Africa", "Asia", "Asia", "Asia",
               "Asia", "Asia", "Asia", "Asia", "Asia", "Asia",
               "Asia", "Asia", "Asia", "Asia", "Asia",
               "Americas", "Americas", "Americas", "Americas", "Americas", "Americas",
               "Europe", "Europe", "Europe", "Europe", "Europe", "Europe",
               "Europe", "Europe", "Europe", "Europe", "Europe", "Europe",
               "Europe", "Europe", "Europe", "Europe", "Europe", "Europe",
               "Europe", "Europe", "Europe", "Europe"],
    "Weekly_Flights": [500, 140, 98, 70, 56, 70,
                       84, 70, 56, 35, 42, 49,
                       28, 28, 35, 42, 56, 42, 35,
                       28, 21, 21, 21, 28, 21,
                       70, 35, 56, 42, 28, 28,
                       28, 21, 21, 21, 21, 14,
                       28, 35, 35, 42, 28, 21, 28,
                       21, 21, 21, 21, 21, 14, 14,
                       14, 7, 7, 14, 7, 7, 7,
                       7, 7, 7, 14, 14, 14,
                       14, 14, 14, 7, 7, 14,
                       7, 7, 7, 7, 7,
                       14, 7, 7, 7, 7, 7,
                       21, 14, 21, 28, 28, 14,
                       14, 14, 28, 21, 14, 21,
                       14, 14, 7, 14, 7, 7,
                       21, 14, 7, 7]
}

df = pd.DataFrame(destinations_data)

# Summary stats - Official figures from THY Investor Relations
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Countries Served", "132")
with col2:
    st.metric("Total Destinations", "356")
with col3:
    st.metric("Domestic", "53")
with col4:
    st.metric("International", "303")
with col5:
    regions = df['Region'].nunique()
    st.metric("Regions", f"{regions}")

st.markdown("<br>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["🗺️ World Map", "📊 By Region", "📋 Full List"])

with tab1:
    st.subheader("Interactive Destination Map")
    
    # Create choropleth map
    fig = px.choropleth(
        df,
        locations="ISO",
        color="Destinations",
        hover_name="Country",
        hover_data={"Weekly_Flights": True, "Region": True, "ISO": False},
        color_continuous_scale=[
            [0, "#1a1a2e"],
            [0.3, "#4a2040"],
            [0.6, "#8a1538"],
            [1, "#c8102e"]
        ],
        title="Turkish Airlines Global Network"
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        geo=dict(
            bgcolor='rgba(0,0,0,0)',
            showframe=False,
            showcoastlines=True,
            coastlinecolor='#333',
            showland=True,
            landcolor='#1a1a2e',
            showocean=True,
            oceancolor='#0a0a15',
            showlakes=False,
            projection_type='natural earth'
        ),
        font_color='white',
        title_font_size=18,
        height=600,
        margin=dict(l=0, r=0, t=50, b=0)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Bubble map alternative
    st.subheader("Flight Frequency by Country")
    
    # Add approximate coordinates for bubble map
    coords = {
        "Turkey": (39.0, 35.0), "Germany": (51.0, 10.0), "United States": (38.0, -97.0),
        "United Kingdom": (54.0, -2.0), "France": (46.0, 2.0), "Italy": (42.0, 12.0),
        "Russia": (60.0, 100.0), "Saudi Arabia": (24.0, 45.0), "UAE": (24.0, 54.0),
        "Netherlands": (52.0, 5.0), "Spain": (40.0, -4.0), "Switzerland": (47.0, 8.0),
        "India": (20.0, 77.0), "China": (35.0, 105.0), "Japan": (36.0, 138.0),
        "South Korea": (36.0, 128.0), "Brazil": (-14.0, -51.0), "Australia": (-25.0, 133.0)
    }
    
    df_coords = df.copy()
    df_coords['Lat'] = df_coords['Country'].map(lambda x: coords.get(x, (0, 0))[0])
    df_coords['Lon'] = df_coords['Country'].map(lambda x: coords.get(x, (0, 0))[1])
    df_coords = df_coords[df_coords['Lat'] != 0]
    
    fig2 = px.scatter_geo(
        df_coords,
        lat='Lat',
        lon='Lon',
        size='Weekly_Flights',
        color='Region',
        hover_name='Country',
        size_max=40,
        title="Weekly Flight Frequency"
    )
    
    fig2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        geo=dict(
            bgcolor='rgba(0,0,0,0)',
            showframe=False,
            showcoastlines=True,
            coastlinecolor='#333',
            showland=True,
            landcolor='#1a1a2e',
            showocean=True,
            oceancolor='#0a0a15',
            projection_type='natural earth'
        ),
        font_color='white',
        height=500
    )
    
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("Destinations by Region")
    
    # Regional summary
    region_summary = df.groupby('Region').agg({
        'Country': 'count',
        'Destinations': 'sum',
        'Weekly_Flights': 'sum'
    }).reset_index()
    region_summary.columns = ['Region', 'Countries', 'Total Destinations', 'Weekly Flights']
    region_summary = region_summary.sort_values('Total Destinations', ascending=False)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(
            region_summary,
            x='Region',
            y='Total Destinations',
            color='Region',
            title='Destinations by Region'
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.pie(
            region_summary,
            values='Weekly Flights',
            names='Region',
            title='Weekly Flights Distribution'
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.dataframe(region_summary, use_container_width=True, hide_index=True)

with tab3:
    st.subheader("Complete Destination List")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        region_filter = st.multiselect("Filter by Region", options=df['Region'].unique())
    with col2:
        sort_by = st.selectbox("Sort by", ["Destinations", "Weekly_Flights", "Country"])
    
    # Apply filters
    filtered_df = df.copy()
    if region_filter:
        filtered_df = filtered_df[filtered_df['Region'].isin(region_filter)]
    
    filtered_df = filtered_df.sort_values(sort_by, ascending=(sort_by == "Country"))
    
    st.dataframe(
        filtered_df[['Country', 'Region', 'Destinations', 'Weekly_Flights']],
        use_container_width=True,
        hide_index=True,
        column_config={
            "Weekly_Flights": st.column_config.NumberColumn("Weekly Flights", format="%d")
        }
    )

# Key facts
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="info-card">
    <h3 style="color: #c8102e; font-family: 'Orbitron', monospace;">💡 Key Points for Interview</h3>
    <ul style="color: #d0d0d0; font-family: 'Rajdhani', sans-serif; line-height: 2;">
        <li><strong>Network Leader:</strong> Turkish Airlines flies to <strong>132 countries</strong> - more than any other airline in the world</li>
        <li><strong>Total Network:</strong> 356 destinations (53 domestic + 303 international)</li>
        <li><strong>Istanbul Hub:</strong> Strategic location enables connections between Europe, Asia, Africa, and Americas - Istanbul is within 3-hour flight of 1.5 billion people</li>
        <li><strong>Europe Focus:</strong> Largest regional network due to geographic proximity</li>
        <li><strong>Africa Expansion:</strong> THY serves more African destinations than any other non-African carrier</li>
        <li><strong>Geographic Advantage:</strong> Istanbul's position allows one-stop connections to most of the world</li>
        <li><strong>Star Alliance:</strong> Member since 2008, providing connectivity to 1,300+ airports worldwide</li>
    </ul>
    <p style="color: #888; font-size: 0.9rem; margin-top: 1rem;">
        📊 Source: <a href="https://investor.turkishairlines.com/en/financial-and-operational/flight-network" target="_blank" style="color: #c8102e;">THY Investor Relations</a>
    </p>
</div>
""", unsafe_allow_html=True)

# AI Insights Section
destinations_summary = """
- Total Destinations: 356 (53 domestic, 303 international)
- Countries Served: 132 countries
- Hub: Istanbul Airport (IST) - world's largest airport terminal
- Key Markets: Europe (dominant), Middle East, Africa, Asia, Americas
- Star Alliance member since 2008
- Unique Advantage: Istanbul's geographic position allows one-stop connections to most of the world
"""

render_ai_section(
    page_name='destinations',
    card_type='insight',
    generate_func=gemini.get_destinations_insights,
    generate_args=(destinations_summary,),
    section_title="🤖 AI Destinations Insights"
)

# Back button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("← Back to Home"):
    st.switch_page("app.py")

