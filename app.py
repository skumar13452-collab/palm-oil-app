import streamlit as st

st.set_page_config(
    page_title="PalmTrack",
    page_icon="🌴",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0d3d0d,#145214,#0d3d0d);
}

.main-title{
text-align:center;
color:white;
font-size:40px;
font-weight:bold;
}

.sub-title{
text-align:center;
color:#d0d0d0;
margin-bottom:30px;
}

.phone{
background:white;
border-radius:25px;
padding:15px;
height:700px;
box-shadow:0px 5px 20px rgba(0,0,0,0.3);
}

.card{
background:#f5f5f5;
padding:15px;
border-radius:15px;
margin-bottom:15px;
}

.green{
background:#e9f7e9;
}

.metric{
font-size:28px;
font-weight:bold;
color:#2e7d32;
}

.header{
background:#2e7d32;
padding:15px;
border-radius:15px;
color:white;
text-align:center;
margin-bottom:15px;
}

.feature{
padding:15px;
border-radius:15px;
color:white;
height:130px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='main-title'>PalmTrack</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Farm Management · Fruit Cutting · Fertilizer · Revenue</div>",
    unsafe_allow_html=True
)

col1,col2,col3=st.columns(3)

# DASHBOARD
with col1:

    st.markdown("<div class='phone'>",unsafe_allow_html=True)

    st.markdown("""
    <div class='header'>
    <h3>Dashboard</h3>
    June 2026 - All Blocks
    </div>
    """,unsafe_allow_html=True)

    a,b=st.columns(2)

    with a:
        st.markdown("""
        <div class='card green'>
        Total Harvest
        <div class='metric'>4,820</div>
        kg
        </div>
        """,unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class='card'>
        Fertilizer
        <div class='metric'>380</div>
        kg used
        </div>
        """,unsafe_allow_html=True)

    st.markdown("""
    <div class='card green'>
    Revenue This Month
    <div class='metric'>₹1,24,000</div>
    </div>
    """,unsafe_allow_html=True)

    st.bar_chart({
        "Block A":[70],
        "Block B":[40],
        "Block C":[60]
    })

    st.markdown("""
    <div class='card'>
    📅 Block C Cutting - 12 Jun
    </div>
    """,unsafe_allow_html=True)

    st.markdown("</div>",unsafe_allow_html=True)

# FRUIT CUTTING
with col2:

    st.markdown("<div class='phone'>",unsafe_allow_html=True)

    st.markdown("""
    <div class='header'>
    <h3>Fruit Cutting</h3>
    Record & Track Harvest
    </div>
    """,unsafe_allow_html=True)

    st.text_input("Date","10/06/2026")
    st.text_input("Block","A")
    st.text_input("Workers","6")
    st.text_input("Qty (kg)","820")

    st.button("➕ Add")

    st.markdown("### Recent Records")

    st.dataframe(
        {
            "Date":["10 Jun","09 Jun","08 Jun"],
            "Block":["A","B","C"],
            "Qty":[820,640,510]
        },
        use_container_width=True
    )

    st.success("This Week Total : 3340 kg")

    st.markdown("</div>",unsafe_allow_html=True)

# REVENUE
with col3:

    st.markdown("<div class='phone'>",unsafe_allow_html=True)

    st.markdown("""
    <div class='header'>
    <h3>Revenue & Fertilizer</h3>
    Track Income & Inputs
    </div>
    """,unsafe_allow_html=True)

    st.dataframe(
        {
            "Date":["10 Jun","09 Jun","07 Jun"],
            "Amount":[19680,15360,17940]
        },
        use_container_width=True
    )

    st.metric(
        "Total Revenue",
        "₹1,24,000"
    )

    st.markdown("Block A - NPK")
    st.progress(80)

    st.markdown("Block B - Urea")
    st.progress(55)

    st.markdown("Block C - MOP")
    st.progress(30)

    st.markdown("Block C - CIRP")
    st.progress(65)

    st.markdown("</div>",unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

st.markdown(
    "<h3 style='text-align:center;color:white'>Key Features</h3>",
    unsafe_allow_html=True
)

f1,f2,f3,f4=st.columns(4)

with f1:
    st.markdown("""
    <div class='feature' style='background:#2e7d32'>
    <h4>✂ Fruit Cutting</h4>
    Track workers and harvest
    </div>
    """,unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class='feature' style='background:#827717'>
    <h4>💧 Fertilizer</h4>
    NPK, Urea, MOP Tracking
    </div>
    """,unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class='feature' style='background:#00695c'>
    <h4>₹ Revenue</h4>
    Income & Profit Reports
    </div>
    """,unsafe_allow_html=True)

with f4:
    st.markdown("""
    <div class='feature' style='background:#0d47a1'>
    <h4>📊 Reports</h4>
    Monthly Analytics
    </div>
    """,unsafe_allow_html=True)
