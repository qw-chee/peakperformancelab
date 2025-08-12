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
        "page": "/Growth.py",
        "color": "#27AE60",
        "key": "growth"
    },
    {
        "title": "Inner Critic Boss Fight",
        "icon": "⚔️",
        "description": "Face your challenges head-on with positive self-talk. Build mental toughness through gamified scenarios.",
        "page": "/Fight",
        "color": "#E74C3C",
        "key": "fight"
    },
    {
        "title": "Mission: SMART Possible",
        "icon": "🚀",
        "description": "Identify SMART goals that drive results. Learn the framework for setting and achieving meaningful objectives.",
        "page": "/Smart",
        "color": "#F39C12",
        "key": "smart"
    },
    {
        "title": "Imagery Rehearsal Stage",
        "icon": "🎬",
        "description": "Master the art of mental rehearsal and visualization. Train your mind through guided imagery techniques.",
        "page": "/Imagery",
        "color": "#9B59B6",
        "key": "imagery"
    }
]

# ---------------------------- CLEAN CARD STYLES ----------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Remove sidebar */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Clean background - shows your green */
    .stApp {
        background: transparent;
    }
    
    /* Title styling */
    .main-title {
        font-family: 'Inter', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }
    
    .main-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: #34495e;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }
    
    /* Module cards */
    .module-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.8);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .module-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
    }
    
    .module-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .module-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    
    .module-description {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        color: #5d6d7e;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    /* Custom button styling */
    .stButton > button {
        width: 100%;
        height: 50px;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        border-radius: 12px;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* Individual button colors */
    .growth-btn button {
        background: linear-gradient(135deg, #27AE60, #2ECC71) !important;
        color: white !important;
    }
    
    .fight-btn button {
        background: linear-gradient(135deg, #E74C3C, #EC7063) !important;
        color: white !important;
    }
    
    .smart-btn button {
        background: linear-gradient(135deg, #F39C12, #F4D03F) !important;
        color: white !important;
    }
    
    .imagery-btn button {
        background: linear-gradient(135deg, #9B59B6, #BB8FCE) !important;
        color: white !important;
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

# Debug info to help troubleshoot
st.markdown("---")
st.markdown("**Debug Info:** If navigation isn't working, check that these files exist:")
for module in MODULES:
    st.write(f"- {module['page']}")
