import streamlit as st
import random
import openai

st.set_page_config(
    page_title="Inner Critic Boss Fight", 
    layout="centered",
    page_icon="⚔️"
)

openai.api_key = st.secrets.get("openai_api_key")

# ---------------------------- SCENARIOS ----------------------------
SCENARIO_LINES = {
    "Studying for Exam": [
        "I'm never going to remember all of this.", "I can't cover everything with so little time.", "I'm not smart enough to get this.",
        "Others are way ahead of me.", "I always mess up exams.", "This topic is too hard for me.",
        "I don’t remember things like I used to.", "I don't have what it takes.", "I'm so behind—what's the point?",
        "I'm a terrible student.", "I'll never catch up.", "Everyone else gets it but me.",
        "I'll only get a B grade anyway.", "Everyone else has more time to study; I'm at a disadvantage.", "I always procrastinate and never change."
    ],
    "Job Interview Preparation": [
        "I'm not qualified enough.", "If I make one mistake, it’s over.", "Why would they hire me?",
        "I'm going to mess this up.", "Others are way more impressive.", "I always panic during interviews.",
        "I don't deserve this opportunity.", "They'll ask something I can't answer.", "I'm going to look so nervous.",
        "I'm wasting the interviewer's time.", "I'm not a good communicator.", "I don't have real experience.",
        "I won't make a good impression.", "I'm too awkward.", "They'll never take me seriously."
    ],
    "Work-life Balance": [
        "If I take a break, I'm just being lazy.", "It doesn't matter what I eat. I just need a quick meal.",
        "I can't handle everything — I'm failing.", "Other people manage fine, why can't I?",
        "There's too much going on. I'm just not cut out for this.", "Other people can handle stress better than me.",
        "I keep messing up my priorities.", "I don't have time for friends — I need to focus on my work.",
        "I don't deserve to relax until I finish everything.", "Sleep can wait.",
        "If I stop now, I'll fall even further behind.", "Resting is just procrastinating.",
        "I chose this path, so I can't complain.", "Exercise is a waste of time.",
        "It's selfish to feel burned out when I have so many opportunities."
    ]
}

