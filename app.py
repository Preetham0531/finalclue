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
        /* Hide Streamlit default elements and ALL branding */
        #MainMenu {visibility: hidden !important; display: none !important;}
        footer {visibility: hidden !important; display: none !important; height: 0 !important;}
        header {visibility: hidden !important; display: none !important; height: 0 !important;}
        [data-testid="stHeader"] {visibility: hidden !important; display: none !important; height: 0 !important;}
        [data-testid="stToolbar"] {visibility: hidden !important; display: none !important; height: 0 !important;}
        [data-testid="stDecoration"] {visibility: hidden !important; display: none !important; height: 0 !important;}
        .stDeployButton {display: none !important; visibility: hidden !important;}
        #stDecoration {display: none !important; visibility: hidden !important;}
        /* Hide any text containing username or "hosted by" */
        *:not(script):not(style) {
            text-transform: none !important;
        }
        /* Aggressive hiding of any Streamlit branding */
        .stApp > footer,
        .stApp > header,
        [data-testid="stAppViewContainer"] > footer,
        [data-testid="stAppViewContainer"] > header,
        iframe[title*="streamlit"],
        div[class*="stHeader"],
        div[class*="stToolbar"],
        div[id*="stHeader"],
        div[id*="stToolbar"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            width: 0 !important;
            opacity: 0 !important;
        }
    </style>
    <script>
        // Aggressive JavaScript to remove ALL branding and username references
        (function() {
            function removeBranding() {
                // Remove any element containing "preetham0531" or "hosted by"
                const allElements = document.querySelectorAll('*');
                allElements.forEach(el => {
                    const text = el.textContent || el.innerText || '';
                    const html = el.innerHTML || '';
                    if (text.toLowerCase().includes('preetham0531') || 
                        text.toLowerCase().includes('hosted by') ||
                        html.toLowerCase().includes('preetham0531') ||
                        html.toLowerCase().includes('hosted by')) {
                        el.style.display = 'none';
                        el.style.visibility = 'hidden';
                        el.remove();
                    }
                });
                
                // Remove Streamlit branding elements
                const selectors = [
                    'footer',
                    'header',
                    '[data-testid="stHeader"]',
                    '[data-testid="stToolbar"]',
                    '[data-testid="stDecoration"]',
                    '.stDeployButton',
                    '#stDecoration',
                    '[class*="stHeader"]',
                    '[class*="stToolbar"]',
                    '[id*="stHeader"]',
                    '[id*="stToolbar"]'
                ];
                
                selectors.forEach(selector => {
                    document.querySelectorAll(selector).forEach(el => {
                        el.style.display = 'none';
                        el.style.visibility = 'hidden';
                        el.style.height = '0';
                        el.style.width = '0';
                        el.style.opacity = '0';
                        el.remove();
                    });
                });
            }
            
            // Run immediately
            removeBranding();
            
            // Run on DOM load
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', removeBranding);
            }
            
            // Use MutationObserver to catch dynamically added elements
            const observer = new MutationObserver(function(mutations) {
                removeBranding();
            });
            
            observer.observe(document.body, {
                childList: true,
                subtree: true,
                attributes: true,
                characterData: true
            });
            
            // Also run periodically to catch late-loading elements
            setInterval(removeBranding, 100);
        })();
    </script>
""", unsafe_allow_html=True)

# Main content - using inline style as backup
st.markdown('<h1 class="well-done" style="color: #FF0000 !important; font-size: 8rem !important; font-weight: 700 !important; text-align: center !important;">well done</h1>', unsafe_allow_html=True)

# Bouquet logo/emoji - using a beautiful bouquet emoji
st.markdown("""
    <div class="bouquet-container">
        <div class="bouquet">💐</div>
    </div>
""", unsafe_allow_html=True)