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
        "accent_color": "#2ECC71",
        "key": "growth"
    },
    {
        "title": "Inner Critic Boss Fight",
        "icon": "⚔️",
        "description": "Face your challenges head-on with positive self-talk. Build mental toughness through gamified scenarios.",
        "page": "/Fight",
        "accent_color": "#E74C3C",
        "key": "fight"
    },
    {
        "title": "Mission: SMART Possible",
        "icon": "🚀",
        "description": "Identify SMART goals that drive results. Learn the framework for setting and achieving meaningful objectives.",
        "page": "/Smart",
        "accent_color": "#F39C12",
        "key": "smart"
    },
    {
        "title": "Imagery Rehearsal Stage",
        "icon": "🎬",
        "description": "Master the art of mental rehearsal and visualization. Train your mind through guided imagery techniques.",
        "page": "/Imagery",
        "accent_color": "#9B59B6",
        "key": "imagery"
    }
]

# ---------------------------- LIQUID GLASS STYLES ----------------------------
def get_liquid_glass_styles():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    section[data-testid="stSidebar"] {
        display: none !important;
    }

    button[kind="header"][data-testid="baseButton-header"] {
        display: none !important;
    }

    .main .block-container {
        padding: 0 !important;
        max-width: none !important;
    }

    /* LIQUID GLASS BASE - Transparent to show your green background */
    .stApp {
        background: transparent !important;
        min-height: 100vh;
        position: relative;
        overflow-x: hidden;
    }

    /* FLOATING LIQUID BUBBLES */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(255, 255, 255, 0.1) 0%, transparent 40%),
            radial-gradient(circle at 80% 20%, rgba(255, 255, 255, 0.08) 0%, transparent 35%),
            radial-gradient(circle at 40% 80%, rgba(255, 255, 255, 0.12) 0%, transparent 45%),
            radial-gradient(circle at 90% 70%, rgba(255, 255, 255, 0.06) 0%, transparent 30%);
        animation: liquidFloat 20s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
    }

    @keyframes liquidFloat {
        0%, 100% { transform: translate(0px, 0px) scale(1); }
        33% { transform: translate(30px, -20px) scale(1.05); }
        66% { transform: translate(-20px, 15px) scale(0.95); }
    }

    /* LIQUID GLASS CONTAINERS */
    .glass-container {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 24px;
        padding: 40px;
        margin: 30px 0;
        position: relative;
        z-index: 10;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.3),
            0 1px 0 rgba(255, 255, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        overflow: hidden;
    }

    .glass-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        animation: shimmer 3s ease-in-out infinite;
    }

    @keyframes shimmer {
        0%, 100% { opacity: 0; transform: translateX(-100%); }
        50% { opacity: 1; transform: translateX(100%); }
    }

    .glass-container:hover {
        transform: translateY(-2px);
        box-shadow: 
            0 12px 40px rgba(0, 0, 0, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.4),
            0 1px 0 rgba(255, 255, 255, 0.2);
        border-color: rgba(255, 255, 255, 0.3);
    }

    /* LIQUID GLASS TITLE */
    .glass-title {
        font-family: 'Outfit', sans-serif;
        font-weight: 800;
        font-size: 3.5em;
        color: rgba(0, 0, 0, 0.8);
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.5);
        animation: titleFlow 6s ease-in-out infinite;
        line-height: 1.1;
        position: relative;
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.9) 0%, rgba(0, 0, 0, 0.7) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    @keyframes titleFlow {
        0%, 100% { 
            transform: translateY(0px);
            filter: blur(0px);
        }
        50% { 
            transform: translateY(-3px);
            filter: blur(0.5px);
        }
    }

    .glass-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.3em;
        font-weight: 400;
        color: rgba(0, 0, 0, 0.7);
        text-align: center;
        margin-bottom: 40px;
        animation: subtitleWave 4s ease-in-out infinite;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.3);
    }

    @keyframes subtitleWave {
        0%, 100% { opacity: 0.7; transform: scale(1); }
        50% { opacity: 0.9; transform: scale(1.01); }
    }

    /* LIQUID GLASS MODULE CARDS */
    .liquid-card {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 28px;
        padding: 35px 25px;
        text-align: center;
        position: relative;
        overflow: hidden;
        min-height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.08),
            inset 0 1px 0 rgba(255, 255, 255, 0.4),
            0 1px 0 rgba(255, 255, 255, 0.15);
        user-select: none;
        animation: cardLiquidFloat 8s ease-in-out infinite;
        tabindex: 0;
    }

    @keyframes cardLiquidFloat {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-8px) rotate(0.3deg); }
        50% { transform: translateY(-4px) rotate(-0.2deg); }
        75% { transform: translateY(-12px) rotate(0.5deg); }
    }

    /* LIQUID RIPPLE EFFECT */
    .liquid-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--accent-color), transparent);
        opacity: 0;
        animation: liquidRipple 3s ease-in-out infinite;
    }

    @keyframes liquidRipple {
        0%, 100% { 
            opacity: 0; 
            transform: translateX(-100%) scaleX(0.5); 
        }
        50% { 
            opacity: 0.6; 
            transform: translateX(100%) scaleX(1); 
        }
    }

    /* LIQUID HOVER EFFECTS */
    .liquid-card:hover {
        transform: translateY(-15px) scale(1.05);
        box-shadow: 
            0 20px 60px rgba(0, 0, 0, 0.15),
            0 0 0 1px var(--accent-color),
            inset 0 1px 0 rgba(255, 255, 255, 0.5);
        border-color: var(--accent-color);
        background: rgba(255, 255, 255, 0.3);
    }

    .liquid-card:hover::before {
        animation: liquidRippleActive 0.8s ease-out;
        opacity: 0.8;
    }

    @keyframes liquidRippleActive {
        0% { transform: translateX(-100%) scaleX(0); opacity: 0; }
        50% { transform: translateX(0%) scaleX(1); opacity: 0.8; }
        100% { transform: translateX(100%) scaleX(0); opacity: 0; }
    }

    /* LIQUID SURFACE EFFECT */
    .liquid-card::after {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, 
            rgba(255, 255, 255, 0.1) 0%,
            rgba(255, 255, 255, 0.05) 25%,
            rgba(255, 255, 255, 0.1) 50%,
            rgba(255, 255, 255, 0.05) 75%,
            rgba(255, 255, 255, 0.1) 100%);
        border-radius: 30px;
        z-index: -1;
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .liquid-card:hover::after {
        opacity: 1;
        animation: liquidSurface 2s ease-in-out infinite;
    }

    @keyframes liquidSurface {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    /* FLOATING GLASS ICONS */
    .liquid-icon {
        font-size: 4em;
        margin-bottom: 24px;
        display: block;
        position: relative;
        animation: iconLiquidBob 5s ease-in-out infinite;
        filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.1));
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    .liquid-card:hover .liquid-icon {
        transform: scale(1.2);
        animation: iconLiquidActive 1s ease-out, iconLiquidBob 5s ease-in-out infinite;
        filter: drop-shadow(0 8px 24px rgba(0, 0, 0, 0.2));
    }

    @keyframes iconLiquidBob {
        0%, 100% { transform: translateY(0px) scale(1); }
        25% { transform: translateY(-8px) scale(1.02); }
        50% { transform: translateY(-4px) scale(1); }
        75% { transform: translateY(-12px) scale(1.01); }
    }

    @keyframes iconLiquidActive {
        0% { transform: scale(1) rotateY(0deg); }
        50% { transform: scale(1.3) rotateY(180deg); }
        100% { transform: scale(1.2) rotateY(360deg); }
    }

    /* LIQUID GLASS TYPOGRAPHY */
    .liquid-title {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
        font-size: 1.6em;
        color: rgba(0, 0, 0, 0.85);
        margin-bottom: 20px;
        text-shadow: 0 1px 3px rgba(255, 255, 255, 0.5);
        position: relative;
        transition: all 0.4s ease;
        animation: titleLiquidWave 7s ease-in-out infinite;
    }

    @keyframes titleLiquidWave {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-2px); }
    }

    .liquid-card:hover .liquid-title {
        color: rgba(0, 0, 0, 0.95);
        text-shadow: 
            0 1px 3px rgba(255, 255, 255, 0.7),
            0 0 20px var(--accent-color);
        transform: translateY(-4px) scale(1.05);
    }

    .liquid-description {
        font-family: 'Inter', sans-serif;
        font-size: 1em;
        font-weight: 400;
        color: rgba(0, 0, 0, 0.65);
        line-height: 1.6;
        text-align: center;
        margin-bottom: 30px;
        flex-grow: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.3);
        animation: descriptionLiquidFlow 6s ease-in-out infinite;
    }

    @keyframes descriptionLiquidFlow {
        0%, 100% { opacity: 0.65; transform: translateY(0px); }
        50% { opacity: 0.8; transform: translateY(-1px); }
    }

    .liquid-card:hover .liquid-description {
        color: rgba(0, 0, 0, 0.8);
        transform: translateY(-3px);
        text-shadow: 0 1px 3px rgba(255, 255, 255, 0.5);
    }

    /* LIQUID CALL TO ACTION */
    .liquid-cta {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
        font-size: 0.95em;
        color: var(--accent-color);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: auto;
        padding: 16px 24px;
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.5);
        animation: ctaLiquidPulse 4s ease-in-out infinite;
        position: relative;
        overflow: hidden;
    }

    @keyframes ctaLiquidPulse {
        0%, 100% { 
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
            transform: scale(1);
        }
        50% { 
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
            transform: scale(1.01);
        }
    }

    .liquid-cta::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.6s ease;
    }

    .liquid-card:hover .liquid-cta {
        background: var(--accent-color);
        color: white;
        transform: translateY(-4px) scale(1.05);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        border-color: var(--accent-color);
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
    }

    .liquid-card:hover .liquid-cta::before {
        left: 100%;
    }

    /* LIQUID ACCESSIBILITY */
    .liquid-card[tabindex="0"]:focus {
        outline: 2px solid var(--accent-color);
        outline-offset: 4px;
        transform: translateY(-10px) scale(1.03);
    }
    
    .liquid-card:active {
        transform: translateY(-5px) scale(0.98);
        transition: all 0.1s ease-out;
    }

    /* LIQUID LOADING OVERLAY */
    #liquid-loading {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(20px);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        animation: liquidLoadingFade 3s ease-in-out forwards;
    }

    .liquid-loading-content {
        text-align: center;
        position: relative;
    }

    .liquid-loading-title {
        font-family: 'Outfit', sans-serif;
        font-size: 3em;
        font-weight: 700;
        color: rgba(0, 0, 0, 0.8);
        margin-bottom: 30px;
        text-shadow: 0 2px 4px rgba(255, 255, 255, 0.5);
        animation: liquidLoadingPulse 2s ease-in-out infinite;
    }

    @keyframes liquidLoadingPulse {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.05); opacity: 1; }
    }

    .liquid-progress {
        width: 300px;
        height: 6px;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 3px;
        overflow: hidden;
        position: relative;
        margin: 0 auto 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .liquid-progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #2ECC71, #27AE60, #2ECC71);
        background-size: 200% 100%;
        border-radius: 2px;
        animation: liquidProgressFlow 2s ease-in-out infinite, liquidProgressFill 3s ease-out forwards;
        width: 0%;
    }

    @keyframes liquidProgressFlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    @keyframes liquidProgressFill {
        0% { width: 0%; }
        100% { width: 100%; }
    }

    .liquid-loading-text {
        color: rgba(0, 0, 0, 0.6);
        margin-top: 20px;
        font-family: 'Inter', sans-serif;
        font-size: 1.1em;
        font-weight: 400;
        animation: liquidLoadingTextPulse 3s ease-in-out infinite;
    }

    @keyframes liquidLoadingTextPulse {
        0%, 100% { opacity: 0.6; }
        50% { opacity: 0.9; }
    }

    @keyframes liquidLoadingFade {
        0% { opacity: 1; }
        85% { opacity: 1; }
        100% { opacity: 0; pointer-events: none; }
    }

    /* RESPONSIVE LIQUID GLASS */
    @media (max-width: 768px) {
        .glass-title {
            font-size: 2.5em;
        }
        
        .liquid-icon {
            font-size: 3.5em;
        }
        
        .liquid-title {
            font-size: 1.4em;
        }
        
        .liquid-card {
            min-height: 280px;
            padding: 30px 20px;
        }
        
        .liquid-loading-title {
            font-size: 2.2em;
        }
        
        .liquid-progress {
            width: 250px;
        }
    }
    </style>
    """

# Apply the LIQUID GLASS styles
st.markdown(get_liquid_glass_styles(), unsafe_allow_html=True)

# ---------------------------- LIQUID LOADING OVERLAY ----------------------------
if not st.session_state.modules_background_loaded:
    st.markdown("""
    <div id="liquid-loading">
        <div class="liquid-loading-content">
            <div class="liquid-loading-title">🏆 Peak Performance Lab</div>
            <div class="liquid-progress">
                <div class="liquid-progress-fill"></div>
            </div>
            <div class="liquid-loading-text">Preparing your liquid interface...</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.modules_background_loaded = True

