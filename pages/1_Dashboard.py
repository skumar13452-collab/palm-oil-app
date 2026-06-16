import streamlit as st
import pandas as pd
from utils.styles import load_css

load_css()

st.markdown("""
<div class='estate-card'>
<h2>🌴 Riverside Palm Estate</h2>
250 hectares • Block A-D
<br><br>
<b>16 Jun 2026</b>
</div>
""",unsafe_allow_html=True)

c1,c2,c3,c4=st.columns(4)

with c1:
    st.markdown("""
    <div class='metric-card'>
    <h5>Total Harvest</h5>
    <h2>248.5 MT</h2>
    </div>
    """,unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='metric-card'>
    <h5>Revenue</h5>
    <h2>₹4.12L</h2>
    </div>
    """,unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='metric-card'>
    <h5>Workers</h5>
    <h2>34</h2>
    </div>
    """,unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='metric-card'>
    <h5>Fertilizer</h5>
    <h2>1.8 MT</h2>
    </div>
    """,unsafe_allow_html=True)

left,right=st.columns([2,1])

with left:

    st.subheader("Recent Cuttings")

    data=pd.DataFrame({
        "Work":["Morning Cut A","Evening Cut B","Morning Cut C"],
        "Block":["A","B","C"],
        "Tonnes":[18.2,14.7,22.1],
        "Status":["Delivered","In Transit","Delivered"]
    })

    st.dataframe(data,use_container_width=True)

with right:

    st.subheader("Transport Today")

    st.info("TN01AB1234 - Completed")
    st.warning("TN02CD5678 - En Route")
