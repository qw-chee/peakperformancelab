import streamlit as st

# ---------------------------- SESSION STATE INIT ----------------------------
def init_session_state():
    if 'home_background_loaded' not in st.session_state:
        st.session_state.home_background_loaded = False

init_session_state()

# JavaScript to handle click anywhere and redirect
click_handler = """
<script>
document.addEventListener('click', function(e) {
    // Prevent default behavior for actual Streamlit elements
    if (e.target.closest('[data-testid]') || e.target.closest('button') || e.target.closest('a')) {
        return;
    }
    
    // Redirect to Instructions page
    window.location.href = window.location.origin + '/Instructions';
});

// Also handle keyboard events for accessibility
document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' || e.key === ' ') {
        window.location.href = window.location.origin + '/Instructions';
    }
});
</script>
"""

# CSS for loading overlay and full-screen background
page_styles = """
<style>
/* Hide Streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Remove padding from main container */
.main .block-container {
    padding: 0 !important;
    max-width: none !important;
}

/* Full screen background */
.stApp {
    background-image: url('https://raw.githubusercontent.com/qw-chee/peakperformancelab/main/assets/Home.gif');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    min-height: 100vh;
    cursor: pointer;
}

/* Loading overlay */
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

.loading-title {
    font-family: 'Arial', sans-serif;
    font-size: 3.5em;
    font-weight: 700;
    color: white;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    animation: title-glow 2s ease-in-out infinite;
}

.loading-bar-container {
    width: 300px;
    height: 8px;
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

.loading-subtitle {
    color: rgba(255, 255, 255, 0.9);
    margin-top: 15px;
    font-size: 1.3em;
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

/* Invisible overlay to capture clicks */
.click-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 1000;
    cursor: pointer;
    background: transparent;
}
</style>
"""

# Apply styles
st.markdown(page_styles, unsafe_allow_html=True)

# ---------------------------- LOADING OVERLAY ----------------------------
if not st.session_state.home_background_loaded:
    st.markdown("""
    <div id="loading-overlay">
        <div class="loading-content">
            <div class="loading-title">🏆 Peak Performance Lab</div>
            <div class="loading-bar-container">
                <div class="loading-bar"></div>
            </div>
            <div class="loading-subtitle">Preparing your performance journey...</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.home_background_loaded = True

# Add click handler
st.markdown(click_handler, unsafe_allow_html=True)

# Invisible clickable overlay
st.markdown("""
<div class="click-overlay" title=" "></div>
""", unsafe_allow_html=True)

# Add empty content to prevent Streamlit from showing default content
st.markdown("")
