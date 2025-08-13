import streamlit as st
import random

st.set_page_config(
    page_title="Mission: SMART Possible", 
    layout="centered",
    page_icon="🎯"
)

# ---------------------------- GOALS DATABASE ----------------------------
GOALS_DATABASE = [
    # Missing 1 element
    {
        "text": "I will apply to 10 jobs to increase my chances of employment.",
        "missing": ["Timebound"],
        "feedback": "This goal isn't <strong>Timebound</strong> - there's no deadline specified. Add a timeframe like 'within the next 2 months' or 'by the end of this quarter'.<br><br><strong>SMART Version:</strong> 'I will apply to 10 jobs within the next 6 weeks to increase my chances of employment in my field.'"
    },
    {
        "text": "To manage time, I will write some of my TMA every evening.",
        "missing": ["Measurable"],
        "feedback": "This goal isn't <strong>Measurable</strong> - 'some' is vague. Specify exactly how much work, like '2 pages' or '500 words' or '1 hour of writing'.<br><br><strong>SMART Version:</strong> 'To manage time effectively, I will write 300 words of my TMA every evening until completion.'"
    },
    {
        "text": "I will finish reading 10 books to improve my writing by tomorrow.",
        "missing": ["Achievable"],
        "feedback": "This goal isn't <strong>Achievable</strong> - reading 10 books in one day is unrealistic. A more achievable timeline would be several months.<br><br><strong>SMART Version:</strong> 'I will finish reading 10 books over the next 6 months to improve my writing skills by expanding my vocabulary and understanding different writing styles.'"
    },
    {
        "text": "I will exercise more for better health each day.",
        "missing": ["Measurable"],
        "feedback": "This goal isn't <strong>Measurable</strong> - 'more' is vague. Specify exactly how much exercise, like '30 minutes of cardio' or 'attend 3 gym sessions per week'.<br><br><strong>SMART Version:</strong> 'I will exercise for 30 minutes each day for the next 3 months to improve my cardiovascular health and energy levels.'"
    },
    {
        "text": "I will aim to improve my GPA by 0.5 for better career prospects.",
        "missing": ["Timebound"],
        "feedback": "This goal isn't <strong>Timebound</strong> - there's no deadline specified. Add a timeframe like 'by the end of this semester' or 'within one academic year'.<br><br><strong>SMART Version:</strong> 'I will improve my GPA by 0.5 points by the end of this academic year through consistent study habits to enhance my career prospects.'"
    },
    {
        "text": "I will volunteer twice at the foodbank each month.",
        "missing": ["Relevant"],
        "feedback": "This goal lacks clear <strong>Relevance</strong> - it doesn't explain how volunteering connects to your personal or professional development goals.<br><br><strong>SMART Version:</strong> 'I will volunteer twice at the foodbank each month for 6 months to develop my leadership skills and give back to my community.'"
    },
    
    # Missing 2 elements
    {
        "text": "I want to save 10 million dollars by the end of this year.",
        "missing": ["Achievable", "Relevant"],
        "feedback": "This goal isn't <strong>Achievable</strong> (10 million in one year is unrealistic for most people) and lacks <strong>Relevance</strong> (why this specific amount? What's the purpose?).<br><br><strong>SMART Version:</strong> 'I will save $5,000 by the end of this year to build an emergency fund for my family's financial security.'"
    },
    {
        "text": "I plan to improve my lane-changing skills to be a better driver.",
        "missing": ["Measurable", "Timebound"],
        "feedback": "This goal isn't <strong>Measurable</strong> (how will you gauge improvement?) and isn't <strong>Timebound</strong> (by when?).<br><br><strong>SMART Version:</strong> 'I will practice lane-changing in a safe environment for 30 minutes twice per week for the next month to improve my driving confidence and safety.'"
    },
    {
        "text": "I want to contribute to household bills to help my parents.",
        "missing": ["Measurable", "Timebound"],
        "feedback": "This goal isn't <strong>Measurable</strong> (how much will you contribute?) and isn't <strong>Timebound</strong> (when will you start and for how long?).<br><br><strong>SMART Version:</strong> 'I will contribute $200 monthly to household bills starting next month to help reduce my parents' financial burden.'"
    },
    {
        "text": "I will aim to attend professional development courses each year.",
        "missing": ["Measurable", "Relevant"],
        "feedback": "This goal isn't <strong>Measurable</strong> (how many courses?) and lacks <strong>Relevance</strong> (which specific skills or career goals will this support?).<br><br><strong>SMART Version:</strong> 'I will attend 3 professional development courses this year focused on project management to advance my career in operations.'"
    },
    {
        "text": "I will arrive earlier for class starting next week.",
        "missing": ["Measurable", "Relevant"],
        "feedback": "This goal isn't <strong>Measurable</strong> (how much earlier?) and lacks <strong>Relevance</strong> (why is arriving earlier important for your academic success?).<br><br><strong>SMART Version:</strong> 'I will arrive 15 minutes earlier for each class starting next week to review notes and improve my academic performance.'"
    },
    
    # Missing 3 elements
    {
        "text": "I will contribute to GBA group discussions more actively.",
        "missing": ["Measurable", "Relevant", "Timebound"],
        "feedback": "This goal isn't <strong>Measurable</strong> (what does 'more actively' mean?), lacks <strong>Relevance</strong> (why is this important to your goals?), and isn't <strong>Timebound</strong> (no deadline specified).<br><br><strong>SMART Version:</strong> 'I will contribute at least 2 meaningful comments per GBA discussion session over the next 8 weeks to improve my participation grade and deepen my understanding.'"
    },
    {
        "text": "I will start exploring other types of exercise next week.",
        "missing": ["Specific", "Measurable", "Relevant"],
        "feedback": "This goal isn't <strong>Specific</strong> (which types of exercise?), isn't <strong>Measurable</strong> (how much exploration?), and lacks <strong>Relevance</strong> (why explore new exercises?).<br><br><strong>SMART Version:</strong> 'I will try 3 new types of exercise (yoga, swimming, and cycling) for 30 minutes each next week to find enjoyable activities that will help me maintain long-term fitness.'"
    },
    {
        "text": "I will become fluent in Japanese and Arabic to better connect with people.",
        "missing": ["Measurable", "Achievable", "Timebound"],
        "feedback": "This goal isn't <strong>Measurable</strong> (what defines fluency?), isn't <strong>Achievable</strong> (three languages simultaneously is unrealistic), and isn't <strong>Timebound</strong> (no deadline specified).<br><br><strong>SMART Version:</strong> 'I will achieve conversational level in Korean (able to hold 10-minute conversations) within 18 months by studying 1 hour daily to connect with Korean colleagues at work.'"
    },
    {
        "text": "I will ask for more feedback during the next meeting.",
        "missing": ["Specific", "Measurable", "Relevant"],
        "feedback": "This goal isn't <strong>Specific</strong> (feedback about what?), isn't <strong>Measurable</strong> (how much is 'more'?), and lacks <strong>Relevance</strong> (why do you need this feedback?).<br><br><strong>SMART Version:</strong> 'I will ask my supervisor for specific feedback on 3 key areas of my project performance during next Tuesday's meeting to improve my work quality and meet project deadlines.'"
    },
    {
        "text": "I will be more confident in meetings to improve my public-speaking skills.",
        "missing": ["Specific", "Measurable", "Timebound"],
        "feedback": "This goal lacks <strong>Specificity</strong> (what specific actions will build confidence?), isn't <strong>Measurable</strong> (how will you track confidence?), and has no <strong>Timebound</strong> deadline.<br><br><strong>SMART Version:</strong> 'I will speak up at least twice during each weekly team meeting for the next 2 months to build confidence and improve my public-speaking skills.'"
    },
  
    # Missing 4 elements
    {
        "text": "I will launch a successful online business by next week.",
        "missing": ["Specific", "Measurable", "Achievable", "Relevant"],
        "feedback": "This goal isn't <strong>Specific</strong> (what type of business?), isn't <strong>Measurable</strong> (what defines success?), isn't <strong>Achievable</strong> (launching a successful business in one week is unrealistic), and lacks <strong>Relevance</strong> (why this business? How does it fit your skills?).<br><br><strong>SMART Version:</strong> 'I will launch my freelance graphic design website with 5 portfolio pieces and contact 20 potential clients within 6 months to generate $1,000 monthly income using my design skills.'"
    },
    {
        "text": "I want to build better habits.",
        "missing": ["Specific", "Measurable", "Relevant", "Timebound"],
        "feedback": "This goal lacks <strong>Specificity</strong> (which habits?), isn't <strong>Measurable</strong> (how will you track progress?), lacks <strong>Relevance</strong> (why these habits?), and has no <strong>Timebound</strong> deadline.<br><br><strong>SMART Version:</strong> 'I will establish a morning routine of 30 minutes of reading and 10 minutes of meditation daily for the next 30 days to improve my focus and productivity at work.'"
    },
    {
        "text": "I want to eat healthier.",
        "missing": ["Specific", "Measurable", "Relevant", "Timebound"],
        "feedback": "This goal lacks <strong>Specificity</strong> (what does healthier mean?), isn't <strong>Measurable</strong> (how will you track it?), lacks <strong>Relevance</strong> (why is this important to you?), and has no <strong>Timebound</strong> deadline.<br><br><strong>SMART Version:</strong> 'I will eat 5 servings of fruits and vegetables daily for the next 3 months to improve my energy levels and overall health.'"
    },
    
    # Missing 5 elements
    {
        "text": "I will do better.",
        "missing": ["Specific", "Measurable", "Achievable", "Relevant", "Timebound"],
        "feedback": "This goal is missing all SMART elements: it's not <strong>Specific</strong> (better at what?), not <strong>Measurable</strong> (how to track progress?), not <strong>Achievable</strong> (too vague to assess), not <strong>Relevant</strong> (to what purpose?), and not <strong>Timebound</strong> (no deadline).<br><br><strong>SMART Version:</strong> 'I will improve my math test scores by 15% within the next semester by studying 1 hour daily and attending weekly tutoring sessions.'"
    }
]

