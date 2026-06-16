import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="PalmTrack",
    page_icon="🌴",
    layout="wide"
)

# ---------------------------------------------------
# CSS
# ---------------------------------------------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background:#f4f3ee;
}

section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#103d17,#0d2f13);
}

.sidebar-title{
    color:white;
    font-size:24px;
    font-weight:bold;
}

.sidebar-sub{
    color:#cccccc;
    font-size:12px;
}

.estate-card{
    background:linear-gradient(90deg,#1c4d1a,#387820);
    color:white;
    padding:25px;
    border-radius:15px;
    margin-bottom:20px;
}

.metric-box{
    background:white;
    border-radius:15px;
    padding:20px;
    box-shadow:0 2px 8px rgba(0,0,0,0.08);
    text-align:center;
}

.metric-title{
    color:#666;
    font-size:12px;
}

.metric-value{
    font-size:32px;
    font-weight:bold;
    color:#222;
}

.metric-change-green{
    color:green;
    font-size:12px;
}

.metric-change-red{
    color:red;
    font-size:12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOGIN
# ---------------------------------------------------
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

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
with st.sidebar:

    st.markdown(
        "<div class='sidebar-title'>🌴 PalmTrack</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sidebar-sub'>Estate Manager</div>",
        unsafe_allow_html=True
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Harvest",
            "Workers",
            "Fertilizer",
            "Transport",
            "Reports"
        ]
    )

# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------
if page == "Dashboard":

    st.markdown("""
    <div class='estate-card'>
        <h1>🌴 Riverside Palm Estate</h1>
        <b>250 hectares • Block A-D</b>
        <br><br>
        <b>16 Jun 2026</b>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

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

    left, right = st.columns([2,1])

    with left:

        st.subheader("✂ Recent Cuttings")

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

# ---------------------------------------------------
# HARVEST
# ---------------------------------------------------
elif page == "Harvest":

    st.title("🌾 Harvest Management")

    date = st.date_input("Harvest Date")

    block = st.selectbox(
        "Block",
        ["A","B","C","D","E"]
    )

    tonnes = st.number_input(
        "Tonnes",
        min_value=0.0
    )

    slip = st.file_uploader(
        "Upload Harvest Slip"
    )

    if st.button("Save Harvest"):
        st.success("Harvest Saved")

# ---------------------------------------------------
# WORKERS
# ---------------------------------------------------
elif page == "Workers":

    st.title("👨‍🌾 Workers")

    name = st.text_input("Worker Name")
    phone = st.text_input("Phone")
    salary = st.number_input("Salary")

    photo = st.file_uploader(
        "Worker Photo"
    )

    if st.button("Add Worker"):
        st.success("Worker Added")

# ---------------------------------------------------
# FERTILIZER
# ---------------------------------------------------
elif page == "Fertilizer":

    st.title("🧪 Fertilizer")

    fert = st.text_input("Fertilizer Name")

    qty = st.number_input(
        "Quantity",
        min_value=0.0
    )

    cost = st.number_input(
        "Cost",
        min_value=0.0
    )

    block = st.selectbox(
        "Block",
        ["A","B","C","D"]
    )

    if st.button("Save Fertilizer"):
        st.success("Fertilizer Saved")

# ---------------------------------------------------
# TRANSPORT
# ---------------------------------------------------
elif page == "Transport":

    st.title("🚚 Transport")

    vehicle = st.text_input(
        "Vehicle Number"
    )

    driver = st.text_input(
        "Driver Name"
    )

    tonnes = st.number_input(
        "Tonnes",
        min_value=0.0
    )

    charges = st.number_input(
        "Charges",
        min_value=0.0
    )

    status = st.selectbox(
        "Status",
        [
            "Completed",
            "En Route",
            "Pending"
        ]
    )

    if st.button("Save Transport"):
        st.success("Transport Saved")

# ---------------------------------------------------
# REPORTS
# ---------------------------------------------------
elif page == "Reports":

    st.title("📊 Reports")

    report_df = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr"],
        "Harvest":[220,235,248,260]
    })

    st.dataframe(
        report_df,
        use_container_width=True
    )

    st.bar_chart(
        report_df.set_index("Month")
    )