# ---------------------------- SESSION STATE INIT ----------------------------
def init_game_state():
    defaults = {
        'player_hp': 100, 'boss_hp': 100, 'scenario': None, 'current_line': "", 'awaiting_response': False,
        'is_evaluating': False, 'current_feedback': "", 'last_comment': "", 'used_lines': [], 'user_response_submitted': "",
        'background_loaded': False, 'game_over': False, 'victory': False
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_game_state()

# ---------------------------- STYLES ----------------------------
@st.cache_data
def get_styles():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quantico&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Audiowide&display=swap');

    /* Desktop/Laptop Only Styles */
    @media screen and (min-width: 1024px) {
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

        .stApp > div:first-child {
            padding-top: 0 !important;
            margin-top: -3rem !important;
        }

        .block-container {
            padding-top: 0 !important;
            margin-top: -2rem !important;
        }

        /* Responsive container - scales based on 2033x983 reference */
        .main .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: none !important;
            position: relative !important;
            z-index: 100 !important;
            transform: scale(clamp(0.6, calc(100vw / 2033), 1.4));
            transform-origin: top center;
        }
        
        /* Remove padding from main container */
        .main .block-container {
            padding: 0 !important;
            max-width: none !important;
        }
        
        /* Full screen background */
        .stApp {
            background-image: url('https://raw.githubusercontent.com/qw-chee/peakperformancelab/main/assets/ICBF.gif');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            min-height: 100vh;
            position: relative;
        }
        
        .overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(126,190,254,0.9);
            z-index: 9999; display: flex; align-items: center; justify-content: center;
            font: bold 2em 'Quantico', monospace; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
           
        .pixel-card {
            background: rgba(255,255,255,0.95); 
            border: clamp(2px, 0.3vw, 3px) solid #175dcf; 
            border-radius: clamp(6px, 1vw, 8px);
            padding: clamp(8px, 1.2vw, 12px); 
            margin: clamp(2px, 0.4vh, 6px) 0; 
            margin-bottom: 10px !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            font-family: 'Quantico', monospace;
        }
        
        .pixel-title {
            font-family: 'Audiowide'; 
            font-weight: 900;
            font-size: clamp(1rem, 1.8vw, 2em);
            color: #0052a3;
            text-align: center;
            text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
            margin-top: -5px;
            margin-bottom: -5px;
        }
        
        .pixel-text { 
            font: 400 clamp(0.8rem, 1vw, 1.8em) 'Quantico', monospace; 
            color: #2d3748; 
            line-height: 1.5; 
            font-family: 'Quantico', monospace;
        }
        
        .hp-container {
            display: flex; 
            align-items: center; 
            gap: clamp(10px, 1.5vw, 15px); 
            margin-bottom: clamp(10px, 1.5vh, 15px); 
            padding: clamp(8px, 1.2vw, 15px);
            background: white; 
            border: clamp(2px, 0.3vw, 3px) solid #175dcf; 
            border-radius: clamp(6px, 1vw, 8px); 
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .hp-bar { 
            height: clamp(15px, 2vh, 20px); 
            background: #f1f5f9; 
            border: clamp(1px, 0.2vw, 2px) solid #ffc738; 
            border-radius: clamp(3px, 0.5vw, 4px); 
            width: 100%; 
            overflow: hidden; 
        }
        
        .hp-fill-boss { 
            height: 100%; 
            background: linear-gradient(90deg, #ff0000 0%, #ff7373 100%); 
            transition: width 0.5s ease; 
        }
        
        .hp-fill-user { 
            height: 100%; 
            background: linear-gradient(90deg, #175dcf 0%, #00ccff 100%); 
            transition: width 0.5s ease; 
        }
        
        .hp-label { 
            font: 700 clamp(16px, 2vw, 20px) 'Quantico', monospace; 
            color: #175dcf; 
            min-width: clamp(50px, 6vw, 60px); 
            text-align: center; 
        }
        
        .hp-icon { 
            width: clamp(40px, 5vw, 50px); 
            height: clamp(40px, 5vw, 50px); 
            border-radius: clamp(4px, 0.8vw, 6px); 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            font-size: clamp(18px, 2.5vw, 24px); 
            background: white; 
        }
        
        .stForm > div:first-child { 
            background: rgba(255,255,255,0.95) !important; 
            border: clamp(2px, 0.3vw, 3px) solid #175dcf !important; 
            border-radius: clamp(6px, 1vw, 8px) !important; 
            padding: clamp(10px, 1.5vw, 15px) !important; 
            margin: -10px 0 !important; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important; 
        }
        
        .stTextInput > div > div > input { 
            font: clamp(12px, 1.4vw, 14px) 'Quantico', monospace !important; 
            border: clamp(1px, 0.2vw, 2px) solid #7ebefe !important; 
            border-radius: clamp(4px, 0.8vw, 6px) !important; 
            padding: clamp(8px, 1.2vw, 12px) !important; 
        }
        
        .stFormSubmitButton > button, div[data-testid="stButton"] > button { 
            background: white !important; 
            color: #175dcf !important; 
            border: clamp(2px, 0.3vw, 3px) solid #175dcf !important;
            font: 600 clamp(14px, 1.6vw, 16px) 'Quantico', monospace !important;
            padding: clamp(8px, 1.2vw, 12px) clamp(20px, 2.5vw, 25px) !important;
            border-radius: clamp(15px, 2vw, 20px) !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(23, 93, 207, 0.2) !important;
        }
        
        .stFormSubmitButton > button:hover, div[data-testid="stButton"] > button:hover { 
            transform: translateY(-2px) !important; 
            box-shadow: 0 6px 20px rgba(126,190,254,0.4) !important; 
        }

        /* Force font on all text elements within buttons */
        div[data-testid="stButton"] * {
            font-family: 'Quantico' !important;
        }

        /* Specific breakpoint adjustments for optimal scaling */
        
        /* Standard Desktop (1024-1439px) */
        @media screen and (min-width: 1024px) and (max-width: 1439px) {
            .main .block-container {
                transform: scale(0.75);
            }
        }

        /* Large Desktop (1440-1919px) */
        @media screen and (min-width: 1440px) and (max-width: 1919px) {
            .main .block-container {
                transform: scale(0.85);
            }
        }

        /* Reference size (1920-2200px) - Perfect scaling maintained */
        @media screen and (min-width: 1920px) and (max-width: 2200px) {
            .main .block-container {
                transform: scale(1.0);
            }
        }

        /* Ultra-wide (2200px+) */
        @media screen and (min-width: 2200px) {
            .main .block-container {
                transform: scale(1.15);
            }
        }

        .game-over-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
            animation: gameOverAppear 1s ease-out;
        }

        @keyframes gameOverAppear {
            0% { opacity: 0; transform: scale(0.5); }
            100% { opacity: 1; transform: scale(1); }
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-20px); }
            60% { transform: translateY(-10px); }
        }

        @keyframes sparkle {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.7; transform: scale(1.1); }
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .victory-animation {
            animation: bounce 2s infinite;
        }

        .defeat-animation {
            animation: pulse 2s infinite;
        }

        .sparkle-effect {
            animation: sparkle 1.5s infinite;
        }

        ::-webkit-scrollbar {
            width: clamp(8px, 1vw, 12px);
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(23, 93, 207, 0.1);
            border-radius: 6px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, #175dcf, #7ebefe);
            border-radius: 6px;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(45deg, #7ebefe, #00ccff);
        }
    }
    </style>
    """

st.markdown(get_styles(), unsafe_allow_html=True)

# ---------------------------- HP DISPLAY ----------------------------
def render_hp_bars():
    st.markdown(f"""
    <div class="hp-container">
        <div class="hp-icon" style="color: #029316;">😈</div>
        <div style="flex: 1;">
            <div style="font: 700 clamp(14px, 1.8vw, 20px) 'Quantico', monospace; color: #da531f; margin-bottom: 5px;">Inner Critic Boss</div>
            <div class="hp-bar"><div class="hp-fill-boss" style="width: {st.session_state.boss_hp}%;"></div></div>
        </div>
        <div class="hp-label">{st.session_state.boss_hp} HP</div>
    </div>
    <div class="hp-container">
        <div class="hp-icon" style="color: white;">🧠</div>
        <div style="flex: 1;">
            <div style="font: 700 clamp(14px, 1.8vw, 20px) 'Quantico', monospace; color: #175dcf; margin-bottom: 5px;">Your Mental Strength</div>
            <div class="hp-bar"><div class="hp-fill-user" style="width: {st.session_state.player_hp}%;"></div></div>
        </div>
        <div class="hp-label">{st.session_state.player_hp} HP</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------- EVALUATION ----------------------------
def evaluate_response():
    try:
        prompt = f"""You are evaluating how well a student reframes negative self-talk. Rate their response in relevance to the inner critic using the scoring criteria below and give feedback.

Inner Critic: "{st.session_state.current_line}"
Response: "{st.session_state.user_response_submitted}"

Scoring criteria:
- "Strong and positive": Constructive, positive, or realistic reframe that encourages growth, self-care, or motivation. It may directly counter the critic OR highlights clear benefits or values that offer a healthier perspective.
- "Weak or Generic": On-topic but vague, shallow, overly hopeful, or too general without giving a concrete positive angle.
- "Irrelevant": Agrees with the critic, defeatist, off-topic, overly passive (e.g., "whatever", "ok"), or completely fails to address the critic.

Format your response **strictly** as:
Verdict: [Strong and positive / Weak or Generic / Irrelevant]
Comment: [Feedback must match the verdict. Be encouraging only for "Strong and positive" and "Weak or Generic". If "Irrelevant", the comment must highlight the problem directly or express concern, and give useful suggestions for reframing the critic. Write in laymen terms, be direct, not fluffy. Write in 30 words or less.]"""
        
        response = openai.ChatCompletion.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_tokens=70,temperature=0.7,timeout=30)
        content = response.choices[0].message.content.strip()
        
        verdict, comment = "Weak or Generic", "Try being more specific."
        for line in content.split("\n"):
            if line.startswith("Verdict:"): verdict = line.split(":", 1)[1].strip()
            elif line.startswith("Comment:"): comment = line.split(":", 1)[1].strip()

        st.session_state.last_comment = comment
        
        if verdict == "Strong and positive":
            st.session_state.boss_hp = max(0, st.session_state.boss_hp - 15)
            st.session_state.current_feedback = "✅ Powerful reframe! Boss loses 15 HP."
        elif verdict == "Weak or Generic":
            st.session_state.boss_hp = max(0, st.session_state.boss_hp - 5)
            st.session_state.current_feedback = "👍 Not bad! Boss loses 5 HP."
        else:
            st.session_state.player_hp = max(0, st.session_state.player_hp - 15)
            st.session_state.current_feedback = "❌ Weak response. You lose 15 HP."
            
        # Check for game over conditions
        if st.session_state.boss_hp <= 0:
            st.session_state.game_over = True
            st.session_state.victory = True
        elif st.session_state.player_hp <= 0:
            st.session_state.game_over = True
            st.session_state.victory = False
            
    except Exception as e:
        st.error(f"Error: {e}")
        st.session_state.current_feedback = "Error evaluating response."

