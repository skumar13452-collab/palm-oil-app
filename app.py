import streamlit as st
import pandas as pd
from datetime import datetime
import textwrap
import base64
import os

# Set page configuration
st.set_page_config(
    page_title="RK Forms",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helper function to completely minify HTML/CSS strings on-the-fly
# This strips ALL leading and trailing spaces from every line, eliminating any possibility 
# of the Markdown engine parsing indented lines as preformatted code blocks.
def clean_html(html_str):
    return " ".join([line.strip() for line in html_str.split("\n") if line.strip()])

# Function to safely load a local image and convert it to base64
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Load background image from repository root
IMAGE_FILE = "oip-palm.jpg"
img_base64 = get_base64_image(IMAGE_FILE)

# Dynamic CSS for background image injection if the image is successfully loaded
background_css = ""
if img_base64:
    background_css = f"""
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpeg;base64,{img_base64}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}
    /* Semi-transparent protective overlay to maintain 100% text readability */
    [data-testid="stAppViewContainer"]::before {{
        content: "" !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        background-color: rgba(253, 246, 233, 0.80) !important; /* Warm ivory protective layer that lets the palm-fruit tones glow through */
        z-index: -1 !important;
    }}
    /* Frosted glass glassmorphism, retinted warm-ivory/gold to harmonise with the background photo */
    .kpi-card, .panel-card {{
        background-color: rgba(255, 250, 240, 0.90) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border: 1px solid rgba(201, 138, 61, 0.30) !important;
    }}
    """

# Custom CSS for high-fidelity matching
custom_css = f"""
<style>
/* Global styles and main background */
html, body, [data-testid="stAppViewContainer"] {{
    background-color: transparent !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #1A231C;
}}

/* Remove default padding and margins of Streamlit layout */
[data-testid="stHeader"] {{
    background-color: transparent !important;
}}

[data-testid="stSidebar"] {{
    background: linear-gradient(165deg, #1B3D21 0%, #102217 100%) !important;
    border-right: 1px solid #C9963F;
}}

/* Sidebar Logo Area */
.sidebar-logo-container {{
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 0px 24px 0px;
    border-bottom: 1px solid rgba(201, 150, 63, 0.35);
    margin-bottom: 15px;
}}
.logo-icon-box {{
    background-color: #3B6B40;
    width: 42px;
    height: 42px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    box-shadow: 0 0 0 2px rgba(217, 164, 64, 0.45);
}}
.logo-text-title {{
    font-size: 18px;
    font-weight: 700;
    color: #FFFFFF !important;
    line-height: 1.2;
}}
.logo-text-subtitle {{
    font-size: 13px;
    color: #D9B97A !important;
}}

/* Sidebar Section Headers */
.sidebar-section-header {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #C79A56 !important;
    text-transform: uppercase;
    margin-top: 22px;
    margin-bottom: 10px;
    padding-left: 5px;
}}

/* Sidebar Custom Buttons - SCOPED strictly inside the Sidebar container */
[data-testid="stSidebar"] div.stButton > button {{
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    width: 100% !important;
    background-color: transparent !important;
    border: none !important;
    color: #BFD0B8 !important;
    padding: 10px 14px !important;
    text-align: left !important;
    border-radius: 8px !important;
    font-size: 15px !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}}
[data-testid="stSidebar"] div.stButton > button:hover {{
    background-color: #25492B !important;
    color: #FFFFFF !important;
}}
[data-testid="stSidebar"] div.stButton > button:active {{
    background-color: #D9A440 !important;
    color: #1B2E12 !important;
}}

/* Active Nav Button Styling */
.active-nav-btn div.stButton > button {{
    background-color: #D9A440 !important;
    color: #1B2E12 !important;
    font-weight: 700 !important;
}}

/* Floating Sidebar Expand Chevron Styling (just in case collapsed) */
[data-testid="stSidebarCollapsedControl"] {{
    background-color: #1B3D21 !important;
    border-radius: 8px !important;
    padding: 6px !important;
    z-index: 999999 !important;
    top: 15px !important;
    left: 15px !important;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2) !important;
}}
[data-testid="stSidebarCollapsedControl"] button {{
    color: #FFFFFF !important;
}}
[data-testid="stSidebarCollapsedControl"] svg {{
    fill: #FFFFFF !important;
    color: #FFFFFF !important;
}}

/* Main Banner container */
.main-banner {{
    background: linear-gradient(120deg, #1F4424 0%, #3B6B3F 60%, #6B7F3A 100%);
    border-radius: 14px;
    padding: 24px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
    box-shadow: inset 0 -3px 0 0 rgba(217, 164, 64, 0.55);
}}
.banner-left {{
    display: flex;
    align-items: center;
    gap: 18px;
}}
.banner-logo-wrapper {{
    background-color: rgba(217, 164, 64, 0.18);
    border-radius: 12px;
    padding: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
}}
.banner-title {{
    font-size: 24px;
    font-weight: 700;
    margin: 0;
    line-height: 1.2;
    color: white;
}}
.banner-subtitle {{
    font-size: 14px;
    color: #E3D5AE;
    margin: 4px 0 0 0;
}}
.banner-right {{
    text-align: right;
}}
.banner-today {{
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #E8C170;
    margin: 0;
}}
.banner-date {{
    font-size: 24px;
    font-weight: 700;
    margin: 4px 0 0 0;
    color: white;
}}

/* Metric Cards style */
.kpi-card {{
    background-color: #FAF3E7;
    border-radius: 12px;
    padding: 20px;
    border: 1px solid #EFE0C2;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}
.kpi-header {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 11px;
    font-weight: 700;
    color: #5C6B5E;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 12px;
}}
.kpi-header-icon {{
    font-size: 14px;
}}
.kpi-value {{
    font-size: 32px;
    font-weight: 700;
    color: #1A231C;
    line-height: 1.1;
    margin-bottom: 4px;
}}
.kpi-subtitle {{
    font-size: 13px;
    color: #5C6B5E;
    margin-bottom: 12px;
    line-height: 1.3;
}}
.kpi-trend-green {{
    font-size: 13px;
    font-weight: 600;
    color: #2E7D32;
}}
.kpi-trend-gray {{
    font-size: 13px;
    font-weight: 500;
    color: #7A8B7D;
}}
.kpi-trend-red {{
    font-size: 13px;
    font-weight: 600;
    color: #B22B27;
}}

/* Panel Containers */
.panel-card {{
    background-color: #FFFBF4;
    border-radius: 14px;
    border: 1px solid #EFE0C2;
    padding: 24px;
    height: 100%;
}}
.panel-header-container {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
}}
.panel-title {{
    font-size: 18px;
    font-weight: 700;
    color: #1A231C;
    display: flex;
    align-items: center;
    gap: 8px;
}}
.arrow-btn {{
    border: 1px solid #EAE9E4;
    border-radius: 8px;
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    background-color: white;
    color: #1A231C;
    font-weight: bold;
}}

/* Cuttings Table Style */
.cuttings-table {{
    width: 100%;
    border-collapse: collapse;
}}
.cuttings-table th {{
    font-size: 11px;
    font-weight: 700;
    color: #5C6B5E;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    padding-bottom: 12px;
    text-align: left;
    border-bottom: 1px solid #EFE0C2;
}}
.cuttings-table td {{
    padding: 14px 0;
    font-size: 14px;
    color: #1A231C;
    border-bottom: 1px solid #F6EEDD;
}}
.cuttings-table tr:last-child td {{
    border-bottom: none;
}}
.work-name {{
    font-weight: 600;
}}

/* Badges styling */
.badge {{
    display: inline-block;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    text-align: center;
}}
.badge-delivered {{
    background-color: #E2F3E2;
    color: #2E7D32;
}}
.badge-transit {{
    background-color: #FFF3E0;
    color: #EF6C00;
}}
.badge-weighed {{
    background-color: #E3F2FD;
    color: #1565C0;
}}
.badge-completed {{
    background-color: #E2F3E2;
    color: #2E7D32;
}}
.badge-enroute {{
    background-color: #FFF3E0;
    color: #EF6C00;
}}

/* Transport elements */
.transport-list {{
    display: flex;
    flex-direction: column;
    gap: 12px;
}}
.transport-item {{
    background-color: #FCF5E9;
    border-radius: 12px;
    padding: 14px 16px;
    border: 1px solid #EFE0C2;
    display: flex;
    align-items: center;
    justify-content: space-between;
}}
.transport-left {{
    display: flex;
    align-items: center;
    gap: 12px;
}}
.transport-icon-box {{
    background-color: #E2F3E2;
    width: 44px;
    height: 44px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}}
.transport-details {{
    display: flex;
    flex-direction: column;
}}
.transport-id {{
    font-weight: 700;
    font-size: 14px;
    color: #1A231C;
}}
.transport-desc {{
    font-size: 12px;
    color: #5C6B5E;
    margin-top: 2px;
}}

/* Remove the top padding from the main block container */
.block-container {{
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
}}

{background_css}
</style>
"""
st.markdown(clean_html(custom_css), unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Initialize Mock Data in Session State for Real interactivity
# -----------------------------------------------------------------------------
if "price_per_tonne" not in st.session_state:
    st.session_state.price_per_tonne = 1658

if "cuttings" not in st.session_state:
    st.session_state.cuttings = []

if "transport" not in st.session_state:
    st.session_state.transport = []

if "fertiliser_used" not in st.session_state:
    st.session_state.fertiliser_used = 0.0

if "workers_on_leave" not in st.session_state:
    st.session_state.workers_on_leave = 0

if "active_workers" not in st.session_state:
    st.session_state.active_workers = 0

if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Dashboard"

# -----------------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------------
with st.sidebar:
    # Sidebar Brand Area
    st.markdown(clean_html('''
        <div class="sidebar-logo-container">
            <div class="logo-icon-box">
                <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 24px; height: 24px;">
                    <path d="M12 22V12" />
                    <path d="M12 12C12 12 7 10 5 13" />
                    <path d="M12 12C12 12 17 10 19 13" />
                    <path d="M12 15C12 15 8 14 6 17" />
                    <path d="M12 15C12 15 16 14 18 17" />
                </svg>
            </div>
            <div>
                <div class="logo-text-title">PalmTrack</div>
                <div class="logo-text-subtitle">Estate Manager</div>
            </div>
        </div>
    '''), unsafe_allow_html=True)
    
    # Overview section
    st.markdown('<div class="sidebar-section-header">Overview</div>', unsafe_allow_html=True)
    
    # Navigation items using flat buttons and Custom CSS classes to show active states
    is_dashboard_active = st.session_state.selected_page == "Dashboard"
    if is_dashboard_active:
        st.markdown('<div class="active-nav-btn">', unsafe_allow_html=True)
    if st.button("📊 Dashboard", key="btn_dash", use_container_width=True):
        st.session_state.selected_page = "Dashboard"
        st.rerun()
    if is_dashboard_active:
        st.markdown('</div>', unsafe_allow_html=True)
        
    # Operations Section
    st.markdown('<div class="sidebar-section-header">Operations</div>', unsafe_allow_html=True)
    
    # Harvest
    is_harvest_active = st.session_state.selected_page == "Harvest"
    if is_harvest_active:
        st.markdown('<div class="active-nav-btn">', unsafe_allow_html=True)
    if st.button("✂️ Harvest", key="btn_harv", use_container_width=True):
        st.session_state.selected_page = "Harvest"
        st.rerun()
    if is_harvest_active:
        st.markdown('</div>', unsafe_allow_html=True)
        
    # Fertiliser
    is_fert_active = st.session_state.selected_page == "Fertiliser"
    if is_fert_active:
        st.markdown('<div class="active-nav-btn">', unsafe_allow_html=True)
    if st.button("🧪 Fertiliser", key="btn_fert", use_container_width=True):
        st.session_state.selected_page = "Fertiliser"
        st.rerun()
    if is_fert_active:
        st.markdown('</div>', unsafe_allow_html=True)

    # Workers
    is_workers_active = st.session_state.selected_page == "Workers"
    if is_workers_active:
        st.markdown('<div class="active-nav-btn">', unsafe_allow_html=True)
    if st.button("👥 Workers", key="btn_work", use_container_width=True):
        st.session_state.selected_page = "Workers"
        st.rerun()
    if is_workers_active:
        st.markdown('</div>', unsafe_allow_html=True)

    # Transport
    is_trans_active = st.session_state.selected_page == "Transport"
    if is_trans_active:
        st.markdown('<div class="active-nav-btn">', unsafe_allow_html=True)
    if st.button("🚚 Transport", key="btn_trans", use_container_width=True):
        st.session_state.selected_page = "Transport"
        st.rerun()
    if is_trans_active:
        st.markdown('</div>', unsafe_allow_html=True)

    # Finance Section
    st.markdown('<div class="sidebar-section-header">Finance</div>', unsafe_allow_html=True)
    
    # Pricing
    is_pricing_active = st.session_state.selected_page == "Pricing"
    if is_pricing_active:
        st.markdown('<div class="active-nav-btn">', unsafe_allow_html=True)
    if st.button("🪙 Pricing", key="btn_price", use_container_width=True):
        st.session_state.selected_page = "Pricing"
        st.rerun()
    if is_pricing_active:
        st.markdown('</div>', unsafe_allow_html=True)

    
# -----------------------------------------------------------------------------
# MAIN HEADER BANNER (Shared across all pages)
# -----------------------------------------------------------------------------
banner_svg = """
<svg width="56" height="56" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
    <!-- Trunk -->
    <path d="M57,60 L54,110 L66,110 L63,60 Z" fill="#B2D8B5" />
    <path d="M58,60 C58,75 56,90 54,110 L66,110 C64,90 62,75 62,60 Z" fill="#8EAE91" />
    <!-- Coconuts -->
    <circle cx="50" cy="62" r="6" fill="#A0522D" />
    <circle cx="70" cy="62" r="6" fill="#A0522D" />
    <circle cx="60" cy="68" r="6" fill="#8B4513" />
    <!-- Central Leaf (Straight Up) -->
    <path d="M60,60 C60,40 60,10 60,10 C60,10 56,35 60,60 Z" fill="#B2D8B5" />
    <!-- Symmetrical Left Leaves -->
    <path d="M60,60 C50,45 25,25 15,35 C30,35 50,50 60,60 Z" fill="#D3EDD5" />
    <path d="M60,60 C45,55 20,55 10,70 C25,65 45,60 60,60 Z" fill="#9CC19E" />
    <!-- Symmetrical Right Leaves -->
    <path d="M60,60 C70,45 95,25 105,35 C90,35 70,50 60,60 Z" fill="#D3EDD5" />
    <path d="M60,60 C75,55 100,55 110,70 C95,65 75,60 60,60 Z" fill="#9CC19E" />
</svg>
"""

st.markdown(clean_html(f'''
<div class="main-banner">
    <div class="banner-left">
        <div class="banner-logo-wrapper">
            {banner_svg}
        </div>
        <div>
            <div class="banner-title">RK Forms</div>
            <div class="banner-subtitle">Configure your estate details</div>
        </div>
    </div>
    <div class="banner-right">
        <div class="banner-today">Today</div>
        <div class="banner-date">16 Jun 2026</div>
    </div>
</div>
'''), unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# DYNAMIC MATH COMPUTATIONS
# -----------------------------------------------------------------------------
base_harvest = 0
active_cuttings_tonnes = sum(c['tonnes'] for c in st.session_state.cuttings)
total_harvest = active_cuttings_tonnes

# Revenue calculation using the price_per_tonne configurator
total_revenue_rs = total_harvest * st.session_state.price_per_tonne
total_revenue_lakhs = total_revenue_rs / 100000


# -----------------------------------------------------------------------------
# PAGE ROUTING
# -----------------------------------------------------------------------------

# PAGE: DASHBOARD (The main high-fidelity recreation)
if st.session_state.selected_page == "Dashboard":
    
    # 1. KPI Cards Row
    kpi_cols = st.columns(4)
    
    with kpi_cols[0]:
        st.markdown(clean_html(f'''
            <div class="kpi-card">
                <div class="kpi-header">
                    <span class="kpi-header-icon">✂️</span> TOTAL HARVEST
                </div>
                <div>
                    <div class="kpi-value">{total_harvest:.1f}</div>
                    <div class="kpi-subtitle">tonnes this month</div>
                </div>
                <div class="kpi-trend-green">No data available</div>
            </div>
        '''), unsafe_allow_html=True)

    with kpi_cols[1]:
        st.markdown(clean_html(f'''
            <div class="kpi-card">
                <div class="kpi-header">
                    <span class="kpi-header-icon">🪙</span> REVENUE
                </div>
                <div>
                    <div class="kpi-value">₹{total_revenue_lakhs:.2f}L</div>
                    <div class="kpi-subtitle">at ₹{st.session_state.price_per_tonne:,}/tonne</div>
                </div>
                <div class="kpi-trend-green">No data available</div>
            </div>
        '''), unsafe_allow_html=True)

    with kpi_cols[2]:
        st.markdown(clean_html(f'''
            <div class="kpi-card">
                <div class="kpi-header">
                    <span class="kpi-header-icon">👥</span> ACTIVE WORKERS
                </div>
                <div>
                    <div class="kpi-value">{st.session_state.active_workers}</div>
                    <div class="kpi-subtitle">across all blocks</div>
                </div>
                <div class="kpi-trend-gray">{st.session_state.workers_on_leave} on leave today</div>
            </div>
        '''), unsafe_allow_html=True)

    with kpi_cols[3]:
        st.markdown(clean_html(f'''
            <div class="kpi-card">
                <div class="kpi-header">
                    <span class="kpi-header-icon">🧪</span> FERTILISER USED
                </div>
                <div>
                    <div class="kpi-value">{st.session_state.fertiliser_used:.1f}</div>
                    <div class="kpi-subtitle">tonnes this cycle</div>
                </div>
                <div class="kpi-trend-red">No data available</div>
            </div>
        '''), unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)

    # 2. Bottom Row (Recent Cuttings + Transport Today)
    bottom_cols = st.columns([3, 2], gap="large")

    # Bottom Left: Recent Cuttings Table
    with bottom_cols[0]:
        table_rows_html = ""
        for item in st.session_state.cuttings[:5]: # display top 5
            status = item['status']
            badge_class = "badge-delivered" if status == "Delivered" else ("badge-transit" if status == "In Transit" else "badge-weighed")
            table_rows_html += f'''
            <tr>
                <td class="work-name">{item['name']}</td>
                <td>{item['block']}</td>
                <td style="font-weight: 500;">{item['tonnes']:.1f}</td>
                <td><span class="badge {badge_class}">{status}</span></td>
            </tr>
            '''
            
        cuttings_card = f'''
        <div class="panel-card">
            <div class="panel-header-container">
                <div class="panel-title">
                    <span style="color: #C9852E; font-size: 20px;">✂️</span> Recent Cuttings
                </div>
                <div class="arrow-btn">➔</div>
            </div>
            <table class="cuttings-table">
                <thead>
                    <tr>
                        <th style="width: 35%;">Work Name</th>
                        <th style="width: 25%;">Block</th>
                        <th style="width: 20%;">Tonnes</th>
                        <th style="width: 20%;">Status</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows_html}
                </tbody>
            </table>
        </div>
        '''
        st.markdown(clean_html(cuttings_card), unsafe_allow_html=True)

    # Bottom Right: Transport Today List
    with bottom_cols[1]:
        transport_items_html = ""
        for trans in st.session_state.transport[:3]: # display top 3
            status = trans['status']
            badge_class = "badge-completed" if status == "Completed" else "badge-enroute"
            transport_items_html += f'''
            <div class="transport-item">
                <div class="transport-left">
                    <div class="transport-icon-box">🚚</div>
                    <div class="transport-details">
                        <div class="transport-id">{trans['id']}</div>
                        <div class="transport-desc">{trans['type']} · {trans['tonnes']:.1f} t · ₹{trans['charge']:,} charge</div>
                    </div>
                </div>
                <div>
                    <span class="badge {badge_class}">{status}</span>
                </div>
            </div>
            '''

        transport_card = f'''
        <div class="panel-card">
            <div class="panel-header-container" style="margin-bottom: 16px;">
                <div class="panel-title">
                    <span style="color: #C9852E; font-size: 20px;">🚚</span> Transport Today
                </div>
            </div>
            <div class="transport-list">
                {transport_items_html}
            </div>
        </div>
        '''
        st.markdown(clean_html(transport_card), unsafe_allow_html=True)


# PAGE: HARVEST (Log harvests dynamically)
elif st.session_state.selected_page == "Harvest":
    st.markdown('<h2 style="color: #2D5B2F; font-weight: 700;">✂️ Harvest Operations</h2>', unsafe_allow_html=True)
    st.write("Manage daily palm oil cuttings and log harvest tonnes block-by-block.")
    
    # Grid of harvest status summary
    stat_cols = st.columns(3)
    with stat_cols[0]:
        st.metric("Harvest Cuttings Active", len(st.session_state.cuttings))
    with stat_cols[1]:
        st.metric("Total Harvest Active (tonnes)", f"{active_cuttings_tonnes:.1f} t")
    with stat_cols[2]:
        st.metric("Avg Cutting Weight", f"{(active_cuttings_tonnes / max(1, len(st.session_state.cuttings))):.1f} t")
        
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2], gap="large")
    
    # Form to Log New Harvest Cutting
    with col1:
        st.markdown('<h3 style="color: #2D5B2F; font-size: 18px; margin-bottom: 10px;">Log New Cutting</h3>', unsafe_allow_html=True)
        with st.form("new_cutting_form", clear_on_submit=True):
            work_name = st.text_input("Work Name", placeholder="e.g. Morning Cut D")
            block = st.selectbox("Assign Block", ["Block A", "Block B", "Block C", "Block D"])
            tonnes = st.number_input("Tonnage Yield (tonnes)", min_value=0.1, max_value=100.0, value=15.0, step=0.1)
            status = st.selectbox("Current Status", ["Weighed", "In Transit", "Delivered"])
            
            submit_btn = st.form_submit_button("Submit Cutting Log", use_container_width=True)
            if submit_btn:
                if work_name.strip() == "":
                    st.error("Please enter a valid work name!")
                else:
                    new_log = {
                        "name": work_name.strip(),
                        "block": block,
                        "tonnes": tonnes,
                        "status": status
                    }
                    st.session_state.cuttings.insert(0, new_log)
                    st.success(f"Log added: {work_name} ({tonnes} tonnes) assigned to {block}.")
                    st.rerun()

    # List and Delete cutting logs
    with col2:
        st.markdown('<h3 style="color: #2D5B2F; font-size: 18px; margin-bottom: 10px;">Active Harvest Records</h3>', unsafe_allow_html=True)
        
        # Interactive table container
        for idx, cutting in enumerate(st.session_state.cuttings):
            c_cols = st.columns([3, 2, 2, 2, 1])
            with c_cols[0]:
                st.write(f"**{cutting['name']}**")
            with c_cols[1]:
                st.write(cutting['block'])
            with c_cols[2]:
                st.write(f"{cutting['tonnes']:.1f} tonnes")
            with c_cols[3]:
                st.write(f"`{cutting['status']}`")
            with c_cols[4]:
                if st.button("❌", key=f"del_cut_{idx}"):
                    st.session_state.cuttings.pop(idx)
                    st.success(f"Removed log: {cutting['name']}")
                    st.rerun()
            st.markdown('<hr style="margin: 6px 0; border: none; border-bottom: 1px solid #ECEBE6;" />', unsafe_allow_html=True)


# PAGE: FERTILISER
elif st.session_state.selected_page == "Fertiliser":
    st.markdown('<h2 style="color: #2D5B2F; font-weight: 700;">🧪 Fertiliser Management</h2>', unsafe_allow_html=True)
    st.write("Track fertiliser input applications and monitor cycles against budget limits.")
    
    fert_cols = st.columns(2)
    with fert_cols[0]:
        st.markdown(textwrap.dedent(f'''
            <div class="panel-card" style="padding: 24px;">
                <h4 style="margin: 0; color: #1A231C; font-size: 16px;">Current Fertiliser Cycle usage</h4>
                <div style="font-size: 36px; font-weight: 700; margin: 10px 0; color: #2D5B2F;">
                    {st.session_state.fertiliser_used:.1f} tonnes
                </div>
                <p style="color: #5C6B5E; font-size: 14px; margin-bottom: 15px;">Allocated Budget: <b>2.0 tonnes</b> for Cycle A</p>
            </div>
        '''), unsafe_allow_html=True)
        
        st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)
        st.write("#### Add Fertiliser Application Logs")
        new_fert = st.number_input("Apply additional fertiliser (tonnes)", min_value=0.1, max_value=5.0, value=0.2, step=0.1)
        if st.button("Apply to Crop Blocks"):
            st.session_state.fertiliser_used += new_fert
            st.success(f"Successfully recorded application of {new_fert} tonnes.")
            st.rerun()

    with fert_cols[1]:
        st.markdown(textwrap.dedent('''
            <div class="panel-card">
                <h4 style="margin: 0; color: #1A231C; font-size: 16px; margin-bottom: 15px;">Cycle budget distribution</h4>
            </div>
        '''), unsafe_allow_html=True)
        # Display progress bar for visual context
        pct = min(1.0, st.session_state.fertiliser_used / 2.0)
        st.progress(pct, text=f"Budget Usage: {pct*100:.0f}%")
        if pct >= 1.0:
            st.error("⚠️ Over Budget! Adjust parameters or cycle planning.")
        else:
            st.info("👍 Operations are within acceptable budget limit.")


