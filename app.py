# ==================================================
# PAGE CONFIG
# ==================================================
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PalmTrack Estate Manager",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# CSS
# ==================================================
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background-color:#0f172a;
    color:white;
}

/* FORCE SIDEBAR WIDTH */
section[data-testid="stSidebar"]{
    min-width:300px !important;
    max-width:300px !important;
    background:linear-gradient(180deg,#064e3b,#14532d);
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

[data-testid="stSidebarNav"]{
    display:none;
}

.sidebar-logo{
    text-align:center;
    font-size:34px;
    font-weight:bold;
    padding-top:15px;
}

.sidebar-sub{
    text-align:center;
    color:#d1fae5;
    padding-bottom:10px;
}

.estate-card{
    background:linear-gradient(90deg,#14532d,#22c55e);
    padding:30px;
    border-radius:20px;
    color:white;
}

[data-testid="metric-container"]{
    background:#1e293b;
    border:1px solid #334155;
    border-radius:15px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# LOGIN
# ==================================================
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

# ==================================================
# SIDEBAR
# ==================================================
with st.sidebar:

    st.markdown(
        "<div class='sidebar-logo'>🌴 PalmTrack</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sidebar-sub'>Estate Manager</div>",
        unsafe_allow_html=True
    )

    st.divider()

    page = st.radio(
        "MENU",
        [
            "📊 Dashboard",
            "🌾 Harvest",
            "👨‍🌾 Workers",
            "🧪 Fertilizer",
            "🚚 Transport",
            "📈 Reports"
        ]
    )

    st.divider()

    st.success("Admin Login")

# ==================================================
# DASHBOARD
# ==================================================
if page == "📊 Dashboard":

    st.markdown("""
    <div class='estate-card'>
    <h1>🌴 Riverside Palm Estate</h1>
    <h4>250 Hectares • Block A-D</h4>
    <h4>Season Jan-Dec 2026</h4>
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.metric("TOTAL HARVEST","248.5 MT","+12%")

    with c2:
        st.metric("REVENUE","₹4.12L","+8%")

    with c3:
        st.metric("WORKERS","34","6 Leave")

    with c4:
        st.metric("FERTILIZER","1.8 MT","-5%")

    st.divider()

    left,right = st.columns([2,1])

    with left:
        st.subheader("Recent Cuttings")

        df = pd.DataFrame({
            "Work":["Morning Cut A","Evening Cut B","Morning Cut C"],
            "Block":["A","B","C"],
            "Tonnes":[18.2,14.7,22.1],
            "Status":["Delivered","In Transit","Delivered"]
        })

        st.dataframe(df, use_container_width=True)

    with right:
        st.subheader("Transport Today")

        st.success("TN01AB1234\n\nCompleted")
        st.warning("TN02CD5678\n\nEn Route")

# ==================================================
# HARVEST
# ==================================================
elif page == "🌾 Harvest":
    st.title("🌾 Harvest Management")

# ==================================================
# WORKERS
# ==================================================
elif page == "👨‍🌾 Workers":
    st.title("👨‍🌾 Workers Management")

# ==================================================
# FERTILIZER
# ==================================================
elif page == "🧪 Fertilizer":
    st.title("🧪 Fertilizer Management")

# ==================================================
# TRANSPORT
# ==================================================
elif page == "🚚 Transport":
    st.title("🚚 Transport Management")

# ==================================================
# REPORTS
# ==================================================
elif page == "📈 Reports":
    st.title("📈 Reports")
