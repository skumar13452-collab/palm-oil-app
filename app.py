import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.set_page_config(page_title="PalmTrack Pro", page_icon="🌴", layout="wide")

DB="palmtrack.db"

def db():
    return sqlite3.connect(DB, check_same_thread=False)

con=db()
cur=con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS harvest(
id INTEGER PRIMARY KEY,
dt TEXT, block TEXT, weight REAL, bunches INTEGER, vehicle TEXT, slip TEXT)""")

cur.execute("""CREATE TABLE IF NOT EXISTS labour(
id INTEGER PRIMARY KEY,
dt TEXT, block TEXT, workers INTEGER, worktype TEXT, amount REAL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS fertilizer(
id INTEGER PRIMARY KEY,
dt TEXT, block TEXT, fert TEXT, qty REAL, cost REAL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS sales(
id INTEGER PRIMARY KEY,
dt TEXT, buyer TEXT, weight REAL, price REAL, revenue REAL)""")
con.commit()

st.markdown("""
<style>
.stApp{background:#f4f7f4;}
section[data-testid="stSidebar"]{background:#0b5d1e;}
</style>
""", unsafe_allow_html=True)

if "login" not in st.session_state:
    st.session_state.login=False

if not st.session_state.login:
    st.title("🌴 PalmTrack Pro Login")
    u=st.text_input("Username")
    p=st.text_input("Password", type="password")
    if st.button("Login"):
        if u=="admin" and p=="RK":
            st.session_state.login=True
            st.rerun()
        else:
            st.error("Invalid credentials")
    st.stop()

menu=st.sidebar.radio("Menu",[
"Dashboard","Harvest","Labour","Fertilizer","Sales","Reports"
])

st.sidebar.success("Blocks: A,B,C,D,E")

if menu=="Dashboard":
    st.title("🌴 PalmTrack Dashboard")

    h=pd.read_sql("select * from harvest",con)
    l=pd.read_sql("select * from labour",con)
    f=pd.read_sql("select * from fertilizer",con)
    s=pd.read_sql("select * from sales",con)

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Harvest (MT)", round(h["weight"].sum(),2) if not h.empty else 0)
    c2.metric("Revenue ₹", round(s["revenue"].sum(),2) if not s.empty else 0)
    c3.metric("Labour ₹", round(l["amount"].sum(),2) if not l.empty else 0)
    c4.metric("Fertilizer Kg", round(f["qty"].sum(),2) if not f.empty else 0)

    col1,col2=st.columns(2)

    with col1:
        if not h.empty:
            st.subheader("Block Wise Harvest")
            st.bar_chart(h.groupby("block")["weight"].sum())

    with col2:
        if not s.empty:
            st.subheader("Revenue Trend")
            st.line_chart(s.groupby("dt")["revenue"].sum())

elif menu=="Harvest":
    st.header("✂ Harvest Management")
    with st.form("h"):
        dt=st.date_input("Date",date.today())
        block=st.selectbox("Block",["A","B","C","D","E"])
        bunch=st.number_input("Bunch Count",0)
        wt=st.number_input("Weight MT",0.0)
        veh=st.text_input("Vehicle")
        slip=st.file_uploader("Harvest Slip")
        ok=st.form_submit_button("Save")
        if ok:
            cur.execute("insert into harvest(dt,block,weight,bunches,vehicle,slip) values(?,?,?,?,?,?)",
                        (str(dt),block,wt,bunch,veh,getattr(slip,'name','')))
            con.commit()
            st.success("Saved")

elif menu=="Labour":
    st.header("👷 Labour Management")
    with st.form("l"):
        dt=st.date_input("Date",date.today())
        block=st.selectbox("Block",["A","B","C","D","E"])
        workers=st.number_input("Workers",0)
        wt=st.selectbox("Work Type",["Harvesting","Maintenance","Fertilizer"])
        amt=st.number_input("Amount ₹",0.0)
        if st.form_submit_button("Save"):
            cur.execute("insert into labour(dt,block,workers,worktype,amount) values(?,?,?,?,?)",
                        (str(dt),block,workers,wt,amt))
            con.commit()
            st.success("Saved")

elif menu=="Fertilizer":
    st.header("💧 Fertilizer")
    with st.form("f"):
        dt=st.date_input("Date",date.today())
        block=st.selectbox("Block",["A","B","C","D","E"])
        fert=st.selectbox("Type",["NPK","Urea","MOP","CIRP"])
        qty=st.number_input("Qty Kg",0.0)
        cost=st.number_input("Cost ₹",0.0)
        if st.form_submit_button("Save"):
            cur.execute("insert into fertilizer(dt,block,fert,qty,cost) values(?,?,?,?,?)",
                        (str(dt),block,fert,qty,cost))
            con.commit()
            st.success("Saved")

elif menu=="Sales":
    st.header("💰 Sales")
    with st.form("s"):
        dt=st.date_input("Date",date.today())
        buyer=st.text_input("Buyer")
        weight=st.number_input("Weight MT",0.0)
        price=st.number_input("Price Per Tonne ₹",0.0)
        revenue=weight*price
        st.info(f"Revenue: ₹{revenue:,.2f}")
        if st.form_submit_button("Save"):
            cur.execute("insert into sales(dt,buyer,weight,price,revenue) values(?,?,?,?,?)",
                        (str(dt),buyer,weight,price,revenue))
            con.commit()
            st.success("Saved")

elif menu=="Reports":
    st.header("📊 Reports")
    for t in ["harvest","labour","fertilizer","sales"]:
        st.subheader(t.title())
        df=pd.read_sql(f"select * from {t}",con)
        st.dataframe(df,use_container_width=True)
