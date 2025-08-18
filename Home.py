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

/* Block tablet and mobile devices */
@media screen and (max-width: 1023px) {
    .stApp {
        display: none !important;
    }
    body::before {
        content: "This application is designed for desktop and laptop screens only.";
        display: flex;
        justify-content: center;
        align-items: center;
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: linear-gradient(135deg, #64ccba 0%, #41c0a9 50%, #1da088 100%);
        color: white;
        font-size: 1.5rem;
        text-align: center;
        z-index: 99999;
        font-family: 'Capriola', sans-serif;
    }
}

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
        background-image: url('https://raw.githubusercontent.com/qw-chee/peakperformancelab/main/assets/Hm.gif');
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
        animation: loading-sequence 3s ease-in-out forwards;
    }

    .loading-content {
        text-align: center;
    }

    /* Responsive title sizing */
    .loading-title {
        font-family: 'Capriola', sans-serif;
        font-size: clamp(2rem, 4vw, 4rem);
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

    /* Responsive subtitle */
    .loading-subtitle {
        color: rgba(255, 255, 255, 0.9);
        margin-top: clamp(10px, 1.5vh, 20px);
        font-family: 'Segoe UI', sans-serif !important;
        font-size: clamp(1rem, 1.5vw, 1.5rem);
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

    @keyframes loading-sequence {
        0% { opacity: 1; }
        85% { opacity: 1; }
        100% { opacity: 0; pointer-events: none; }
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
        font-weight: 700 !important;
        font-size: clamp(1.5rem, 3vw, 3.5rem) !important;
        font-family: 'Fredoka', cursive !important;
        padding: clamp(12px, 2vh, 25px) clamp(20px, 3vw, 40px) !important;
        border-radius: clamp(20px, 3vw, 35px) !important;
        box-shadow: 0 clamp(6px, 1vh, 12px) clamp(20px, 3vh, 35px) rgba(29, 160, 136, 0.4) !important;
        transition: all 0.3s ease !important;
        text-transform: none !important;
        letter-spacing: 0.5px !important;
        width: 100% !important;
        min-width: fit-content !important;
        white-space: nowrap !important;
        max-width: clamp(300px, 50vw, 600px) !important;
    }

    .stApp .main .block-container div[data-testid="stButton"] > button:hover,
    .stApp div[data-testid="stButton"] > button[kind="primary"]:hover,
    div[data-testid="stButton"] button:hover {
        background: #f05151 !important;
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 clamp(8px, 1.5vh, 16px) clamp(25px, 4vh, 45px) rgba(29, 160, 136, 0.5) !important;
    }

    /* Responsive spacing for button positioning */
    .button-spacing {
        height: clamp(40vh, 50vh, 65vh) !important;
    }

    /* Force font loading for desktop only */
    .desktop-font {
        font-family: 'Poetsen One', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
}

/* Large Desktop (1440px+) */
@media screen and (min-width: 1440px) {
    .loading-title {
        font-size: 4.5rem;
    }
    
    .loading-subtitle {
        font-size: 1.8rem;
    }
    
    div[data-testid="stButton"] button {
        font-size: 3.5rem !important;
        padding: 25px 45px !important;
    }
}

/* Standard Desktop (1024px-1439px) */
@media screen and (min-width: 1024px) and (max-width: 1439px) {
    .loading-title {
        font-size: 3.5rem;
    }
    
    .loading-subtitle {
        font-size: 1.4rem;
    }
    
    div[data-testid="stButton"] button {
        font-size: 2.8rem !important;
        padding: 18px 35px !important;
    }
}

/* Ultrawide and 4K adjustments */
@media screen and (min-width: 1920px) {
    .loading-bar-container {
        width: 500px;
    }
    
    .loading-title {
        font-size: 5rem;
    }
    
    .loading-subtitle {
        font-size: 2rem;
    }
    
    div[data-testid="stButton"] button {
        font-size: 4rem !important;
        padding: 30px 50px !important;
        max-width: 700px !important;
    }
}

</style>
"""

# Apply styles
st.markdown(page_styles, unsafe_allow_html=True)

# Force styles with JavaScript (additional fix) - Desktop only
st.markdown("""
<script>
// Only apply if screen width > 1024px
if (window.innerWidth >= 1024) {
    setTimeout(function() {
        const buttons = document.querySelectorAll('button');
        buttons.forEach(button => {
            button.classList.add('desktop-font');
            button.style.fontFamily = 'Poetsen One, cursive';
            const screenWidth = window.innerWidth;
            if (screenWidth >= 1920) {
                button.style.fontSize = '4rem';
                button.style.padding = '30px 50px';
            } else if (screenWidth >= 1440) {
                button.style.fontSize = '3.5rem';
                button.style.padding = '25px 45px';
            } else {
                button.style.fontSize = '2.8rem';
                button.style.padding = '18px 35px';
            }
            button.style.fontWeight = '700';
            button.style.color = 'white';
            button.style.background = '#f05151';
            button.style.border = Math.max(4, screenWidth * 0.005) + 'px solid #353535';
            button.style.borderRadius = Math.max(20, screenWidth * 0.02) + 'px';
            button.style.minWidth = 'fit-content';
        });
    }, 100);
    
    // Handle window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth < 1024) {
            document.body.style.display = 'none';
            document.body.innerHTML = '<div style="display: flex; justify-content: center; align-items: center; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: linear-gradient(135deg, #64ccba 0%, #41c0a9 50%, #1da088 100%); color: white; font-size: 1.5rem; text-align: center; font-family: Capriola, sans-serif;">This application is designed for desktop and laptop screens only.</div>';
        }
    });
}
</script>
""", unsafe_allow_html=True)

# ---------------------------- LOADING OVERLAY ----------------------------
if not st.session_state.home_background_loaded:
    st.markdown("""
    <div id="loading-overlay">
        <div class="loading-content">
            <div class="loading-title">🏆 Peak Performance Lab</div>
            <div class="loading-bar-container">
                <div class="loading-bar"></div>
            </div>
            <div class="loading-subtitle">Launching your performance journey...</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.home_background_loaded = True

# ---------------------------- MAIN CONTENT ----------------------------
# Add responsive spacing to position the button
st.markdown("<div class='button-spacing'></div>", unsafe_allow_html=True)

# Navigation button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("S T A R T!", use_container_width=True):
        st.switch_page("pages/Instructions.py")

# Add empty content to prevent Streamlit from showing default content
st.markdown("")
