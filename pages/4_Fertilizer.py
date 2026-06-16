import streamlit as st
from utils.db import conn

st.title("🧪 Fertilizer")

with st.form("fert"):

    fert=st.text_input("Fertilizer")
    qty=st.number_input("Quantity")
    cost=st.number_input("Cost")
    block=st.selectbox("Block",["A","B","C","D"])

    if st.form_submit_button("Save"):

        conn.execute("""
        INSERT INTO fertilizer
        (fert_type,quantity,cost,block_name)
        VALUES(?,?,?,?)
        """,(fert,qty,cost,block))

        conn.commit()

        st.success("Saved")