# ---------------------------- END GAME DISPLAYS ----------------------------
def render_victory_screen():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #029316 0%, #7ebefe 100%); color: white; border: clamp(2px, 0.3vw, 3px) solid #029316;
                border-radius: clamp(6px, 1vw, 8px); padding: clamp(10px, 1.5vw, 15px); text-align: center; margin: clamp(10px, 1.5vh, 15px) 0; box-shadow: 0 8px 25px rgba(2,147,22,0.3);'>
        <div style='font-size: clamp(2rem, 4vw, 3em); margin-bottom: 0px;'>🎉</div>
        <h1 style='margin: 0; font: 900 clamp(1.5rem, 2.5vw, 2em) Quantico, monospace; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>VICTORY!</h1>
        <p style='font: clamp(1rem, 1.6vw, 1.2em) Quantico, monospace; margin-top: 0px;'>You're a champion of self-talk! The inner critic has been silenced!</p>
        <p style='font: clamp(0.8rem, 1.4vw, 1em) Quantico, monospace; margin-top: 0px;'>💡 <strong>Remember:</strong> You now have the tools to counter negative self-talk in real life! Your positive reframes are your superpower! 🦸‍♂️</p>
    </div>
    """, unsafe_allow_html=True)

def render_defeat_screen():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #da531f 0%, #029316 100%); color: white; border: clamp(2px, 0.3vw, 3px) solid #da531f;
                border-radius: clamp(6px, 1vw, 8px); padding: clamp(10px, 1.5vw, 15px); text-align: center; margin: clamp(10px, 1.5vh, 15px) 0; box-shadow: 0 8px 25px rgba(218,83,31,0.3);'>
        <div style='font-size: clamp(2rem, 4vw, 3em); margin-bottom: 0px;'>💀</div>
        <h1 style='margin: 0; font: 900 clamp(1.5rem, 2.5vw, 2em) Quantico, monospace; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>DEFEAT</h1>
        <p style='font: clamp(1rem, 1.6vw, 1.2em) Quantico, monospace; margin-top: 0px;'>Practice makes perfect - let's train that positive mindset! Try again!</p>
        <p style='font: clamp(0.8rem, 1.4vw, 1em) Quantico, monospace; margin-top: 0px;'>💡 <strong>Pro Tip:</strong> Focus on specific, positive reframes that directly counter the critic's message. You're building stronger mental muscles with each battle! 🧠💪</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------- LOADING OVERLAY ----------------------------
st.markdown("""
    <div id="loading-overlay">
        <div class="loading-content">
            <div class="loading-title">⚔️ Summoning The Boss...</div>
            <div class="loading-bar-container">
                <div class="loading-bar"></div>
            </div>
            <div class="loading-subtitle">Preparing your mental battlefield</div>
        </div>
    </div>

    <style>
    @media screen and (min-width: 1024px) {
        #loading-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #134bab 0%, #5a98d1 50%, #02756f 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            animation: loading-sequence 4s ease-in-out forwards;
        }

        .loading-content {
            text-align: center;
        }

        .loading-title {
            font-family: 'Quantico', monospace;
            font-size: clamp(2rem, 4vw, 3em);
            font-weight: 900;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            margin-bottom: clamp(15px, 2vh, 20px);
            animation: pulse 2s ease-in-out infinite;
        }

        .loading-bar-container {
            width: clamp(150px, 20vw, 200px);
            height: clamp(3px, 0.5vh, 4px);
            background: rgba(255, 255, 255, 0.3);
            border-radius: 2px;
            overflow: hidden;
            position: relative;
            margin: 0 auto;
        }

        .loading-bar {
            width: 40%;
            height: 100%;
            background: linear-gradient(90deg, #ffffff, #ffff00);
            border-radius: 2px;
            animation: loading-bar 2s ease-in-out infinite;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.6);
        }

        .loading-subtitle {
            font-family: 'Quantico', monospace;
            color: rgba(255, 255, 255, 0.9);
            margin-top: clamp(10px, 1.5vh, 15px);
            font-size: clamp(1rem, 1.5vw, 1.3em);
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
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
    }
    </style>
