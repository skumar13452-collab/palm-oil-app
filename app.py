import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Palm Oil Management",
    page_icon="🌴",
    layout="wide"
)

st.title("🌴 Palm Oil Harvest Management System")

# Dashboard
col1, col2, col3 = st.columns(3)

col1.metric("Total Harvest", "120 Tons")
col2.metric("Total Income", "₹22,50,000")
col3.metric("Average Price", "₹18,750")

st.divider()

left, right = st.columns([2, 1])

with left:
    st.subheader("Harvest Entry")

    date = st.date_input("Cutting Date")

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

    total = weight * price

    st.success(f"Total Amount : ₹{total:,.2f}")

    if st.button("💾 Save Record"):
        st.success("Record Saved Successfully")

with right:
    st.subheader("Summary")
    st.info("Current Harvest Details")

st.divider()

st.subheader("Harvest Records")

sample = pd.DataFrame({
    "Date":["10-Jun-2026","20-Jun-2026"],
    "Plot":["Plot-A","Plot-B"],
    "Weight":[5.2,4.8],
    "Amount":[96200,91200]
})

st.dataframe(sample, use_container_width=True)
