import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from datetime import datetime
import os

FILE_NAME = "harvest_data.xlsx"

st.set_page_config(
    page_title="Palm Oil Management",
    page_icon="🌴",
    layout="wide"
)

# Sidebar
with st.sidebar:
    selected = option_menu(
        "Palm Oil System",
        ["Dashboard", "Harvest Entry", "Reports"],
        icons=["speedometer2", "plus-circle", "bar-chart"],
        menu_icon="tree-fill",
        default_index=0,
    )

# Load Data
if os.path.exists(FILE_NAME):
    df = pd.read_excel(FILE_NAME)
else:
    df = pd.DataFrame(columns=[
        "Date",
        "Plot",
        "Weight",
        "Price",
        "Amount"
    ])

# DASHBOARD
if selected == "Dashboard":

    st.title("🌴 Palm Oil Dashboard")

    total_weight = df["Weight"].sum() if not df.empty else 0
    total_amount = df["Amount"].sum() if not df.empty else 0
    avg_price = df["Price"].mean() if not df.empty else 0

    col1, col2, col3 = st.columns(3)

    col1.metric("🌴 Total Harvest", f"{total_weight:.2f} Tons")
    col2.metric("💰 Total Revenue", f"₹{total_amount:,.0f}")
    col3.metric("📈 Avg Price/Ton", f"₹{avg_price:,.0f}")

    st.divider()

    if not df.empty:

        chart = px.bar(
            df,
            x="Plot",
            y="Amount",
            color="Plot",
            title="Revenue by Plot"
        )

        st.plotly_chart(chart, use_container_width=True)

        trend = px.line(
            df,
            x="Date",
            y="Weight",
            markers=True,
            title="Harvest Trend"
        )

        st.plotly_chart(trend, use_container_width=True)

# ENTRY
elif selected == "Harvest Entry":

    st.title("➕ Harvest Entry")

    with st.form("entry_form"):

        date = st.date_input("Cutting Date")

        plot = st.selectbox(
            "Plot",
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

        st.success(f"Total Amount : ₹{amount:,.2f}")

        submit = st.form_submit_button("💾 Save")

        if submit:

            new_row = pd.DataFrame({
                "Date":[date],
                "Plot":[plot],
                "Weight":[weight],
                "Price":[price],
                "Amount":[amount]
            })

            df = pd.concat(
                [df, new_row],
                ignore_index=True
            )

            df.to_excel(FILE_NAME, index=False)

            st.success("Record Saved Successfully")

# REPORTS
elif selected == "Reports":

    st.title("📊 Reports")

    if not df.empty:

        st.dataframe(
            df,
            use_container_width=True
        )

        st.download_button(
            "📥 Download Excel",
            open(FILE_NAME, "rb"),
            file_name="PalmOilReport.xlsx"
        )

    else:
        st.info("No records available.")
