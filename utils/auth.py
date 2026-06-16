import streamlit as st

USERNAME="admin"
PASSWORD="RK"

def login():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in=False

    if not st.session_state.logged_in:

        st.title("🌴 PalmTrack Login")

        user=st.text_input("Username")
        pwd=st.text_input("Password",type="password")

        if st.button("Login"):
            if user==USERNAME and pwd==PASSWORD:
                st.session_state.logged_in=True
                st.rerun()
            else:
                st.error("Invalid Credentials")

        st.stop()
