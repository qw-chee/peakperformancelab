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
        "description": "Discover your beliefs about ability and learning. Analyse growth potential through an interactive mindset assessment.",
        "page": "/Growth",
        "color": "#59250E",
        "energy_color": "#32CD32",
        "button_text": "🌱 ENTER THE GARDEN"
    },
    {
        "title": "Inner Critic Boss Fight",
        "icon": "⚔️",
        "description": "Face your challenges head-on with positive self-talk. Build mental toughness through gamified scenarios.",
        "page": "/Fight",
        "color": "#8B0000",
        "energy_color": "#FFD700",
        "button_text": "⚔️ START THE BATTLE"
    },
    {
        "title": "Mission: SMART Possible",
        "icon": "🚀",
        "description": "Identify SMART goals that drive results. Learn the framework for setting and achieving meaningful objectives.",
        "page": "/Smart",
        "color": "#FF8C00",
        "energy_color": "#9370DB",
        "button_text": "🚀 LAUNCH MISSION"
    },
    {
        "title": "Imagery Rehearsal Stage",
        "icon": "🎬",
        "description": "Master the art of mental rehearsal and visualization. Train your mind through guided imagery techniques.",
        "page": "/Imagery",
        "color": "#4B0082",
        "energy_color": "#FF4500",
        "button_text": "🎬 ENTER THE STAGE"
    }
]

