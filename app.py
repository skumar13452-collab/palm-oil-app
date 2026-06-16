import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PalmTrack",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------
# LOGIN
# --------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🌴 PalmTrack Login")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "RK":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid Credentials")

    st.stop()

# --------------------------
# SIDEBAR
# --------------------------
with st.sidebar:
    st.title("🌴 PalmTrack")
    st.write("Estate Manager")

    page = st.radio(
        "Menu",
        [
            "Dashboard",
            "Harvest",
            "Workers",
            "Fertilizer",
            "Transport",
            "Reports"
        ]
    )

# --------------------------
# DASHBOARD
# --------------------------
if page == "Dashboard":

    st.title("🌴 Riverside Palm Estate")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Harvest", "248.5 MT", "+12%")
    col2.metric("Revenue", "₹4.12L", "+8%")
    col3.metric("Workers", "34")
    col4.metric("Fertilizer", "1.8 MT")

    df = pd.DataFrame({
        "Block": ["A", "B", "C"],
        "Tonnes": [18.2, 14.7, 22.1],
        "Status": ["Delivered", "Transit", "Delivered"]
    })

    st.dataframe(df, width="stretch")

# --------------------------
# HARVEST
# --------------------------
elif page == "Harvest":
    st.title("🌾 Harvest Management")

# --------------------------
# WORKERS
# --------------------------
elif page == "Workers":
    st.title("👨‍🌾 Workers Management")

# --------------------------
# FERTILIZER
# --------------------------
elif page == "Fertilizer":
    st.title("🧪 Fertilizer Management")

# --------------------------
# TRANSPORT
# --------------------------
elif page == "Transport":
    st.title("🚚 Transport Management")

# --------------------------
# REPORTS
# --------------------------
elif page == "Reports":
    st.title("📈 Reports")