# ---------------------------- SESSION STATE INIT ----------------------------
def init_game_state():
    defaults = {
        'current_question': 0, 'score': 0, 'total_questions': len(GOALS_DATABASE),
        'current_goal': None, 'awaiting_response': False, 'show_feedback': False,
        'user_selections': [], 'game_completed': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_game_state()

# ---------------------------- FUTURISTIC STYLES ----------------------------
def get_futuristic_styles():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');

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
    
    /* Full screen background */
    .stApp {
        background-image: url('https://raw.githubusercontent.com/qw-chee/peakperformancelab/main/assets/smart.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        min-height: 100vh;
        position: relative;
    }
     
    .neon-container {
        background: rgba(15, 15, 35, 0.95);
        border: 2px solid transparent;
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        position: relative;
        backdrop-filter: blur(10px);
        box-shadow: 
            0 0 30px rgba(0, 255, 255, 0.2),
            inset 0 0 30px rgba(0, 255, 255, 0.05);
    }
    
    .neon-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        border-radius: 18px;
        padding: 2px;
        background: linear-gradient(45deg, 
            rgba(0, 255, 255, 0.8), 
            rgba(255, 0, 255, 0.8), 
            rgba(0, 255, 127, 0.8), 
            rgba(255, 255, 0, 0.8));
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask-composite: subtract;
        z-index: -1;
        animation: border-glow 3s ease-in-out infinite alternate;
    }
    
    @keyframes border-glow {
        0% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    .cyber-title {
        font-family: 'Orbitron', monospace;
        font-weight: 900;
        font-size: 2.8em;
        background: linear-gradient(45deg, #00ffff, #ff00ff, #00ff7f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
        animation: title-pulse 2s ease-in-out infinite alternate;
    }
    
    @keyframes title-pulse {
        0% { filter: brightness(1) saturate(1); }
        100% { filter: brightness(1.2) saturate(1.3); }
    }
    
    .cyber-subtitle, .cyber-text {
        font-family: 'Rajdhani', sans-serif;
        color: rgba(0, 255, 255, 0.8);
        text-align: center;
        margin-bottom: 15px;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.3);
    }
    
    .cyber-subtitle {
        font-weight: 400;
        font-size: 1.2em;
    }
    
    .cyber-text {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1em;
        line-height: 1.6;
    }
    
    .smart-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 5px;
        margin: 5px 0;
    }
    
    .smart-card {
        background: rgba(0, 255, 255, 0.1);
        border: 1px solid rgba(0, 255, 255, 0.3);
        border-radius: 5px;
        padding: 15px;
        text-align: center;
        transition: all 0.3s ease;
        backdrop-filter: blur(5px);
    }
    
    .smart-card:hover {
        background: rgba(0, 255, 255, 0.2);
        border-color: rgba(0, 255, 255, 0.6);
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0, 255, 255, 0.2);
    }
    
    .smart-letter {
        font-family: 'Orbitron', monospace;
        font-weight: 700;
        font-size: 2em;
        background: linear-gradient(45deg, #00ffff, #00ff7f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        display: block;
        margin-bottom: 5px;
    }
    
    .cyber-progress {
        background: rgba(15, 15, 35, 0.9);
        border: 1px solid rgba(0, 255, 255, 0.3);
        border-radius: 12px;
        padding: 15px;
        margin: 15px 0;
        backdrop-filter: blur(10px);
    }
    
    .progress-track {
        height: 8px;
        background: rgba(0, 255, 255, 0.2);
        border-radius: 4px;
        overflow: hidden;
        position: relative;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #00ffff, #00ff7f);
        border-radius: 4px;
        transition: width 1s ease;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.6);
        animation: progress-glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes progress-glow {
        0% { box-shadow: 0 0 15px rgba(0, 255, 255, 0.6); }
        100% { box-shadow: 0 0 25px rgba(0, 255, 255, 0.9); }
    }
    
    .progress-text {
        font-family: 'Orbitron', monospace;
        color: #00ffff;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
        font-size: 1.1em;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
    }
    
    .goal-statement {
        background: rgba(15, 15, 35, 0.9);
        border: 2px solid rgba(255, 0, 255, 0.3);
        border-radius: 12px;
        padding: 15px;
        margin: 15px 0;
        position: relative;
        backdrop-filter: blur(5px);
    }
    
    .goal-statement::before, .goal-statement::after {
        position: absolute;
        font-size: 4em;
        color: rgba(255, 0, 255, 0.6);
        font-family: 'Orbitron', monospace;
    }
    
    .goal-statement::before {
        content: '"';
        top: -10px;
        left: 20px;
    }
    
    .goal-statement::after {
        content: '"';
        bottom: -30px;
        right: 20px;
    }
    
    .goal-text {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.3em;
        color: rgba(255, 255, 255, 0.95);
        font-style: italic;
        line-height: 1.5;
        margin: 0;
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.3);
    }
    
    .cyber-hint {
        background: rgba(0, 255, 127, 0.1);
        border: 1px solid rgba(0, 255, 127, 0.4);
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        backdrop-filter: blur(5px);
    }
    
    .hint-icon {
        color: #00ff7f;
        font-size: 1.2em;
        margin-right: 8px;
    }
    
    .hint-text {
        color: rgba(0, 255, 127, 0.9);
        font-family: 'Rajdhani', sans-serif;
        font-weight: 500;
    }
    
    .feedback-success {
        background: rgba(15, 15, 35, 0.9);
        border: 2px solid rgba(0, 255, 127, 0.6);
        border-radius: 5px;
        padding: 5px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 30px rgba(0, 255, 127, 0.3);
    }
    
    .feedback-learning {
        background: rgba(15, 15, 35, 0.9);
        border: 2px solid rgba(255, 80, 80, 0.6);
        border-radius: 5px;
        padding: 5px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 30px rgba(255, 80, 80, 0.3);
    }
    
    .feedback-title {
        font-family: 'Orbitron', monospace;
        font-weight: 700;
        font-size: 2.2em;
        margin: 0;
        text-shadow: 0 0 15px currentColor;
    }
    
    .feedback-icon {
        font-size: 2.5em;
        margin-bottom: 10px;
        display: block;
    }
    
    .missing-components {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
        margin: 20px 0;
    }
    
    .component-tag {
        background: rgba(255, 255, 0, 0.2);
        color: #ffff00;
        border: 1px solid rgba(255, 255, 0, 0.5);
        padding: 8px 16px;
        border-radius: 20px;
        font-family: 'Orbitron', monospace;
        font-weight: 600;
        font-size: 0.9em;
        text-shadow: 0 0 10px rgba(255, 255, 0, 0.5);
    }
    
    .results-container {
        text-align: center;
        padding: 20px;
    }
    
    .score-display {
        font-family: 'Orbitron', monospace;
        font-size: 3.5em;
        font-weight: 900;
        background: linear-gradient(45deg, #00ffff, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 15px 0;
        text-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
    }
    
    .stCheckbox > label {
        font-family: 'Rajdhani', sans-serif !important;
        color: white !important;
        font-size: 1em !important;
        font-weight: 600 !important;
        background: rgba(0, 255, 255, 0.05) !important;
        border: 1px solid rgba(0, 255, 255, 0.2) !important;
        border-radius: 8px !important;
        padding: 6px 8px !important;
        margin: 2px 0 !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(5px) !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
       
    .stCheckbox > label[data-checked="true"] {
        background-color: rgba(0, 255, 255) !important;
        border-color: #00ffff !important;
        margin-bottom: -10px;
    }
    
    .stCheckbox > label:hover {
        background: rgba(0, 255, 255, 0.1) !important;
        border-color: rgba(0, 255, 255, 0.4) !important;
        transform: translateX(5px) !important;
    }
    
    .stCheckbox > label > div[data-checked="true"] {
        background: linear-gradient(45deg, #00ffff, #00ff7f) !important;
        border: none !important;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.6) !important;
    }
    
    .stCheckbox > label > span, .stCheckbox * {
        color: white !important;
    }

    div[data-testid="stForm"] {
        background-color: rgba(15, 15, 35, 0.9) !important;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #333;
    }
    
    div[data-testid="stForm"] label {
        color: white !important;
    }
    
    div[data-testid="stForm"] [data-testid="column"] {
        padding-left: -0.5rem !important;
        padding-right: -0.5rem !important;
    }
    
    div[data-testid="stForm"] .element-container {
        margin: 0 !important;
    }
    
    div[data-testid="stButton"] > button[kind="primary"] {
        background: linear-gradient(135deg, #00ffff 0%, #ff00ff 50%, #00ff7f 100%) !important;
        border: 2px solid rgba(0, 255, 255, 0.5) !important;
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 1.1em !important;
        font-family: 'Orbitron', monospace !important;
        padding: 15px 25px !important;
        border-radius: 25px !important;
        box-shadow: 
            0 0 20px rgba(0, 255, 255, 0.4),
            inset 0 0 20px rgba(255, 255, 255, 0.2) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }

    div[data-testid="stButton"] > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #ff00ff 0%, #00ff7f 50%, #00ffff 100%) !important;
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 
            0 5px 25px rgba(0, 255, 255, 0.6),
            0 0 30px rgba(255, 0, 255, 0.4),
            inset 0 0 25px rgba(255, 255, 255, 0.3) !important;
        border-color: rgba(255, 0, 255, 0.8) !important;
    }

    div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, rgba(0, 255, 255, 0.2) 0%, rgba(255, 0, 255, 0.2) 100%) !important;
        border: 1px solid rgba(0, 255, 255, 0.4) !important;
        color: #00ffff !important;
        font-weight: 600 !important;
        font-family: 'Rajdhani', sans-serif !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stButton"] > button:hover {
        background: linear-gradient(135deg, rgba(0, 255, 255, 0.3) 0%, rgba(255, 0, 255, 0.3) 100%) !important;
        border-color: rgba(0, 255, 255, 0.6) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3) !important;
    }

    div[data-testid="stForm"] div[data-testid="stButton"] > button[kind="primary"] {
        width: 100% !important;
        margin-top: 20px !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(15, 15, 35, 0.5);
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #00ffff, #ff00ff);
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #ff00ff, #00ff7f);
    }
    </style>
    """

st.markdown(get_futuristic_styles(), unsafe_allow_html=True)

# ---------------------------- LOADING OVERLAY ----------------------------
st.markdown("""
<div id="loading-overlay">
    <div class="loading-content">
        <div class="loading-title">LAUNCHING MISSION...</div>
        <div class="loading-bar-container">
            <div class="loading-bar"></div>
        </div>
        <div class="loading-subtitle">Initializing SMART Protocol</div>
    </div>
