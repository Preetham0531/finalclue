import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Well Done",
    page_icon="🌸",
    layout="centered"
)

# Custom CSS for beautification
st.markdown("""
    <style>
        .main {
            background-color: white;
        }
        .stApp {
            background-color: white;
        }
        [data-testid="stAppViewContainer"] {
            background-color: white;
        }
        .well-done {
            font-size: 8rem;
            font-weight: 700;
            text-align: center;
            color: #000000;
            margin-bottom: 3rem;
            letter-spacing: 3px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            padding-top: 2rem;
        }
        .bouquet-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 2rem;
            padding: 2rem;
        }
        .bouquet {
            font-size: 10rem;
            text-align: center;
            line-height: 1.2;
            filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1));
        }
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="well-done">well done</h1>', unsafe_allow_html=True)

# Bouquet logo/emoji - using a beautiful bouquet emoji
st.markdown("""
    <div class="bouquet-container">
        <div class="bouquet">💐</div>
    </div>
""", unsafe_allow_html=True)

