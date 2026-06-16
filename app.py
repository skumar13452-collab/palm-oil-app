import streamlit as st
import pandas as pd
import sqlite3
from datetime import date
import os

st.set_page_config(page_title="PalmTrack", page_icon="🌴", layout="wide")

DB = "palm_oil.db"
os.makedirs("uploads/workers", exist_ok=True)
os.makedirs("uploads/slips", exist_ok=True)

conn = sqlite3.connect(DB, check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS harvest(
id INTEGER PRIMARY KEY AUTOINCREMENT,
hdate TEXT, block_name TEXT, qty REAL, worker TEXT, slip TEXT)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS workers(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT, phone TEXT, salary REAL, photo TEXT)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS fertilizer(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fdate TEXT, item TEXT, qty REAL, cost REAL)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS transport(
id INTEGER PRIMARY KEY AUTOINCREMENT,
tdate TEXT, vehicle TEXT, driver TEXT, qty REAL, charges REAL)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
edate TEXT, category TEXT, amount REAL, remarks TEXT)
""")
conn.commit()

st.markdown("""
<style>
.stApp {background-color:#0f172a;color:white;}
section[data-testid="stSidebar"] {background:#14532d;}
</style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🌴 PalmTrack Login")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    if st.button("Login"):
        if u == "admin" and p == "RK":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials")
    st.stop()

with st.sidebar:
    st.title("🌴 PalmTrack")
    page = st.radio("Menu",
        ["Dashboard","Harvest","Workers","Fertilizer","Transport","Expenses","Reports"])

if page == "Dashboard":
    st.title("Dashboard")
    h = pd.read_sql("select * from harvest", conn)
    w = pd.read_sql("select * from workers", conn)
    e = pd.read_sql("select * from expenses", conn)

    c1,c2,c3 = st.columns(3)
    c1.metric("Harvest Records", len(h))
    c2.metric("Workers", len(w))
    c3.metric("Expenses", f"₹{e['amount'].sum() if len(e) else 0:,.0f}")

elif page == "Harvest":
    st.title("Harvest Entry")
    d = st.date_input("Date", date.today())
    block = st.selectbox("Block", ["A","B","C","D","E"])
    qty = st.number_input("Quantity (MT)", 0.0)
    worker = st.text_input("Worker")
    slip = st.file_uploader("Harvest Slip")
    if st.button("Save Harvest"):
        slipname=""
        if slip:
            slipname=f"uploads/slips/{slip.name}"
            with open(slipname,"wb") as f:
                f.write(slip.getbuffer())
        cur.execute("insert into harvest(hdate,block_name,qty,worker,slip) values(?,?,?,?,?)",
                    (str(d),block,qty,worker,slipname))
        conn.commit()
        st.success("Saved")

elif page == "Workers":
    st.title("Workers")
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    salary = st.number_input("Salary",0.0)
    photo = st.file_uploader("Worker Photo")
    if st.button("Add Worker"):
        photoname=""
        if photo:
            photoname=f"uploads/workers/{photo.name}"
            with open(photoname,"wb") as f:
                f.write(photo.getbuffer())
        cur.execute("insert into workers(name,phone,salary,photo) values(?,?,?,?)",
                    (name,phone,salary,photoname))
        conn.commit()
        st.success("Worker Added")

elif page == "Fertilizer":
    st.title("Fertilizer")
    d = st.date_input("Date", date.today(), key="f")
    item = st.text_input("Item")
    qty = st.number_input("Qty MT",0.0,key="fq")
    cost = st.number_input("Cost INR",0.0)
    if st.button("Save Fertilizer"):
        cur.execute("insert into fertilizer(fdate,item,qty,cost) values(?,?,?,?)",
                    (str(d),item,qty,cost))
        conn.commit()
        st.success("Saved")

elif page == "Transport":
    st.title("Transport")
    d = st.date_input("Date", date.today(), key="t")
    vehicle = st.text_input("Vehicle No")
    driver = st.text_input("Driver")
    qty = st.number_input("Load MT",0.0,key="tq")
    charges = st.number_input("Charges INR",0.0)
    if st.button("Save Transport"):
        cur.execute("insert into transport(tdate,vehicle,driver,qty,charges) values(?,?,?,?,?)",
                    (str(d),vehicle,driver,qty,charges))
        conn.commit()
        st.success("Saved")

elif page == "Expenses":
    st.title("Expenses")
    d = st.date_input("Date", date.today(), key="e")
    cat = st.text_input("Category")
    amt = st.number_input("Amount INR",0.0)
    rem = st.text_area("Remarks")
    if st.button("Save Expense"):
        cur.execute("insert into expenses(edate,category,amount,remarks) values(?,?,?,?)",
                    (str(d),cat,amt,rem))
        conn.commit()
        st.success("Saved")

elif page == "Reports":
    st.title("Reports")
    tabs = {
        "Harvest": "harvest",
        "Workers": "workers",
        "Fertilizer": "fertilizer",
        "Transport": "transport",
        "Expenses": "expenses"
    }
    t = st.selectbox("Select Report", list(tabs.keys()))
    df = pd.read_sql(f"select * from {tabs[t]}", conn)
    st.dataframe(df, width="stretch")
    st.download_button("Download CSV", df.to_csv(index=False),
                       file_name=f"{tabs[t]}.csv")
