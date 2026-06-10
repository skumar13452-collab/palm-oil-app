import streamlit as st
import pandas as pd
import plotly.express as px
import os

FILE_NAME = "harvest_data.xlsx"

st.set_page_config(
    page_title="Anumolu's Palm Oil Management",
    page_icon="🌴",
    layout="wide"
)

# Header
st.markdown("""
<div style="
background-color:#2E8B57;
padding:15px;
border-radius:10px;
text-align:center;">
<h1 style="color:white;">
🌴 Anumolu's Palm Oil Management System
</h1>
<h4 style="color:white;">
Harvest Tracking & Revenue Management
</h4>
</div>
""", unsafe_allow_html=True)

st.write("")

# Create uploads folder
os.makedirs("uploads", exist_ok=True)

# Load existing data
if os.path.exists(FILE_NAME):
    df = pd.read_excel(FILE_NAME)
else:
    df = pd.DataFrame(columns=[
        "Date",
        "Plot",
        "Weight",
        "Price",
        "Amount",
        "Image"
    ])

# Dashboard Cards
total_weight = df["Weight"].sum() if not df.empty else 0
total_amount = df["Amount"].sum() if not df.empty else 0
avg_price = df["Price"].mean() if not df.empty else 0

c1, c2, c3 = st.columns(3)

c1.metric("🌴 Total Harvest", f"{total_weight:.2f} Tons")
c2.metric("💰 Total Revenue", f"₹{total_amount:,.0f}")
c3.metric("📈 Avg Price/Ton", f"₹{avg_price:,.0f}")

st.divider()

# Harvest Entry
st.subheader("➕ New Harvest Entry")

col1, col2 = st.columns(2)

with col1:

    date = st.date_input("Harvest Date")

    plot = st.selectbox(
        "Plot Name",
        ["Plot-A", "Plot-B", "Plot-C"]
    )

    weight = st.number_input(
        "Weight (Tons)",
        min_value=0.0,
        step=0.1
    )

with col2:

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
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.image(
        uploaded_file,
        width=300
    )

if st.button("💾 Save Record"):

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
        "Image":[image_name]
    })

    df = pd.concat(
        [df, new_row],
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

# Charts
if not df.empty:

    st.subheader("📊 Revenue by Plot")

    chart1 = px.bar(
        df,
        x="Plot",
        y="Amount",
        color="Plot"
    )

    st.plotly_chart(
        chart1,
        use_container_width=True
    )

    st.subheader("📈 Harvest Trend")

    chart2 = px.line(
        df,
        x="Date",
        y="Weight",
        markers=True
    )

    st.plotly_chart(
        chart2,
        use_container_width=True
    )

st.divider()

# Records
st.subheader("📋 Harvest Records")

st.dataframe(
    df,
    use_container_width=True
)

# Download
if os.path.exists(FILE_NAME):

    with open(FILE_NAME, "rb") as file:

        st.download_button(
            "📥 Download Excel Report",
            file,
            file_name="PalmOilReport.xlsx"
        )
