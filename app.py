
import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.set_page_config(page_title="PalmTrack", page_icon="🌴", layout="wide")

DB="palmtrack.db"

def init_db():
    conn=sqlite3.connect(DB)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS harvest(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        harvest_date TEXT, block_name TEXT, workers INTEGER, weight REAL
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS fertilizer(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        applied_date TEXT, block_name TEXT, fert_type TEXT, qty REAL
    )""")
    conn.commit()
    conn.close()

init_db()

st.markdown("# 🌴 PalmTrack")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Menu", ["Dashboard","Harvest","Fertilizer"])

if page == "Dashboard":
    st.subheader("Dashboard")
    c1,c2=st.columns(2)
    conn=sqlite3.connect(DB)
    h=pd.read_sql("select * from harvest", conn)
    f=pd.read_sql("select * from fertilizer", conn)
    conn.close()
    with c1:
        st.metric("Harvest Records", len(h))
    with c2:
        st.metric("Fertilizer Records", len(f))
    if not h.empty:
        st.bar_chart(h.groupby("block_name")["weight"].sum())

elif page == "Harvest":
    st.subheader("Harvest Entry")
    with st.form("harvest"):
        d=st.date_input("Date", date.today())
        b=st.text_input("Block")
        w=st.number_input("Workers", 0, 100, 5)
        wt=st.number_input("Weight (kg)", 0.0, 100000.0, 0.0)
        s=st.form_submit_button("Save")
        if s:
            conn=sqlite3.connect(DB)
            conn.execute("insert into harvest(harvest_date,block_name,workers,weight) values(?,?,?,?)",
                         (str(d),b,w,wt))
            conn.commit(); conn.close()
            st.success("Saved")

elif page == "Fertilizer":
    st.subheader("Fertilizer Entry")
    with st.form("fert"):
        d=st.date_input("Applied Date", date.today())
        b=st.text_input("Block Name")
        t=st.selectbox("Type",["NPK","Urea","MOP","CIRP"])
        q=st.number_input("Quantity (kg)",0.0,100000.0,0.0)
        s=st.form_submit_button("Save")
        if s:
            conn=sqlite3.connect(DB)
            conn.execute("insert into fertilizer(applied_date,block_name,fert_type,qty) values(?,?,?,?)",
                         (str(d),b,t,q))
            conn.commit(); conn.close()
            st.success("Saved")
