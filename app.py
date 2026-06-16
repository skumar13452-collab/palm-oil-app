import streamlit as st
from utils.auth import login
from utils.styles import load_css

st.set_page_config(
    page_title="PalmTrack",
    page_icon="🌴",
    layout="wide"
)

load_css()
login()

st.markdown("""
<div class='estate-card'>
<h2>🌴 Riverside Palm Estate</h2>
250 hectares • Block A-D
<br><br>
<b>16 Jun 2026</b>
</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "TOTAL HARVEST",
        "248.5 MT",
        "+12%"
    )

with c2:
    st.metric(
        "REVENUE",
        "₹4.12L",
        "+8%"
    )

with c3:
    st.metric(
        "ACTIVE WORKERS",
        "34",
        "-6 Leave"
    )

with c4:
    st.metric(
        "FERTILIZER USED",
        "1.8 MT",
        "-5%"
    )

st.divider()

left,right = st.columns([2,1])

with left:

    st.subheader("✂ Recent Cuttings")

    import pandas as pd

    df = pd.DataFrame({
        "Work":[
            "Morning Cut A",
            "Evening Cut B",
            "Morning Cut C",
            "Night Cut A"
        ],
        "Block":["A","B","C","A"],
        "Tonnes":[18.2,14.7,22.1,9.8],
        "Status":[
            "Delivered",
            "In Transit",
            "Delivered",
            "Weighed"
        ]
    })

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

with right:

    st.subheader("🚚 Transport Today")

    st.success(
        "TN01AB1234\n\nLorry - 18.2T\n\nCompleted"
    )

    st.warning(
        "TN02CD5678\n\nTrailer - 14.7T\n\nEn Route"
    )

with st.sidebar:
    st.markdown("## 🌴 PalmTrack")
    st.caption("Estate Manager")

    st.divider()

    st.page_link(
        "pages/1_Dashboard.py",
        label="Dashboard",
        icon="📊"
    )

   st.sidebar.markdown("## Navigation")
page = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Harvest",
        "Workers",
        "Fertilizer",
        "Transport",
        "Reports"
    ]
)

if page == "Dashboard":
    st.title("Dashboard")

elif page == "Harvest":
    st.title("Harvest")

elif page == "Workers":
    st.title("Workers")

elif page == "Fertilizer":
    st.title("Fertilizer")

elif page == "Transport":
    st.title("Transport")

elif page == "Reports":
    st.title("Reports")

    st.page_link(
        "pages/4_Fertilizer.py",
        label="Fertilizer",
        icon="🧪"
    )

    st.page_link(
        "pages/5_Transport.py",
        label="Transport",
        icon="🚚"
    )
