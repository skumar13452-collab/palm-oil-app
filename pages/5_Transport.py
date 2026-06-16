import streamlit as st
from utils.db import conn

st.title("🚚 Transport")

with st.form("transport"):

    vehicle=st.text_input("Vehicle Number")
    driver=st.text_input("Driver")
    tonnes=st.number_input("Tonnes")
    charge=st.number_input("Charges")

    status=st.selectbox(
        "Status",
        ["Completed","En Route","Pending"]
    )

    if st.form_submit_button("Save"):

        conn.execute("""
        INSERT INTO transport
        (vehicle_no,driver_name,tonnes,charges,status)
        VALUES(?,?,?,?,?)
        """,(vehicle,driver,tonnes,charge,status))

        conn.commit()

        st.success("Saved")