# PAGE: WORKERS
elif st.session_state.selected_page == "Workers":
    st.markdown('<h2 style="color: #2D5B2F; font-weight: 700;">👥 Labour & Worker Roster</h2>', unsafe_allow_html=True)
    st.write("Log details on worker block assignments, daily rosters and leave statuses.")
    
    w_cols = st.columns(2)
    with w_cols[0]:
        st.subheader("Roster Statistics")
        st.metric("Total Active Labor", st.session_state.active_workers)
        st.metric("On Approved Leave Today", st.session_state.workers_on_leave)
        
        # Change active roster numbers dynamically
        st.write("---")
        st.write("#### Update Labour Statistics")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("➕ Increment Active Worker"):
                st.session_state.active_workers += 1
                st.rerun()
        with c2:
            if st.button("➖ Decrement Active Worker") and st.session_state.active_workers > 0:
                st.session_state.active_workers -= 1
                st.rerun()
                
        c1_l, c2_l = st.columns(2)
        with c1_l:
            if st.button("➕ Increment Workers on Leave"):
                st.session_state.workers_on_leave += 1
                st.rerun()
        with c2_l:
            if st.button("➖ Decrement Workers on Leave") and st.session_state.workers_on_leave > 0:
                st.session_state.workers_on_leave -= 1
                st.rerun()

    with w_cols[1]:
        st.markdown(textwrap.dedent('''
            <div class="panel-card">
                <h4 style="margin: 0 0 15px 0; color: #1A231C; font-size: 16px;">Active Block Assignment Roster</h4>
                <table class="cuttings-table">
                    <thead>
                        <tr>
                            <th>Labour Block</th>
                            <th>Lead Supervisor</th>
                            <th>Headcount</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td colspan="3" style="text-align:center;">No worker records available</td></tr>
                    </tbody>
                </table>
            </div>
        '''), unsafe_allow_html=True)