# ---------------------------- LIQUID GLASS MAIN CONTENT ----------------------------
# Instructions section with liquid glass
st.markdown("""
<div class="glass-container">
    <div class="glass-title">🏆 Peak Performance Lab</div>
    <div class="glass-subtitle">
        Ready to unlock your potential? Click on any module card to begin your journey toward peak performance. 
        Each module builds specific mental skills and strategies.
    </div>
</div>
""", unsafe_allow_html=True)

# Create module cards with direct navigation
col1, col2 = st.columns(2, gap="large")
col3, col4 = st.columns(2, gap="large")

# Simple click-based navigation using columns
with col1:
    module = MODULES[0]
    st.markdown(f"""
    <div class="liquid-card" 
         style="--accent-color: {module['accent_color']};"
         tabindex="0">
        <span class="liquid-icon">{module['icon']}</span>
        <div class="liquid-title">{module['title']}</div>
        <div class="liquid-description">{module['description']}</div>
        <div class="liquid-cta">🌱 ENTER THE GARDEN</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Make the entire column clickable
    if st.button("🌱 ENTER THE GARDEN", key="btn_growth", use_container_width=True):
        st.switch_page("pages/Growth.py")

with col2:
    module = MODULES[1]
    st.markdown(f"""
    <div class="liquid-card" 
         style="--accent-color: {module['accent_color']};"
         tabindex="0">
        <span class="liquid-icon">{module['icon']}</span>
        <div class="liquid-title">{module['title']}</div>
        <div class="liquid-description">{module['description']}</div>
        <div class="liquid-cta">⚔️ START THE BATTLE</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("⚔️ START THE BATTLE", key="btn_fight", use_container_width=True):
        st.switch_page("pages/Fight.py")

with col3:
    module = MODULES[2]
    st.markdown(f"""
    <div class="liquid-card" 
         style="--accent-color: {module['accent_color']};"
         tabindex="0">
        <span class="liquid-icon">{module['icon']}</span>
        <div class="liquid-title">{module['title']}</div>
        <div class="liquid-description">{module['description']}</div>
        <div class="liquid-cta">🚀 LAUNCH MISSION</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 LAUNCH MISSION", key="btn_smart", use_container_width=True):
        st.switch_page("pages/Smart.py")

with col4:
    module = MODULES[3]
    st.markdown(f"""
    <div class="liquid-card" 
         style="--accent-color: {module['accent_color']};"
         tabindex="0">
        <span class="liquid-icon">{module['icon']}</span>
        <div class="liquid-title">{module['title']}</div>
        <div class="liquid-description">{module['description']}</div>
        <div class="liquid-cta">🎬 ENTER THE STAGE</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🎬 ENTER THE STAGE", key="btn_imagery", use_container_width=True):
        st.switch_page("pages/Imagery.py")

# Style the navigation buttons to match the liquid glass theme
st.markdown("""
<style>
/* Style the navigation buttons to blend with liquid glass */
.stButton > button {
    background: rgba(255, 255, 255, 0.3) !important;
    backdrop-filter: blur(15px) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 20px !important;
    color: rgba(0, 0, 0, 0.8) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95em !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    padding: 16px 24px !important;
    margin-top: 20px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1) !important;
}

.stButton > button:hover {
    background: rgba(255, 255, 255, 0.5) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15) !important;
    border-color: rgba(255, 255, 255, 0.4) !important;
}

.stButton > button:active {
    transform: translateY(0px) !important;
    background: rgba(255, 255, 255, 0.6) !important;
}

/* Position buttons below cards */
.stButton {
    margin-top: -10px !important;
}
</style>
""", unsafe_allow_html=True)
