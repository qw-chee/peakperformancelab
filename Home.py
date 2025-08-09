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

# Enhanced JavaScript with debugging
click_handler = """
<script>
console.log('JavaScript loaded successfully!');

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded');
});

document.addEventListener('click', function(e) {
    console.log('Click detected on:', e.target);
    console.log('Click coordinates:', e.clientX, e.clientY);
    
    // Check if it's a Streamlit element
    if (e.target.closest('[data-testid]') || e.target.closest('button') || e.target.closest('a')) {
        console.log('Streamlit element clicked, ignoring');
        return;
    }
    
    console.log('Valid click detected, trying multiple navigation methods...');
    console.log('Current URL:', window.location.href);
    console.log('Target URL:', window.location.origin + '/Instructions');
    
    // Add alert to confirm JavaScript is working
    alert('Redirecting to Instructions page...');
    
    // Try multiple navigation methods
    try {
        // Method 1: Direct assignment
        window.location.href = '/Instructions';
    } catch (e1) {
        console.log('Method 1 failed:', e1);
        try {
            // Method 2: window.open
            window.open('/Instructions', '_self');
        } catch (e2) {
            console.log('Method 2 failed:', e2);
            try {
                // Method 3: location.assign
                window.location.assign('/Instructions');
            } catch (e3) {
                console.log('All navigation methods failed:', e3);
            }
        }
    }
}, true); // Use capture phase

// Also handle keyboard events for accessibility
document.addEventListener('keydown', function(e) {
    console.log('Key pressed:', e.key);
    if (e.key === 'Enter' || e.key === ' ') {
        console.log('Enter/Space pressed, redirecting...');
        window.location.href = window.location.origin + '/Instructions';
    }
});

// Test if overlay is blocking
document.addEventListener('click', function(e) {
    console.log('Second listener - Element clicked:', e.target.className);
}, false);
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

/* Invisible overlay to capture clicks - make it visible for debugging */
.click-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 1000;
    cursor: pointer;
    background: rgba(255, 0, 0, 0.1); /* Temporarily visible for debugging */
}

/* Debug info */
.debug-info {
    position: fixed;
    top: 10px;
    right: 10px;
    background: rgba(0, 0, 0, 0.8);
    color: white;
    padding: 10px;
    border-radius: 5px;
    z-index: 10000;
    font-family: monospace;
    font-size: 12px;
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

# Add debug info
st.markdown("""
<div class="debug-info">
    Debug Mode: Click anywhere<br>
    Press F12 for console logs<br>
    Red tint = clickable area
</div>
""", unsafe_allow_html=True)

# Add click handler
st.markdown(click_handler, unsafe_allow_html=True)

# Invisible clickable overlay (temporarily visible)
st.markdown("""
<div class="click-overlay" title="Click me!"></div>
""", unsafe_allow_html=True)

# Fallback navigation button using JavaScript
st.markdown("""
<div style="position: fixed; bottom: 20px; right: 20px; z-index: 10001;">
    <button onclick="window.open('/Instructions', '_self')" 
            style="background: linear-gradient(135deg, #1da088 0%, #41c0a9 100%); 
                   border: none; 
                   color: white; 
                   padding: 15px 20px; 
                   border-radius: 25px; 
                   font-size: 16px; 
                   cursor: pointer; 
                   box-shadow: 0 4px 15px rgba(29, 160, 136, 0.3);
                   font-family: 'Fredoka', cursive;
                   font-weight: 600;">
        🚀 Go to Instructions (JS)
    </button>
</div>
""", unsafe_allow_html=True)

# Add empty content to prevent Streamlit from showing default content
st.markdown("")