# PAGE: TRANSPORT (Log logistics/truck trips)
elif st.session_state.selected_page == "Transport":
    st.markdown('<h2 style="color: #2D5B2F; font-weight: 700;">🚚 Logistics & Transport</h2>', unsafe_allow_html=True)
    st.write("Track haulage vehicle trips, weighbridge statuses, and transport costs.")
    
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.markdown('<h3 style="color: #2D5B2F; font-size: 18px;">Dispatch New Vehicle</h3>', unsafe_allow_html=True)
        with st.form("new_transport_form", clear_on_submit=True):
            vehicle_id = st.text_input("Vehicle Plate Number", placeholder="e.g. TN 03 EF 9999")
            v_type = st.selectbox("Vehicle Type", ["Lorry", "Trailer", "Tractor"])
            v_tonnes = st.number_input("Payload Weight (tonnes)", min_value=0.1, max_value=50.0, value=15.0, step=0.1)
            v_charge = st.number_input("Transport Charge (₹)", min_value=500, max_value=50000, value=4000, step=100)
            v_status = st.selectbox("Delivery Status", ["En Route", "Completed"])
            
            submit_trans = st.form_submit_button("Dispatch Vehicle", use_container_width=True)
            if submit_trans:
                if vehicle_id.strip() == "":
                    st.error("Please enter a valid vehicle plate ID!")
                else:
                    new_trip = {
                        "id": vehicle_id.strip().upper(),
                        "type": v_type,
                        "tonnes": v_tonnes,
                        "charge": v_charge,
                        "status": v_status
                    }
                    st.session_state.transport.insert(0, new_trip)
                    st.success(f"Trip created: {vehicle_id} dispatched.")
                    st.rerun()

    with col2:
        st.markdown('<h3 style="color: #2D5B2F; font-size: 18px;">Haulage Logs</h3>', unsafe_allow_html=True)
        for idx, trans in enumerate(st.session_state.transport):
            t_cols = st.columns([3, 3, 2, 1])
            with t_cols[0]:
                st.write(f"🚚 **{trans['id']}** ({trans['type']})")
            with t_cols[1]:
                st.write(f"{trans['tonnes']:.1f} t · ₹{trans['charge']:,} charge")
            with t_cols[2]:
                st.write(f"`{trans['status']}`")
            with t_cols[3]:
                if st.button("❌", key=f"del_trans_{idx}"):
                    st.session_state.transport.pop(idx)
                    st.success(f"Trip removed: {trans['id']}")
                    st.rerun()
            st.markdown('<hr style="margin: 6px 0; border: none; border-bottom: 1px solid #ECEBE6;" />', unsafe_allow_html=True)


