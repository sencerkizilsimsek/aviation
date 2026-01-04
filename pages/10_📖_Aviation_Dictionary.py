"""
Comprehensive Aviation Dictionary for Pilot Candidates
"""

import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config import config
from utils.gemini_helper import gemini, render_ai_section, render_ai_card, render_ai_disclaimer

st.set_page_config(
    page_title="Aviation Dictionary | Cadet Prep",
    page_icon="📖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
    
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
        font-size: 1.1rem;
        color: #888;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .term-card {
        background: linear-gradient(145deg, rgba(30, 30, 50, 0.9), rgba(20, 20, 35, 0.95));
        border: 1px solid rgba(200, 16, 46, 0.3);
        border-radius: 12px;
        padding: 1.2rem;
        margin: 0.8rem 0;
        transition: all 0.3s ease;
    }
    
    .term-card:hover {
        border-color: rgba(200, 16, 46, 0.6);
        box-shadow: 0 8px 30px rgba(200, 16, 46, 0.15);
    }
    
    .term-abbrev {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.4rem;
        font-weight: 600;
        color: #c8102e;
        margin-bottom: 0.3rem;
    }
    
    .term-full {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.1rem;
        color: #fff;
        margin-bottom: 0.5rem;
    }
    
    .term-definition {
        font-family: 'Rajdhani', sans-serif;
        font-size: 0.95rem;
        color: #b0b0b0;
        line-height: 1.6;
    }
    
    .category-badge {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        background: rgba(200, 16, 46, 0.15);
        border: 1px solid rgba(200, 16, 46, 0.3);
        border-radius: 15px;
        font-size: 0.75rem;
        color: #c8102e;
        margin-right: 0.5rem;
        margin-top: 0.5rem;
    }
    
    .difficulty-easy {
        background: rgba(46, 213, 115, 0.15);
        border-color: rgba(46, 213, 115, 0.3);
        color: #2ed573;
    }
    
    .difficulty-medium {
        background: rgba(255, 165, 2, 0.15);
        border-color: rgba(255, 165, 2, 0.3);
        color: #ffa502;
    }
    
    .difficulty-advanced {
        background: rgba(255, 71, 87, 0.15);
        border-color: rgba(255, 71, 87, 0.3);
        color: #ff4757;
    }
    
    .stats-card {
        background: linear-gradient(145deg, rgba(30, 30, 50, 0.9), rgba(20, 20, 35, 0.95));
        border: 1px solid rgba(200, 16, 46, 0.3);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }
    
    .filter-section {
        background: rgba(20, 20, 40, 0.8);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Comprehensive Aviation Dictionary Data
# Categories: Abbreviations, V-Speeds, Navigation, Meteorology, Aircraft Systems, 
#             Aerodynamics, Regulations, Communications, Instruments, Emergencies,
#             Flight Operations, Airport, ATC, Human Factors

dictionary_data = [
    # ==================== ABBREVIATIONS - GENERAL ====================
    {"term": "ATC", "full_name": "Air Traffic Control", "category": "ATC", "difficulty": "Basic",
     "definition": "Ground-based personnel and equipment that direct aircraft movements on the ground and in the air. ATC provides separation services, traffic information, and navigation assistance."},
    
    {"term": "IFR", "full_name": "Instrument Flight Rules", "category": "Regulations", "difficulty": "Basic",
     "definition": "Rules and regulations for flying aircraft by reference to instruments only. Required when visibility is below VFR minimums or when flying in controlled airspace above certain altitudes."},
    
    {"term": "VFR", "full_name": "Visual Flight Rules", "category": "Regulations", "difficulty": "Basic",
     "definition": "Rules that permit a pilot to fly in weather conditions clear enough to see and avoid other aircraft and obstacles. Requires minimum visibility and cloud clearance."},
    
    {"term": "IMC", "full_name": "Instrument Meteorological Conditions", "category": "Meteorology", "difficulty": "Basic",
     "definition": "Weather conditions that require pilots to fly primarily by reference to instruments. Visibility below 3 statute miles or ceiling below 1000 feet AGL."},
    
    {"term": "VMC", "full_name": "Visual Meteorological Conditions", "category": "Meteorology", "difficulty": "Basic",
     "definition": "Weather conditions in which VFR flight is permitted. In aviation, VMC also refers to Minimum Control Speed with critical engine inoperative."},
    
    {"term": "PIC", "full_name": "Pilot in Command", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "The pilot responsible for the operation and safety of an aircraft during flight. Has final authority and responsibility for the flight."},
    
    {"term": "SIC", "full_name": "Second in Command", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "A pilot who is designated as second in command of an aircraft during flight. Also known as First Officer or Co-pilot in airline operations."},
    
    {"term": "FO", "full_name": "First Officer", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "The second pilot in command on an airline flight. Sits in the right seat and assists the Captain."},
    
    {"term": "CPL", "full_name": "Commercial Pilot License", "category": "Regulations", "difficulty": "Basic",
     "definition": "A pilot license that allows the holder to act as pilot in command of an aircraft for compensation or hire."},
    
    {"term": "ATPL", "full_name": "Airline Transport Pilot License", "category": "Regulations", "difficulty": "Basic",
     "definition": "The highest level of pilot certificate. Required to act as PIC of scheduled airline aircraft."},
    
    {"term": "PPL", "full_name": "Private Pilot License", "category": "Regulations", "difficulty": "Basic",
     "definition": "A pilot license that allows the holder to fly as PIC but not for compensation or hire."},
    
    {"term": "IR", "full_name": "Instrument Rating", "category": "Regulations", "difficulty": "Basic",
     "definition": "A rating added to a pilot license that allows flight under IFR conditions."},
    
    {"term": "MEP", "full_name": "Multi-Engine Piston", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Aircraft powered by more than one piston engine. Requires additional training and rating."},
    
    {"term": "SEP", "full_name": "Single-Engine Piston", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Aircraft powered by a single piston engine. The most common type for training."},
    
    {"term": "ICAO", "full_name": "International Civil Aviation Organization", "category": "Regulations", "difficulty": "Basic",
     "definition": "A United Nations specialized agency that sets international standards and regulations for civil aviation."},
    
    {"term": "IATA", "full_name": "International Air Transport Association", "category": "Regulations", "difficulty": "Basic",
     "definition": "Trade association of the world's airlines. Sets standards for airline operations and ticket sales."},
    
    {"term": "FAA", "full_name": "Federal Aviation Administration", "category": "Regulations", "difficulty": "Basic",
     "definition": "The national aviation authority of the United States, responsible for regulation and oversight of civil aviation."},
    
    {"term": "EASA", "full_name": "European Union Aviation Safety Agency", "category": "Regulations", "difficulty": "Basic",
     "definition": "The European Union agency responsible for civil aviation safety."},
    
    {"term": "SHGM", "full_name": "Sivil Havacılık Genel Müdürlüğü", "category": "Regulations", "difficulty": "Basic",
     "definition": "Directorate General of Civil Aviation of Turkey. The Turkish civil aviation authority."},
    
    # ==================== V-SPEEDS ====================
    {"term": "V1", "full_name": "Takeoff Decision Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The maximum speed at which a takeoff can be safely aborted. After V1, the takeoff must continue even if an engine fails. Critical decision point."},
    
    {"term": "VR", "full_name": "Rotation Speed", "category": "V-Speeds", "difficulty": "Basic",
     "definition": "The speed at which the pilot begins to apply back pressure to rotate the aircraft nose up for takeoff. The aircraft becomes airborne shortly after."},
    
    {"term": "V2", "full_name": "Takeoff Safety Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The minimum speed that must be maintained after an engine failure during takeoff to ensure adequate climb performance."},
    
    {"term": "VX", "full_name": "Best Angle of Climb Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The speed that produces the greatest altitude gain over a given horizontal distance. Used for obstacle clearance after takeoff."},
    
    {"term": "VY", "full_name": "Best Rate of Climb Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The speed that produces the greatest altitude gain per unit of time. Used for normal climb operations."},
    
    {"term": "VYSE", "full_name": "Best Single-Engine Rate of Climb Speed", "category": "V-Speeds", "difficulty": "Advanced",
     "definition": "The speed that provides the best rate of climb with one engine inoperative. Marked with a blue radial line on the airspeed indicator (Blue Line)."},
    
    {"term": "VXSE", "full_name": "Best Single-Engine Angle of Climb Speed", "category": "V-Speeds", "difficulty": "Advanced",
     "definition": "The speed that provides the best angle of climb with one engine inoperative. Used for obstacle clearance after engine failure."},
    
    {"term": "VMC", "full_name": "Minimum Control Speed (Airborne)", "category": "V-Speeds", "difficulty": "Advanced",
     "definition": "The minimum speed at which directional control can be maintained with the critical engine inoperative. Marked with a red radial line. Flight below VMC with engine failure risks loss of control."},
    
    {"term": "VMCG", "full_name": "Minimum Control Speed (Ground)", "category": "V-Speeds", "difficulty": "Advanced",
     "definition": "The minimum speed during takeoff run at which directional control can be maintained on the ground with the critical engine inoperative."},
    
    {"term": "VMCA", "full_name": "Minimum Control Speed (Air)", "category": "V-Speeds", "difficulty": "Advanced",
     "definition": "Same as VMC. The air subscript distinguishes it from ground minimum control speed."},
    
    {"term": "VA", "full_name": "Maneuvering Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The maximum speed at which full deflection of any single flight control can be applied without causing structural damage. Decreases with lower weight."},
    
    {"term": "VNE", "full_name": "Never Exceed Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The maximum speed the aircraft should ever reach. Exceeding VNE may cause structural failure. Marked with a red radial line."},
    
    {"term": "VNO", "full_name": "Maximum Structural Cruising Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The maximum speed for normal operations. Do not exceed VNO except in smooth air. Top of the green arc on the airspeed indicator."},
    
    {"term": "VFE", "full_name": "Maximum Flap Extended Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The maximum speed at which flaps can be extended. May vary based on flap setting. Top of the white arc."},
    
    {"term": "VLE", "full_name": "Maximum Landing Gear Extended Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The maximum speed at which the aircraft can be flown with the landing gear extended."},
    
    {"term": "VLO", "full_name": "Maximum Landing Gear Operating Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The maximum speed at which the landing gear can be extended or retracted. May be lower than VLE due to door loads."},
    
    {"term": "VS0", "full_name": "Stall Speed (Landing Configuration)", "category": "V-Speeds", "difficulty": "Basic",
     "definition": "The stall speed in landing configuration (gear down, flaps extended, power off). Bottom of the white arc. Lower than VS1."},
    
    {"term": "VS1", "full_name": "Stall Speed (Clean Configuration)", "category": "V-Speeds", "difficulty": "Basic",
     "definition": "The stall speed in clean configuration (gear up, flaps retracted, power off). Bottom of the green arc."},
    
    {"term": "VREF", "full_name": "Reference Landing Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The target speed for crossing the runway threshold during landing. Typically 1.3 x VS0 plus adjustments for wind."},
    
    {"term": "VAPP", "full_name": "Approach Speed", "category": "V-Speeds", "difficulty": "Intermediate",
     "definition": "The target speed during the approach phase before reaching VREF. Includes corrections for wind and configuration."},
    
    {"term": "VSSE", "full_name": "Safe Single-Engine Speed", "category": "V-Speeds", "difficulty": "Advanced",
     "definition": "The minimum speed for intentionally rendering an engine inoperative during training. Provides safety margin above VMC."},
    
    # ==================== NAVIGATION ====================
    {"term": "VOR", "full_name": "VHF Omnidirectional Range", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "A ground-based radio navigation system that provides bearing information to/from the station. Forms the basis of airways system."},
    
    {"term": "NDB", "full_name": "Non-Directional Beacon", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "A ground-based radio transmitter that broadcasts in all directions. Used with ADF for navigation."},
    
    {"term": "ADF", "full_name": "Automatic Direction Finder", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "Aircraft equipment that displays the bearing to an NDB station. Points toward the station."},
    
    {"term": "DME", "full_name": "Distance Measuring Equipment", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "Equipment that measures the slant range distance between aircraft and a ground station. Often paired with VOR."},
    
    {"term": "ILS", "full_name": "Instrument Landing System", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "A precision approach system providing lateral (localizer) and vertical (glideslope) guidance for landing."},
    
    {"term": "LOC", "full_name": "Localizer", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "The lateral guidance component of ILS. Provides left/right guidance to the runway centerline."},
    
    {"term": "GS", "full_name": "Glideslope", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "The vertical guidance component of ILS. Typically provides a 3-degree descent path to the runway."},
    
    {"term": "GPS", "full_name": "Global Positioning System", "category": "Navigation", "difficulty": "Basic",
     "definition": "Satellite-based navigation system providing accurate position, velocity, and time information worldwide."},
    
    {"term": "GNSS", "full_name": "Global Navigation Satellite System", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "General term for satellite navigation systems including GPS (US), GLONASS (Russia), Galileo (EU), and BeiDou (China)."},
    
    {"term": "RNAV", "full_name": "Area Navigation", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "Navigation method allowing aircraft to fly any desired flight path using onboard systems. Not limited to flying to/from ground stations."},
    
    {"term": "RNP", "full_name": "Required Navigation Performance", "category": "Navigation", "difficulty": "Advanced",
     "definition": "RNAV with onboard performance monitoring and alerting. Specifies accuracy requirements (e.g., RNP 0.3 = within 0.3 nm 95% of time)."},
    
    {"term": "WAAS", "full_name": "Wide Area Augmentation System", "category": "Navigation", "difficulty": "Advanced",
     "definition": "A system that improves GPS accuracy and integrity for aviation use. Enables GPS approaches to near-ILS precision."},
    
    {"term": "FMS", "full_name": "Flight Management System", "category": "Navigation", "difficulty": "Advanced",
     "definition": "Computerized system that automates navigation, performance calculations, and flight planning. Core of modern aircraft automation."},
    
    {"term": "CDI", "full_name": "Course Deviation Indicator", "category": "Instruments", "difficulty": "Intermediate",
     "definition": "Instrument display showing aircraft position relative to a selected course. Needle deflection indicates correction needed."},
    
    {"term": "HSI", "full_name": "Horizontal Situation Indicator", "category": "Instruments", "difficulty": "Intermediate",
     "definition": "Combined heading indicator and CDI. Shows aircraft heading and navigation information on a single instrument."},
    
    {"term": "OBS", "full_name": "Omni-Bearing Selector", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "Control knob used to select the desired radial on a VOR indicator."},
    
    {"term": "MEA", "full_name": "Minimum En Route Altitude", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "The lowest altitude on an airway that ensures adequate signal reception and obstacle clearance."},
    
    {"term": "MOCA", "full_name": "Minimum Obstruction Clearance Altitude", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "The lowest altitude providing obstacle clearance but with navigation signal only within 22nm of a VOR."},
    
    {"term": "MDA", "full_name": "Minimum Descent Altitude", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "The lowest altitude to which descent is authorized during a non-precision approach without visual contact."},
    
    {"term": "DA/DH", "full_name": "Decision Altitude/Decision Height", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "The altitude/height at which a missed approach must be initiated if the runway is not in sight during a precision approach."},
    
    {"term": "MSA", "full_name": "Minimum Safe Altitude", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "The lowest altitude within a specified radius of a navigation aid that provides 1000ft obstacle clearance."},
    
    # ==================== METEOROLOGY ====================
    {"term": "METAR", "full_name": "Meteorological Aerodrome Report", "category": "Meteorology", "difficulty": "Basic",
     "definition": "A routine weather observation report for a specific airport. Issued every 30-60 minutes. Standard format worldwide."},
    
    {"term": "TAF", "full_name": "Terminal Aerodrome Forecast", "category": "Meteorology", "difficulty": "Basic",
     "definition": "A weather forecast for a specific airport, typically covering 24-30 hours. Predicts wind, visibility, clouds, and significant weather."},
    
    {"term": "ATIS", "full_name": "Automatic Terminal Information Service", "category": "Communications", "difficulty": "Basic",
     "definition": "Continuous broadcast of recorded airport information including weather, active runways, and NOTAMs. Updated hourly or when conditions change."},
    
    {"term": "SIGMET", "full_name": "Significant Meteorological Information", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "Weather advisory for significant hazards affecting all aircraft: severe turbulence, icing, thunderstorms, volcanic ash."},
    
    {"term": "AIRMET", "full_name": "Airman's Meteorological Information", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "Weather advisory for conditions hazardous to smaller aircraft: moderate turbulence, icing, low ceilings/visibility, mountain obscuration."},
    
    {"term": "PIREP", "full_name": "Pilot Report", "category": "Meteorology", "difficulty": "Basic",
     "definition": "A report of actual weather conditions encountered by pilots in flight. Includes turbulence, icing, cloud tops, visibility."},
    
    {"term": "QNH", "full_name": "Query: Nautical Height", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "Altimeter setting that shows altitude above mean sea level. Standard setting for approach and landing."},
    
    {"term": "QFE", "full_name": "Query: Field Elevation", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "Altimeter setting that shows height above the airport. Altimeter reads zero on the runway."},
    
    {"term": "QNE", "full_name": "Query: Nautical Elevation", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "Standard pressure setting (1013.25 hPa / 29.92 inHg). Used above transition altitude for flight levels."},
    
    {"term": "ISA", "full_name": "International Standard Atmosphere", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "Standard atmospheric model: 15°C at sea level, lapse rate of 2°C per 1000ft, pressure 1013.25 hPa. Used for performance calculations."},
    
    {"term": "OAT", "full_name": "Outside Air Temperature", "category": "Meteorology", "difficulty": "Basic",
     "definition": "The temperature of the air outside the aircraft. Critical for performance calculations and icing assessment."},
    
    {"term": "DA", "full_name": "Density Altitude", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "Pressure altitude corrected for non-standard temperature. Indicates aircraft performance capability. High DA = reduced performance."},
    
    {"term": "PA", "full_name": "Pressure Altitude", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "The altitude indicated when the altimeter is set to 29.92 inHg (1013.25 hPa). Used for standardized altitude above transition."},
    
    {"term": "TA", "full_name": "Transition Altitude", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "The altitude below which altitude is referenced to QNH (local pressure). Above this, switch to standard pressure (flight levels)."},
    
    {"term": "TL", "full_name": "Transition Level", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "The lowest flight level available for use above the transition altitude."},
    
    {"term": "CB", "full_name": "Cumulonimbus", "category": "Meteorology", "difficulty": "Basic",
     "definition": "Thunderstorm cloud. Characterized by severe turbulence, lightning, hail, heavy rain, and potential for microbursts. Avoid by at least 20nm."},
    
    {"term": "TCU", "full_name": "Towering Cumulus", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "A cumulus cloud showing significant vertical development. May develop into CB. Indicates instability."},
    
    {"term": "CAT", "full_name": "Clear Air Turbulence", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "Turbulence occurring in clear air, usually at high altitudes near jet streams. Cannot be detected by radar."},
    
    {"term": "LLWS", "full_name": "Low Level Wind Shear", "category": "Meteorology", "difficulty": "Advanced",
     "definition": "A sudden change in wind speed/direction at low altitude. Extremely hazardous during takeoff and landing. Can cause loss of control."},
    
    # ==================== AIRCRAFT SYSTEMS ====================
    {"term": "APU", "full_name": "Auxiliary Power Unit", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Small gas turbine engine providing electrical power and bleed air when main engines are not running. Used for ground operations and engine start."},
    
    {"term": "GPU", "full_name": "Ground Power Unit", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "External power source providing electrical power to aircraft on the ground."},
    
    {"term": "FADEC", "full_name": "Full Authority Digital Engine Control", "category": "Aircraft Systems", "difficulty": "Advanced",
     "definition": "Computer system with complete control over engine operation. Optimizes performance, protects engine limits. Single-lever power control."},
    
    {"term": "EGT", "full_name": "Exhaust Gas Temperature", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Temperature of gases leaving the engine. Critical limit indicator. High EGT indicates potential engine damage or incorrect operation."},
    
    {"term": "CHT", "full_name": "Cylinder Head Temperature", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Temperature of engine cylinder heads in piston engines. Monitored to prevent overheating and ensure proper cooling."},
    
    {"term": "ITT", "full_name": "Interstage Turbine Temperature", "category": "Aircraft Systems", "difficulty": "Advanced",
     "definition": "Temperature measured between turbine stages in turbine engines. Primary engine temperature limit."},
    
    {"term": "N1", "full_name": "Low Pressure Compressor Speed", "category": "Aircraft Systems", "difficulty": "Advanced",
     "definition": "The rotational speed of the low-pressure (fan) section of a turbofan engine, expressed as percentage of maximum."},
    
    {"term": "N2", "full_name": "High Pressure Compressor Speed", "category": "Aircraft Systems", "difficulty": "Advanced",
     "definition": "The rotational speed of the high-pressure compressor section, expressed as percentage of maximum."},
    
    {"term": "EPR", "full_name": "Engine Pressure Ratio", "category": "Aircraft Systems", "difficulty": "Advanced",
     "definition": "Ratio of turbine discharge pressure to compressor inlet pressure. Used as thrust indicator on some engines."},
    
    {"term": "TOGA", "full_name": "Takeoff/Go-Around", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Maximum thrust setting used for takeoff and go-around maneuvers. Also refers to autothrottle mode."},
    
    {"term": "FLEX", "full_name": "Flexible Takeoff Thrust", "category": "Aircraft Systems", "difficulty": "Advanced",
     "definition": "Reduced thrust takeoff based on assumed temperature higher than actual. Reduces engine wear when full thrust not required."},
    
    {"term": "TCAS", "full_name": "Traffic Collision Avoidance System", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Independent system that detects nearby aircraft and provides resolution advisories (climb/descend) to prevent collision."},
    
    {"term": "GPWS", "full_name": "Ground Proximity Warning System", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "System that warns pilots of unsafe proximity to terrain or obstacles. Older technology replaced by EGPWS."},
    
    {"term": "EGPWS", "full_name": "Enhanced Ground Proximity Warning System", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Advanced GPWS with terrain database. Provides predictive terrain warnings and enhanced situational awareness."},
    
    {"term": "TAWS", "full_name": "Terrain Awareness and Warning System", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Generic term for terrain warning systems including GPWS and EGPWS. Required equipment for many operations."},
    
    {"term": "FBW", "full_name": "Fly-By-Wire", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Flight control system where pilot inputs are transmitted electronically to actuators. Computers interpret and may modify inputs for safety."},
    
    {"term": "PFD", "full_name": "Primary Flight Display", "category": "Instruments", "difficulty": "Basic",
     "definition": "Electronic display showing essential flight instruments: attitude, airspeed, altitude, heading, vertical speed."},
    
    {"term": "MFD", "full_name": "Multi-Function Display", "category": "Instruments", "difficulty": "Basic",
     "definition": "Electronic display showing navigation, engine parameters, weather, traffic, and other selectable information."},
    
    {"term": "EFIS", "full_name": "Electronic Flight Instrument System", "category": "Instruments", "difficulty": "Intermediate",
     "definition": "Integrated system of electronic displays replacing traditional analog instruments. Includes PFD and ND."},
    
    {"term": "ND", "full_name": "Navigation Display", "category": "Instruments", "difficulty": "Intermediate",
     "definition": "Electronic display showing navigation information, route, waypoints, weather radar, and traffic."},
    
    {"term": "EICAS", "full_name": "Engine Indicating and Crew Alerting System", "category": "Instruments", "difficulty": "Advanced",
     "definition": "System displaying engine parameters and aircraft warnings/cautions. Centralizes alerts and crew notifications."},
    
    {"term": "ECAM", "full_name": "Electronic Centralized Aircraft Monitor", "category": "Instruments", "difficulty": "Advanced",
     "definition": "Airbus equivalent of EICAS. Displays system status, alerts, and provides electronic checklists."},
    
    {"term": "ADC", "full_name": "Air Data Computer", "category": "Aircraft Systems", "difficulty": "Advanced",
     "definition": "Computer that processes pitot-static data to calculate airspeed, altitude, vertical speed, and outside air temperature."},
    
    {"term": "AHRS", "full_name": "Attitude and Heading Reference System", "category": "Aircraft Systems", "difficulty": "Advanced",
     "definition": "Solid-state system providing aircraft attitude and heading information. Replaces traditional gyroscopic instruments."},
    
    {"term": "IRU", "full_name": "Inertial Reference Unit", "category": "Navigation", "difficulty": "Advanced",
     "definition": "Self-contained navigation system using accelerometers and gyros. Provides position, attitude, and velocity data."},
    
    {"term": "RAT", "full_name": "Ram Air Turbine", "category": "Aircraft Systems", "difficulty": "Advanced",
     "definition": "Emergency power source deployed into airstream to generate hydraulic/electrical power during complete engine failure."},
    
    # ==================== AERODYNAMICS ====================
    {"term": "AOA", "full_name": "Angle of Attack", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "The angle between the wing chord line and the relative wind. Increasing AOA increases lift until the critical (stall) angle."},
    
    {"term": "CL", "full_name": "Coefficient of Lift", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Dimensionless coefficient relating lift force to dynamic pressure and wing area. Increases with AOA until stall."},
    
    {"term": "CD", "full_name": "Coefficient of Drag", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Dimensionless coefficient relating drag force to dynamic pressure and reference area."},
    
    {"term": "L/D", "full_name": "Lift to Drag Ratio", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Measure of aerodynamic efficiency. Maximum L/D occurs at a specific AOA and determines best glide performance."},
    
    {"term": "CG", "full_name": "Center of Gravity", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "The point where the aircraft's weight is concentrated. Must be within limits for safe flight. Affects stability and control."},
    
    {"term": "MAC", "full_name": "Mean Aerodynamic Chord", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Reference chord length used for CG calculations. CG position often expressed as percent MAC."},
    
    {"term": "TAS", "full_name": "True Airspeed", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "The actual speed of the aircraft through the air. Increases from IAS with altitude due to decreased air density."},
    
    {"term": "IAS", "full_name": "Indicated Airspeed", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "The airspeed shown on the cockpit indicator. Based on dynamic pressure. All V-speeds are referenced to IAS."},
    
    {"term": "CAS", "full_name": "Calibrated Airspeed", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "IAS corrected for instrument and position errors. Close to IAS in normal flight."},
    
    {"term": "EAS", "full_name": "Equivalent Airspeed", "category": "Aerodynamics", "difficulty": "Advanced",
     "definition": "CAS corrected for compressibility effects at high speed. Used for structural load calculations."},
    
    {"term": "GS", "full_name": "Ground Speed", "category": "Navigation", "difficulty": "Basic",
     "definition": "The speed of the aircraft relative to the ground. TAS corrected for wind component."},
    
    {"term": "MTOW", "full_name": "Maximum Takeoff Weight", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "The maximum certified weight at which an aircraft can take off. Structural and performance limit."},
    
    {"term": "MLW", "full_name": "Maximum Landing Weight", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "The maximum certified weight at which an aircraft can land. Often lower than MTOW due to landing gear limits."},
    
    {"term": "MZFW", "full_name": "Maximum Zero Fuel Weight", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Maximum weight of aircraft without usable fuel. Protects wing root structure from bending stress."},
    
    {"term": "DOW", "full_name": "Dry Operating Weight", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Empty aircraft weight plus crew, catering, and equipment. Does not include fuel or payload."},
    
    {"term": "OEW", "full_name": "Operating Empty Weight", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Same as DOW. The weight of the aircraft ready for operation but without fuel and payload."},
    
    {"term": "ZFW", "full_name": "Zero Fuel Weight", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Aircraft weight minus usable fuel. Equals DOW plus payload."},
    
    # ==================== COMMUNICATIONS ====================
    {"term": "SELCAL", "full_name": "Selective Calling", "category": "Communications", "difficulty": "Intermediate",
     "definition": "System allowing ground stations to alert specific aircraft on HF radio. Pilots can turn down speaker volume until called."},
    
    {"term": "ACARS", "full_name": "Aircraft Communications Addressing and Reporting System", "category": "Communications", "difficulty": "Intermediate",
     "definition": "Digital datalink system for transmitting text messages between aircraft and ground. Used for clearances, weather, and company messages."},
    
    {"term": "CPDLC", "full_name": "Controller-Pilot Data Link Communications", "category": "Communications", "difficulty": "Advanced",
     "definition": "Text-based communication between ATC and pilots. Reduces voice congestion and allows for more complex clearances."},
    
    {"term": "HF", "full_name": "High Frequency", "category": "Communications", "difficulty": "Intermediate",
     "definition": "Radio frequency band (3-30 MHz) used for long-range oceanic and remote area communications."},
    
    {"term": "VHF", "full_name": "Very High Frequency", "category": "Communications", "difficulty": "Basic",
     "definition": "Radio frequency band (118-137 MHz) used for most aviation communications. Line-of-sight range."},
    
    {"term": "UHF", "full_name": "Ultra High Frequency", "category": "Communications", "difficulty": "Intermediate",
     "definition": "Radio frequency band above VHF. Used primarily by military aviation."},
    
    {"term": "SATCOM", "full_name": "Satellite Communications", "category": "Communications", "difficulty": "Intermediate",
     "definition": "Communication via satellite. Provides global coverage for voice and data communications."},
    
    {"term": "SID", "full_name": "Standard Instrument Departure", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Published departure procedure providing obstacle clearance and traffic flow from an airport. Reduces radio congestion."},
    
    {"term": "STAR", "full_name": "Standard Terminal Arrival Route", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Published arrival procedure guiding aircraft from the en route structure to an approach. Includes altitude and speed restrictions."},
    
    {"term": "IAP", "full_name": "Instrument Approach Procedure", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Published procedure for guiding aircraft from the arrival phase to a position for landing in IMC."},
    
    {"term": "NOTAM", "full_name": "Notice to Airmen", "category": "ATC", "difficulty": "Basic",
     "definition": "Official notice containing information essential to flight safety. Includes runway closures, navigation aid status, and hazards."},
    
    {"term": "AIP", "full_name": "Aeronautical Information Publication", "category": "Regulations", "difficulty": "Intermediate",
     "definition": "Official publication containing permanent aeronautical information: airports, airspace, procedures, and regulations."},
    
    {"term": "ATIS", "full_name": "Automatic Terminal Information Service", "category": "Communications", "difficulty": "Basic",
     "definition": "Recorded broadcast of airport information. Each update identified by a letter (Alpha, Bravo, etc.)."},
    
    {"term": "D-ATIS", "full_name": "Digital ATIS", "category": "Communications", "difficulty": "Intermediate",
     "definition": "ATIS information delivered via datalink rather than voice broadcast."},
    
    # ==================== ATC ====================
    {"term": "CTR", "full_name": "Control Zone", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Controlled airspace extending from the surface to a specified upper limit around an airport. VFR requires clearance."},
    
    {"term": "TMA", "full_name": "Terminal Control Area", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Controlled airspace surrounding major airports above the CTR. Designed to accommodate arriving and departing traffic."},
    
    {"term": "FIR", "full_name": "Flight Information Region", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Airspace within which flight information service and alerting service are provided. May include controlled and uncontrolled airspace."},
    
    {"term": "UIR", "full_name": "Upper Information Region", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Airspace above the FIR, typically above FL245/FL285. Usually Class A (IFR only)."},
    
    {"term": "ACC", "full_name": "Area Control Center", "category": "ATC", "difficulty": "Intermediate",
     "definition": "ATC facility responsible for en route traffic. Provides separation services within its FIR."},
    
    {"term": "APP", "full_name": "Approach Control", "category": "ATC", "difficulty": "Basic",
     "definition": "ATC service for arriving and departing traffic in the terminal area. Sequences traffic for the runway."},
    
    {"term": "TWR", "full_name": "Tower", "category": "ATC", "difficulty": "Basic",
     "definition": "ATC service for airport traffic. Controls takeoffs, landings, and ground movement on runways."},
    
    {"term": "GND", "full_name": "Ground Control", "category": "ATC", "difficulty": "Basic",
     "definition": "ATC service for ground movement on taxiways and ramp areas. Separate from Tower for runway control."},
    
    {"term": "DEL", "full_name": "Delivery (Clearance Delivery)", "category": "ATC", "difficulty": "Basic",
     "definition": "ATC position that issues IFR clearances to departing aircraft before taxiing."},
    
    {"term": "RVSM", "full_name": "Reduced Vertical Separation Minimum", "category": "ATC", "difficulty": "Advanced",
     "definition": "Airspace between FL290-FL410 where vertical separation is reduced to 1000ft (from 2000ft). Requires approved aircraft and operations."},
    
    {"term": "MNPS", "full_name": "Minimum Navigation Performance Specifications", "category": "ATC", "difficulty": "Advanced",
     "definition": "Navigation performance requirements for North Atlantic operations. Being replaced by RNP requirements."},
    
    {"term": "NAT", "full_name": "North Atlantic Tracks", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Organized track system for North Atlantic crossings. Tracks change daily based on wind patterns."},
    
    {"term": "OCA", "full_name": "Oceanic Control Area", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Controlled airspace over international waters. Often uses procedural control rather than radar."},
    
    {"term": "SSR", "full_name": "Secondary Surveillance Radar", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Radar system that interrogates aircraft transponders to receive identity and altitude information."},
    
    {"term": "PSR", "full_name": "Primary Surveillance Radar", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Radar that detects aircraft by reflected signals. Shows position but not identity or altitude."},
    
    {"term": "ADS-B", "full_name": "Automatic Dependent Surveillance-Broadcast", "category": "ATC", "difficulty": "Intermediate",
     "definition": "Surveillance technology where aircraft broadcast their position. Enables better tracking and traffic services."},
    
    {"term": "ETOPS", "full_name": "Extended-range Twin-engine Operational Performance Standards", "category": "Regulations", "difficulty": "Advanced",
     "definition": "Regulations allowing twin-engine aircraft to fly extended routes over water/remote areas. Requires specific aircraft and crew certification."},
    
    {"term": "EDTO", "full_name": "Extended Diversion Time Operations", "category": "Regulations", "difficulty": "Advanced",
     "definition": "ICAO equivalent of ETOPS. The maximum time an aircraft can be from an adequate airport."},
    
    # ==================== EMERGENCIES ====================
    {"term": "PAN PAN", "full_name": "Pan Pan (Urgency)", "category": "Emergencies", "difficulty": "Basic",
     "definition": "International urgency signal. Indicates a condition concerning the safety of aircraft or persons but not requiring immediate assistance."},
    
    {"term": "MAYDAY", "full_name": "Mayday (Distress)", "category": "Emergencies", "difficulty": "Basic",
     "definition": "International distress signal. Indicates grave and imminent danger requiring immediate assistance. Highest priority."},
    
    {"term": "ELT", "full_name": "Emergency Locator Transmitter", "category": "Emergencies", "difficulty": "Intermediate",
     "definition": "Device that transmits a distress signal on 121.5 MHz and 406 MHz after a crash or when manually activated."},
    
    {"term": "SQUAWK", "full_name": "Transponder Code", "category": "Communications", "difficulty": "Basic",
     "definition": "Four-digit code set on transponder. Special codes: 7500 (hijack), 7600 (radio failure), 7700 (emergency)."},
    
    {"term": "QRH", "full_name": "Quick Reference Handbook", "category": "Emergencies", "difficulty": "Intermediate",
     "definition": "Manual containing abbreviated checklists for abnormal and emergency procedures. Used for quick reference in the cockpit."},
    
    {"term": "ECAM", "full_name": "Electronic Centralized Aircraft Monitor", "category": "Emergencies", "difficulty": "Advanced",
     "definition": "Airbus system that displays system status and provides electronic checklists during abnormal situations."},
    
    {"term": "MEL", "full_name": "Minimum Equipment List", "category": "Regulations", "difficulty": "Intermediate",
     "definition": "Document specifying which equipment can be inoperative while still allowing legal flight. Based on the Master MEL."},
    
    {"term": "CDL", "full_name": "Configuration Deviation List", "category": "Regulations", "difficulty": "Intermediate",
     "definition": "List of external parts that may be missing while still allowing safe flight with specified limitations."},
    
    {"term": "TLAR", "full_name": "That Looks About Right", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Informal term for visual verification. Important principle: if something doesn't look right, investigate before proceeding."},
    
    # ==================== HUMAN FACTORS ====================
    {"term": "CRM", "full_name": "Crew Resource Management", "category": "Human Factors", "difficulty": "Basic",
     "definition": "Training to improve crew coordination, communication, and decision-making. Emphasizes teamwork and error management."},
    
    {"term": "TEM", "full_name": "Threat and Error Management", "category": "Human Factors", "difficulty": "Intermediate",
     "definition": "Framework for understanding how threats and errors can lead to undesired aircraft states. Proactive safety approach."},
    
    {"term": "SA", "full_name": "Situational Awareness", "category": "Human Factors", "difficulty": "Basic",
     "definition": "The perception, comprehension, and projection of elements in the environment. Critical for safe flight operations."},
    
    {"term": "ADM", "full_name": "Aeronautical Decision Making", "category": "Human Factors", "difficulty": "Intermediate",
     "definition": "Systematic approach to mental process used by pilots to determine best course of action in response to circumstances."},
    
    {"term": "IMSAFE", "full_name": "Illness, Medication, Stress, Alcohol, Fatigue, Emotion", "category": "Human Factors", "difficulty": "Basic",
     "definition": "Personal fitness checklist for pilots before flight. All factors can impair performance and safety."},
    
    {"term": "PAVE", "full_name": "Pilot, Aircraft, enVironment, External pressures", "category": "Human Factors", "difficulty": "Intermediate",
     "definition": "Risk assessment framework considering all factors that affect flight safety."},
    
    {"term": "DECIDE", "full_name": "Detect, Estimate, Choose, Identify, Do, Evaluate", "category": "Human Factors", "difficulty": "Intermediate",
     "definition": "Decision-making model for addressing problems in flight. Structured approach to complex situations."},
    
    {"term": "SOP", "full_name": "Standard Operating Procedure", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Established procedures that all crew members must follow. Ensures consistency and reduces errors."},
    
    {"term": "FRAT", "full_name": "Flight Risk Assessment Tool", "category": "Human Factors", "difficulty": "Intermediate",
     "definition": "Checklist-based tool for assessing overall flight risk before departure. Helps identify cumulative risks."},
    
    {"term": "EBT", "full_name": "Evidence-Based Training", "category": "Human Factors", "difficulty": "Advanced",
     "definition": "Training approach based on data analysis of actual operations. Focuses on competencies rather than just maneuvers."},
    
    # ==================== FLIGHT OPERATIONS ====================
    {"term": "CTOT", "full_name": "Calculated Takeoff Time", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "Assigned takeoff time issued by flow control. Aircraft must be ready to take off at this time."},
    
    {"term": "COBT", "full_name": "Calculated Off-Block Time", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "Planned time for aircraft to push back from the gate. Used for ground handling and flow management."},
    
    {"term": "TOBT", "full_name": "Target Off-Block Time", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "The time that the aircraft operator or ground handler estimates the aircraft will be ready for pushback."},
    
    {"term": "ETA", "full_name": "Estimated Time of Arrival", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Predicted arrival time at destination or waypoint based on current conditions."},
    
    {"term": "ETD", "full_name": "Estimated Time of Departure", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Predicted departure time from an airport."},
    
    {"term": "ETE", "full_name": "Estimated Time En Route", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Expected flight time from departure to destination."},
    
    {"term": "ATA", "full_name": "Actual Time of Arrival", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "The actual time an aircraft arrives at a location."},
    
    {"term": "ATD", "full_name": "Actual Time of Departure", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "The actual time an aircraft departs."},
    
    {"term": "EOBT", "full_name": "Estimated Off-Block Time", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "Estimated time for pushback from the gate as filed in the flight plan."},
    
    {"term": "ETH", "full_name": "Elapsed Time from Takeoff to Touchdown", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Total airborne time for a flight."},
    
    {"term": "TOD", "full_name": "Top of Descent", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "The point at which descent from cruise altitude should begin to arrive at destination at correct altitude."},
    
    {"term": "TOC", "full_name": "Top of Climb", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "The point at which the aircraft reaches cruise altitude."},
    
    {"term": "CI", "full_name": "Cost Index", "category": "Flight Operations", "difficulty": "Advanced",
     "definition": "Ratio of time cost to fuel cost used by FMS to calculate optimal cruise speed. Higher CI = faster, more fuel."},
    
    {"term": "LRC", "full_name": "Long Range Cruise", "category": "Flight Operations", "difficulty": "Advanced",
     "definition": "Cruise speed providing 99% of maximum specific range. Balances range and time efficiency."},
    
    {"term": "MRC", "full_name": "Maximum Range Cruise", "category": "Flight Operations", "difficulty": "Advanced",
     "definition": "Cruise speed for maximum fuel efficiency and range. Slower than LRC."},
    
    {"term": "ECON", "full_name": "Economy Speed", "category": "Flight Operations", "difficulty": "Advanced",
     "definition": "Cruise speed calculated by FMS based on cost index to minimize total operating cost."},
    
    {"term": "FL", "full_name": "Flight Level", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Altitude in hundreds of feet based on standard pressure (1013.25 hPa). FL350 = 35,000 feet pressure altitude."},
    
    {"term": "RVR", "full_name": "Runway Visual Range", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "Horizontal distance a pilot can see down the runway from a moving aircraft. Measured by transmissometers."},
    
    {"term": "SVR", "full_name": "Slant Visual Range", "category": "Flight Operations", "difficulty": "Advanced",
     "definition": "The visual range along the pilot's line of sight on approach. Can differ from RVR."},
    
    {"term": "CAT I/II/III", "full_name": "Category I/II/III Approach", "category": "Flight Operations", "difficulty": "Advanced",
     "definition": "ILS approach categories with decreasing minima. CAT I: DH 200ft, RVR 550m. CAT III: Can be zero visibility."},
    
    {"term": "LNAV", "full_name": "Lateral Navigation", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "Autopilot/FMS mode for lateral guidance along a programmed route."},
    
    {"term": "VNAV", "full_name": "Vertical Navigation", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "Autopilot/FMS mode for vertical profile guidance including climbs, descents, and altitude constraints."},
    
    {"term": "LPV", "full_name": "Localizer Performance with Vertical guidance", "category": "Navigation", "difficulty": "Advanced",
     "definition": "GPS-based approach with vertical guidance similar to ILS. Requires WAAS-capable GPS."},
    
    {"term": "CDFA", "full_name": "Continuous Descent Final Approach", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "Technique for non-precision approaches maintaining constant descent angle. Improves safety and reduces noise."},
    
    # ==================== AIRPORT ====================
    {"term": "RWY", "full_name": "Runway", "category": "Airport", "difficulty": "Basic",
     "definition": "Defined rectangular area for aircraft takeoff and landing. Numbered by magnetic heading divided by 10."},
    
    {"term": "TWY", "full_name": "Taxiway", "category": "Airport", "difficulty": "Basic",
     "definition": "Defined path for aircraft ground movement between runway and ramp. Identified by letters."},
    
    {"term": "APN", "full_name": "Apron", "category": "Airport", "difficulty": "Basic",
     "definition": "Area for aircraft parking, loading, fueling, and boarding. Also called ramp."},
    
    {"term": "PAPI", "full_name": "Precision Approach Path Indicator", "category": "Airport", "difficulty": "Intermediate",
     "definition": "Visual approach slope indicator. Four lights showing red/white pattern indicating position relative to glidepath."},
    
    {"term": "VASI", "full_name": "Visual Approach Slope Indicator", "category": "Airport", "difficulty": "Intermediate",
     "definition": "Older visual glidepath indicator using red/white lights. Being replaced by PAPI."},
    
    {"term": "REIL", "full_name": "Runway End Identifier Lights", "category": "Airport", "difficulty": "Intermediate",
     "definition": "Synchronized flashing lights at runway threshold for identification at night or in low visibility."},
    
    {"term": "ALS", "full_name": "Approach Lighting System", "category": "Airport", "difficulty": "Intermediate",
     "definition": "Pattern of lights extending from runway threshold. Provides visual guidance during approach."},
    
    {"term": "MALSR", "full_name": "Medium Intensity Approach Lighting System with RAIL", "category": "Airport", "difficulty": "Advanced",
     "definition": "Common approach lighting system in the US with sequenced flashing lights."},
    
    {"term": "PCN", "full_name": "Pavement Classification Number", "category": "Airport", "difficulty": "Intermediate",
     "definition": "Number indicating pavement bearing strength. Must be compared to aircraft ACN."},
    
    {"term": "ACN", "full_name": "Aircraft Classification Number", "category": "Airport", "difficulty": "Intermediate",
     "definition": "Number indicating aircraft load on pavement. Must not exceed runway PCN."},
    
    {"term": "ARFF", "full_name": "Aircraft Rescue and Fire Fighting", "category": "Airport", "difficulty": "Intermediate",
     "definition": "Airport fire and rescue services. Category determined by aircraft size served."},
    
    {"term": "FOD", "full_name": "Foreign Object Debris/Damage", "category": "Airport", "difficulty": "Basic",
     "definition": "Any object on the movement area that could cause damage to aircraft. FOD prevention is critical for safety."},
    
    {"term": "ASDA", "full_name": "Accelerate-Stop Distance Available", "category": "Airport", "difficulty": "Intermediate",
     "definition": "Runway length plus stopway available for aborting a takeoff."},
    
    {"term": "TODA", "full_name": "Takeoff Distance Available", "category": "Airport", "difficulty": "Intermediate",
     "definition": "Runway length plus clearway available for takeoff."},
    
    {"term": "TORA", "full_name": "Takeoff Run Available", "category": "Airport", "difficulty": "Intermediate",
     "definition": "The length of runway declared available for the ground run of an aircraft taking off."},
    
    {"term": "LDA", "full_name": "Landing Distance Available", "category": "Airport", "difficulty": "Intermediate",
     "definition": "The length of runway declared available for landing."},
    
    {"term": "RESA", "full_name": "Runway End Safety Area", "category": "Airport", "difficulty": "Intermediate",
     "definition": "Cleared area beyond runway end providing space for aircraft undershooting or overrunning."},
    
    # ==================== ADDITIONAL IMPORTANT TERMS ====================
    {"term": "SAF", "full_name": "Sustainable Aviation Fuel", "category": "Regulations", "difficulty": "Intermediate",
     "definition": "Jet fuel produced from sustainable sources. Can reduce lifecycle carbon emissions by up to 80%."},
    
    {"term": "eVTOL", "full_name": "Electric Vertical Takeoff and Landing", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Electric aircraft capable of vertical takeoff and landing. Core technology for urban air mobility."},
    
    {"term": "UAM", "full_name": "Urban Air Mobility", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "Air transportation system for passengers and cargo in urban areas using new aircraft technologies."},
    
    {"term": "AAM", "full_name": "Advanced Air Mobility", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "Broader term encompassing urban, regional, and point-to-point air mobility using emerging technologies."},
    
    {"term": "CORSIA", "full_name": "Carbon Offsetting and Reduction Scheme for International Aviation", "category": "Regulations", "difficulty": "Advanced",
     "definition": "ICAO program requiring airlines to offset CO2 emissions growth from international flights above 2019 levels."},
    
    {"term": "SMS", "full_name": "Safety Management System", "category": "Regulations", "difficulty": "Intermediate",
     "definition": "Systematic approach to managing safety, including organizational structure, policies, and procedures."},
    
    {"term": "FOQA", "full_name": "Flight Operational Quality Assurance", "category": "Human Factors", "difficulty": "Advanced",
     "definition": "Program analyzing flight data to identify and address safety issues before they result in accidents."},
    
    {"term": "FDM", "full_name": "Flight Data Monitoring", "category": "Human Factors", "difficulty": "Advanced",
     "definition": "Systematic use of recorded flight data to improve aviation safety. Similar to FOQA."},
    
    {"term": "QAR", "full_name": "Quick Access Recorder", "category": "Aircraft Systems", "difficulty": "Advanced",
     "definition": "Device recording flight data for operational analysis. Easily accessible unlike the FDR."},
    
    {"term": "FDR", "full_name": "Flight Data Recorder", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Device recording flight parameters. Protected for crash survival. Used for accident investigation."},
    
    {"term": "CVR", "full_name": "Cockpit Voice Recorder", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Device recording cockpit audio. Protected for crash survival. Records last 2+ hours of audio."},
    
    {"term": "PBN", "full_name": "Performance-Based Navigation", "category": "Navigation", "difficulty": "Advanced",
     "definition": "Navigation based on performance requirements rather than specific sensors. Includes RNAV and RNP."},
    
    {"term": "SBAS", "full_name": "Satellite-Based Augmentation System", "category": "Navigation", "difficulty": "Advanced",
     "definition": "System using geostationary satellites to improve GNSS accuracy and integrity. WAAS is a SBAS."},
    
    {"term": "GBAS", "full_name": "Ground-Based Augmentation System", "category": "Navigation", "difficulty": "Advanced",
     "definition": "Ground stations providing local GPS corrections for precision approaches. Future replacement for ILS."},
    
    {"term": "TAT", "full_name": "Total Air Temperature", "category": "Meteorology", "difficulty": "Advanced",
     "definition": "Temperature measured by probe including heating from air compression. Higher than OAT at high speeds."},
    
    {"term": "SAT", "full_name": "Static Air Temperature", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "Actual temperature of undisturbed air. Same as OAT. Used for performance calculations."},
    
    {"term": "MORA", "full_name": "Minimum Off-Route Altitude", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "Altitude providing 1000ft clearance above obstacles within 10nm of route centerline."},
    
    {"term": "GRID MORA", "full_name": "Grid Minimum Off-Route Altitude", "category": "Navigation", "difficulty": "Intermediate",
     "definition": "Obstacle clearance altitude for a specific grid area on navigational charts."},
    
    # ==================== AVIATION TERMS (Non-Abbreviations) ====================
    {"term": "Aileron", "full_name": "Flight Control Surface", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "Hinged control surfaces on the trailing edge of each wing that control roll (bank) by moving in opposite directions."},
    
    {"term": "Elevator", "full_name": "Pitch Control Surface", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "Hinged control surface on the horizontal stabilizer that controls pitch (nose up/down movement)."},
    
    {"term": "Rudder", "full_name": "Yaw Control Surface", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "Hinged control surface on the vertical stabilizer that controls yaw (nose left/right movement)."},
    
    {"term": "Flaps", "full_name": "High-Lift Devices", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "Hinged surfaces on the trailing edge of the wing that increase lift and drag. Used during takeoff and landing to reduce speed."},
    
    {"term": "Slats", "full_name": "Leading Edge High-Lift Device", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Movable panels on the leading edge of the wing that extend to increase lift at low speeds and high angles of attack."},
    
    {"term": "Spoilers", "full_name": "Lift Dump/Speed Brake", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Panels on the upper wing surface that deploy to reduce lift and increase drag. Used for descent, roll assist, and ground braking."},
    
    {"term": "Trim", "full_name": "Control Surface Trimming", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Adjustment of control surfaces to relieve control pressure. Allows hands-off flight at a desired attitude."},
    
    {"term": "Stall", "full_name": "Aerodynamic Stall", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "Condition where the wing exceeds its critical angle of attack and airflow separates, causing sudden loss of lift. Not related to engine."},
    
    {"term": "Spin", "full_name": "Autorotation", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Aggravated stall resulting in autorotation around the vertical axis. One wing is more stalled than the other."},
    
    {"term": "Spiral Dive", "full_name": "Spiral Instability", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Steep descending turn with increasing airspeed. Unlike a spin, the aircraft is not stalled. Requires different recovery."},
    
    {"term": "Dutch Roll", "full_name": "Combined Yaw-Roll Oscillation", "category": "Aerodynamics", "difficulty": "Advanced",
     "definition": "Coupled oscillation in yaw and roll. The aircraft 'waddles' side to side. Common in swept-wing aircraft. Yaw dampers prevent it."},
    
    {"term": "Crosswind", "full_name": "Wind Perpendicular to Runway", "category": "Meteorology", "difficulty": "Basic",
     "definition": "Wind component blowing across the runway. Requires crab or slip technique for landing. Each aircraft has a maximum crosswind limit."},
    
    {"term": "Headwind", "full_name": "Wind Opposing Flight", "category": "Meteorology", "difficulty": "Basic",
     "definition": "Wind blowing against the direction of flight. Increases ground distance for takeoff but improves aircraft performance."},
    
    {"term": "Tailwind", "full_name": "Wind From Behind", "category": "Meteorology", "difficulty": "Basic",
     "definition": "Wind blowing in the same direction as flight. Reduces takeoff/landing performance. Usually limited to 10 knots for landing."},
    
    {"term": "Turbulence", "full_name": "Atmospheric Disturbance", "category": "Meteorology", "difficulty": "Basic",
     "definition": "Irregular motion of air causing bumps. Categories: Light, Moderate, Severe, Extreme. Can be caused by terrain, weather, or jet streams."},
    
    {"term": "Icing", "full_name": "Ice Accumulation", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "Formation of ice on aircraft surfaces. Types include rime (rough), clear (smooth), and mixed. Degrades performance significantly."},
    
    {"term": "Windshear", "full_name": "Sudden Wind Change", "category": "Meteorology", "difficulty": "Intermediate",
     "definition": "Rapid change in wind speed or direction over short distance. Extremely hazardous during takeoff and landing."},
    
    {"term": "Microburst", "full_name": "Localized Downdraft", "category": "Meteorology", "difficulty": "Advanced",
     "definition": "Intense, localized downdraft from thunderstorm causing sudden wind changes. Can cause rapid loss of airspeed and altitude."},
    
    {"term": "Wake Turbulence", "full_name": "Vortex Wake", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Rotating air masses trailing behind aircraft wingtips. Strongest behind heavy aircraft at slow speeds. Requires separation."},
    
    {"term": "Prop Wash", "full_name": "Propeller Slipstream", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "Spiraling airflow behind a propeller. Causes left-turning tendency in single-engine aircraft. Requires right rudder on takeoff."},
    
    {"term": "Torque", "full_name": "Engine Reaction Force", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Reaction to propeller rotation that tends to roll the aircraft in the opposite direction. One of four left-turning tendencies."},
    
    {"term": "P-Factor", "full_name": "Asymmetric Propeller Loading", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "At high angles of attack, the descending blade produces more thrust than ascending blade, causing yaw."},
    
    {"term": "Slipstream", "full_name": "Propeller Airflow", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "Accelerated airflow produced by the propeller. Creates spiral flow around fuselage affecting rudder and causing yaw."},
    
    {"term": "Feathering", "full_name": "Propeller Blade Alignment", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Rotating propeller blades parallel to airflow to minimize drag when engine fails. Critical for multi-engine aircraft."},
    
    {"term": "Thrust", "full_name": "Forward Force", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "Forward force produced by engines/propellers. One of four forces of flight. Opposes drag."},
    
    {"term": "Lift", "full_name": "Upward Aerodynamic Force", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "Force perpendicular to relative wind, primarily generated by wings. Opposes weight. Created by pressure differential."},
    
    {"term": "Drag", "full_name": "Resistance Force", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "Force opposing motion through air. Types include parasite (form, skin friction, interference) and induced (from lift)."},
    
    {"term": "Weight", "full_name": "Gravitational Force", "category": "Aerodynamics", "difficulty": "Basic",
     "definition": "Force of gravity acting on aircraft mass. One of four forces of flight. Opposes lift."},
    
    {"term": "Chord", "full_name": "Wing Cross-Section Line", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Straight line from leading edge to trailing edge of an airfoil. Used as reference for angle of attack."},
    
    {"term": "Camber", "full_name": "Airfoil Curvature", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Curvature of an airfoil from leading to trailing edge. More camber generally produces more lift."},
    
    {"term": "Dihedral", "full_name": "Wing Upward Angle", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Upward angle of wings from root to tip when viewed from front. Provides lateral (roll) stability."},
    
    {"term": "Anhedral", "full_name": "Wing Downward Angle", "category": "Aerodynamics", "difficulty": "Intermediate",
     "definition": "Downward angle of wings from root to tip. Used on some military aircraft for improved maneuverability."},
    
    {"term": "Fuselage", "full_name": "Aircraft Body", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Main body of the aircraft containing cabin, cockpit, and cargo areas. Wings and tail attach to it."},
    
    {"term": "Empennage", "full_name": "Tail Assembly", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Complete tail section including horizontal stabilizer, elevator, vertical stabilizer, and rudder."},
    
    {"term": "Nacelle", "full_name": "Engine Housing", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Streamlined enclosure for an engine. Houses engine and accessories while reducing drag."},
    
    {"term": "Cowling", "full_name": "Engine Cover", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Removable cover over the engine. Provides streamlining and directs cooling air."},
    
    {"term": "Pitot Tube", "full_name": "Dynamic Pressure Sensor", "category": "Instruments", "difficulty": "Basic",
     "definition": "Tube facing forward that measures ram air pressure. Combined with static pressure to calculate airspeed."},
    
    {"term": "Static Port", "full_name": "Static Pressure Sensor", "category": "Instruments", "difficulty": "Basic",
     "definition": "Opening on aircraft side measuring ambient atmospheric pressure. Used by altimeter, airspeed, and VSI."},
    
    {"term": "Altimeter", "full_name": "Altitude Indicator", "category": "Instruments", "difficulty": "Basic",
     "definition": "Instrument measuring altitude based on atmospheric pressure. Must be set to correct pressure setting."},
    
    {"term": "Airspeed Indicator", "full_name": "ASI", "category": "Instruments", "difficulty": "Basic",
     "definition": "Instrument showing speed through the air by measuring difference between pitot and static pressure."},
    
    {"term": "Attitude Indicator", "full_name": "Artificial Horizon", "category": "Instruments", "difficulty": "Basic",
     "definition": "Gyroscopic instrument showing aircraft pitch and bank relative to the horizon. Primary instrument for IFR."},
    
    {"term": "Heading Indicator", "full_name": "Directional Gyro", "category": "Instruments", "difficulty": "Basic",
     "definition": "Gyroscopic instrument showing aircraft heading. Must be periodically aligned with magnetic compass."},
    
    {"term": "Turn Coordinator", "full_name": "Rate of Turn Indicator", "category": "Instruments", "difficulty": "Basic",
     "definition": "Instrument showing rate of turn and coordination. Miniature aircraft banks with turn, ball shows slip/skid."},
    
    {"term": "Vertical Speed Indicator", "full_name": "VSI / Variometer", "category": "Instruments", "difficulty": "Basic",
     "definition": "Instrument showing rate of climb or descent in feet per minute. Measures rate of change of static pressure."},
    
    {"term": "Compass", "full_name": "Magnetic Compass", "category": "Instruments", "difficulty": "Basic",
     "definition": "Direct-reading magnetic direction indicator. Subject to errors (deviation, variation, dip, acceleration, turning)."},
    
    {"term": "Throttle", "full_name": "Power Control", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Control that regulates engine power by controlling fuel/air mixture flow. Usually a black lever."},
    
    {"term": "Mixture", "full_name": "Fuel-Air Ratio Control", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Control adjusting the ratio of fuel to air entering the engine. Leaned at altitude, rich for takeoff. Usually red lever."},
    
    {"term": "Propeller Control", "full_name": "RPM/Blade Angle Control", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Control adjusting propeller blade angle to control RPM. Used on constant-speed propellers. Usually blue lever."},
    
    {"term": "Yoke", "full_name": "Control Column", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Wheel-shaped control in cockpit that operates ailerons (turn) and elevator (push/pull). Alternative to stick."},
    
    {"term": "Sidestick", "full_name": "Side-Mounted Control Stick", "category": "Aircraft Systems", "difficulty": "Intermediate",
     "definition": "Control stick mounted on the side console in Airbus aircraft. Operates fly-by-wire flight controls."},
    
    {"term": "Pedals", "full_name": "Rudder Pedals", "category": "Aircraft Systems", "difficulty": "Basic",
     "definition": "Foot controls operating the rudder and nose wheel steering. Also used for differential braking."},
    
    {"term": "Flare", "full_name": "Landing Transition", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Gradual pitch-up maneuver just before touchdown to reduce descent rate and allow main gear to touch first."},
    
    {"term": "Rotation", "full_name": "Takeoff Pitch-Up", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Raising the nose during takeoff roll at rotation speed (VR) to become airborne."},
    
    {"term": "Touchdown", "full_name": "Landing Contact", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Moment when aircraft wheels make contact with the runway during landing."},
    
    {"term": "Rollout", "full_name": "Landing Deceleration", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Phase after touchdown where aircraft decelerates on the runway using brakes, spoilers, and reverse thrust."},
    
    {"term": "Taxi", "full_name": "Ground Movement", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Ground movement of aircraft under its own power. Speed typically limited to 20-30 knots."},
    
    {"term": "Pushback", "full_name": "Ramp Departure", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Moving aircraft backward from gate using a tug vehicle. Aircraft cannot reverse under own power."},
    
    {"term": "Holding", "full_name": "Airborne Delay Pattern", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "Racetrack pattern flown to delay arrival. Standard pattern has right turns, 1-minute legs."},
    
    {"term": "Circling", "full_name": "Circling Approach", "category": "Flight Operations", "difficulty": "Advanced",
     "definition": "Visual maneuvering to a different runway than the instrument approach runway. Has specific visibility and ceiling requirements."},
    
    {"term": "Missed Approach", "full_name": "Go-Around Procedure", "category": "Flight Operations", "difficulty": "Intermediate",
     "definition": "Published procedure when landing cannot be completed. Add power, clean up, climb, and follow published route."},
    
    {"term": "Go-Around", "full_name": "Aborted Landing", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Decision to abort landing and climb away. Apply full power, pitch up, retract gear/flaps incrementally."},
    
    {"term": "Abort", "full_name": "Rejected Takeoff", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Decision to stop takeoff before V1. Reduce power, apply brakes, deploy spoilers/reversers."},
    
    {"term": "Waypoint", "full_name": "Navigation Fix", "category": "Navigation", "difficulty": "Basic",
     "definition": "Geographic position used for navigation. Can be a radio navaid, intersection, or GPS coordinate."},
    
    {"term": "Intersection", "full_name": "Airway Junction", "category": "Navigation", "difficulty": "Basic",
     "definition": "Point defined by the intersection of two VOR radials or other navigation references."},
    
    {"term": "Radial", "full_name": "VOR Bearing", "category": "Navigation", "difficulty": "Basic",
     "definition": "Magnetic bearing FROM a VOR station. 360 radials emanate from each VOR."},
    
    {"term": "Bearing", "full_name": "Direction TO Station", "category": "Navigation", "difficulty": "Basic",
     "definition": "Magnetic direction TO a navigation station from the aircraft. Opposite of radial."},
    
    {"term": "Track", "full_name": "Path Over Ground", "category": "Navigation", "difficulty": "Basic",
     "definition": "Actual path of aircraft over the ground. May differ from heading due to wind."},
    
    {"term": "Heading", "full_name": "Aircraft Nose Direction", "category": "Navigation", "difficulty": "Basic",
     "definition": "Direction the aircraft nose is pointed. True heading referenced to true north, magnetic to magnetic north."},
    
    {"term": "Course", "full_name": "Intended Track", "category": "Navigation", "difficulty": "Basic",
     "definition": "Intended direction of flight. The path you want to fly."},
    
    {"term": "Clearance", "full_name": "ATC Authorization", "category": "ATC", "difficulty": "Basic",
     "definition": "Authorization from ATC to proceed under specified conditions. Must be read back and complied with."},
    
    {"term": "Squawk", "full_name": "Transponder Code", "category": "Communications", "difficulty": "Basic",
     "definition": "Four-digit code assigned by ATC for radar identification. 'Squawk 1234' means set transponder to 1234."},
    
    {"term": "Roger", "full_name": "Message Received", "category": "Communications", "difficulty": "Basic",
     "definition": "Radio term meaning 'I have received and understood your message.' Does not mean agreement."},
    
    {"term": "Wilco", "full_name": "Will Comply", "category": "Communications", "difficulty": "Basic",
     "definition": "Radio term meaning 'I have received your message and will comply.' Includes acknowledgment."},
    
    {"term": "Affirmative", "full_name": "Yes", "category": "Communications", "difficulty": "Basic",
     "definition": "Radio term meaning 'yes' or 'that is correct.' Avoids confusion with similar-sounding words."},
    
    {"term": "Negative", "full_name": "No", "category": "Communications", "difficulty": "Basic",
     "definition": "Radio term meaning 'no' or 'that is not correct.' Clear alternative to 'no'."},
    
    {"term": "Standby", "full_name": "Wait", "category": "Communications", "difficulty": "Basic",
     "definition": "Radio term meaning wait for further communication. No response required."},
    
    {"term": "Unable", "full_name": "Cannot Comply", "category": "Communications", "difficulty": "Basic",
     "definition": "Radio term indicating inability to comply with a clearance or instruction. State the reason."},
    
    {"term": "Checklist", "full_name": "Procedural List", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Systematic list of items to be verified or actions to be performed. Critical for safe operations."},
    
    {"term": "Briefing", "full_name": "Pre-flight Discussion", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Crew discussion before flight covering expected conditions, procedures, and contingencies."},
    
    {"term": "Preflight", "full_name": "Pre-flight Inspection", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Systematic inspection of aircraft before flight. Pilot's responsibility to ensure airworthiness."},
    
    {"term": "Walkaround", "full_name": "Exterior Inspection", "category": "Flight Operations", "difficulty": "Basic",
     "definition": "Visual inspection of aircraft exterior following a specific pattern. Part of preflight."},
    
    {"term": "Callout", "full_name": "Verbal Announcement", "category": "Human Factors", "difficulty": "Basic",
     "definition": "Verbal announcement of aircraft state, speed, or configuration. Standard callouts at specific points improve crew coordination."},
    
    {"term": "Crosscheck", "full_name": "Verification", "category": "Human Factors", "difficulty": "Basic",
     "definition": "Verification of information or action by comparing with another source or crew member."},
    
    {"term": "Sterile Cockpit", "full_name": "Critical Phase Protocol", "category": "Human Factors", "difficulty": "Intermediate",
     "definition": "Regulation requiring crew to refrain from non-essential activities during critical phases of flight (below 10,000 ft or during taxi)."},
]

# Convert to DataFrame
df = pd.DataFrame(dictionary_data)

st.markdown('<h1 class="page-header">📖 Aviation Dictionary</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Comprehensive glossary of aviation terms, abbreviations, and concepts</p>', unsafe_allow_html=True)

# Statistics
total_terms = len(df)
categories = df['category'].nunique()
basic = len(df[df['difficulty'] == 'Basic'])
intermediate = len(df[df['difficulty'] == 'Intermediate'])
advanced = len(df[df['difficulty'] == 'Advanced'])

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Total Terms", total_terms)
with col2:
    st.metric("Categories", categories)
with col3:
    st.metric("Basic", basic)
with col4:
    st.metric("Intermediate", intermediate)
with col5:
    st.metric("Advanced", advanced)

st.markdown("<br>", unsafe_allow_html=True)

# Filters Section
st.markdown('<div class="filter-section">', unsafe_allow_html=True)
st.markdown("### 🔍 Filter & Search")

col1, col2, col3 = st.columns(3)

with col1:
    search_term = st.text_input("🔎 Search term or abbreviation", placeholder="e.g., VOR, stall, IFR...")

with col2:
    category_options = ["All Categories"] + sorted(df['category'].unique().tolist())
    selected_category = st.selectbox("📁 Category", category_options)

with col3:
    difficulty_options = ["All Levels", "Basic", "Intermediate", "Advanced"]
    selected_difficulty = st.selectbox("📊 Difficulty", difficulty_options)

# Study Mode
col1, col2 = st.columns(2)
with col1:
    sort_option = st.selectbox("📌 Sort by", ["Alphabetical (A-Z)", "Alphabetical (Z-A)", "Category", "Difficulty"])
with col2:
    display_mode = st.radio("📋 Display Mode", ["Full Cards", "Compact Table", "Flashcard Mode"], horizontal=True)

st.markdown('</div>', unsafe_allow_html=True)

# Apply filters
filtered_df = df.copy()

if search_term:
    mask = (
        filtered_df['term'].str.contains(search_term, case=False, na=False) |
        filtered_df['full_name'].str.contains(search_term, case=False, na=False) |
        filtered_df['definition'].str.contains(search_term, case=False, na=False)
    )
    filtered_df = filtered_df[mask]

if selected_category != "All Categories":
    filtered_df = filtered_df[filtered_df['category'] == selected_category]

if selected_difficulty != "All Levels":
    filtered_df = filtered_df[filtered_df['difficulty'] == selected_difficulty]

# Apply sorting
if sort_option == "Alphabetical (A-Z)":
    filtered_df = filtered_df.sort_values('term')
elif sort_option == "Alphabetical (Z-A)":
    filtered_df = filtered_df.sort_values('term', ascending=False)
elif sort_option == "Category":
    filtered_df = filtered_df.sort_values(['category', 'term'])
elif sort_option == "Difficulty":
    difficulty_order = {"Basic": 0, "Intermediate": 1, "Advanced": 2}
    filtered_df['difficulty_order'] = filtered_df['difficulty'].map(difficulty_order)
    filtered_df = filtered_df.sort_values(['difficulty_order', 'term'])
    filtered_df = filtered_df.drop('difficulty_order', axis=1)

# Display results count
st.markdown(f"**Showing {len(filtered_df)} of {total_terms} terms**")
st.markdown("<br>", unsafe_allow_html=True)

# Display based on mode
if display_mode == "Full Cards":
    for _, row in filtered_df.iterrows():
        difficulty_class = f"difficulty-{row['difficulty'].lower()}"
        st.markdown(f"""
        <div class="term-card">
            <div class="term-abbrev">{row['term']}</div>
            <div class="term-full">{row['full_name']}</div>
            <div class="term-definition">{row['definition']}</div>
            <span class="category-badge">{row['category']}</span>
            <span class="category-badge {difficulty_class}">{row['difficulty']}</span>
        </div>
        """, unsafe_allow_html=True)

elif display_mode == "Compact Table":
    st.dataframe(
        filtered_df[['term', 'full_name', 'category', 'difficulty']],
        use_container_width=True,
        hide_index=True,
        column_config={
            "term": st.column_config.TextColumn("Abbreviation", width="small"),
            "full_name": st.column_config.TextColumn("Full Name", width="medium"),
            "category": st.column_config.TextColumn("Category", width="small"),
            "difficulty": st.column_config.TextColumn("Level", width="small"),
        }
    )
    
    # Expandable definitions
    with st.expander("📖 Click to view definitions"):
        for _, row in filtered_df.iterrows():
            st.markdown(f"**{row['term']}** - {row['definition']}")

elif display_mode == "Flashcard Mode":
    st.markdown("### 🎴 Flashcard Study Mode")
    st.markdown("*Click to reveal the answer*")
    
    if len(filtered_df) > 0:
        # Session state for flashcard navigation
        if 'flashcard_index' not in st.session_state:
            st.session_state.flashcard_index = 0
        if 'show_answer' not in st.session_state:
            st.session_state.show_answer = False
        if 'shuffled_indices' not in st.session_state:
            st.session_state.shuffled_indices = None
        if 'last_filter_hash' not in st.session_state:
            st.session_state.last_filter_hash = None
        
        # Create a hash of current filters to detect changes
        current_filter_hash = f"{search_term}_{selected_category}_{selected_difficulty}"
        
        # Reset shuffle if filters changed
        if st.session_state.last_filter_hash != current_filter_hash:
            st.session_state.shuffled_indices = None
            st.session_state.flashcard_index = 0
            st.session_state.last_filter_hash = current_filter_hash
        
        # Use shuffled order if available, otherwise use filtered_df order
        if st.session_state.shuffled_indices is not None:
            # Get valid indices that still exist in filtered_df
            valid_indices = [i for i in st.session_state.shuffled_indices if i < len(filtered_df)]
            if len(valid_indices) > 0:
                display_order = valid_indices
            else:
                display_order = list(range(len(filtered_df)))
                st.session_state.shuffled_indices = None
        else:
            display_order = list(range(len(filtered_df)))
        
        # Reset index if out of bounds
        if st.session_state.flashcard_index >= len(display_order):
            st.session_state.flashcard_index = 0
        
        current_idx = display_order[st.session_state.flashcard_index]
        current_term = filtered_df.iloc[current_idx]
        
        # Display flashcard
        st.markdown(f"""
        <div class="term-card" style="text-align: center; padding: 3rem;">
            <div class="term-abbrev" style="font-size: 3rem;">{current_term['term']}</div>
            <p style="color: #888; margin-top: 1rem;">Card {st.session_state.flashcard_index + 1} of {len(display_order)}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.button("⬅️ Previous"):
                st.session_state.flashcard_index = (st.session_state.flashcard_index - 1) % len(display_order)
                st.session_state.show_answer = False
                st.rerun()
        
        with col2:
            if st.button("🔄 Show/Hide Answer", use_container_width=True):
                st.session_state.show_answer = not st.session_state.show_answer
                st.rerun()
        
        with col3:
            if st.button("Next ➡️"):
                st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % len(display_order)
                st.session_state.show_answer = False
                st.rerun()
        
        if st.session_state.show_answer:
            st.markdown(f"""
            <div class="term-card" style="background: rgba(200, 16, 46, 0.1); border-color: rgba(200, 16, 46, 0.5);">
                <div class="term-full" style="font-size: 1.3rem; margin-bottom: 1rem;">{current_term['full_name']}</div>
                <div class="term-definition">{current_term['definition']}</div>
                <br>
                <span class="category-badge">{current_term['category']}</span>
                <span class="category-badge difficulty-{current_term['difficulty'].lower()}">{current_term['difficulty']}</span>
            </div>
            """, unsafe_allow_html=True)
        
        # Shuffle button
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔀 Shuffle Cards", use_container_width=True):
            import random
            shuffled = list(range(len(filtered_df)))
            random.shuffle(shuffled)
            st.session_state.shuffled_indices = shuffled
            st.session_state.flashcard_index = 0
            st.session_state.show_answer = False
            st.rerun()
        
        # Reset to original order button
        if st.session_state.shuffled_indices is not None:
            if st.button("↩️ Reset Order", use_container_width=True):
                st.session_state.shuffled_indices = None
                st.session_state.flashcard_index = 0
                st.session_state.show_answer = False
                st.rerun()
    else:
        st.warning("No terms match your current filters.")

# Gemini AI Additions Section
existing_terms = df['term'].tolist()

render_ai_section(
    page_name='dictionary',
    card_type='dictionary',
    generate_func=gemini.get_dictionary_additions,
    generate_args=(existing_terms,),
    section_title="🤖 AI-Suggested Terms"
)

# Category quick links
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("### 📚 Quick Study Categories")

category_counts = df['category'].value_counts().to_dict()

cols = st.columns(4)
for i, (category, count) in enumerate(sorted(category_counts.items())):
    with cols[i % 4]:
        if st.button(f"{category} ({count})", key=f"cat_{category}", use_container_width=True):
            st.session_state.selected_category = category
            st.rerun()

# Back button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("← Back to Home"):
    st.switch_page("app.py")

