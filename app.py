import streamlit as st

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

