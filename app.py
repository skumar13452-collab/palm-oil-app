import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import os
from PIL import Image

FILE_NAME = "harvest_data.xlsx"

st.set_page_config(
    page_title="Palm Oil Management",
    page_icon="🌴",
    layout="wide"
)

# Create uploads folder
os.makedirs("uploads", exist_ok=True)

# Sidebar
with st.sidebar:
    selected = option_menu(
        "🌴 Palm Oil System",
        ["Dashboard", "Harvest Entry", "Reports"],
        icons=["speedometer2", "plus-circle", "bar-chart"],
        menu_icon="tree-fill",
        default_index=0,
    )

# Load data
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

# ==========================
# DASHBOARD
# ==========================
if selected == "Dashboard":

    st.title("🌴 Palm Oil Dashboard")

    total_weight = df["Weight"].sum() if not df.empty else 0
    total_amount = df["Amount"].sum() if not df.empty else 0
    avg_price = df["Price"].mean() if not df.empty else 0

    c1, c2, c3 = st.columns(3)

    c1.metric("🌴 Total Harvest", f"{total_weight:.2f} Tons")
    c2.metric("💰 Total Revenue", f"₹{total_amount:,.0f}")
    c3.metric("📈 Avg Price/Ton", f"₹{avg_price:,.0f}")

    st.divider()

    if not df.empty:

        chart1 = px.bar(
            df,
            x="Plot",
            y="Amount",
            color="Plot",
            title="Revenue by Plot"
        )

        st.plotly_chart(chart1, use_container_width=True)

        chart2 = px.line(
            df,
            x="Date",
            y="Weight",
            markers=True,
            title="Harvest Trend"
        )

        st.plotly_chart(chart2, use_container_width=True)

# ==========================
# HARVEST ENTRY
# ==========================
elif selected == "Harvest Entry":

    st.title("➕ New Harvest Entry")

    with st.form("harvest_form"):

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

        price = st.number_input(
            "Price Per Ton",
            min_value=0.0
        )

        amount = weight * price

        st.success(f"💰 Total Amount : ₹{amount:,.2f}")

        uploaded_file = st.file_uploader(
            "Upload Harvester Card",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file:
            st.image(uploaded_file, width=300)

        submit = st.form_submit_button("💾 Save Record")

        if submit:

            image_name = ""

            if uploaded_file:

                image_name = uploaded_file.name

                image_path = os.path.join(
                    "uploads",
                    image_name
                )

                with open(image_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

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

            df.to_excel(FILE_NAME, index=False)

            st.success("Record Saved Successfully")

# ==========================
# REPORTS
# ==========================
elif selected == "Reports":

    st.title("📊 Harvest Reports")

    if not df.empty:

        st.dataframe(
            df,
            use_container_width=True
        )

        st.subheader("Record Images")

        for i, row in df.iterrows():

            image_path = os.path.join(
                "uploads",
                str(row["Image"])
            )

            if os.path.exists(image_path):

                st.write(
                    f"Date: {row['Date']} | Plot: {row['Plot']}"
                )

                st.image(
                    image_path,
                    width=250
                )

        with open(FILE_NAME, "rb") as file:
            st.download_button(
                "📥 Download Excel",
                file,
                file_name="PalmOilReport.xlsx"
            )

    else:
        st.info("No records available.")
