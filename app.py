st.markdown("""
<style>

/* Main Background */
.stApp{
    background: linear-gradient(
        135deg,
        #0B3D0B,
        #145A14,
        #1B5E20
    );
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #082808,
        #0B3D0B
    );
}

/* Sidebar Text */
section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Headers */
h1,h2,h3,h4,h5,h6{
    color:white !important;
    font-weight:700;
}

/* Labels */
label{
    color:white !important;
    font-weight:600;
}

/* Metric Cards */
div[data-testid="metric-container"]{
    background:white !important;
    border-radius:18px;
    padding:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.25);
    border:1px solid #dcdcdc;
}

/* Metric Values */
div[data-testid="metric-container"] label{
    color:#333 !important;
}

div[data-testid="metric-container"] div{
    color:#111 !important;
}

/* Input Fields */
.stTextInput input,
.stNumberInput input,
.stDateInput input{
    background:white !important;
    color:black !important;
    border-radius:8px;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"]{
    background:white !important;
    color:black !important;
}

/* Buttons */
.stButton button{
    background:#2E7D32 !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
    font-weight:bold !important;
}

.stButton button:hover{
    background:#1B5E20 !important;
}

/* DataFrames */
[data-testid="stDataFrame"]{
    background:white;
    border-radius:12px;
    padding:5px;
}

/* Tabs */
button[data-baseweb="tab"]{
    color:white !important;
}

/* Success */
.stSuccess{
    background:#1B5E20 !important;
}

/* Info */
.stInfo{
    background:#0D47A1 !important;
}

/* Warning */
.stWarning{
    background:#F57F17 !important;
}

/* Custom Dashboard Cards */
.kpi-card{
    background:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 4px 15px rgba(0,0,0,.2);
}

.kpi-value{
    font-size:32px;
    font-weight:bold;
    color:#2E7D32;
}

.kpi-title{
    color:#666;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)
