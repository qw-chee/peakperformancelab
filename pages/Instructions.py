import streamlit as st

st.set_page_config(
    page_title="Peak Performance Lab", 
    layout="centered",
    page_icon="🏆"
)

# ---------------------------- SESSION STATE INIT ----------------------------
def init_session_state():
    if 'home_background_loaded' not in st.session_state:
        st.session_state.home_background_loaded = False

init_session_state()

# CSS for loading overlay and full-screen background - Desktop/Laptop Responsive
page_styles = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poetsen+One&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Capriola&display=swap');

/* Desktop/Laptop Only Styles */
@media screen and (min-width: 1024px) {
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Hide sidebar permanently */
    section[data-testid="stSidebar"] {
        display: none !important;
    }

    /* Hide sidebar toggle button */
    button[kind="header"][data-testid="baseButton-header"] {
        display: none !important;
    }

    /* Expand main content to full width */
    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: none !important;
    }
    /* Remove padding from main container */
    .main .block-container {
        padding: 0 !important;
        max-width: none !important;
    }

    /* Full screen background */
    .stApp {
        background-image: url('https://raw.githubusercontent.com/qw-chee/peakperformancelab/main/assets/Instruction.gif');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        min-height: 100vh;
        position: relative;
    }

/* Loading overlay - responsive sizing */
        #loading-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #64ccba 0%, #41c0a9 50%, #1da088 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            animation: loading-sequence 2.5s ease-in-out forwards;
        }
        
        @keyframes loading-sequence {
            0% { opacity: 1; }
            85% { opacity: 1; }
            100% { opacity: 0; pointer-events: none; }
        }
        
        .loading-content {
            text-align: center;
        }
        
        /* Responsive loading title */
        .loading-title {
            font-family: 'Capriola', sans-serif;
            font-size: clamp(1.5rem, 4vw, 3rem);
            font-weight: 700;
            color: white;
            margin-bottom: clamp(15px, 2vh, 25px);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            animation: title-glow 2s ease-in-out infinite;
        }
        
        /* Responsive loading bar */
        .loading-bar-container {
            width: clamp(250px, 30vw, 400px);
            height: clamp(6px, 1vh, 10px);
            background: rgba(255, 255, 255, 0.3);
            border-radius: 4px;
            overflow: hidden;
            position: relative;
            margin: 0 auto;
            border: 1px solid white;
        }
        
        .loading-bar {
            width: 40%;
            height: 100%;
            background: linear-gradient(90deg, white, #fbbf24);
            border-radius: 4px;
            animation: loading-bar 2s ease-in-out infinite;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.8);
        }
        
        /* Responsive loading subtitle */
        .loading-subtitle {
            color: rgba(255, 255, 255, 0.9);
            margin-top: clamp(10px, 1.5vh, 20px);
            font-family: 'Segoe UI', sans-serif !important;
            font-size: clamp(0.8rem, 1.5vw, 1.2rem);
            font-weight: 500;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }
        
        @keyframes title-glow {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.8; transform: scale(1.05); }
        }
        
        @keyframes loading-bar {
            0% { transform: translateX(-100%); }
            50% { transform: translateX(0%); }
            100% { transform: translateX(300%); }
        }

    /* Responsive button styling for different desktop sizes */
    .stApp .main .block-container div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
    }

    .stApp .main .block-container div[data-testid="stButton"] > button,
    .stApp div[data-testid="stButton"] > button[kind="primary"],
    div[data-testid="stButton"] button {
        background: #f05151 !important;
        border: clamp(4px, 0.5vw, 8px) solid #353535 !important;
        color: white !important;
        border-radius: clamp(20px, 3vw, 35px) !important;
        box-shadow: 0 clamp(6px, 1vh, 12px) clamp(20px, 3vh, 35px) rgba(29, 160, 136, 0.4) !important;
        transition: all 0.3s ease !important;
        text-transform: none !important;
        letter-spacing: 0.5px !important;
        width: fit-content;
        margin-left: auto !important;
        margin-right: auto !important;
        display: block !important;
    }

    .stApp .main .block-container div[data-testid="stButton"] > button:hover,
    .stApp div[data-testid="stButton"] > button[kind="primary"]:hover,
    div[data-testid="stButton"] button:hover {
        background: #f05151 !important;
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 clamp(8px, 1.5vh, 16px) clamp(25px, 4vh, 45px) rgba(29, 160, 136, 0.5) !important;
    }
        
    /* Force font on all text elements within buttons */
    div[data-testid="stButton"] * {
        font-weight: 500 !important;
        font-size: clamp(0.5rem, 1vw, 3.5rem) !important;
        font-family: 'Poetsen One', cursive !important;
    }
        
    /* Force font loading for desktop only */
    .desktop-font {
        font-family: 'Poetsen One', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Responsive spacing for button positioning */
    .button-spacing {
        height: clamp(43vh, 56vh, 66vh) !important;
    }

    /* Force font loading for desktop only - Remove conflicting universal selector */
    .stApp {
        font-family: 'Poetsen One', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
}

/* Large Desktop (1440px+) */
@media screen and (min-width: 1440px) {
    div[data-testid="stButton"] button {
        font-size: 3.5rem !important;
        padding: 25px 45px !important;
    }
}

/* Standard Desktop (1024px-1439px) */
@media screen and (min-width: 1024px) and (max-width: 1439px) {    
    div[data-testid="stButton"] button {
        font-size: 2.8rem !important;
        padding: 18px 35px !important;
    }
    
    .button-spacing {
        height: 50vh !important;
    }
}

/* Ultrawide and 4K adjustments */
@media screen and (min-width: 1920px) {    
    div[data-testid="stButton"] button {
        font-size: 4rem !important;
        padding: 30px 50px !important;
        max-width: 700px !important;
    }
    
    .button-spacing {
        height: 56vh !important;
    }
}

</style>
"""

# Apply styles
st.markdown(page_styles, unsafe_allow_html=True)

# ---------------------------- LOADING OVERLAY (Always loads first) ----------------------------
st.markdown("""
<div id="loading-overlay">
    <div class="loading-content">
        <div class="loading-title">🏆 Peak Performance Lab</div>
        <div class="loading-bar-container">
            <div class="loading-bar"></div>
        </div>
        <div class="loading-subtitle">Onboarding your mindset...</div>
    </div>
</div>
""", unsafe_allow_html=True)

# JavaScript for enhanced font loading and responsive handling - Desktop only
st.markdown("""
<script>
// Only apply if screen width > 1024px
if (window.innerWidth >= 1024) {
    // Force font loading
    const fontLoad = new FontFace('Poetsen One', 'url(https://fonts.gstatic.com/s/poetsenone/v7/LhWmMV3BOfM6WJbVa1wdF0MzZA6sNw.woff2)');
    fontLoad.load().then(function(font) {
        document.fonts.add(font);
    });
    
    function applyButtonStyles() {
        const buttons = document.querySelectorAll('button');
        buttons.forEach(button => {
            const screenWidth = window.innerWidth;
            
            // Apply font with higher specificity
            button.style.setProperty('font-family', 'Poetsen One, cursive', 'important');
            button.style.setProperty('font-weight', '700', 'important');
            button.style.setProperty('color', 'white', 'important');
            button.style.setProperty('background', '#f05151', 'important');
            
            if (screenWidth >= 1920) {
                button.style.setProperty('font-size', '4rem', 'important');
                button.style.setProperty('padding', '30px 50px', 'important');
            } else if (screenWidth >= 1440) {
                button.style.setProperty('font-size', '3.5rem', 'important');
                button.style.setProperty('padding', '25px 45px', 'important');
            } else {
                button.style.setProperty('font-size', '2.8rem', 'important');
                button.style.setProperty('padding', '18px 35px', 'important');
            }
            
            button.style.setProperty('border', Math.max(4, screenWidth * 0.005) + 'px solid #353535', 'important');
            button.style.setProperty('border-radius', Math.max(20, screenWidth * 0.02) + 'px', 'important');
            button.style.setProperty('min-width', 'fit-content', 'important');
        });
    }
    
    // Apply styles multiple times to ensure they stick
    setTimeout(applyButtonStyles, 100);
    setTimeout(applyButtonStyles, 500);
    setTimeout(applyButtonStyles, 1000);
    
    // Watch for new buttons
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length) {
                setTimeout(applyButtonStyles, 100);
            }
        });
    });
    observer.observe(document.body, { childList: true, subtree: true });
    
    // Handle window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth < 1024) {
            document.body.style.display = 'none';
            document.body.innerHTML = '<div style="display: flex; justify-content: center; align-items: center; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: linear-gradient(135deg, #64ccba 0%, #41c0a9 50%, #1da088 100%); color: white; font-size: 1.5rem; text-align: center; font-family: Capriola, sans-serif;">This application is designed for desktop and laptop screens only.</div>';
        } else {
            applyButtonStyles();
        }
    });
}
</script>
""", unsafe_allow_html=True)

# ---------------------------- MAIN CONTENT ----------------------------
# Add responsive spacing to position the button
st.markdown("<div class='button-spacing'></div>", unsafe_allow_html=True)

# Navigation button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("L E T' S\u00A0\u00A0G O!", use_container_width=True):
        st.switch_page("pages/Modules.py")

# Add empty content to prevent Streamlit from showing default content
st.markdown("")
