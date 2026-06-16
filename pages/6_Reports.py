import streamlit as st
import pandas as pd
from utils.db import conn

st.title("📊 Reports")

df=pd.read_sql_query(
    "SELECT * FROM harvest",
    conn
)

st.dataframe(df,use_container_width=True)

excel=df.to_excel("harvest_report.xlsx",index=False)

with open("harvest_report.xlsx","rb") as f:

    st.download_button(
        "Download Excel",
        f,
        "harvest_report.xlsx"
    )
