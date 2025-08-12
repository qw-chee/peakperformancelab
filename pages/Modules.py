import streamlit as st

st.set_page_config(
    page_title="Peak Performance Lab", 
    layout="centered",
    page_icon="🏆"
)

# Add this debug section at the top to test if Streamlit is working
st.write("DEBUG: If you can see this text, Streamlit is working!")

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

# ---------------------------- SIMPLIFIED STYLES FOR DEBUGGING ----------------------------
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
    
    /* FIXED: Solid background instead of transparent */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        position: relative;
        overflow-x: hidden;
        min-height: 100vh;
    }
    
    /* Ensure content is visible */
    .main .block-container {
        padding-top: 2rem !important;
        z-index: 100 !important;
        position: relative !important;
    }
    
    /* Title styling - SIMPLIFIED */
    .main-title {
        font-family: 'Inter', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        color: white !important;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 0 2px 8px rgba(0,0,0,0.3);
        position: relative;
        z-index: 101 !important;
    }
    
    .main-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.9) !important;
        text-align: center;
        margin-bottom: 3rem;
        position: relative;
        z-index: 101 !important;
    }
    
    /* Module cards - SIMPLIFIED */
    .module-card {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 24px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        text-align: center;
        position: relative;
        z-index: 101 !important;
    }
    
    .module-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        display: block;
    }
    
    .module-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.6rem;
        font-weight: 600;
        color: #333 !important;
        margin-bottom: 1.2rem;
    }
    
    .module-description {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        color: #666 !important;
        line-height: 1.6;
        margin-bottom: 2rem;
    }
    
    /* Buttons - SIMPLIFIED */
    .stButton > button {
        width: 100%;
        height: 55px;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        border-radius: 18px;
        border: none !important;
        color: white !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .growth-btn button {
        background: #27AE60 !important;
    }
    
    .fight-btn button {
        background: #E74C3C !important;
    }
    
    .smart-btn button {
        background: #F39C12 !important;
    }
    
    .imagery-btn button {
        background: #9B59B6 !important;
    }
</style>
""", unsafe_allow_html=True)

# Test basic HTML rendering
st.markdown("DEBUG: Testing HTML rendering below:")

# ---------------------------- MAIN CONTENT ----------------------------
st.markdown("""
<div class="main-title">🏆 Peak Performance Lab</div>
<div class="main-subtitle">Ready to unlock your potential? Choose a module to begin your journey toward peak performance.</div>
""", unsafe_allow_html=True)

# Test if this shows up
st.write("DEBUG: If you can see this, we're past the title section")

# Create a 2x2 grid
col1, col2 = st.columns(2)

# Row 1
with col1:
    st.write("DEBUG: Column 1 content")
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
        st.write("Button clicked!")  # Debug
        # st.switch_page(module['page'])  # Commented out for debugging
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.write("DEBUG: Column 2 content")
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
        st.write("Button clicked!")  # Debug
        # st.switch_page(module['page'])  # Commented out for debugging
    st.markdown('</div>', unsafe_allow_html=True)

# Add final debug message
st.write("DEBUG: If you see this, the app reached the end successfully!")
