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
    
    /* Loading overlay (unchanged as requested) */
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
    
    /* Super fun bouncing cards */
    .module-card {
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 30px;
        padding: 2rem;
        margin: 2rem 1rem;
        box-shadow: 
            0 15px 35px rgba(0,0,0,0.1),
            0 5px 15px rgba(0,0,0,0.05),
            inset 0 1px 0 rgba(255,255,255,0.6);
        border: 3px solid;
        transition: all 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        text-align: center;
        position: relative;
        overflow: visible;
        animation: cardBounceFloat 8s ease-in-out infinite;
        z-index: 101 !important;
        transform-origin: center;
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
    
    /* Individual fun card colors with rainbow borders */
    .growth-card {
        border-color: #27AE60 !important;
        animation-delay: 0s;
    }
    
    .fight-card {
        border-color: #E74C3C !important;
        animation-delay: 0.2s;
    }
    
    .smart-card {
        border-color: #F39C12 !important;
        animation-delay: 0.4s;
    }
    
    .imagery-card {
        border-color: #9B59B6 !important;
        animation-delay: 0.6s;
    }
    
    /* Rainbow shimmer effect */
    .module-card::before {
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
    .module-card:hover {
        transform: translateY(-30px) scale(1.08) rotate(3deg) !important;
        box-shadow: 
            0 25px 50px rgba(0,0,0,0.2),
            0 10px 25px rgba(0,0,0,0.1),
            inset 0 1px 0 rgba(255,255,255,0.8) !important;
        animation: none;
    }
    
    .module-card:hover::before {
        opacity: 0.3;
    }
    
    /* Bouncing dancing icons */
    .module-icon {
        font-size: 4.5rem;
        margin-bottom: 1.5rem;
        display: inline-block;
        position: relative;
        animation: iconDance 2s ease-in-out infinite;
        filter: drop-shadow(0 8px 16px rgba(0,0,0,0.15));
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        z-index: 102 !important;
    }
    
    @keyframes iconDance {
        0%, 100% { 
            transform: translateY(0px) scale(1) rotate(0deg); 
        }
        25% { 
            transform: translateY(-15px) scale(1.1) rotate(-5deg); 
        }
        50% { 
            transform: translateY(-8px) scale(0.95) rotate(5deg); 
        }
        75% { 
            transform: translateY(-20px) scale(1.05) rotate(-3deg); 
        }
    }
    
    .module-card:hover .module-icon {
        transform: scale(1.3) rotateY(360deg) !important;
        animation: iconParty 0.8s ease-out, iconDance 2s ease-in-out infinite 0.8s;
    }
    
    @keyframes iconParty {
        0% { transform: scale(1) rotateY(0deg) rotateZ(0deg); }
        25% { transform: scale(1.1) rotateY(90deg) rotateZ(10deg); }
        50% { transform: scale(1.2) rotateY(180deg) rotateZ(-10deg); }
        75% { transform: scale(1.1) rotateY(270deg) rotateZ(5deg); }
        100% { transform: scale(1.3) rotateY(360deg) rotateZ(0deg); }
    }
    
    /* Fun bouncy text */
    .module-title {
        font-family: 'Baloo 2', cursive;
        font-size: 1.6rem;
        font-weight: 700;
        color: #2C3E50 !important;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        animation: textBounce 3s ease-in-out infinite;
        transition: all 0.4s ease;
        position: relative;
        z-index: 102 !important;
    }
    
    @keyframes textBounce {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-3px); }
    }
    
    .module-card:hover .module-title {
        color: #E74C3C !important;
        transform: translateY(-5px) scale(1.05);
        text-shadow: 3px 3px 6px rgba(0,0,0,0.2);
    }
    
    .module-description {
        font-family: 'Baloo 2', cursive;
        font-size: 1rem;
        font-weight: 500;
        color: #34495E !important;
        line-height: 1.6;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
        animation: descriptionWave 4s ease-in-out infinite;
        transition: all 0.3s ease;
        position: relative;
        z-index: 102 !important;
    }
    
    @keyframes descriptionWave {
        0%, 100% { opacity: 0.9; }
        50% { opacity: 1; }
    }
    
    .module-card:hover .module-description {
        color: #2C3E50 !important;
        transform: translateY(-2px);
    }
    
    /* Super fun bouncy buttons */
    .stButton > button {
        width: 100% !important;
        height: 60px !important;
        font-family: 'Fredoka', cursive !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        border-radius: 30px !important;
        border: 3px solid rgba(255,255,255,0.8) !important;
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        position: relative !important;
        overflow: hidden !important;
        box-shadow: 
            0 8px 25px rgba(0,0,0,0.15),
            inset 0 1px 0 rgba(255,255,255,0.3) !important;
        z-index: 102 !important;
        animation: buttonBounce 3s ease-in-out infinite;
    }
    
    @keyframes buttonBounce {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-2px) scale(1.01); }
    }
    
    .stButton > button::before {
        content: '✨';
        position: absolute;
        top: 50%;
        left: -30px;
        transform: translateY(-50%);
        font-size: 1.2rem;
        transition: all 0.6s ease;
        animation: sparkleMove 2s ease-in-out infinite;
    }
    
    @keyframes sparkleMove {
        0%, 100% { left: -30px; opacity: 0; }
        50% { left: 10px; opacity: 1; }
    }
    
    .stButton > button::after {
        content: '✨';
        position: absolute;
        top: 50%;
        right: -30px;
        transform: translateY(-50%);
        font-size: 1.2rem;
        transition: all 0.6s ease;
        animation: sparkleMove2 2s ease-in-out infinite;
    }
    
    @keyframes sparkleMove2 {
        0%, 100% { right: -30px; opacity: 0; }
        50% { right: 10px; opacity: 1; }
    }
    
    .stButton > button:hover {
        transform: translateY(-8px) scale(1.05) !important;
        box-shadow: 
            0 15px 35px rgba(0,0,0,0.25),
            inset 0 1px 0 rgba(255,255,255,0.4) !important;
        animation: buttonParty 0.6s ease-out infinite;
    }
    
    @keyframes buttonParty {
        0%, 100% { transform: translateY(-8px) scale(1.05) rotate(0deg); }
        25% { transform: translateY(-8px) scale(1.05) rotate(1deg); }
        75% { transform: translateY(-8px) scale(1.05) rotate(-1deg); }
    }
    
    .stButton > button:hover::before,
    .stButton > button:hover::after {
        animation-duration: 0.5s;
    }
    
    /* Colorful fun buttons */
    .growth-btn button {
        background: linear-gradient(135deg, #27AE60, #2ECC71) !important;
        color: white !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
        box-shadow: 0 8px 25px rgba(39, 174, 96, 0.3), inset 0 1px 0 rgba(255,255,255,0.3) !important;
    }
    
    .growth-btn button:hover {
        background: linear-gradient(135deg, #2ECC71, #27AE60) !important;
        box-shadow: 0 15px 35px rgba(39, 174, 96, 0.4), inset 0 1px 0 rgba(255,255,255,0.4) !important;
    }
    
    .fight-btn button {
        background: linear-gradient(135deg, #E74C3C, #C0392B) !important;
        color: white !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
        box-shadow: 0 8px 25px rgba(231, 76, 60, 0.3), inset 0 1px 0 rgba(255,255,255,0.3) !important;
    }
    
    .fight-btn button:hover {
        background: linear-gradient(135deg, #C0392B, #E74C3C) !important;
        box-shadow: 0 15px 35px rgba(231, 76, 60, 0.4), inset 0 1px 0 rgba(255,255,255,0.4) !important;
    }
    
    .smart-btn button {
        background: linear-gradient(135deg, #F39C12, #E67E22) !important;
        color: white !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
        box-shadow: 0 8px 25px rgba(243, 156, 18, 0.3), inset 0 1px 0 rgba(255,255,255,0.3) !important;
    }
    
    .smart-btn button:hover {
        background: linear-gradient(135deg, #E67E22, #F39C12) !important;
        box-shadow: 0 15px 35px rgba(243, 156, 18, 0.4), inset 0 1px 0 rgba(255,255,255,0.4) !important;
    }
    
    .imagery-btn button {
        background: linear-gradient(135deg, #9B59B6, #8E44AD) !important;
        color: white !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
        box-shadow: 0 8px 25px rgba(155, 89, 182, 0.3), inset 0 1px 0 rgba(255,255,255,0.3) !important;
    }
    
    .imagery-btn button:hover {
        background: linear-gradient(135deg, #8E44AD, #9B59B6) !important;
        box-shadow: 0 15px 35px rgba(155, 89, 182, 0.4), inset 0 1px 0 rgba(255,255,255,0.4) !important;
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
if 'home_background_loaded' not in st.session_state:
    st.session_state.home_background_loaded = False

if not st.session_state.home_background_loaded:
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
    st.session_state.home_background_loaded = True

# ---------------------------- MAIN CONTENT ----------------------------
st.markdown("""
<div class="main-subtitle">🚀 Ready to unlock your potential? 🌟</div>
<div class="main-subtitle">Choose a module to begin your epic journey toward peak performance! ✨</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

# Module 1 - Growth
with col1:
    module = MODULES[0]  # Growth
    st.markdown(f"""
    <div class="module-card growth-card">
        <div class="module-icon">{module['icon']}</div>
        <div class="module-title">{module['title']}</div>
        <div class="module-description">{module['description']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="growth-btn">', unsafe_allow_html=True)
    if st.button("🌱 ENTER THE GARDEN", key="growth", use_container_width=True):
        st.switch_page(module['page'])
    st.markdown('</div>', unsafe_allow_html=True)

# Module 2 - Fight
with col2:
    module = MODULES[1]  # Fight
    st.markdown(f"""
    <div class="module-card fight-card">
        <div class="module-icon">{module['icon']}</div>
        <div class="module-title">{module['title']}</div>
        <div class="module-description">{module['description']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="fight-btn">', unsafe_allow_html=True)
    if st.button("⚔️ START THE BATTLE", key="fight", use_container_width=True):
        st.switch_page(module['page'])
    st.markdown('</div>', unsafe_allow_html=True)

# Module 3 - Smart
with col3:
    module = MODULES[2]  # Smart
    st.markdown(f"""
    <div class="module-card smart-card">
        <div class="module-icon">{module['icon']}</div>
        <div class="module-title">{module['title']}</div>
        <div class="module-description">{module['description']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="smart-btn">', unsafe_allow_html=True)
    if st.button("🚀 LAUNCH MISSION", key="smart", use_container_width=True):
        st.switch_page(module['page'])
    st.markdown('</div>', unsafe_allow_html=True)

# Module 4 - Imagery
with col4:
    module = MODULES[3]  # Imagery
    st.markdown(f"""
    <div class="module-card imagery-card">
        <div class="module-icon">{module['icon']}</div>
        <div class="module-title">{module['title']}</div>
        <div class="module-description">{module['description']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="imagery-btn">', unsafe_allow_html=True)
    if st.button("🎬 ENTER THE STAGE", key="imagery", use_container_width=True):
        st.switch_page(module['page'])
    st.markdown('</div>', unsafe_allow_html=True)