</div>

<style>
#loading-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #0a0a0a;
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
    font-family: 'Orbitron', monospace;
    font-size: 3em;
    font-weight: 900;
    background: linear-gradient(45deg, #00ffff, #ff00ff, #00ff7f);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 20px;
    animation: pulse 2s ease-in-out infinite;
}

.loading-bar-container {
    width: 200px;
    height: 4px;
    background: rgba(0, 255, 255, 0.2);
    border-radius: 2px;
    overflow: hidden;
    position: relative;
    margin: 0 auto;
}

.loading-bar {
    width: 40%;
    height: 100%;
    background: linear-gradient(90deg, #00ffff, #00ff7f);
    border-radius: 2px;
    animation: loading-bar 2s ease-in-out infinite;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.6);
}

.loading-subtitle {
    font-family: 'Rajdhani', sans-serif;
    color: rgba(255, 255, 255, 0.7);
    margin-top: 15px;
    font-size: 1.2em;
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.7; transform: scale(1.05); }
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
</style>
""", unsafe_allow_html=True)

# ---------------------------- HELPER FUNCTIONS ----------------------------
def reset_to_question(question_num):
    """Reset game state to a specific question"""
    st.session_state.current_question = question_num
    st.session_state.awaiting_response = True
    st.session_state.show_feedback = False
    st.session_state.user_selections = []
    if question_num > 0:
        st.session_state.current_goal = GOALS_DATABASE[question_num - 1]

def get_result_config(score_percentage):
    """Get result configuration based on score"""
    if score_percentage >= 80:
        return {
            "style": "feedback-success", "icon": "🏆", "title": "PROTOCOL MASTERED",
            "message": "EXCEPTIONAL PERFORMANCE: Neural pathways optimized for SMART goal identification.",
            "color": "#00ff7f"
        }
    elif score_percentage >= 50:
        return {
            "style": "neon-container", "icon": "🎯", "title": "SYSTEM UPGRADED",
            "message": "GOOD PROGRESS: Core algorithms functioning within acceptable parameters.",
            "color": "#00ffff"
        }
    else:
        return {
            "style": "feedback-learning", "icon": "🔄", "title": "RECALIBRATION REQUIRED",
            "message": "LEARNING MODE: Additional training cycles recommended for optimization.",
            "color": "#ff5050"
        }

# ---------------------------- OVERVIEW PAGE ----------------------------
if st.session_state.current_question == 0 and not st.session_state.game_completed:
    st.markdown("""
    <div class="neon-container">
        <h1 class="cyber-title">Mission: SMART Possible</h1>
        <div class="cyber-text" style="text-align: center; margin-bottom: 5px;">
            Initialize your goal-setting algorithms. Identify missing SMART components 
            to transform abstract goals into executable objectives.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="neon-container">
        <h3 style="color: #00ffff; font-family: 'Orbitron', monospace; text-align: center; margin-bottom: -5px; font-size: 1.8em;">
            📡 SMART PROTOCOL COMPONENTS
        </h3>
        <div class="smart-grid">
            <div class="smart-card">
                <span class="smart-letter">S</span>
                <strong style="color: #00ffff;">SPECIFIC</strong><br>
                <i style="color: rgba(255,255,255,0.7);">Is it well-defined?</i>
            </div>
            <div class="smart-card">
                <span class="smart-letter">M</span>
                <strong style="color: #00ffff;">MEASURABLE</strong><br>
                <i style="color: rgba(255,255,255,0.7);">Is it quantifiable?</i>
            </div>
            <div class="smart-card">
                <span class="smart-letter">A</span>
                <strong style="color: #00ffff;">ACHIEVABLE</strong><br>
                <i style="color: rgba(255,255,255,0.7);">Is it realistic?</i>
            </div>
            <div class="smart-card">
                <span class="smart-letter">R</span>
                <strong style="color: #00ffff;">RELEVANT</strong><br>
                <i style="color: rgba(255,255,255,0.7);">Is there a purpose?</i>
            </div>
            <div class="smart-card">
                <span class="smart-letter">T</span>
                <strong style="color: #00ffff;">TIMEBOUND</strong><br>
                <i style="color: rgba(255,255,255,0.7);">Is there a time horizon?</i>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="neon-container">
        <h3 style="color: #ff00ff; font-family: 'Orbitron', monospace; text-align: center; margin-bottom: -5px; font-size: 1.6em;">
            ⚡ MISSION PARAMETERS
        </h3>
        <div class="cyber-text" style="text-align: center; margin-bottom: 5px;">
            Analyze each goal statement. Identify the missing components. Process feedback. Complete all 20 challenges to succeed!
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 INITIALIZE PROTOCOL", use_container_width=True, type="primary"):
        reset_to_question(1)
        st.rerun()
    
    st.stop()

