import streamlit as st

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
        "url": "/🌱 Mindset Growth Garden",
        "color": "#59250e",
        "bg_color": "rgba(89, 37, 14, 0.1)",
        "border_color": "#32CD32"
    },
    {
        "title": "Inner Critic Boss Fight",
        "icon": "⚔️",
        "description": "Face your challenges head-on with positive self-talk and resilience. Build mental toughness through gamified scenarios.",
        "url": "/⚔️ Inner Critic Boss Fight",
        "color": "#8B0000",
        "bg_color": "rgba(139, 0, 0, 0.1)",
        "border_color": "#FF4500"
    },
    {
        "title": "Mission: SMART Possible",
        "icon": "🚀",
        "description": "Identify SMART goals that drive results. Learn the framework for setting and achieving meaningful objectives.",
        "url": "/🚀 Mission: SMART Possible",
        "color": "#FF8C00",
        "bg_color": "rgba(255, 140, 0, 0.1)",
        "border_color": "#FFD700"
    },
    {
        "title": "Imagery Rehearsal Stage",
        "icon": "🎬",
        "description": "Master the art of mental rehearsal and visualization. Train your mind to perform at peak levels through guided imagery techniques.",
        "url": "/🎬 Imagery Rehearsal Studio",
        "color": "#4B0082",
        "bg_color": "rgba(75, 0, 130, 0.1)",
        "border_color": "#9370DB"
    }
]

# ---------------------------- STYLES ----------------------------
def get_styles():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300;400;500;600;700&family=Comfortaa:wght@300;400;500;600;700&display=swap');

    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

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
        font-family: 'Fredoka', cursive;
        font-weight: 700;
        font-size: 3.2em;
        color: #1da088;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(29, 160, 136, 0.2);
        line-height: 1.1;
    }
    
    .subtitle {
        font-family: 'Comfortaa', cursive;
        font-size: 1.3em;
        color: #41c0a9;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 500;
        text-shadow: 1px 1px 2px rgba(65, 192, 169, 0.2);
    }

    /* Module grid */
    .modules-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 25px;
        margin: 30px 0;
    }

    /* Module cards */
    .module-card {
        background: rgba(255, 255, 255, 0.9);
        border: 3px solid var(--border-color);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        cursor: pointer;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(5px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
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
        font-size: 3.5em;
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
    }

    .module-description {
        font-family: 'Comfortaa', cursive;
        font-size: 0.95em;
        color: #2c5f5a;
        line-height: 1.4;
        font-weight: 400;
        text-align: center;
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
        font-family: 'Fredoka', cursive;
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
        font-family: 'Comfortaa', cursive;
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

    /* Responsive design */
    @media (max-width: 768px) {
        .modules-grid {
            grid-template-columns: 1fr;
            gap: 20px;
        }
        
        .main-title {
            font-size: 2.5em;
        }
        
        .module-card {
            min-height: 180px;
            padding: 20px;
        }
        
        .module-icon {
            font-size: 3em;
        }
        
        .module-title {
            font-size: 1.6em;
        }
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(29, 160, 136, 0.1);
        border-radius: 6px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #1da088, #41c0a9);
        border-radius: 6px;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #41c0a9, #64ccba);
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

# Modules Grid
modules_html = '<div class="main-container"><div class="modules-grid">'

for module in MODULES:
    # JavaScript for navigation
    click_script = f"""
    <script>
    function navigate_{module['title'].replace(' ', '_').lower()}() {{
        window.location.href = window.location.origin + window.location.pathname.replace(/\/[^\/]*$/, '') + '{module["url"]}';
    }}
    </script>
    """
    
    modules_html += f"""
    {click_script}
    <div class="module-card" 
         onclick="navigate_{module['title'].replace(' ', '_').lower()}()" 
         style="--border-color: {module['border_color']}; --title-color: {module['color']}; background: {module['bg_color']};">
        <span class="module-icon">{module['icon']}</span>
        <div class="module-title">{module['title']}</div>
        <div class="module-description">{module['description']}</div>
    </div>
    """

modules_html += '</div></div>'

st.markdown(modules_html, unsafe_allow_html=True)

# Instructions section
st.markdown("""
<div class="main-container">
    <div style="font-family: 'Comfortaa', cursive; font-size: 1.1em; color: #2c5f5a; text-align: center; line-height: 1.5;">
        <strong>Ready to unlock your potential?</strong><br>
        Click on any module above to begin your journey toward peak performance. 
        Each module is designed to build specific mental skills and strategies.
    </div>
</div>
""", unsafe_allow_html=True)

# Add bottom spacing
st.markdown("<div style='height: 3vh;'></div>", unsafe_allow_html=True)