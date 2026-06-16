import streamlit as st
from utils.db import conn

st.title("🌴 Harvest Management")

with st.form("harvest"):

    date=st.date_input("Date")
    block=st.selectbox("Block",["A","B","C","D","E"])
    tonnes=st.number_input("Tonnes")

    slip=st.file_uploader("Harvest Slip")

    submit=st.form_submit_button("Save")

    if submit:

        conn.execute("""
        INSERT INTO harvest
        (harvest_date,block_name,tonnes,slip_file)
        VALUES(?,?,?,?)
        """,
        (str(date),block,tonnes,""))

        conn.commit()

        st.success("Saved")
