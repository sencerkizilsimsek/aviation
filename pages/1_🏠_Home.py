"""
Redirect to main app
"""
import streamlit as st

st.set_page_config(
    page_title="THY Cadet Pilot Prep",
    page_icon="✈️",
    layout="wide"
)

# Redirect to main app
st.switch_page("app.py")

