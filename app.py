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

st.switch_page("pages/1_Dashboard.py")
