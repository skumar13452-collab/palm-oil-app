import streamlit as st

st.title("🌴 Palm Oil Harvest Management")

weight = st.number_input("Weight (Tons)", min_value=0.0)
price = st.number_input("Price Per Ton", min_value=0.0)

total = weight * price

st.write(f"Total Amount: ₹{total:,.2f}")
