import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="Anumolu's Palm Oil Management",
    page_icon="🌴",
    layout="wide"
)

FILE_NAME = "harvest_data.xlsx"

os.makedirs("uploads/cards", exist_ok=True)
os.makedirs("uploads/slips", exist_ok=True)

# -----------------------------
# LOGIN
# -----------------------------
USERNAME = "Anumolu"
PASSWORD = "RK"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.markdown("""
    <div style='text-align:center;padding-top:50px'>
        <h1 style='color:green'>
            🌴 Anumolu's Palm Oil Management System
        </h1>
        <h3>Login</h3>
    </div>
    """, unsafe_allow_html=True)

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):

        if user == USERNAME and pwd == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid Username or Password")

    st.stop()

# -----------------------------
# LOAD DATA
# -----------------------------
if os.path.exists(FILE_NAME):
    df = pd.read_excel(FILE_NAME)
else:
    df = pd.DataFrame(columns=[
        "Date",
        "Plot",
        "Card No",
        "Weight",
        "Price Per Tone ",
        "Total Amount",
        "Remarks",
        "Card Image",
        "Slip Image"
    ])

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.main-header{
background: linear-gradient(90deg,#1B5E20,#43A047);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
margin-bottom:20px;
}

.card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 3px 8px rgba(0,0,0,0.1);
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
col1,col2 = st.columns([10,1])

with col1:
    st.markdown("""
    <div class="main-header">
    <h1>🌴 Anumolu's Palm Oil Management System</h1>
    <h4>Harvest Tracking • Revenue Analytics • Card Management</h4>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.write("")
    st.write("")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# -----------------------------
# KPI
# -----------------------------
total_weight = df["Weight"].sum() if not df.empty else 0
total_amount = df["Amount"].sum() if not df.empty else 0
avg_price = df["Price"].mean() if not df.empty else 0
records = len(df)

c1,c2,c3,c4 = st.columns(4)

c1.metric("🌴 Total Harvest", f"{total_weight:.2f} Tons")
c2.metric("💰 Total Revenue", f"₹{total_amount:,.0f}")
c3.metric("📈 Avg Price", f"₹{avg_price:,.0f}")
c4.metric("📋 Records", records)

st.divider()

# -----------------------------
# ENTRY FORM
# -----------------------------
st.subheader("➕ New Harvest Entry")

left,right = st.columns(2)

with left:

    date = st.date_input("Harvest Date")

    plot = st.text_input("Plot Name")

    card_no = st.text_input("Harvester Card Number")

    weight = st.number_input(
        "Weight (Tons)",
        min_value=0.0,
        step=0.1
    )

with right:

    price_per_Tone = st.number_input(
        "Price Per Ton",
        min_value=0.0
    )

    remarks = st.text_area(
        "Remarks"
    )

    amount = weight * price

    st.success(
        f"💰 Total Amount : ₹{amount:,.2f}"
    )

card_image = st.file_uploader(
    "Upload Harvester Card",
    type=["jpg","jpeg","png"]
)

slip_image = st.file_uploader(
    "Upload Weight Slip",
    type=["jpg","jpeg","png"]
)

if card_image:
    st.image(card_image,width=300)

if slip_image:
    st.image(slip_image,width=300)

if st.button("💾 Save Harvest Record"):

    card_name = ""
    slip_name = ""

    if card_image:

        card_name = card_image.name

        with open(
            os.path.join(
                "uploads/cards",
                card_name
            ),
            "wb"
        ) as f:
            f.write(card_image.getbuffer())

    if slip_image:

        slip_name = slip_image.name

        with open(
            os.path.join(
                "uploads/slips",
                slip_name
            ),
            "wb"
        ) as f:
            f.write(slip_image.getbuffer())

    new_row = pd.DataFrame({
        "Date":[date],
        "Plot":[plot],
        "Card No":[card_no],
        "Weight":[weight],
        "Price":[price],
        "Amount":[amount],
        "Remarks":[remarks],
        "Card Image":[card_name],
        "Slip Image":[slip_name]
    })

    df = pd.concat(
        [df,new_row],
        ignore_index=True
    )

    df.to_excel(FILE_NAME,index=False)

    st.success(
        "Record Saved Successfully"
    )

    st.rerun()

st.divider()

# -----------------------------
# CHARTS
# -----------------------------
if not df.empty:

    ch1,ch2 = st.columns(2)

    with ch1:

        st.subheader("📊 Revenue By Plot")

        fig1 = px.bar(
            df,
            x="Plot",
            y="Amount",
            color="Plot",
            text_auto=True
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with ch2:

        st.subheader("📈 Harvest Trend")

        fig2 = px.line(
            df,
            x="Date",
            y="Weight",
            markers=True
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

st.divider()

# -----------------------------
# RECORDS
# -----------------------------
st.subheader("📋 Harvest Records")

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------
# DOWNLOAD
# -----------------------------
if os.path.exists(FILE_NAME):

    with open(FILE_NAME,"rb") as f:

        st.download_button(
            "📥 Download Excel Report",
            f,
            file_name="RK_PalmOilReport.xlsx"
        )