# ---------------------------- MAIN GAME ----------------------------
if not st.session_state.game_completed:
    # Progress Bar
    progress_percentage = ((st.session_state.current_question - 1) / st.session_state.total_questions) * 100
    
    st.markdown(f"""
    <div class="cyber-progress">
        <div class="progress-text">CHALLENGE {st.session_state.current_question} OF {st.session_state.total_questions}</div>
        <div class="progress-track">
            <div class="progress-fill" style="width: {progress_percentage}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.awaiting_response:
        goal = st.session_state.current_goal
        missing_count = len(goal["missing"])
        
        st.markdown(f"""
        <div class="goal-statement" style="text-align: center;">
            <div class="goal-text">{goal['text']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="neon-container">
            <h3 style="color: #00ffff; font-family: 'Orbitron', monospace; margin-bottom: -10px; font-size: 1.4em;">
                🔍 WHICH SMART COMPONENTS ARE MISSING?
            </h3>
            <div class="cyber-hint">
                <span class="hint-icon">💡</span>
                <span class="hint-text">Hint: This goal is missing <strong>{missing_count}</strong> SMART component{"s" if missing_count != 1 else ""}.</span>
            </div>
        """, unsafe_allow_html=True)

        with st.form("smart_form", clear_on_submit=False):
            st.markdown('<div class="cyber-text" style="margin: 0 0 0 0">Select all missing components:</div>', unsafe_allow_html=True)
            
            selected_missing = []
            smart_components = ["Specific", "Measurable", "Achievable", "Relevant", "Timebound"]
            
            # Use equal columns for better fit
            cols = st.columns(5)
            
            for i, component in enumerate(smart_components):
                with cols[i]:
                    if st.checkbox(component, key=f"chk_{component}_{st.session_state.current_question}"):
                        selected_missing.append(component)
            
            submitted = st.form_submit_button("⚡ EXECUTE ANALYSIS", use_container_width=True, type="primary")
            
            if submitted:
                st.session_state.user_selections = selected_missing
                st.session_state.awaiting_response = False
                st.session_state.show_feedback = True
                
                # Check if answer is correct
                if set(selected_missing) == set(goal["missing"]):
                    st.session_state.score += 1
                
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    elif st.session_state.show_feedback:
        goal = st.session_state.current_goal
        user_correct = set(st.session_state.user_selections) == set(goal["missing"])
        
        # Feedback styling
        feedback_class = "feedback-success" if user_correct else "feedback-learning"
        feedback_icon = "✅" if user_correct else "❌"
        feedback_title = "SUCCESS" if user_correct else "INCORRECT"
        title_color = "#00ff7f" if user_correct else "#ff5050"
        
        st.markdown(f"""
        <div class="{feedback_class}">
            <span class="feedback-icon">{feedback_icon}</span>
            <h2 class="feedback-title" style="color: {title_color}; text-align: center;">{feedback_title}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Show correct answer
        st.markdown(f"""
        <div class="neon-container">
            <h3 style="color: #ffff00; font-family: 'Orbitron', monospace; margin-bottom: -20px; font-size: 1.3em; text-align: center;">
                📊 MISSING COMPONENTS DETECTED
            </h3>
            <div class="missing-components">
                {' '.join([f'<span class="component-tag">{comp}</span>' for comp in goal["missing"]])}
            </div>
            <div style="background: rgba(0,255,255,0.1); border: 1px solid rgba(0,255,255,0.3); border-radius: 12px; padding: 20px; margin-top: 20px;">
                <div style="color: #00ffff; font-family: 'Orbitron', monospace; font-weight: 600; margin-bottom: 10px;">
                    📝 SYSTEM ANALYSIS:
                </div>
                <div style="color: rgba(255,255,255,0.9); font-family: 'Rajdhani', sans-serif; line-height: 1.5;">
                    {goal["feedback"]}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.current_question < st.session_state.total_questions:
            if st.button("⚡ NEXT CHALLENGE", use_container_width=True, type="primary"):
                reset_to_question(st.session_state.current_question + 1)
                st.rerun()
        else:
            if st.button("🎉 VIEW RESULTS", use_container_width=True, type="primary"):
                st.session_state.game_completed = True
                st.rerun()

# ---------------------------- END SCREEN ----------------------------
if st.session_state.game_completed:
    score_percentage = (st.session_state.score / st.session_state.total_questions) * 100
    result_config = get_result_config(score_percentage)
    
    st.markdown(f"""
    <div class="{result_config['style']}">
        <div class="results-container">
            <span class="feedback-icon">{result_config['icon']}</span>
            <h1 class="feedback-title" style="color: {result_config['color']}; margin-bottom: 5px;">{result_config['title']}</h1>
            <div style="color: rgba(255,255,255,0.8); font-family: 'Rajdhani', sans-serif; font-size: 1.2em;">
                {result_config['message']}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="neon-container">
        <div class="results-container">
            <h2 style="color: #ff00ff; font-family: 'Orbitron', monospace; margin-bottom: -10px; font-size: 1.8em;">
                📊 PERFORMANCE METRICS
            </h2>
            <div class="score-display">
                {st.session_state.score}/{st.session_state.total_questions}
            </div>
            <div style="color: #00ffff; font-family: 'Orbitron', monospace; font-size: 1.6em; font-weight: 600; margin-bottom: 10px;">
                {score_percentage:.0f}% ACCURACY ACHIEVED
            </div>
            <div style="background: rgba(0,255,255,0.1); border: 1px solid rgba(0,255,255,0.3); border-radius: 12px; padding: 10px;">
                <div style="color: rgba(255,255,255,0.9); font-family: 'Rajdhani', sans-serif; font-size: 1.1em; line-height: 1.5;">
                    SMART goals are important because they make goals clear, focused, and achievable. By being Specific, Measurable, Achievable, Relevant, and Time-bound, SMART goals help you stay organized, track progress, stay motivated, and make better decisions. They turn vague ideas into clear action plans. Always practice SMART goals!
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 RESTART PROTOCOL", use_container_width=True):
            st.session_state.score = 0
            st.session_state.game_completed = False
            reset_to_question(1)
            st.rerun()
    
    with col2:
        if st.button("🏠 RETURN TO BASE", use_container_width=True):
            st.session_state.score = 0
            st.session_state.game_completed = False
            st.session_state.current_goal = None
            reset_to_question(0)
            st.rerun()
