import streamlit as st

st.set_page_config(
    page_title="Peak Performance Lab", 
    layout="wide",
    page_icon="🏆"
)

# ---------------------------- MODULE DATA ----------------------------
MODULES = [
    {
        "title": "Mindset Growth Garden",
        "icon": "🌱",
        "description": "Discover your beliefs about ability and learning. Analyse growth potential through an interactive mindset assessment.",
        "page": "pages/Growth.py",
        "color": "#27AE60",
        "key": "growth"
    },
    {
        "title": "Inner Critic Boss Fight",
        "icon": "⚔️",
        "description": "Face your challenges head-on with positive self-talk. Build mental toughness through gamified scenarios.",
        "page": "pages/Fight.py",
        "color": "#E74C3C",
        "key": "fight"
    },
    {
        "title": "Mission: SMART Possible",
        "icon": "🚀",
        "description": "Identify SMART goals that drive results. Learn the framework for setting and achieving meaningful objectives.",
        "page": "pages/Smart.py",
        "color": "#F39C12",
        "key": "smart"
    },
    {
        "title": "Imagery Rehearsal Stage",
        "icon": "🎬",
        "description": "Master the art of mental rehearsal and visualization. Train your mind through guided imagery techniques.",
        "page": "pages/Imagery.py",
        "color": "#9B59B6",
        "key": "imagery"
    }
]

