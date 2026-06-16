import streamlit as st
import pandas as pd

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="PalmTrack Estate Manager",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# DARK THEME CSS
# ==================================================
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background:#0f172a;
    color:white;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#052e16,#14532d);
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Header Card */
.estate-card{
    background:linear-gradient(90deg,#14532d,#22c55e);
    padding:30px;
    border-radius:18px;
    color:white;
    margin-bottom:20px;
    box-shadow:0px 5px 20px rgba(0,0,0,.35);
}

/* Cards */
.card{
    background:#1e293b;
    border-radius:15px;
    padding:20px;
    border:1px solid #334155;
    box-shadow:0px 4px 12px rgba(0,0,0,.2);
}

/* Metric Cards */
[data-testid="metric-container"]{
    background:#1e293b;
    border:1px solid #334155;
    border-radius:15px;
    padding:15px;
}

[data-testid="metric-container"] label{
    color:#cbd5e1 !important;
}

[data-testid="metric-container"] div{
    color:white !important;
}

/* Inputs */
.stTextInput input,
.stNumberInput input,
.stDateInput input{
    background:#1e293b !important;
    color:white !important;
}

/* Buttons */
.stButton button{
    background:#16a34a;
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
}

.stButton button:hover{
    background:#22c55e;
}

/* Dataframe */
[data-testid="stDataFrame"]{
    border-radius:15px;
    overflow:hidden;
}

h1,h2,h3,h4,h5,h6{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# LOGIN
# ==================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.markdown("""
    <div style="text-align:center;padding-top:100px;">
        <h1>🌴 PalmTrack Estate Manager</h1>
        <h4>Login to Continue</h4>
    </div>
    """, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,1,1])

    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):

            if username == "admin" and password == "RK":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Credentials")

    st.stop()

# ==================================================
# SIDEBAR
# ==================================================
with st.sidebar:

    st.markdown("## 🌴 PalmTrack")
    st.caption("Estate Manager")

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

# ==================================================
# DASHBOARD
# ==================================================
if page == "Dashboard":

    st.markdown("""
    <div class="estate-card">
        <h1>🌴 Riverside Palm Estate</h1>
        <h4>250 Hectares • Block A-D • Season Jan-Dec 2026</h4>
        <h3>16 Jun 2026</h3>
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.metric("TOTAL HARVEST", "248.5 MT", "+12%")

    with c2:
        st.metric("REVENUE", "₹4.12L", "+8%")

    with c3:
        st.metric("ACTIVE WORKERS", "34", "-6 Leave")

    with c4:
        st.metric("FERTILIZER USED", "1.8 MT", "-5%")

    st.write("")

    left,right = st.columns([2,1])

    with left:

        st.subheader("✂ Recent Cuttings")

        df = pd.DataFrame({
            "Work":["Morning Cut A","Evening Cut B","Morning Cut C","Night Cut A"],
            "Block":["A","B","C","A"],
            "Tonnes":[18.2,14.7,22.1,9.8],
            "Status":["Delivered","In Transit","Delivered","Weighed"]
        })

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    with right:

        st.subheader("🚚 Transport Today")

        st.success("""
TN01 AB 1234

Lorry • 18.2 MT

Completed
""")

        st.warning("""
TN02 CD 5678

Trailer • 14.7 MT

En Route
""")

# ==================================================
# HARVEST
# ==================================================
elif page == "Harvest":

    st.title("🌾 Harvest Management")

    date = st.date_input("Harvest Date")

    block = st.selectbox(
        "Block",
        ["A","B","C","D","E"]
    )

    tonnes = st.number_input(
        "Harvest (MT)",
        min_value=0.0
    )

    slip = st.file_uploader(
        "Upload Harvest Slip"
    )

    if st.button("Save Harvest"):
        st.success("Harvest Saved Successfully")

# ==================================================
# WORKERS
# ==================================================
elif page == "Workers":

    st.title("👨‍🌾 Workers Management")

    worker_name = st.text_input(
        "Worker Name"
    )

    phone = st.text_input(
        "Phone Number"
    )

    salary = st.number_input(
        "Salary",
        min_value=0
    )

    photo = st.file_uploader(
        "Worker Photo"
    )

    if st.button("Add Worker"):
        st.success("Worker Added Successfully")

# ==================================================
# FERTILIZER
# ==================================================
elif page == "Fertilizer":

    st.title("🧪 Fertilizer Management")

    fert_name = st.text_input(
        "Fertilizer Name"
    )

    quantity = st.number_input(
        "Quantity (MT)",
        min_value=0.0
    )

    cost = st.number_input(
        "Cost",
        min_value=0
    )

    block = st.selectbox(
        "Block",
        ["A","B","C","D"]
    )

    if st.button("Save Fertilizer"):
        st.success("Fertilizer Saved")

# ==================================================
# TRANSPORT
# ==================================================
elif page == "Transport":

    st.title("🚚 Transport Management")

    vehicle = st.text_input(
        "Vehicle Number"
    )

    driver = st.text_input(
        "Driver Name"
    )

    tonnes = st.number_input(
        "Weight (MT)",
        min_value=0.0
    )

    charges = st.number_input(
        "Transport Charges",
        min_value=0
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

# ==================================================
# REPORTS
# ==================================================
elif page == "Reports":

    st.title("📈 Reports")

    report_df = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May","Jun"],
        "Harvest":[210,220,235,248,255,270]
    })

    st.dataframe(
        report_df,
        use_container_width=True,
        hide_index=True
    )

    st.bar_chart(
        report_df.set_index("Month")
    )

    csv = report_df.to_csv(index=False)

    st.download_button(
        "⬇ Download CSV Report",
        csv,
        "harvest_report.csv",
        "text/csv"
    )