# PAGE: PRICING (Change rate per tonne)
elif st.session_state.selected_page == "Pricing":
    st.markdown('<h2 style="color: #2D5B2F; font-weight: 700;">🪙 Financial Configurations</h2>', unsafe_allow_html=True)
    st.write("Modify the palm oil harvest pricing parameters to update revenue KPI computations on the dashboard.")
    
    st.markdown("---")
    
    st.subheader("Price per Tonne Configuration")
    new_price = st.number_input(
        "Current Market Rate per Tonne (INR)", 
        min_value=500, 
        max_value=100000, 
        value=st.session_state.price_per_tonne, 
        step=10,
        help="This is the value used to multiply your total tonnes to calculate revenue."
    )
    
    if new_price != st.session_state.price_per_tonne:
        st.session_state.price_per_tonne = new_price
        st.success(f"Successfully configured market rate. New rate is: ₹ {new_price:,} / tonne")
        st.info("Navigate back to the Dashboard to see your dynamically updated Revenue metric!")
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Financial breakdown cards
    p_cols = st.columns(2)
    with p_cols[0]:
        st.markdown(textwrap.dedent(f'''
            <div class="panel-card">
                <h4 style="margin:0; color:#5C6B5E; font-size: 13px; text-transform: uppercase;">Estimated Earnings summary</h4>
                <div style="font-size: 28px; font-weight: 700; color: #1A231C; margin: 10px 0;">₹ {total_revenue_rs:,.2f}</div>
                <p style="font-size:14px; color:#5C6B5E; margin:0;">Calculated from {total_harvest:.1f} total harvest tonnes at ₹ {st.session_state.price_per_tonne:,} rate.</p>
            </div>
        '''), unsafe_allow_html=True)
