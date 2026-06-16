import streamlit as st
from utils.db import conn

st.title("👨‍🌾 Workers")

with st.form("worker"):

    name=st.text_input("Name")
    phone=st.text_input("Phone")
    salary=st.number_input("Salary")

    photo=st.file_uploader("Photo")

    if st.form_submit_button("Add Worker"):

        conn.execute("""
        INSERT INTO workers(name,phone,salary,photo)
        VALUES(?,?,?,?)
        """,(name,phone,salary,""))

        conn.commit()

        st.success("Worker Added")