# ---------------------------- FUN PLAYFUL STYLES ----------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Capriola:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Sour+Gummy:wght@300;400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Remove sidebar */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Fun colorful background with the provided image */
    .stApp {
        background-image: url('https://raw.githubusercontent.com/qw-chee/peakperformancelab/main/assets/Modules.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        min-height: 100vh;
        position: relative;
        overflow-x: hidden;
    }
    
    /* Loading overlay - simple CSS animation */
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
    
    /* Wider container for full-screen fun */
    .main .block-container {
        padding: 2rem 1rem !important;
        max-width: none !important;
        position: relative !important;
        z-index: 100 !important;
    }
    
    /* Floating fun particles */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(255, 255, 255, 0.1) 0%, transparent 20%),
            radial-gradient(circle at 80% 80%, rgba(255, 255, 255, 0.08) 0%, transparent 25%),
            radial-gradient(circle at 40% 40%, rgba(255, 255, 255, 0.12) 0%, transparent 30%),
            radial-gradient(circle at 90% 10%, rgba(255, 255, 255, 0.06) 0%, transparent 20%),
            radial-gradient(circle at 20% 90%, rgba(255, 255, 255, 0.09) 0%, transparent 25%);
        animation: funParticleFloat 20s ease-in-out infinite;
        pointer-events: none;
        z-index: 1 !important;
    }
    
    @keyframes funParticleFloat {
        0%, 100% { transform: translate(0px, 0px) scale(1) rotate(0deg); opacity: 0.6; }
        25% { transform: translate(30px, -20px) scale(1.1) rotate(90deg); opacity: 0.8; }
        50% { transform: translate(-20px, 15px) scale(0.9) rotate(180deg); opacity: 0.5; }
        75% { transform: translate(40px, 10px) scale(1.05) rotate(270deg); opacity: 0.7; }
    }
    
    /* Wiggling subtitle */
    .main-subtitle {
        font-family: 'Sour Gummy', cursive;
        font-size: 1.8rem;
        font-weight: 600;
        color: #34495E !important;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.8);
        animation: wiggleSubtitle 4s ease-in-out infinite;
        position: relative;
        z-index: 101 !important;
    }
    
    @keyframes wiggleSubtitle {
        0%, 100% { transform: translateX(0px) rotate(0deg); }
        25% { transform: translateX(2px) rotate(0.5deg); }
        50% { transform: translateX(-2px) rotate(-0.5deg); }
        75% { transform: translateX(1px) rotate(0.3deg); }
    }
    
    /* Super fun bouncing card-buttons */
    .stButton > button {
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 30px !important;
        padding: 2rem !important;
        margin: 1rem 0 !important;
        box-shadow: 
            0 15px 35px rgba(0,0,0,0.1),
            0 5px 15px rgba(0,0,0,0.05),
            inset 0 1px 0 rgba(255,255,255,0.6) !important;
        border: 3px solid !important;
        transition: all 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
        text-align: center !important;
        position: relative !important;
        overflow: visible !important;
        animation: cardBounceFloat 8s ease-in-out infinite !important;
        z-index: 101 !important;
        transform-origin: center !important;
        width: 100% !important;
        height: auto !important;
        min-height: 300px !important;
        font-family: 'Baloo 2', cursive !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        color: #34495E !important;
        line-height: 1.6 !important;
        white-space: pre-line !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8) !important;
    }
    
    @keyframes cardBounceFloat {
        0%, 100% { 
            transform: translateY(0px) rotate(0deg) scale(1);
        }
        25% { 
            transform: translateY(-20px) rotate(1deg) scale(1.02);
        }
        50% { 
            transform: translateY(-10px) rotate(-0.5deg) scale(0.98);
        }
        75% { 
            transform: translateY(-25px) rotate(1.2deg) scale(1.01);
        }
    }
    
    /* Individual card-button colors */
    div[data-testid="column"]:nth-child(1) .stButton > button {
        border-color: #27AE60 !important;
        animation-delay: 0s !important;
    }
    
    div[data-testid="column"]:nth-child(2) .stButton > button {
        border-color: #E74C3C !important;
        animation-delay: 0.2s !important;
    }
    
    div[data-testid="column"]:nth-child(3) .stButton > button {
        border-color: #F39C12 !important;
        animation-delay: 0.4s !important;
    }
    
    div[data-testid="column"]:nth-child(4) .stButton > button {
        border-color: #9B59B6 !important;
        animation-delay: 0.6s !important;
    }
    
    /* Rainbow shimmer effect */
    .stButton > button::before {
        content: '';
        position: absolute;
        top: -5px;
        left: -5px;
        right: -5px;
        bottom: -5px;
        background: linear-gradient(45deg, 
            #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FECA57, #FF9F43, #EE5A24, #0F3460);
        background-size: 400% 400%;
        border-radius: 35px;
        z-index: -1;
        animation: rainbowShimmer 3s ease-in-out infinite;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    @keyframes rainbowShimmer {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Super bouncy hover effects */
    .stButton > button:hover {
        transform: translateY(-30px) scale(1.08) rotate(3deg) !important;
        box-shadow: 
            0 25px 50px rgba(0,0,0,0.2),
            0 10px 25px rgba(0,0,0,0.1),
            inset 0 1px 0 rgba(255,255,255,0.8) !important;
        animation: none !important;
        color: #2C3E50 !important;
    }
    
    .stButton > button:hover::before {
        opacity: 0.3;
    }
    
    /* Button centering */
    .stButton {
        display: flex;
        justify-content: center;
        margin: 1rem 0;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .main-title {
            font-size: 3rem;
        }
        
        .module-icon {
            font-size: 3.5rem;
        }
        
        .module-title {
            font-size: 1.6rem;
        }
        
        .module-card {
            padding: 1.5rem;
            margin: 1rem 0.5rem;
        }
    }
    
    @media (max-width: 480px) {
        .main-title {
            font-size: 2.5rem;
        }
        
        .main-subtitle {
            font-size: 1.2rem;
        }
        
        .module-card {
            margin: 1rem 0;
        }
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------- LOADING OVERLAY (UNCHANGED) ----------------------------
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

# ---------------------------- MAIN CONTENT ----------------------------
st.markdown("""
<div class="main-subtitle">🚀 Ready to unlock your potential? 🌟</div>
<div class="main-subtitle">Choose a module to begin your epic journey toward peak performance! ✨</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

# Module 1 - Growth
with col1:
    module = MODULES[0]  # Growth
    # Make the entire card a clickable button
    if st.button(f"""
        {module['icon']}
        **{module['title']}**
        {module['description']}
        """, 
        key="growth", 
        use_container_width=True,
        help="Click to enter the Mindset Growth Garden"):
        st.switch_page(module['page'])

# Module 2 - Fight
with col2:
    module = MODULES[1]  # Fight
    if st.button(f"""
        {module['icon']}
        **{module['title']}**
        {module['description']}
        """, 
        key="fight", 
        use_container_width=True,
        help="Click to start the Inner Critic Boss Fight"):
        st.switch_page(module['page'])

# Module 3 - Smart
with col3:
    module = MODULES[2]  # Smart
    if st.button(f"""
        {module['icon']}
        **{module['title']}**
        {module['description']}
        """, 
        key="smart", 
        use_container_width=True,
        help="Click to launch Mission: SMART Possible"):
        st.switch_page(module['page'])

# Module 4 - Imagery
with col4:
    module = MODULES[3]  # Imagery
    if st.button(f"""
        {module['icon']}
        **{module['title']}**
        {module['description']}
        """, 
        key="imagery", 
        use_container_width=True,
        help="Click to enter the Imagery Rehearsal Stage"):
        st.switch_page(module['page'])
