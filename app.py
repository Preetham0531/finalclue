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
        [data-testid="stHeader"] {visibility: hidden !important; display: none !important; height: 0 !important;}
        [data-testid="stToolbar"] {visibility: hidden !important; display: none !important; height: 0 !important;}
        [data-testid="stDecoration"] {visibility: hidden !important; display: none !important; height: 0 !important;}
        .stDeployButton {display: none !important; visibility: hidden !important;}
        #stDecoration {display: none !important; visibility: hidden !important;}
        /* Aggressive hiding */
        .stApp > footer,
        .stApp > header,
        [data-testid="stAppViewContainer"] > footer,
        [data-testid="stAppViewContainer"] > header {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            width: 0 !important;
            opacity: 0 !important;
        }
    </style>
    <script>
        // Ultra-aggressive JavaScript to remove ALL branding and username references
        (function() {
            function removeBranding() {
                // Remove any element containing username or "hosted by"
                const allElements = document.querySelectorAll('*');
                allElements.forEach(el => {
                    const text = (el.textContent || el.innerText || '').toLowerCase();
                    const html = (el.innerHTML || '').toLowerCase();
                    if (text.includes('preetham0531') || 
                        text.includes('hosted by') ||
                        text.includes('streamlit') ||
                        html.includes('preetham0531') ||
                        html.includes('hosted by')) {
                        el.style.display = 'none';
                        el.style.visibility = 'hidden';
                        el.style.opacity = '0';
                        el.style.height = '0';
                        el.style.width = '0';
                        el.style.position = 'absolute';
                        el.style.left = '-9999px';
                        try { el.remove(); } catch(e) {}
                    }
                });
                
                // Remove all Streamlit UI elements
                const selectors = [
                    'footer', 'header',
                    '[data-testid="stHeader"]',
                    '[data-testid="stToolbar"]',
                    '[data-testid="stDecoration"]',
                    '.stDeployButton',
                    '#stDecoration',
                    '[class*="stHeader"]',
                    '[class*="stToolbar"]',
                    '[id*="stHeader"]',
                    '[id*="stToolbar"]',
                    '[class*="streamlit"]',
                    '[id*="streamlit"]',
                    '[class*="hosted"]',
                    '[id*="hosted"]',
                    '[class*="preetham"]',
                    '[id*="preetham"]'
                ];
                
                selectors.forEach(selector => {
                    try {
                        document.querySelectorAll(selector).forEach(el => {
                            el.style.display = 'none';
                            el.style.visibility = 'hidden';
                            el.style.height = '0';
                            el.style.width = '0';
                            el.style.opacity = '0';
                            el.style.position = 'absolute';
                            el.style.left = '-9999px';
                            try { el.remove(); } catch(e) {}
                        });
                    } catch(e) {}
                });
            }
            
            // Run immediately
            removeBranding();
            
            // Run on DOM load
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', removeBranding);
            } else {
                removeBranding();
            }
            
            // MutationObserver to catch dynamically added elements
            const observer = new MutationObserver(function(mutations) {
                removeBranding();
            });
            
            try {
                observer.observe(document.body || document.documentElement, {
                    childList: true,
                    subtree: true,
                    attributes: true,
                    characterData: true
                });
            } catch(e) {}
            
            // Run periodically to catch late-loading elements
            setInterval(removeBranding, 100);
            
            // Also run on window load
            window.addEventListener('load', removeBranding);
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