import streamlit as st

st.set_page_config(
    page_title="Peak Performance Lab", 
    layout="centered",
    page_icon="🏆"
)

# ---------------------------- SESSION STATE INIT ----------------------------
def init_session_state():
    if 'modules_background_loaded' not in st.session_state:
        st.session_state.modules_background_loaded = False

init_session_state()

# ---------------------------- MODULE DATA ----------------------------
MODULES = [
    {
        "title": "Mindset Growth Garden",
        "icon": "🌱",
        "description": "Discover your beliefs about ability and learning. Transform fixed thinking into growth potential through an interactive mindset assessment.",
        "page": "pages/Growth.py",
        "color": "#59250e",
        "bg_color": "rgba(89, 37, 14, 0.1)",
        "border_color": "#32CD32",
        "button_text": "🌱 Enter the Garden"
    },
    {
        "title": "Inner Critic Boss Fight",
        "icon": "⚔️",
        "description": "Face your challenges head-on with positive self-talk and resilience. Build mental toughness through gamified scenarios.",
        "page": "pages/Fight.py",
        "color": "#8B0000",
        "bg_color": "rgba(139, 0, 0, 0.1)",
        "border_color": "#FF4500",
        "button_text": "⚔️ Start the Battle"
    },
    {
        "title": "Mission: SMART Possible",
        "icon": "🚀",
        "description": "Identify SMART goals that drive results. Learn the framework for setting and achieving meaningful objectives.",
        "page": "pages/Smart.py",
        "color": "#FF8C00",
        "bg_color": "rgba(255, 140, 0, 0.1)",
        "border_color": "#FFD700",
        "button_text": "🚀 Launch Mission"
    },
    {
        "title": "Imagery Rehearsal Stage",
        "icon": "🎬",
        "description": "Master the art of mental rehearsal and visualization. Train your mind to perform at peak levels through guided imagery techniques.",
        "page": "pages/Imagery.py",
        "color": "#4B0082",
        "bg_color": "rgba(75, 0, 130, 0.1)",
        "border_color": "#9370DB",
        "button_text": "🎬 Enter the Stage"
    }
]