# ---------------------------- KINETIC ENERGY STYLES ----------------------------
def get_kinetic_energy_styles():
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

    /* Remove padding from main container */
    .main .block-container {
        padding: 0 !important;
        max-width: none !important;
    }

    /* KINETIC ENERGY BACKGROUND */
    .stApp {
        background: 
            radial-gradient(circle at 25% 25%, rgba(255, 100, 150, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 75% 75%, rgba(100, 255, 200, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 50% 0%, rgba(150, 100, 255, 0.1) 0%, transparent 50%),
            linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #1a1a2e 100%);
        background-size: 300% 300%, 400% 400%, 200% 200%, 100% 100%;
        animation: energyFlow 20s ease-in-out infinite;
        min-height: 100vh;
        position: relative;
        overflow-x: hidden;
    }

    @keyframes energyFlow {
        0%, 100% { 
            background-position: 0% 0%, 0% 0%, 0% 0%, 0% 0%; 
        }
        33% { 
            background-position: 100% 100%, 50% 50%, 100% 0%, 0% 0%; 
        }
        66% { 
            background-position: 0% 100%, 100% 0%, 50% 100%, 0% 0%; 
        }
    }

    /* FLOATING ENERGY PARTICLES */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(3px 3px at 40px 60px, rgba(255, 255, 100, 0.8), transparent),
            radial-gradient(2px 2px at 80px 40px, rgba(100, 255, 255, 0.6), transparent),
            radial-gradient(4px 4px at 120px 100px, rgba(255, 100, 255, 0.4), transparent),
            radial-gradient(2px 2px at 200px 50px, rgba(255, 255, 255, 0.5), transparent),
            radial-gradient(3px 3px at 300px 120px, rgba(100, 255, 150, 0.7), transparent);
        background-repeat: repeat;
        background-size: 350px 200px;
        animation: particleFloat 25s linear infinite, particlePulse 3s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
        opacity: 0.6;
    }

    @keyframes particleFloat {
        from { transform: translate(0px, 100vh) rotate(0deg); }
        to { transform: translate(100px, -100px) rotate(360deg); }
    }

    @keyframes particlePulse {
        0%, 100% { opacity: 0.4; }
        50% { opacity: 0.8; }
    }
    
    /* ENERGY FIELD CONTAINERS */
    .main-container {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 30px;
        padding: 40px;
        margin: 30px 0;
        position: relative;
        z-index: 10;
        box-shadow: 
            0 10px 40px rgba(0, 0, 0, 0.3),
            inset 0 0 0 1px rgba(255, 255, 255, 0.1),
            0 0 100px rgba(100, 200, 255, 0.1);
        animation: containerCharge 6s ease-in-out infinite;
        transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }

    .main-container:hover {
        transform: scale(1.02);
        box-shadow: 
            0 15px 50px rgba(0, 0, 0, 0.4),
            inset 0 0 0 2px rgba(255, 255, 255, 0.2),
            0 0 120px rgba(255, 200, 100, 0.2);
    }

    @keyframes containerCharge {
        0%, 100% { 
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.1), 0 0 100px rgba(100, 200, 255, 0.1);
        }
        50% { 
            box-shadow: 0 15px 50px rgba(0, 0, 0, 0.4), inset 0 0 0 1px rgba(255, 255, 255, 0.15), 0 0 120px rgba(255, 100, 200, 0.15);
        }
    }

    /* ELECTRIC TITLE EFFECTS */
    .energy-title {
        font-family: 'Poetsen One', cursive;
        font-weight: 700;
        font-size: 4em;
        color: #fff;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 
            0 0 10px rgba(255, 255, 255, 0.8),
            0 0 20px rgba(100, 255, 255, 0.6),
            0 0 30px rgba(255, 100, 255, 0.4);
        animation: titleElectrify 4s ease-in-out infinite, titleBounce 2s ease-in-out infinite;
        line-height: 1;
        position: relative;
    }

    @keyframes titleElectrify {
        0%, 100% { 
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.8), 0 0 20px rgba(100, 255, 255, 0.6), 0 0 30px rgba(255, 100, 255, 0.4);
        }
        25% { 
            text-shadow: 0 0 15px rgba(255, 255, 100, 0.9), 0 0 25px rgba(255, 100, 100, 0.7), 0 0 35px rgba(100, 255, 100, 0.5);
        }
        75% { 
            text-shadow: 0 0 12px rgba(100, 100, 255, 0.8), 0 0 22px rgba(255, 255, 100, 0.6), 0 0 32px rgba(255, 100, 255, 0.4);
        }
    }

    @keyframes titleBounce {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-5px) scale(1.02); }
    }

    .energy-subtitle {
        font-family: 'Capriola', cursive;
        font-size: 1.4em;
        color: rgba(255, 255, 255, 0.9);
        text-align: center;
        margin-bottom: 40px;
        font-weight: 500;
        animation: subtitlePulse 3s ease-in-out infinite;
        text-shadow: 0 2px 10px rgba(255, 255, 255, 0.3);
    }

    @keyframes subtitlePulse {
        0%, 100% { opacity: 0.8; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.03); }
    }

    /* MAGNETIC MODULE CARDS */
    .module-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(12px);
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 25px;
        padding: 20px;
        text-align: center;
        position: relative;
        overflow: hidden;
        min-height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        box-shadow: 
            0 8px 30px rgba(0, 0, 0, 0.3),
            inset 0 0 0 1px rgba(255, 255, 255, 0.1);
        animation: cardFloat 8s ease-in-out infinite;
    }

    @keyframes cardFloat {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-10px) rotate(0.5deg); }
        50% { transform: translateY(-5px) rotate(-0.3deg); }
        75% { transform: translateY(-15px) rotate(0.8deg); }
    }

    /* MAGNETIC ATTRACTION HOVER EFFECT */
    .module-card:hover {
        transform: translateY(-20px) rotateX(8deg) rotateY(8deg) scale(1.08);
        box-shadow: 
            0 25px 60px rgba(0, 0, 0, 0.4),
            0 0 100px var(--energy-color),
            inset 0 0 0 3px var(--energy-color);
        border-color: var(--energy-color);
        background: rgba(255, 255, 255, 0.25);
        animation: cardCharge 0.6s ease-out;
    }

    @keyframes cardCharge {
        0% { filter: brightness(1); }
        50% { filter: brightness(1.5) saturate(1.5); }
        100% { filter: brightness(1.2) saturate(1.2); }
    }

    /* ENERGY WAVE EFFECT ON HOVER */
    .module-card::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        background: radial-gradient(circle, var(--energy-color) 0%, transparent 70%);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        opacity: 0;
        transition: all 0.6s ease-out;
        z-index: -1;
    }

    .module-card:hover::before {
        width: 300px;
        height: 300px;
        opacity: 0.2;
        animation: energyWave 1s ease-out;
    }

    @keyframes energyWave {
        0% { width: 0; height: 0; opacity: 0.5; }
        50% { width: 200px; height: 200px; opacity: 0.3; }
        100% { width: 300px; height: 300px; opacity: 0.1; }
    }

    /* BOUNCING ICONS WITH PHYSICS */
    .module-icon {
        font-size: 4em;
        margin-bottom: 10px;
        display: block;
        position: relative;
        animation: iconBounce 4s ease-in-out infinite;
        filter: drop-shadow(0 5px 15px rgba(0, 0, 0, 0.3));
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }

    .module-card:hover .module-icon {
        animation: iconElectric 0.6s ease-out, iconBounce 4s ease-in-out infinite;
        transform: scale(1.3);
        filter: drop-shadow(0 10px 30px var(--energy-color));
    }

    @keyframes iconBounce {
        0%, 100% { transform: translateY(0px) rotate(0deg) scale(1); }
        25% { transform: translateY(-15px) rotate(5deg) scale(1.05); }
        50% { transform: translateY(-8px) rotate(-3deg) scale(1.02); }
        75% { transform: translateY(-20px) rotate(8deg) scale(1.08); }
    }

    @keyframes iconElectric {
        0% { transform: scale(1) rotate(0deg); filter: drop-shadow(0 5px 15px rgba(0, 0, 0, 0.3)); }
        25% { transform: scale(1.1) rotate(5deg); filter: drop-shadow(0 10px 20px var(--energy-color)); }
        50% { transform: scale(1.4) rotate(-5deg); filter: drop-shadow(0 15px 35px var(--energy-color)); }
        75% { transform: scale(1.2) rotate(8deg); filter: drop-shadow(0 12px 25px var(--energy-color)); }
        100% { transform: scale(1.3) rotate(0deg); filter: drop-shadow(0 10px 30px var(--energy-color)); }
    }

    /* KINETIC MODULE TITLES */
    .module-title {
        font-family: 'Fredoka', cursive;
        font-weight: 700;
        font-size: 1.5em;
        color: rgba(255, 255, 255, 0.95);
        margin-bottom: 15px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        position: relative;
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        animation: titleWave 6s ease-in-out infinite;
    }

    @keyframes titleWave {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-3px); }
    }

    .module-card:hover .module-title {
        color: #fff;
        text-shadow: 
            0 0 10px var(--energy-color),
            0 2px 10px rgba(0, 0, 0, 0.5);
        transform: scale(1.05) translateY(-5px);
        animation: titleCharge 0.5s ease-out;
    }

    @keyframes titleCharge {
        0% { transform: scale(1) translateY(0px); }
        50% { transform: scale(1.1) translateY(-8px); }
        100% { transform: scale(1.05) translateY(-5px); }
    }

    /* DYNAMIC DESCRIPTIONS */
    .module-description {
        font-family: 'Capriola', cursive;
        font-size: 1em;
        color: rgba(255, 255, 255, 0.8);
        line-height: 1.5;
        font-weight: 400;
        text-align: center;
        margin-bottom: 25px;
        flex-grow: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
        animation: descriptionFloat 7s ease-in-out infinite;
    }

    @keyframes descriptionFloat {
        0%, 100% { transform: translateY(0px); opacity: 0.8; }
        50% { transform: translateY(-2px); opacity: 0.9; }
    }

    .module-card:hover .module-description {
        color: rgba(255, 255, 255, 0.95);
        transform: translateY(-3px);
    }

    /* SPRING-LOADED BUTTONS */
    .stApp div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
        margin-top: auto !important;
    }

    .stApp div[data-testid="stButton"] > button {
        background: linear-gradient(45deg, var(--energy-color), rgba(255, 255, 255, 0.1)) !important;
        border: 3px solid var(--energy-color) !important;
        color: #000 !important;
        font-weight: 800 !important;
        font-size: 1.2em !important;
        font-family: 'Fredoka', cursive !important;
        padding: 15px 30px !important;
        border-radius: 50px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        width: 100% !important;
        position: relative !important;
        overflow: hidden !important;
        transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
        box-shadow: 
            0 5px 20px rgba(0, 0, 0, 0.3),
            0 0 30px var(--energy-color) !important;
        animation: buttonCharge 4s ease-in-out infinite !important;
    }

    @keyframes buttonCharge {
        0%, 100% { 
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3), 0 0 30px var(--energy-color);
            transform: scale(1);
        }
        50% { 
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4), 0 0 40px var(--energy-color);
            transform: scale(1.02);
        }
    }

    .stApp div[data-testid="stButton"] > button:hover {
        transform: translateY(-8px) scale(1.08) !important;
        box-shadow: 
            0 15px 40px rgba(0, 0, 0, 0.4),
            0 0 80px var(--energy-color) !important;
        color: #fff !important;
        border-width: 4px !important;
        animation: buttonExplode 0.6s ease-out !important;
    }

    @keyframes buttonExplode {
        0% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-12px) scale(1.12); }
        100% { transform: translateY(-8px) scale(1.08); }
    }

    /* HIGH-ENERGY LOADING OVERLAY */
    #loading-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at center, rgba(255, 255, 100, 0.1) 0%, transparent 70%),
            linear-gradient(135deg, #0a0a0a, #1a1a2e, #16213e);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        animation: loadingSequence 4s ease-in-out forwards;
    }

    .loading-content {
        text-align: center;
        position: relative;
    }

    .loading-title {
        font-family: 'Poetsen One', cursive;
        font-size: 3.5em;
        font-weight: 700;
        color: #fff;
        margin-bottom: 30px;
        text-shadow: 
            0 0 20px rgba(255, 255, 255, 0.8),
            0 0 40px rgba(100, 255, 255, 0.6),
            0 0 60px rgba(255, 100, 255, 0.4);
        animation: loadingBounce 3s ease-in-out infinite, loadingElectrify 3s ease-in-out infinite;
    }

    @keyframes loadingBounce {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-10px) scale(1.05); }
    }

    @keyframes loadingElectrify {
        0%, 100% { 
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.8), 0 0 40px rgba(100, 255, 255, 0.6), 0 0 60px rgba(255, 100, 255, 0.4);
        }
        50% { 
            text-shadow: 0 0 30px rgba(255, 255, 100, 0.9), 0 0 50px rgba(255, 100, 100, 0.7), 0 0 70px rgba(100, 255, 100, 0.5);
        }
    }

    .kinetic-loading-bar {
        width: 400px;
        height: 15px;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 10px;
        overflow: hidden;
        position: relative;
        margin: 0 auto 20px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 
            0 0 20px rgba(255, 255, 255, 0.2),
            inset 0 0 10px rgba(0, 0, 0, 0.5);
    }

    .kinetic-loading-fill {
        height: 100%;
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #ffeaa7);
        background-size: 300% 100%;
        border-radius: 8px;
        animation: kineticLoader 2s ease-in-out infinite, loadingFill 4s ease-out forwards;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
        width: 0%;
    }

    @keyframes kineticLoader {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    @keyframes loadingFill {
        0% { width: 0%; }
        100% { width: 100%; }
    }

    .loading-subtitle {
        color: rgba(255, 255, 255, 0.9);
        margin-top: 20px;
        font-family: 'Capriola', cursive;
        font-size: 1.3em;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 2px;
        animation: subtitleCharge 2s ease-in-out infinite alternate;
    }

    @keyframes subtitleCharge {
        from { 
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.3); 
            transform: scale(1);
        }
        to { 
            text-shadow: 0 0 20px rgba(255, 255, 100, 0.6); 
            transform: scale(1.02);
        }
    }

    @keyframes loadingSequence {
        0% { opacity: 1; }
        90% { opacity: 1; }
        100% { opacity: 0; pointer-events: none; }
    }

    /* RESPONSIVE KINETIC EFFECTS */
    @media (max-width: 768px) {
        .energy-title {
            font-size: 3em;
        }
        
        .module-icon {
            font-size: 4em;
        }
        
        .module-title {
            font-size: 1.7em;
        }
        
        .module-card {
            min-height: 250px;
            padding: 25px;
        }
        
        .loading-title {
            font-size: 2.5em;
        }
        
        .kinetic-loading-bar {
            width: 300px;
        }
    }

    /* FORCE KINETIC FONT LOADING */
    * {
        font-family: 'Poetsen One', 'Capriola', 'Fredoka', sans-serif;
    }
    </style>
    """

# Apply the KINETIC ENERGY styles
st.markdown(get_kinetic_energy_styles(), unsafe_allow_html=True)

# ---------------------------- ENERGY LOADING OVERLAY ----------------------------
if not st.session_state.modules_background_loaded:
    st.markdown("""
    <div id="loading-overlay">
        <div class="loading-content">
            <div class="loading-title">🏆 Peak Performance Lab</div>
            <div class="kinetic-loading-bar">
                <div class="kinetic-loading-fill"></div>
            </div>
            <div class="loading-subtitle">Charging Energy Systems...</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.modules_background_loaded = True