""", unsafe_allow_html=True)

# Handle window resize and mobile blocking with JavaScript
st.markdown("""
<script>
// Block mobile and tablet, handle responsive scaling
if (window.innerWidth >= 1024) {
    // Handle window resize for responsive scaling
    window.addEventListener('resize', function() {
        if (window.innerWidth < 1024) {
            document.body.style.display = 'none';
            document.body.innerHTML = '<div style="display: flex; justify-content: center; align-items: center; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: linear-gradient(135deg, #134bab 0%, #5a98d1 50%, #02756f 100%); color: white; font-size: 1.5rem; text-align: center; font-family: Quantico, monospace;">This application is designed for desktop and laptop screens only.</div>';
        }
    });
}
</script>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .custom-spacer {
        padding: 20px;
        margin: 15px 0;
    }
    @media (min-width: 1300px) {
        .custom-spacer {
            height: 10vh;
        }
    }
    </style>
    <div class="custom-spacer"></div>
    """,
    unsafe_allow_html=True
)

# Check for game over first - if game is over, show end screen and stop
if st.session_state.game_over:
    if st.session_state.victory:
        render_victory_screen()
    else:
        render_defeat_screen()
    
    # Game over buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Try Another Scenario", use_container_width=True, key="restart_game"):
            st.session_state.clear()
            st.rerun()
    with col2:
        if st.button("🏡 Return to Home", use_container_width=True, key="return_home"):
            st.session_state.clear()
            st.switch_page("pages/Modules.py")
    st.stop()

# Scenario selection
if st.session_state.scenario is None:
    st.markdown("""
    <div class='pixel-card' style='text-align: center;'>
        <h3 class='pixel-title' style='color: #0052a3; margin-top: -5px; margin-bottom: -5px;'>⚔️ Inner Critic Boss Fight</h3>
        <p class='pixel-text' style='font-size: clamp(0.8rem, 1.2vw, 1.2em); margin: 0; line-height: 1.1;'>
            Self-talk is a powerful tool that can help you think more positively about yourself and situations, boost your confidence, and cope with uncertainty 
            to achieve peak performance. Positive self-talk should remind you of your qualities and your ability to perservere. <br><br> 
        This challenge helps you practice countering negative thoughts with positive self-talk to cope with real-life challenges.
        </p>
    </div>
    <div class='pixel-card'>
        <h3 class='pixel-title' style='color: #0052a3; margin-top: -10px; margin-bottom: -10px;'>🎮 How to Play</h3>
        <div class='pixel-text' style='font-size: clamp(0.8rem, 1.2vw, 1.2em);'>
            <p style='margin-bottom: clamp(4px, 0.6vh, 8px);'><strong>Mission:</strong> Counter your inner critic with positive self-talk to defeat the Boss!</p>
            <p style='margin-bottom: clamp(4px, 0.6vh, 8px);'><strong>Scoring System:</strong></p>
            <div style='display: grid; grid-template-columns: 1fr 1fr 1fr; gap: clamp(8px, 1.2vw, 12px); margin-bottom: -5px;'>
                <div style='background: #02b322; color: white; padding: clamp(5px, 1vw, 10px); border-radius: clamp(4px, 0.8vw, 6px); text-align: center; border: clamp(1px, 0.2vw, 2px) solid #175dcf;'>
                    <strong style='font-size: clamp(1rem, 1.3vw, 1rem);'>Strong & Positive:</strong><br><small style='font-size: clamp(0.9rem, 1.2vw, 0.9rem);'>Boss loses 15 HP</small>
                </div>
                <div style='background: #ffbb00; color: white; padding: clamp(5px, 1vw, 10px); border-radius: clamp(4px, 0.8vw, 6px); text-align: center; border: clamp(1px, 0.2vw, 2px) solid #175dcf;'>
                    <strong style='font-size: clamp(1rem, 1.3vw, 1rem);'>Weak or Generic:</strong><br><small style='font-size: clamp(0.9rem, 1.2vw, 0.9rem);'>Boss loses 5 HP</small>
                </div>
                <div style='background: #da531f; color: white; padding: clamp(5px, 1vw, 10px); border-radius: clamp(4px, 0.8vw, 6px); text-align: center; border: clamp(1px, 0.2vw, 2px) solid #175dcf;'>
                    <strong style='font-size: clamp(1rem, 1.3vw, 1rem);'>Poor or Irrelevant:</strong><br><small style='font-size: clamp(0.9rem, 1.2vw, 0.9rem);'>You lose 15 HP</small>
                </div>
            </div>
        </div>
    </div>
    <div style='text-align: center; margin-bottom: -25px;'>
        <h3 class='pixel-title' style='margin-top: -10px; margin-bottom: -5px;'>🎯 Choose Your Battle</h3>
    </div>
    """, unsafe_allow_html=True)
    
    scenarios = [("📚 Studying for Exam", "Studying for Exam"), ("💼 Job Interview Prep", "Job Interview Preparation"), ("⚖️ Work-life Balance", "Work-life Balance")]
    
    for i, (col, (label, scenario)) in enumerate(zip(st.columns(3), scenarios)):
        with col:
            if st.button(label, key=f"btn_{i}", use_container_width=True):
                st.session_state.update({"scenario": scenario, "awaiting_response": True, "current_feedback": "", "last_comment": ""})
                st.rerun()
    st.stop()

render_hp_bars()

# Evaluation processing
if st.session_state.is_evaluating:
    st.markdown('<div class="overlay">Evaluating your response...</div>', unsafe_allow_html=True)
    evaluate_response()
    st.session_state.update({"is_evaluating": False, "awaiting_response": False})
    st.rerun()

# Game input state
elif st.session_state.awaiting_response:
    if not st.session_state.current_line:
        available = list(set(SCENARIO_LINES[st.session_state.scenario]) - set(st.session_state.used_lines))
        if not available:
            st.session_state.used_lines = []
            available = SCENARIO_LINES[st.session_state.scenario]
        st.session_state.current_line = random.choice(available)
        st.session_state.used_lines.append(st.session_state.current_line)

    with st.form("reframe_form", clear_on_submit=True):
        st.markdown(f"""
        <div style='font: 700 clamp(1rem, 1.8vw, 1.3em) Quantico, monospace; margin: clamp(3px, 0.5vh, 5px) 0 clamp(8px, 1vh, 10px); color: #da531f;'>❗ <strong>Your inner critic says:</strong></div>
        <blockquote style='font: italic clamp(1rem, 1.6vw, 1.2em) Quantico, monospace; color: #0f8538; margin: clamp(8px, 1vh, 10px) 0; padding: clamp(10px, 1.5vw, 15px); 
                          background: rgba(173,189,79,0.1); border-left: clamp(3px, 0.5vw, 4px) solid #00822e; border-radius: clamp(3px, 0.5vw, 4px);'>
            "{st.session_state.current_line}"
        </blockquote>
        <div style='font: 700 clamp(1rem, 1.6vw, 1.2em) Quantico, monospace; margin: clamp(10px, 1.5vh, 15px) 0 -30px; color: #175dcf;'>✍️ <strong>Your counter-response:</strong></div>
        """, unsafe_allow_html=True)
                
        user_input = st.text_input("", key="user_response",  autocomplete="off", placeholder="Type your positive reframe here...")
        if st.form_submit_button("Submit Response") and user_input.strip():
            st.session_state.update({"user_response_submitted": user_input.strip(), "is_evaluating": True})
            st.rerun()

# Feedback state
else:
    feedback_colors = {"Powerful": "#029316", "Not bad": "#ffb700", "default": "#da531f"}
    color = next((v for k, v in feedback_colors.items() if k in st.session_state.current_feedback), feedback_colors["default"])
    
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {color} 0%, #7ebefe 100%); color: white; border: clamp(2px, 0.3vw, 3px) solid {color};
                border-radius: clamp(6px, 1vw, 8px); padding: clamp(4px, 1.2vw, 20px); text-align: center; margin: clamp(3px, 0.5vh, 5px) 0; box-shadow: 0 6px 20px rgba(0,0,0,0.2);'>
        <h2 style='margin: 0; font: 900 clamp(1.2rem, 2vw, 1.5em) Quantico, monospace; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>{st.session_state.current_feedback}</h2>
    </div>
    <div class='pixel-card' style='border-color: #7ebefe;'>
        <div style='display: flex; align-items: center; gap: clamp(8px, 1vw, 10px); margin-bottom: clamp(8px, 1vh, 10px);'>
            <span style='font-size: clamp(1.2rem, 2vw, 1.5em);'>🤖</span>
            <strong class='pixel-title' style='font-size: clamp(1rem, 1.6vw, 1.2em);'>Feedback</strong>
        </div>
        <p class='pixel-text' style='font-size: clamp(0.9rem, 1.3vw, 1.1em); margin: 0;'>{st.session_state.last_comment}</p>
    </div>
    """, unsafe_allow_html=True)
    
    def next_round():
        st.session_state.update({"awaiting_response": True, "current_line": "", "current_feedback": "", "last_comment": ""})
    
    st.button("⚔️ Next Round", on_click=next_round, use_container_width=True, type="primary")












