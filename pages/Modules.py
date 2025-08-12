import streamlit as st

st.set_page_config(
    page_title="Peak Performance Lab", 
    layout="centered",
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

# ---------------------------- FIXED LIQUID GLASS STYLES ----------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Remove sidebar */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* FIXED: Proper background instead of transparent */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        position: relative;
        overflow-x: hidden;
        min-height: 100vh;
    }
    
    /* FIXED: Ensure main container is visible */
    .main .block-container {
        padding-top: 2rem !important;
        position: relative !important;
        z-index: 100 !important;
    }
    
    /* Floating liquid bubbles - FIXED z-index */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 15% 25%, rgba(255, 255, 255, 0.08) 0%, transparent 35%),
            radial-gradient(circle at 85% 20%, rgba(255, 255, 255, 0.06) 0%, transparent 30%),
            radial-gradient(circle at 35% 75%, rgba(255, 255, 255, 0.1) 0%, transparent 40%),
            radial-gradient(circle at 90% 80%, rgba(255, 255, 255, 0.05) 0%, transparent 25%);
        animation: liquidBubbleFloat 25s ease-in-out infinite;
        pointer-events: none;
        z-index: 1 !important;
    }
    
    @keyframes liquidBubbleFloat {
        0%, 100% { transform: translate(0px, 0px) scale(1); opacity: 0.6; }
        25% { transform: translate(20px, -15px) scale(1.05); opacity: 0.8; }
        50% { transform: translate(-15px, 10px) scale(0.95); opacity: 0.5; }
        75% { transform: translate(25px, 5px) scale(1.02); opacity: 0.7; }
    }
    
    /* Liquid glass title styling - FIXED colors */
    .main-title {
        font-family: 'Outfit', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        color: white !important;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 0 2px 8px rgba(0,0,0,0.3);
        animation: titleLiquidFlow 6s ease-in-out infinite;
        position: relative;
        z-index: 101 !important;
    }
    
    @keyframes titleLiquidFlow {
        0%, 100% { 
            transform: translateY(0px);
            filter: drop-shadow(0 2px 8px rgba(0,0,0,0.3));
        }
        50% { 
            transform: translateY(-3px);
            filter: drop-shadow(0 4px 12px rgba(0,0,0,0.4));
        }
    }
    
    .main-subtitle {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.2rem;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.9) !important;
        text-align: center;
        margin-bottom: 3rem;
        text-shadow: 0 1px 4px rgba(0,0,0,0.2);
        animation: subtitleLiquidWave 8s ease-in-out infinite;
        position: relative;
        z-index: 101 !important;
    }
    
    @keyframes subtitleLiquidWave {
        0%, 100% { opacity: 0.9; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.01); }
    }
    
    /* Liquid glass module cards - FIXED visibility */
    .module-card {
        background: rgba(255, 255, 255, 0.25) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 
            0 8px 32px rgba(0,0,0,0.12),
            inset 0 1px 0 rgba(255,255,255,0.3),
            0 1px 0 rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        text-align: center;
        position: relative;
        overflow: hidden;
        animation: cardLiquidFloat 10s ease-in-out infinite;
        z-index: 101 !important;
    }
    
    @keyframes cardLiquidFloat {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-8px) rotate(0.2deg); }
        50% { transform: translateY(-4px) rotate(-0.15deg); }
        75% { transform: translateY(-12px) rotate(0.3deg); }
    }
    
    /* Liquid shimmer effect */
    .module-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 255, 255, 0.3), 
            transparent);
        transition: left 0.8s ease;
        animation: liquidShimmer 4s ease-in-out infinite;
        z-index: 1;
    }
    
    @keyframes liquidShimmer {
        0%, 100% { left: -100%; opacity: 0; }
        50% { left: 100%; opacity: 1; }
    }
    
    .module-card:hover {
        transform: translateY(-12px) scale(1.03);
        box-shadow: 
            0 20px 60px rgba(0,0,0,0.18),
            inset 0 1px 0 rgba(255,255,255,0.4),
            0 1px 0 rgba(255,255,255,0.2),
            0 0 40px rgba(255,255,255,0.1);
        border-color: rgba(255,255,255,0.35);
        background: rgba(255, 255, 255, 0.35) !important;
    }
    
    .module-card:hover::before {
        animation: liquidShimmerActive 1s ease-out;
    }
    
    @keyframes liquidShimmerActive {
        0% { left: -100%; opacity: 0; }
        50% { left: 50%; opacity: 0.8; }
        100% { left: 100%; opacity: 0; }
    }
    
    /* Floating liquid icons */
    .module-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        display: block;
        position: relative;
        animation: iconLiquidBob 6s ease-in-out infinite;
        filter: drop-shadow(0 4px 12px rgba(0,0,0,0.15));
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        z-index: 102 !important;
    }
    
    @keyframes iconLiquidBob {
        0%, 100% { transform: translateY(0px) scale(1); }
        25% { transform: translateY(-8px) scale(1.02); }
        50% { transform: translateY(-4px) scale(1); }
        75% { transform: translateY(-10px) scale(1.01); }
    }
    
    .module-card:hover .module-icon {
        transform: scale(1.15);
        animation: iconLiquidActive 1.2s ease-out, iconLiquidBob 6s ease-in-out infinite;
        filter: drop-shadow(0 8px 20px rgba(0,0,0,0.2));
    }
    
    @keyframes iconLiquidActive {
        0% { transform: scale(1) rotateY(0deg); }
        50% { transform: scale(1.2) rotateY(180deg); }
        100% { transform: scale(1.15) rotateY(360deg); }
    }
    
    /* Liquid glass typography - FIXED colors */
    .module-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.6rem;
        font-weight: 600;
        color: rgba(255, 255, 255, 0.95) !important;
        margin-bottom: 1.2rem;
        text-shadow: 0 1px 3px rgba(0,0,0,0.3);
        animation: titleLiquidWave 8s ease-in-out infinite;
        transition: all 0.4s ease;
        position: relative;
        z-index: 102 !important;
    }
    
    @keyframes titleLiquidWave {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-2px); }
    }
    
    .module-card:hover .module-title {
        color: rgba(255, 255, 255, 1) !important;
        text-shadow: 0 1px 6px rgba(0,0,0,0.4);
        transform: translateY(-3px) scale(1.02);
    }
    
    .module-description {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        font-weight: 400;
        color: rgba(255, 255, 255, 0.8) !important;
        line-height: 1.6;
        margin-bottom: 2rem;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        animation: descriptionLiquidFlow 7s ease-in-out infinite;
        transition: all 0.3s ease;
        position: relative;
        z-index: 102 !important;
    }
    
    @keyframes descriptionLiquidFlow {
        0%, 100% { opacity: 0.8; transform: translateY(0px); }
        50% { opacity: 0.9; transform: translateY(-1px); }
    }
    
    .module-card:hover .module-description {
        color: rgba(255, 255, 255, 0.9) !important;
        text-shadow: 0 1px 3px rgba(0,0,0,0.3);
        transform: translateY(-2px);
    }
    
    /* Liquid glass buttons - FIXED z-index and visibility */
    .stButton > button {
        width: 100% !important;
        height: 55px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        border-radius: 18px !important;
        border: 1px solid rgba(255,255,255,0.3) !important;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
        backdrop-filter: blur(15px) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        position: relative !important;
        overflow: hidden !important;
        box-shadow: 
            0 4px 20px rgba(0,0,0,0.15),
            inset 0 1px 0 rgba(255,255,255,0.2) !important;
        z-index: 102 !important;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.6s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: 
            0 8px 30px rgba(0,0,0,0.25),
            inset 0 1px 0 rgba(255,255,255,0.3) !important;
        border-color: rgba(255,255,255,0.4) !important;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:active {
        transform: translateY(-2px) scale(0.98) !important;
        transition: all 0.1s ease-out !important;
    }
    
    /* Individual liquid glass button colors */
    .growth-btn button {
        background: rgba(39, 174, 96, 0.8) !important;
        color: white !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3) !important;
    }
    
    .growth-btn button:hover {
        background: rgba(39, 174, 96, 0.9) !important;
        box-shadow: 0 8px 30px rgba(39, 174, 96, 0.4), inset 0 1px 0 rgba(255,255,255,0.3) !important;
    }
    
    .fight-btn button {
        background: rgba(231, 76, 60, 0.8) !important;
        color: white !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3) !important;
    }
    
    .fight-btn button:hover {
        background: rgba(231, 76, 60, 0.9) !important;
        box-shadow: 0 8px 30px rgba(231, 76, 60, 0.4), inset 0 1px 0 rgba(255,255,255,0.3) !important;
    }
    
    .smart-btn button {
        background: rgba(243, 156, 18, 0.8) !important;
        color: white !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3) !important;
    }
    
    .smart-btn button:hover {
        background: rgba(243, 156, 18, 0.9) !important;
        box-shadow: 0 8px 30px rgba(243, 156, 18, 0.4), inset 0 1px 0 rgba(255,255,255,0.3) !important;
    }
    
    .imagery-btn button {
        background: rgba(155, 89, 182, 0.8) !important;
        color: white !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3) !important;
    }
    
    .imagery-btn button:hover {
        background: rgba(155, 89, 182, 0.9) !important;
        box-shadow: 0 8px 30px rgba(155, 89, 182, 0.4), inset 0 1px 0 rgba(255,255,255,0.3) !important;
    }
    
    /* Responsive liquid glass */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem;
        }
        
        .module-icon {
            font-size: 3rem;
        }
        
        .module-title {
            font-size: 1.4rem;
        }
        
        .module-card {
            padding: 2rem;
            margin: 1rem 0;
        }
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------- MAIN CONTENT ----------------------------
st.markdown("""
<div class="main-title">🏆 Peak Performance Lab</div>
<div class="main-subtitle">Ready to unlock your potential? Choose a module to begin your journey toward peak performance.</div>
""", unsafe_allow_html=True)

