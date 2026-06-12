import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="PalmTrack",
    page_icon="🌴",
    layout="wide"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0b4d0b,#0f6a0f,#0b4d0b);
}

.main-title{
    text-align:center;
    color:white;
    font-size:42px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#d9d9d9;
    margin-bottom:20px;
}

.block-container{
    padding-top:1rem;
}

div[data-testid="stMetric"]{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.15);
}

.section-box{
    background:white;
    padding:15px;
    border-radius:20px;
    margin-bottom:15px;
}

h3{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    "<div class='main-title'>🌴 PalmTrack</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Farm Management • Fruit Cutting • Fertilizer • Revenue</div>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# TOP METRICS
# --------------------------------------------------
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("🌴 Total Harvest", "4,820 kg", "+12%")

with m2:
    st.metric("💧 Fertilizer Used", "380 kg", "+5%")

with m3:
    st.metric("💰 Revenue", "₹1,24,000", "+18%")

with m4:
    st.metric("👷 Workers", "26", "+2")

st.markdown("---")

# --------------------------------------------------
# MAIN DASHBOARD
# --------------------------------------------------
col1, col2, col3 = st.columns([1.2,1.1,1])

# ==================================================
# DASHBOARD
# ==================================================
with col1:

    st.subheader("📊 Dashboard")

    chart_df = pd.DataFrame(
        {
            "Harvest":[70,40,60,55]
        },
        index=["Block A","Block B","Block C","Block D"]
    )

    st.bar_chart(chart_df)

    st.info("📅 Upcoming Cutting : Block C - 12 Jun")

    revenue_chart = pd.DataFrame({
        "Revenue":[18000,22000,27000,32000]
    }, index=["Week 1","Week 2","Week 3","Week 4"])

    st.line_chart(revenue_chart)

# ==================================================
# FRUIT CUTTING
# ==================================================
with col2:

    st.subheader("✂ Fruit Cutting")

    date = st.date_input("Date")

    block = st.selectbox(
        "Block",
        ["A","B","C","D"]
    )

    workers = st.number_input(
        "Workers",
        min_value=1,
        value=6
    )

    qty = st.number_input(
        "Quantity (kg)",
        min_value=0,
        value=820
    )

    if st.button("➕ Add Record"):
        st.success("Harvest Record Added Successfully")

    st.markdown("### Recent Records")

    recent_df = pd.DataFrame({
        "Date":["10 Jun","09 Jun","08 Jun"],
        "Block":["A","B","C"],
        "Qty":[820,640,510]
    })

    st.dataframe(
        recent_df,
        use_container_width=True
    )

# ==================================================
# REVENUE & FERTILIZER
# ==================================================
with col3:

    st.subheader("💰 Revenue & Fertilizer")

    revenue_df = pd.DataFrame({
        "Date":["10 Jun","09 Jun","07 Jun"],
        "Amount":[19680,15360,17940]
    })

    st.dataframe(
        revenue_df,
        use_container_width=True
    )

    st.metric(
        "Total Revenue",
        "₹1,24,000"
    )

    st.markdown("##### Block A - NPK")
    st.progress(80)

    st.markdown("##### Block B - Urea")
    st.progress(55)

    st.markdown("##### Block C - MOP")
    st.progress(30)

    st.markdown("##### Block D - CIRP")
    st.progress(65)

# --------------------------------------------------
# FEATURE CARDS
# --------------------------------------------------
st.markdown("---")
st.subheader("🚀 Key Features")

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.success("""
    ✂ Fruit Cutting

    Track harvest quantity,
    workers and block details.
    """)

with f2:
    st.info("""
    💧 Fertilizer

    Manage NPK, Urea,
    MOP and CIRP usage.
    """)

with f3:
    st.warning("""
    💰 Revenue

    Income, expenses
    and profit tracking.
    """)

with f4:
    st.error("""
    📊 Reports

    Monthly analytics
    and export reports.
    """)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.markdown(
    "<center style='color:white'>PalmTrack © 2026 - Palm Oil Farm Management System</center>",
    unsafe_allow_html=True
)
