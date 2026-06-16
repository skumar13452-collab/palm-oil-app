import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .stApp{
        background:#f4f3ee;
    }

    section[data-testid="stSidebar"]{
        background:linear-gradient(180deg,#103d17,#0d2f13);
    }

    .metric-card{
        background:#eceae4;
        padding:20px;
        border-radius:15px;
        box-shadow:0 2px 8px rgba(0,0,0,.08);
    }

    .estate-card{
        background:linear-gradient(90deg,#1c4d1a,#387820);
        color:white;
        padding:25px;
        border-radius:15px;
        margin-bottom:20px;
    }

    </style>
    """,unsafe_allow_html=True)