# ---------------------------- KINETIC MAIN CONTENT ----------------------------
# Instructions section with kinetic energy
st.markdown("""
<div class="main-container">
    <div style="font-family: 'Capriola', cursive; font-size: 1.1em; color: rgba(255, 255, 255, 0.9); text-align: center; line-height: 1.5; animation: instructionsGlow 4s ease-in-out infinite alternate;">
        <strong style="color: #fff; text-shadow: 0 0 10px rgba(255, 255, 100, 0.5); font-size: 1.5em;">Ready to unlock your potential?</strong><br>
        Click on any module to begin your journey toward peak performance. 
        Each module is designed to build specific mental skills and strategies.
    </div>
</div>

<style>
@keyframes instructionsGlow {
    from { text-shadow: 0 2px 10px rgba(255, 255, 255, 0.3); }
    to { text-shadow: 0 2px 15px rgba(255, 255, 100, 0.4); }
}
</style>
""", unsafe_allow_html=True)

# Create 2x2 grid with physics-based interactions
col1, col2 = st.columns(2, gap="large")

# Row 1 - Growth and Fight modules
with col1:
    module = MODULES[0]  # Growth module
    st.markdown(f"""
    <div class="module-card" 
         style="--energy-color: {module['energy_color']};">
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
        --energy-color: {module['energy_color']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    if st.button(module['button_text'], key="growth_module", use_container_width=True):
        st.switch_page(module['page'])

with col2:
    module = MODULES[1]  # Fight module
    st.markdown(f"""
    <div class="module-card" 
         style="--energy-color: {module['energy_color']};">
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
        --energy-color: {module['energy_color']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    if st.button(module['button_text'], key="fight_module", use_container_width=True):
        st.switch_page(module['page'])

# Row 2 - Smart and Imagery modules
col3, col4 = st.columns(2, gap="large")

with col3:
    module = MODULES[2]  # Smart module
    st.markdown(f"""
    <div class="module-card" 
         style="--energy-color: {module['energy_color']};">
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
        --energy-color: {module['energy_color']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    if st.button(module['button_text'], key="smart_module", use_container_width=True):
        st.switch_page(module['page'])

with col4:
    module = MODULES[3]  # Imagery module
    st.markdown(f"""
    <div class="module-card" 
         style="--energy-color: {module['energy_color']};">
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
        --energy-color: {module['energy_color']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    if st.button(module['button_text'], key="imagery_module", use_container_width=True):
        st.switch_page(module['page'])
