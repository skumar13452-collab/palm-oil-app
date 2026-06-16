import streamlit as st
from utils.auth import login
from utils.styles import load_css

st.set_page_config(
    page_title="PalmTrack",
    page_icon="🌴",
    layout="wide"
)

load_css()
login()

st.markdown("""
<div class='estate-card'>
<h2>🌴 Riverside Palm Estate</h2>
250 hectares • Block A-D
<br><br>
<b>16 Jun 2026</b>
</div>
""", unsafe_allow_html=True)

st.write("Dashboard content here...")