# Create a 2x2 grid
col1, col2 = st.columns(2)

# Row 1
with col1:
    module = MODULES[0]  # Growth
    st.markdown(f"""
    <div class="module-card">
        <div class="module-icon">{module['icon']}</div>
        <div class="module-title">{module['title']}</div>
        <div class="module-description">{module['description']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="growth-btn">', unsafe_allow_html=True)
    if st.button("🌱 ENTER THE GARDEN", key="growth", use_container_width=True):
        st.switch_page(module['page'])
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    module = MODULES[1]  # Fight
    st.markdown(f"""
    <div class="module-card">
        <div class="module-icon">{module['icon']}</div>
        <div class="module-title">{module['title']}</div>
        <div class="module-description">{module['description']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="fight-btn">', unsafe_allow_html=True)
    if st.button("⚔️ START THE BATTLE", key="fight", use_container_width=True):
        st.switch_page(module['page'])
    st.markdown('</div>', unsafe_allow_html=True)

# Row 2
col3, col4 = st.columns(2)

with col3:
    module = MODULES[2]  # Smart
    st.markdown(f"""
    <div class="module-card">
        <div class="module-icon">{module['icon']}</div>
        <div class="module-title">{module['title']}</div>
        <div class="module-description">{module['description']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="smart-btn">', unsafe_allow_html=True)
    if st.button("🚀 LAUNCH MISSION", key="smart", use_container_width=True):
        st.switch_page(module['page'])
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    module = MODULES[3]  # Imagery
    st.markdown(f"""
    <div class="module-card">
        <div class="module-icon">{module['icon']}</div>
        <div class="module-title">{module['title']}</div>
        <div class="module-description">{module['description']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="imagery-btn">', unsafe_allow_html=True)
    if st.button("🎬 ENTER THE STAGE", key="imagery", use_container_width=True):
        st.switch_page(module['page'])
    st.markdown('</div>', unsafe_allow_html=True)
