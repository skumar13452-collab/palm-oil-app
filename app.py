import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ------------------------
# CONFIG
# ------------------------
st.set_page_config(
    page_title="Anumolu's Palm Oil Management",
    page_icon="🌴",
    layout="wide"
)

FILE_NAME = "harvest_data.xlsx"

os.makedirs("uploads", exist_ok=True)

# ------------------------
# HEADER
# ------------------------
st.markdown("""
<style>
.main-header {
    background: linear-gradient(90deg,#1b5e20,#4caf50);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
}

.metric-card {
    background:#f1f8e9;
    padding:15px;
    border-radius:12px;
    border-left:6px solid green;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🌴 Anumolu's Palm Oil Management System</h1>
    <h4>Harvest Tracking | Revenue Analytics | Card Management</h4>
</div>
""", unsafe_allow_html=True)

st.write("")

# ------------------------
# LOAD DATA
# ------------------------
if os.path.exists(FILE_NAME):
    df = pd.read_excel(FILE_NAME)
else:
    df = pd.DataFrame(columns=[
        "Date",
        "Plot",
        "Weight",
        "Price",
        "Amount",
        "Card Number",
        "Image"
    ])

# ------------------------
# KPI SECTION
# ------------------------
total_weight = df["Weight"].sum() if not df.empty else 0
total_revenue = df["Amount"].sum() if not df.empty else 0
avg_price = df["Price"].mean() if not df.empty else 0
total_records = len(df)

c1, c2, c3, c4 = st.columns(4)

c1.metric("🌴 Total Harvest", f"{total_weight:.2f} Tons")
c2.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
c3.metric("📈 Avg Price", f"₹{avg_price:,.0f}")
c4.metric("📋 Records", total_records)

st.divider()

# ------------------------
# HARVEST ENTRY
# ------------------------
st.subheader("➕ New Harvest Entry")

left, right = st.columns(2)

with left:

    date = st.date_input("Harvest Date")

    plot = st.selectbox(
        "Plot Name",
        [
            "North Plantation",
            "South Plantation",
            "East Plantation",
            "West Plantation"
        ]
    )

    card_no = st.text_input(
        "Harvester Card Number"
    )

    weight = st.number_input(
        "Harvest Weight (Tons)",
        min_value=0.0,
        step=0.1
    )

with right:

    price = st.number_input(
        "Price Per Ton",
        min_value=0.0
    )

    amount = weight * price

    st.success(
        f"💰 Total Amount : ₹{amount:,.2f}"
    )

    uploaded_file = st.file_uploader(
        "Upload Harvester Card",
        type=["jpg","jpeg","png"]
    )

    if uploaded_file:
        st.image(
            uploaded_file,
            width=300
        )

if st.button("💾 Save Harvest Record"):

    image_name = ""

    if uploaded_file:

        image_name = uploaded_file.name

        image_path = os.path.join(
            "uploads",
            image_name
        )

        with open(image_path, "wb") as f:
            f.write(
                uploaded_file.getbuffer()
            )

    new_row = pd.DataFrame({
        "Date":[date],
        "Plot":[plot],
        "Weight":[weight],
        "Price":[price],
        "Amount":[amount],
        "Card Number":[card_no],
        "Image":[image_name]
    })

    df = pd.concat(
        [df,new_row],
        ignore_index=True
    )

    df.to_excel(
        FILE_NAME,
        index=False
    )

    st.success(
        "Record Saved Successfully"
    )

st.divider()

# ------------------------
# ANALYTICS
# ------------------------
if not df.empty:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📊 Revenue by Plantation")

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

    with col2:

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

# ------------------------
# RECORDS
# ------------------------
st.subheader("📋 Harvest Records")

st.dataframe(
    df,
    use_container_width=True
)

# ------------------------
# DOWNLOAD
# ------------------------
if os.path.exists(FILE_NAME):

    with open(FILE_NAME, "rb") as file:

        st.download_button(
            "📥 Download Excel Report",
            file,
            file_name="PalmOilReport.xlsx"
        )
