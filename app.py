import streamlit as st
import pandas as pd

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="PalmTrack",
    page_icon="🌴",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0d3d0d,#145214,#0d3d0d);
}

.main-title{
    text-align:center;
    color:white;
    font-size:42px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#dddddd;
    margin-bottom:25px;
}

.card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0 4px 15px rgba(0,0,0,0.15);
    min-height:650px;
}

.section-title{
    background:#2e7d32;
    color:white;
    padding:12px;
    border-radius:12px;
    text-align:center;
    font-weight:bold;
    margin-bottom:15px;
}

.metric-box{
    background:#e8f5e9;
    padding:15px;
    border-radius:12px;
    text-align:center;
    margin-bottom:10px;
}

.metric-value{
    font-size:30px;
    font-weight:bold;
    color:#2e7d32;
}

.feature{
    padding:20px;
    border-radius:15px;
    color:white;
    text-align:center;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# TITLE
# -------------------------
st.markdown(
    "<div class='main-title'>🌴 PalmTrack</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Farm Management • Fruit Cutting • Fertilizer • Revenue</div>",
    unsafe_allow_html=True
)

# -------------------------
# MAIN 3 MODULES
# -------------------------
col1, col2, col3 = st.columns(3)

# ==================================================
# DASHBOARD
# ==================================================
with col1:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("""
    <div class='section-title'>
        Dashboard<br>
        June 2026 - All Blocks
    </div>
    """, unsafe_allow_html=True)

    a, b = st.columns(2)

    with a:
        st.markdown("""
        <div class='metric-box'>
        Total Harvest
        <div class='metric-value'>4,820</div>
        kg
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class='metric-box'>
        Fertilizer
        <div class='metric-value'>380</div>
        kg
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class='metric-box'>
    Revenue This Month
    <div class='metric-value'>₹1,24,000</div>
    </div>
    """, unsafe_allow_html=True)

    chart_data = pd.DataFrame(
        {
            "Harvest":[70,40,60]
        },
        index=["Block A","Block B","Block C"]
    )

    st.bar_chart(chart_data)

    st.info("📅 Upcoming Cutting : Block C - 12 Jun")

    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# FRUIT CUTTING
# ==================================================
with col2:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("""
    <div class='section-title'>
        Fruit Cutting<br>
        Record & Track Harvest
    </div>
    """, unsafe_allow_html=True)

    st.text_input("Date", "10/06/2026")
    st.text_input("Block", "A")
    st.text_input("Workers", "6")
    st.text_input("Quantity (kg)", "820")

    st.button("➕ Add Record")

    st.markdown("### Recent Records")

    df = pd.DataFrame({
        "Date":["10 Jun","09 Jun","08 Jun"],
        "Block":["A","B","C"],
        "Qty":[820,640,510]
    })

    st.dataframe(df, use_container_width=True)

    st.success("Weekly Harvest : 3340 kg")

    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# REVENUE & FERTILIZER
# ==================================================
with col3:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("""
    <div class='section-title'>
        Revenue & Fertilizer<br>
        Track Income & Inputs
    </div>
    """, unsafe_allow_html=True)

    revenue_df = pd.DataFrame({
        "Date":["10 Jun","09 Jun","07 Jun"],
        "Amount":[19680,15360,17940]
    })

    st.dataframe(revenue_df, use_container_width=True)

    st.metric("Total Revenue", "₹1,24,000")

    st.write("Block A - NPK")
    st.progress(80)

    st.write("Block B - Urea")
    st.progress(55)

    st.write("Block C - MOP")
    st.progress(30)

    st.write("Block D - CIRP")
    st.progress(65)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# FEATURES
# -------------------------
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<h3 style='text-align:center;color:white;'>Key Features</h3>",
    unsafe_allow_html=True
)

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.markdown("""
    <div class='feature' style='background:#2e7d32'>
    ✂ Fruit Cutting<br><br>
    Track harvest and workers
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class='feature' style='background:#827717'>
    💧 Fertilizer<br><br>
    NPK • Urea • MOP Tracking
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class='feature' style='background:#00695c'>
    ₹ Revenue<br><br>
    Income & Profit Reports
    </div>
    """, unsafe_allow_html=True)

with f4:
    st.markdown("""
    <div class='feature' style='background:#0d47a1'>
    📊 Reports<br><br>
    Monthly Analytics
    </div>
    """, unsafe_allow_html=True)