# ---------------------------- STYLES ----------------------------
def get_styles():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poetsen+One&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Capriola&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300;400;500;600;700&display=swap');

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

    .stApp {
        background-image: url('https://www.dropbox.com/scl/fi/7j3zoxr6e5b6fpy7lxf6m/modules.gif?rlkey=3w4b2hav3g3btlm7t8bh9z0js&st=k7xnptbs&raw=1');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        min-height: 100vh;
    }
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(100, 204, 186, 0.1) 0%, rgba(65, 192, 169, 0.1) 25%, rgba(29, 160, 136, 0.1) 50%, rgba(20, 120, 100, 0.05) 75%, rgba(15, 80, 70, 0.05) 100%);
        z-index: -1;
        pointer-events: none;
    }

    /* Main containers */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        border: 3px solid #1da088;
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        position: relative;
        backdrop-filter: blur(8px);
        box-shadow: 0 8px 32px rgba(29, 160, 136, 0.2), inset 0 0 20px rgba(29, 160, 136, 0.1);
    }
    
    .main-container::before {
        content: '';
        position: absolute;
        top: -5px;
        left: -5px;
        right: -5px;
        bottom: -5px;
        background: white;
        border-radius: 23px;
        z-index: -1;
        opacity: 0.3;
    }

    /* Title styles */
    .main-title {
        font-family: 'Poetsen One', cursive;
        font-weight: 700;
        font-size: 3.2em;
        color: #1da088;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(29, 160, 136, 0.2);
        line-height: 1.1;
    }
    
    .subtitle {
        font-family: 'Capriola', cursive;
        font-size: 1.3em;
        color: #41c0a9;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 500;
        text-shadow: 1px 1px 2px rgba(65, 192, 169, 0.2);
    }

    /* Module cards */
    .module-card {
        background: rgba(255, 255, 255, 0.95);
        border: 3px solid var(--border-color);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(5px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
        min-height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 20px;
    }

    .module-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: left 0.6s ease;
    }

    .module-card:hover {
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.2);
        border-width: 4px;
    }

    .module-card:hover::before {
        left: 100%;
    }

    .module-icon {
        font-size: 4em;
        margin-bottom: 15px;
        display: block;
        animation: float 3s ease-in-out infinite;
        filter: drop-shadow(2px 2px 4px rgba(0, 0, 0, 0.1));
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-8px) rotate(2deg); }
    }

    .module-title {
        font-family: 'Fredoka', cursive;
        font-weight: 700;
        font-size: 1.8em;
        color: var(--title-color);
        margin-bottom: 12px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        line-height: 1.2;
    }

    .module-description {
        font-family: 'Capriola', cursive;
        font-size: 0.95em;
        color: #2c5f5a;
        line-height: 1.4;
        font-weight: 400;
        text-align: center;
        margin-bottom: 20px;
        flex-grow: 1;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Button styling */
    .stApp div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
        margin-top: auto !important;
    }

    .stApp div[data-testid="stButton"] > button,
    div[data-testid="stButton"] button {
        background: var(--button-bg, #f05151) !important;
        border: 3px solid #353535 !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.2em !important;
        font-family: 'Fredoka', cursive !important;
        padding: 12px 24px !important;
        border-radius: 25px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
        transition: all 0.3s ease !important;
        text-transform: none !important;
        letter-spacing: 0.5px !important;
        width: 100% !important;
        white-space: nowrap !important;
    }

    .stApp div[data-testid="stButton"] > button:hover,
    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px) scale(1.05) !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3) !important;
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
        font-family: 'Capriola', sans-serif;
        font-size: 3em;
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
        font-family: 'Segoe UI' !important;
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

    /* Instructions section styling */
    .instructions-text {
        font-family: 'Capriola', cursive; 
        font-size: 1.1em; 
        color: #2c5f5a; 
        text-align: center; 
        line-height: 1.5;
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5em;
        }
        
        .module-icon {
            font-size: 3em;
        }
        
        .module-title {
            font-size: 1.6em;
        }
        
        .module-card {
            min-height: 220px;
            padding: 20px;
        }
    }

    /* Force font loading */
    * {
        font-family: 'Poetsen One', 'Capriola', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """

# Apply styles
st.markdown(get_styles(), unsafe_allow_html=True)

# ---------------------------- LOADING OVERLAY ----------------------------
if not st.session_state.modules_background_loaded:
    st.markdown("""
    <div id="loading-overlay">
        <div class="loading-content">
            <div class="loading-title">🏆 Peak Performance Lab</div>
            <div class="loading-bar-container">
                <div class="loading-bar"></div>
            </div>
            <div class="loading-subtitle">Loading your training arsenal...</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.modules_background_loaded = True

# Add spacing
st.markdown("<div style='height: 3vh;'></div>", unsafe_allow_html=True)

# ---------------------------- MAIN CONTENT ----------------------------
# Title Section
st.markdown("""
<div class="main-container">
    <h1 class="main-title">🏆 Peak Performance Lab</h1>
    <div class="subtitle">Choose your path to peak performance</div>
</div>
""", unsafe_allow_html=True)

# Modules Section
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Create 2x2 grid
col1, col2 = st.columns(2, gap="large")

# Row 1
with col1:
    module = MODULES[0]  # Growth module
    st.markdown(f"""
    <div class="module-card" style="--border-color: {module['border_color']}; --title-color: {module['color']}; background: {module['bg_color']};">
        <div>
            <span class="module-icon">{module['icon']}</span>
            <div class="module-title">{module['title']}</div>
            <div class="module-description">{module['description']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom button styling for this module
    st.markdown(f"""
    <style>
    div[data-testid="column"]:nth-child(1) div[data-testid="stButton"] > button {{
        --button-bg: {module['color']} !important;
        background: {module['color']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    if st.button(module['button_text'], key="growth_module", use_container_width=True):
        st.switch_page(module['page'])

with col2:
    module = MODULES[1]  # Fight module
    st.markdown(f"""
    <div class="module-card" style="--border-color: {module['border_color']}; --title-color: {module['color']}; background: {module['bg_color']};">
        <div>
            <span class="module-icon">{module['icon']}</span>
            <div class="module-title">{module['title']}</div>
            <div class="module-description">{module['description']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom button styling for this module
    st.markdown(f"""
    <style>
    div[data-testid="column"]:nth-child(2) div[data-testid="stButton"] > button {{
        --button-bg: {module['color']} !important;
        background: {module['color']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    if st.button(module['button_text'], key="fight_module", use_container_width=True):
        st.switch_page(module['page'])

# Row 2
col3, col4 = st.columns(2, gap="large")

with col3:
    module = MODULES[2]  # Smart module
    st.markdown(f"""
    <div class="module-card" style="--border-color: {module['border_color']}; --title-color: {module['color']}; background: {module['bg_color']};">
        <div>
            <span class="module-icon">{module['icon']}</span>
            <div class="module-title">{module['title']}</div>
            <div class="module-description">{module['description']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom button styling for this module
    st.markdown(f"""
    <style>
    div[data-testid="column"]:nth-child(1) div[data-testid="stButton"]:last-of-type > button {{
        --button-bg: {module['color']} !important;
        background: {module['color']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    if st.button(module['button_text'], key="smart_module", use_container_width=True):
        st.switch_page(module['page'])

with col4:
    module = MODULES[3]  # Imagery module
    st.markdown(f"""
    <div class="module-card" style="--border-color: {module['border_color']}; --title-color: {module['color']}; background: {module['bg_color']};">
        <div>
            <span class="module-icon">{module['icon']}</span>
            <div class="module-title">{module['title']}</div>
            <div class="module-description">{module['description']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom button styling for this module
    st.markdown(f"""
    <style>
    div[data-testid="column"]:nth-child(2) div[data-testid="stButton"]:last-of-type > button {{
        --button-bg: {module['color']} !important;
        background: {module['color']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    if st.button(module['button_text'], key="imagery_module", use_container_width=True):
        st.switch_page(module['page'])

st.markdown('</div>', unsafe_allow_html=True)

# Instructions section
st.markdown("""
<div class="main-container">
    <div class="instructions-text">
        <strong>Ready to unlock your potential?</strong><br>
        Click on any module above to begin your journey toward peak performance. 
        Each module is designed to build specific mental skills and strategies.
    </div>
</div>
""", unsafe_allow_html=True)

# Add bottom spacing
st.markdown("<div style='height: 3vh;'></div>", unsafe_allow_html=True)
