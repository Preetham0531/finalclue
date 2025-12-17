import streamlit as st
from datetime import datetime, timedelta

# Set deployment date (update this when you deploy)
DEPLOYMENT_DATE = datetime(2025, 12, 17)  # Update this to today's date
EXPIRATION_DAYS = 3
EXPIRATION_DATE = DEPLOYMENT_DATE + timedelta(days=EXPIRATION_DAYS)

# Check if app has expired
if datetime.now() > EXPIRATION_DATE:
    st.set_page_config(
        page_title="Expired",
        page_icon="💐",
        layout="centered"
    )
    st.markdown("""
        <style>
            .main {
                background-color: white !important;
            }
            .stApp {
                background-color: white !important;
            }
            .expired {
                text-align: center;
                font-size: 3rem;
                color: #666;
                margin-top: 20%;
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="expired">This app has expired.</div>', unsafe_allow_html=True)
    st.stop()

# Page configuration
st.set_page_config(
    page_title="Well Done",
    page_icon="💐",
    layout="centered"
)

# Custom CSS for beautification
st.markdown("""
    <style>
        .main {
            background-color: white !important;
        }
        .stApp {
            background-color: white !important;
        }
        [data-testid="stAppViewContainer"] {
            background-color: white !important;
        }
        h1.well-done, .well-done {
            font-size: 8rem !important;
            font-weight: 700 !important;
            text-align: center !important;
            color: #FF0000 !important;
            margin-bottom: 3rem !important;
            letter-spacing: 3px !important;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif !important;
            padding-top: 2rem !important;
        }
        .bouquet-container {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin-top: 2rem !important;
            padding: 2rem !important;
        }
        .bouquet {
            font-size: 10rem !important;
            text-align: center !important;
            line-height: 1.2 !important;
            filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1)) !important;
        }
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Main content - using inline style as backup
st.markdown('<h1 class="well-done" style="color: #FF0000 !important; font-size: 8rem !important; font-weight: 700 !important; text-align: center !important;">well done</h1>', unsafe_allow_html=True)

# Bouquet logo/emoji - using a beautiful bouquet emoji
st.markdown("""
    <div class="bouquet-container">
        <div class="bouquet">💐</div>
    </div>
""", unsafe_allow_html=True)

# QR Code display using online API
app_url = "https://ihavebeenexpectingyou.streamlit.app/"
qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={app_url}"

st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 2rem;">
        <img src="{}" alt="QR Code" style="border: 2px solid #ddd; border-radius: 10px; padding: 10px; background: white;">
    </div>
""".format(qr_code_url), unsafe_allow_html=True)
