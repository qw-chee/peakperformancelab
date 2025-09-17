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
        "text": "To manage time, I will write some of my TMA every weekend.",
        "missing": ["Measurable"],
        "feedback": "This goal isn't <strong>Measurable</strong> - 'some' is vague. How much work should be specified, like '2 pages' or '500 words' or '1 hour of writing'.<br><br><strong>SMART Version:</strong> 'To manage time effectively, I will write 300 words of my TMA every weekend until completion.'"
    },
    {
        "text": "I will finish reading 50 books to improve my writing by tomorrow.",
        "missing": ["Achievable"],
        "feedback": "This goal isn't <strong>Achievable</strong> - reading 10 books in one day is unrealistic. A more achievable timeline would be several months.<br><br><strong>SMART Version:</strong> 'I will finish reading 10 books over the next 6 months to improve my writing skills by expanding my vocabulary and understanding different writing styles.'"
    },
    {
        "text": "I will aim to improve my GPA by 0.2 for better career prospects.",
        "missing": ["Timebound"],
        "feedback": "This goal isn't <strong>Timebound</strong> - there's no deadline specified. There should be a timeframe like 'by the end of this semester' or 'within one academic year'.<br><br><strong>SMART Version:</strong> 'I will improve my GPA by 0.2 points by the end of this academic year through consistent study habits to enhance my career prospects.'"
    },
    {
        "text": "I will volunteer once at the foodbank each month.",
        "missing": ["Relevant"],
        "feedback": "This goal lacks clear <strong>Relevance</strong> - it doesn't explain how volunteering connects to any goals.<br><br><strong>SMART Version:</strong> 'I will volunteer twice at the foodbank each month for 6 months to develop my leadership skills and give back to my community.'"
    },
    
    # Missing 2 elements
    {
        "text": "I want to save 100 million dollars by the end of this year.",
        "missing": ["Achievable", "Relevant"],
        "feedback": "This goal isn't <strong>Achievable</strong> (10 million in one year is unrealistic for most people) and lacks <strong>Relevance</strong> (why this specific amount? What's the purpose?).<br><br><strong>SMART Version:</strong> 'I will save $5,000 by the end of this year to build an emergency fund for my family's financial security.'"
    },
    {
        "text": "I will arrive earlier for NCO112 seminars starting next week.",
        "missing": ["Measurable", "Relevant"],
        "feedback": "This goal isn't <strong>Measurable</strong> (how much earlier?) and lacks <strong>Relevance</strong> (why is arriving earlier important for your academic success?).<br><br><strong>SMART Version:</strong> 'I will arrive 15 minutes earlier for each class starting next week to review notes and improve my academic performance.'"
    },
    
    # Missing 3 elements
    {
        "text": "I will start exploring other types of exercise next week.",
        "missing": ["Specific", "Measurable", "Relevant"],
        "feedback": "This goal isn't <strong>Specific</strong> (which types of exercise?), isn't <strong>Measurable</strong> (how much exploration?), and lacks <strong>Relevance</strong> (why explore new exercises?).<br><br><strong>SMART Version:</strong> 'I will try 3 new types of exercise (yoga, swimming, and cycling) for 30 minutes each next week to find enjoyable activities that will help me maintain long-term fitness.'"
    },
    {
        "text": "I will become fluent in every language to better connect with people.",
        "missing": ["Measurable", "Achievable", "Timebound"],
        "feedback": "This goal isn't <strong>Measurable</strong> (what defines fluency?), isn't <strong>Achievable</strong> (every language is unrealistic), and isn't <strong>Timebound</strong> (no deadline specified).<br><br><strong>SMART Version:</strong> 'I will achieve conversational level in Korean (able to hold 10-minute conversations) within 18 months by studying 1 hour daily to connect with Korean colleagues at work.'"
    },  
    # Missing 4 elements
    {
        "text": "I will launch a successful online business by next week.",
        "missing": ["Specific", "Measurable", "Achievable", "Relevant"],
        "feedback": "This goal isn't <strong>Specific</strong> (what type of business?), isn't <strong>Measurable</strong> (what defines success?), isn't <strong>Achievable</strong> (one week is unrealistic), and lacks <strong>Relevance</strong> (why this business?).<br><br><strong>SMART Version:</strong> 'I will launch a graphic design website with 5 portfolio pieces within 6 months to generate $1,000 monthly income.'"
    },
    {
        "text": "I want to build better habits.",
        "missing": ["Specific", "Measurable", "Relevant", "Timebound"],
        "feedback": "This goal lacks <strong>Specificity</strong> (which habits?), isn't <strong>Measurable</strong> (how will you track progress?), lacks <strong>Relevance</strong> (why these habits?), and has no <strong>Timebound</strong> deadline.<br><br><strong>SMART Version:</strong> 'I will establish a morning routine of 30 minutes of reading and 10 minutes of meditation daily for the next 30 days to improve my focus and productivity at work.'"
    }
]

# ---------------------------- SESSION STATE INIT ----------------------------
def init_game_state():
    defaults = {
        'current_question': 0, 'score': 0, 'total_questions': len(GOALS_DATABASE),
        'current_goal': None, 'awaiting_response': False, 'show_feedback': False,
        'user_selections': [], 'game_completed': False, 'component_errors': {}
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
    
init_game_state()

# ---------------------------- FUTURISTIC STYLES ----------------------------
@st.cache_data
def get_futuristic_styles():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');

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
            margin-top: -3rem;
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
            height: 100% !important;
            max-height: 100% !important;
            overflow-y: auto !important;
        }
        
        /* Full screen background */
        .stApp {
            background-image: url('https://raw.githubusercontent.com/qw-chee/peakperformancelab/main/assets/smart.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            height: 100vh !important;
            max-height: 100vh !important;
            min-height: 100vh !important;
            box-sizing: border-box !important;
            overflow: hidden !important;
            padding: 0 !important;
            margin: 0 !important;
        }
         
        .neon-container {
            background: rgba(15, 15, 35, 0.95);
            border: clamp(1px, 0.2vw, 2px) solid transparent;
            border-radius: clamp(10px, 1.5vw, 15px);
            padding: clamp(1.5px, 0.5vw, 15px);
            margin: clamp(6px, 1vw, 10px) 0;
            margin-bottom: -20px;
            position: relative;
            backdrop-filter: blur(10px);
            box-shadow: 
                0 0 clamp(20px, 3vw, 30px) rgba(0, 255, 255, 0.2),
                inset 0 0 clamp(20px, 3vw, 30px) rgba(0, 255, 255, 0.05);
        }
        
        .neon-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: clamp(10px, 1.5vw, 15px); /* Match the container's border-radius */
            padding: clamp(1px, 0.2vw, 2px); /* Keep padding for border width */
            background: linear-gradient(45deg, 
                rgba(0, 255, 255, 0.8), 
                rgba(255, 0, 255, 0.8), 
                rgba(0, 255, 127, 0.8), 
                rgba(255, 255, 0, 0.8));
            mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            mask-composite: subtract;
            z-index: -1;
        }
        
        @keyframes border-glow {
            0% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        .cyber-title {
            font-family: 'Orbitron', monospace;
            font-weight: 900;
            font-size: clamp(1.8rem, 2.8vw, 2.8em);
            background: linear-gradient(45deg, #00ffff, #ff00ff, #00ff7f);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-align: center;
            margin-bottom: clamp(0.5px, 0.4vw, 10px);
            text-shadow: 0 0 clamp(20px, 3vw, 30px) rgba(0, 255, 255, 0.5);
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
    
        .cyber-text {
            color: rgba(255, 255, 255, 0.9);
            font-size: clamp(1.1rem, 1.3vw, 1.3em);
            line-height: 0.9;
            margin-bottom: 2px;
        }
        
        .smart-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: clamp(3px, 0.5vw, 5px);
            margin: clamp(3px, 0.5vw, 5px) 0;
        }
        
        .smart-card {
            background: rgba(0, 255, 255, 0.1);
            border: clamp(1px, 0.15vw, 1px) solid rgba(0, 255, 255, 0.3);
            border-radius: clamp(4px, 0.7vw, 7px);
            padding: clamp(2.5px, 0.6vw, 5px);
            text-align: center;
            transition: all 0.3s ease;
            backdrop-filter: blur(5px);
        }
        
        .smart-card:hover {
            background: rgba(0, 255, 255, 0.2);
            border-color: rgba(0, 255, 255, 0.6);
            transform: translateY(clamp(-2px, -0.3vw, -3px));
            box-shadow: 0 clamp(8px, 1.5vw, 10px) clamp(15px, 2vw, 20px) rgba(0, 255, 255, 0.2);
        }
        
        .smart-letter {
            font-family: 'Orbitron', monospace;
            font-weight: 700;
            font-size: clamp(1.3em, 1.8vw, 1.8em);
            background: linear-gradient(45deg, #00ffff, #00ff7f);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            display: block;
            margin-bottom: clamp(2px, 0.3vw, 3px);
        }
        
        .cyber-progress {
            background: rgba(15, 15, 35, 0.9);
            border: clamp(1px, 0.15vw, 1px) solid rgba(0, 255, 255, 0.3);
            border-radius: clamp(8px, 1.2vw, 12px);
            padding: clamp(8px, 1.5vw, 15px);
            margin: clamp(8px, 1.5vw, 15px) 0;
            margin-bottom: -5px;
            backdrop-filter: blur(10px);
        }
        
        .progress-track {
            height: clamp(6px, 0.8vw, 8px);
            background: rgba(0, 255, 255, 0.2);
            border-radius: clamp(3px, 0.4vw, 4px);
            overflow: hidden;
            position: relative;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #00ffff, #00ff7f);
            border-radius: clamp(3px, 0.4vw, 4px);
            transition: width 1s ease;
            box-shadow: 0 0 clamp(10px, 1.5vw, 15px) rgba(0, 255, 255, 0.6);
            animation: progress-glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes progress-glow {
            0% { box-shadow: 0 0 clamp(10px, 1.5vw, 15px) rgba(0, 255, 255, 0.6); }
            100% { box-shadow: 0 0 clamp(18px, 2.5vw, 25px) rgba(0, 255, 255, 0.9); }
        }
        
        .progress-text {
            font-family: 'Orbitron', monospace;
            color: #00ffff;
            font-weight: 700;
            text-align: center;
            margin-bottom: clamp(6px, 1vw, 10px);
            font-size: clamp(0.9rem, 1.1vw, 1.1em);
            text-shadow: 0 0 clamp(6px, 1vw, 10px) rgba(0, 255, 255, 0.5);
        }
        
        .goal-statement {
            background: rgba(15, 15, 35, 0.9);
            border: clamp(1px, 0.2vw, 2px) solid rgba(255, 0, 255, 0.3);
            border-radius: clamp(8px, 1.2vw, 12px);
            padding: clamp(8px, 1.5vw, 15px);
            margin: clamp(8px, 1.5vw, 15px) 0;
            position: relative;
            backdrop-filter: blur(5px);
        
            /* Halo effect */
            box-shadow: 0 0 15px rgba(255, 0, 255, 0.6),
                        0 0 30px rgba(255, 0, 255, 0.4),
                        0 0 45px rgba(255, 0, 255, 0.2);
        }
        
        .goal-statement::before, .goal-statement::after {
            position: absolute;
            font-size: clamp(2.5em, 4vw, 4em);
            color: rgba(255, 0, 255, 0.6);
            font-family: 'Orbitron', monospace;
        }
        
        .goal-statement::before {
            content: '"';
            top: clamp(-6px, -1vw, -10px);
            left: clamp(12px, 2vw, 20px);
        }
        
        .goal-statement::after {
            content: '"';
            bottom: clamp(-20px, -3vw, -30px);
            right: clamp(12px, 2vw, 20px);
        }
        
        .goal-text {
            font-family: 'Rajdhani', sans-serif;
            font-size: clamp(1.15rem, 1.35vw, 1.25em);
            color: rgba(255, 255, 255, 0.95);
            font-style: italic;
            font-weight: 700;
            line-height: 1.5;
            margin: 0;
            text-shadow: 0 0 clamp(3px, 0.5vw, 5px) rgba(255, 255, 255, 0.7);
        }
        
        .cyber-hint {
            background: rgba(0, 255, 127, 0.1);
            border: clamp(1px, 0.15vw, 1px) solid rgba(0, 255, 127, 0.4);
            border-radius: clamp(6px, 1vw, 10px);
            padding: clamp(6px, 1vw, 10px);
            margin: clamp(6px, 1vw, 10px) 0;
            backdrop-filter: blur(5px);
        }
        
        .hint-text {
            color: rgba(0, 255, 127, 0.9);
            font-family: 'Rajdhani', sans-serif;
            font-weight: 500;
            font-size: clamp(1.1rem, 1.3vw, 1.2em);
        }

        .hint-text .missing-count {
            font-size: clamp(1.2rem, 1.4vw, 1.3em);
            font-weight: 900;
        }

        .feedback-success {
            background: rgba(15, 15, 35, 0.9);
            border: clamp(1px, 0.2vw, 2px) solid rgba(0, 255, 127, 0.6);
            border-radius: clamp(3px, 0.5vw, 5px);
            padding: clamp(3px, 0.5vw, 5px);
            text-align: center;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 clamp(20px, 3vw, 30px) rgba(0, 255, 127, 0.3);
        }
        
        .feedback-learning {
            background: rgba(15, 15, 35, 0.9);
            border: clamp(1px, 0.2vw, 2px) solid rgba(255, 80, 80, 0.6);
            border-radius: clamp(3px, 0.5vw, 5px);
            padding: clamp(3px, 0.5vw, 5px);
            text-align: center;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 clamp(20px, 3vw, 30px) rgba(255, 80, 80, 0.3);
        }
        
        .feedback-title {
            font-family: 'Orbitron', monospace;
            font-weight: 700;
            font-size: clamp(1.2rem, 2vw, 2.2em);
            margin: 0;
            text-shadow: 0 0 clamp(10px, 1.5vw, 15px) currentColor;
        }
        
        .feedback-icon {
            font-size: clamp(1.5rem, 2vw, 2.5em);
            margin-bottom: clamp(6px, 1vw, 10px);
            display: block;
        }
        
        .missing-components {
            display: flex;
            flex-wrap: wrap;
            gap: clamp(6px, 1vw, 10px);
            justify-content: center;
            margin-top: 13px;
            margin-bottom: 3px;
        }
        
        .component-tag {
            background: rgba(255, 255, 0, 0.2);
            color: #ffff00;
            border: clamp(1px, 0.15vw, 1px) solid rgba(255, 255, 0, 0.5);
            padding: clamp(5px, 0.8vw, 8px) clamp(10px, 1.6vw, 16px);
            border-radius: clamp(12px, 2vw, 20px);
            font-family: 'Orbitron', monospace;
            font-weight: 600;
            font-size: clamp(0.8rem, 1vw, 1em);
            text-shadow: 0 0 clamp(6px, 1vw, 10px) rgba(255, 255, 0, 0.5);
        }
        
        .results-container {
            text-align: center;
            padding: clamp(8px, 1.5vw, 20px);
        }
        
        .score-display {
            font-family: 'Orbitron', monospace;
            font-size: clamp(1.6rem, 2.8vw, 3.5em);
            font-weight: 900;
            background: linear-gradient(45deg, #00ffff, #ff00ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-top: -3px;
            margin-bottom: -3px;
            text-shadow: 0 0 clamp(20px, 3vw, 30px) rgba(0, 255, 255, 0.5);
        }
        
        .stCheckbox > label {
            font-family: 'Rajdhani', sans-serif !important;
            color: white !important;
            font-size: clamp(0.8rem, 1vw, 1em) !important;
            font-weight: 600 !important;
            background: rgba(0, 255, 255, 0.05) !important;
            border: clamp(1px, 0.15vw, 1px) solid rgba(0, 255, 255, 0.2) !important;
            border-radius: clamp(5px, 0.8vw, 8px) !important;
            padding: clamp(4px, 0.6vw, 6px) clamp(5px, 0.8vw, 8px) !important;
            margin: clamp(1px, 0.2vw, 2px) 0 !important;
            transition: all 0.3s ease !important;
            backdrop-filter: blur(5px) !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
           
        .stCheckbox > label[data-checked="true"] {
            background-color: rgba(0, 255, 255) !important;
            border-color: #00ffff !important;
            margin-bottom: clamp(-8px, -1vw, -10px);
        }
        
        .stCheckbox > label:hover {
            background: rgba(0, 255, 255, 0.1) !important;
            border-color: rgba(0, 255, 255, 0.4) !important;
            transform: translateX(clamp(3px, 0.5vw, 5px)) !important;
        }
        
        .stCheckbox > label > div[data-checked="true"] {
            background: linear-gradient(45deg, #00ffff, #00ff7f) !important;
            border: none !important;
            box-shadow: 0 0 clamp(10px, 1.5vw, 15px) rgba(0, 255, 255, 0.6) !important;
        }
        
        .stCheckbox > label > span, .stCheckbox * {
            color: white !important;
        }

        div[data-testid="stForm"] {
            background-color: rgba(15, 15, 35, 0.9) !important;
            padding: clamp(12px, 2vw, 20px);
            border-radius: clamp(6px, 1vw, 10px);
            border: clamp(1px, 0.15vw, 1px) solid #333;
        }
        
        div[data-testid="stForm"] label {
            color: white !important;
        }
        
        div[data-testid="stForm"] [data-testid="column"] {
            padding-left: clamp(-0.3rem, -0.5vw, -0.5rem) !important;
            padding-right: clamp(-0.3rem, -0.5vw, -0.5rem) !important;
        }
        
        div[data-testid="stForm"] .element-container {
            margin: 0 !important;
        }
        
        div[data-testid="stButton"] > button[kind="primary"] {
            background: linear-gradient(135deg, #5000fc 0%, #ff00ff 50%, #00ff7f 100%) !important;
            border: clamp(1px, 0.2vw, 2px) solid #00ffee !important;
            color: #00ffff !important;
            font-weight: 900 !important;
            font-size: clamp(0.9rem, 1.1vw, 1.1em) !important;
            font-family: 'Orbitron', monospace !important;
            padding: clamp(10px, 1.5vw, 15px) clamp(15px, 2.5vw, 25px) !important;
            margin-top: 10px !important;
            border-radius: clamp(15px, 2.5vw, 25px) !important;
            box-shadow: 
                0 0 clamp(12px, 2vw, 20px) rgba(0, 255, 255, 0.4),
                inset 0 0 clamp(12px, 2vw, 20px) rgba(255, 255, 255, 0.2) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase !important;
            letter-spacing: clamp(0.5px, 0.1vw, 1px) !important;
        }

        div[data-testid="stButton"] > button[kind="primary"]:hover {
            background: linear-gradient(135deg, #ff00ff 0%, #00ff7f 50%, #00ffff 100%) !important;
            transform: translateY(clamp(-2px, -0.3vw, -3px)) scale(1.02) !important;
            box-shadow: 
                0 clamp(3px, 0.5vw, 5px) clamp(15px, 2.5vw, 25px) rgba(0, 255, 255, 0.6),
                0 0 clamp(20px, 3vw, 30px) rgba(255, 0, 255, 0.4),
                inset 0 0 clamp(15px, 2.5vw, 25px) rgba(255, 255, 255, 0.3) !important;
            border-color: rgba(255, 0, 255, 0.8) !important;
            color: #c4108b !important;
        }

        div[data-testid="stButton"] > button {
            background: linear-gradient(135deg, #5000fc 0%, #ff00ff 50%, #00ff7f 100%) !important;
            border: clamp(1px, 0.2vw, 2px) solid #f277e6 !important;
            color: #00ffff !important;
            font-weight: 600 !important;
            font-family: 'Rajdhani', sans-serif !important;
            border-radius: clamp(10px, 1.5vw, 15px) !important;
            backdrop-filter: blur(10px) !important;
            transition: all 0.3s ease !important;
        }

        div[data-testid="stButton"] > button:hover {
            background: linear-gradient(135deg, #ff00ff 0%, #00ff7f 50%, #00ffff 100%) !important;
            border: clamp(1px, 0.2vw, 2px) solid #00ffee !important;
            transform: translateY(clamp(-1px, -0.2vw, -2px)) !important;
            box-shadow: 0 clamp(3px, 0.5vw, 5px) clamp(10px, 1.5vw, 15px) rgba(0, 255, 255, 0.3) !important;
            color: #c4108b !important;
        }

        /* Force font on all text elements within buttons */
        div[data-testid="stButton"] * {
            font-weight: 600;
            font-family: 'Rajdhani' !important;
        }

        div[data-testid="stForm"] div[data-testid="stButton"] > button[kind="primary"] {
            width: 100% !important;
            margin-top: clamp(12px, 2vw, 20px) !important;
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

        ::-webkit-scrollbar {
            width: clamp(6px, 1vw, 8px);
        }

        ::-webkit-scrollbar-track {
            background: rgba(15, 15, 35, 0.5);
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, #00ffff, #ff00ff);
            border-radius: clamp(2px, 0.4vw, 4px);
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(45deg, #ff00ff, #00ff7f);
        }
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
@media screen and (min-width: 1024px) {
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
        animation: loading-sequence 4s ease-in-out forwards;
    }

    .loading-content {
        text-align: center;
    }

    .loading-title {
        font-family: 'Orbitron', monospace;
        font-size: clamp(2rem, 3vw, 3em);
        font-weight: 900;
        background: linear-gradient(45deg, #00ffff, #ff00ff, #00ff7f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: clamp(12px, 2vw, 20px);
        animation: pulse 2s ease-in-out infinite;
    }

    .loading-bar-container {
        width: clamp(120px, 20vw, 200px);
        height: clamp(3px, 0.4vw, 4px);
        background: rgba(0, 255, 255, 0.2);
        border-radius: clamp(1px, 0.2vw, 2px);
        overflow: hidden;
        position: relative;
        margin: 0 auto;
    }

    .loading-bar {
        width: 40%;
        height: 100%;
        background: linear-gradient(90deg, #00ffff, #00ff7f);
        border-radius: clamp(1px, 0.2vw, 2px);
        animation: loading-bar 2s ease-in-out infinite;
        box-shadow: 0 0 clamp(10px, 1.5vw, 15px) rgba(0, 255, 255, 0.6);
    }

    .loading-subtitle {
        font-family: 'Rajdhani', sans-serif;
        color: rgba(255, 255, 255, 0.7);
        margin-top: clamp(8px, 1.5vw, 15px);
        font-size: clamp(1rem, 1.4vw, 1.4em);
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
}
</style>
""", unsafe_allow_html=True)

# Block mobile and tablet, handle responsive scaling with JavaScript
st.markdown("""
<script>
// Block mobile and tablet, handle responsive scaling
if (window.innerWidth >= 1024) {
    // Handle window resize for responsive scaling
    window.addEventListener('resize', function() {
        if (window.innerWidth < 1024) {
            document.body.style.display = 'none';
            document.body.innerHTML = '<div style="display: flex; justify-content: center; align-items: center; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%); color: white; font-size: 1.5rem; text-align: center; font-family: Orbitron, monospace;">This application is designed for desktop and laptop screens only.</div>';
        }
    });
}
</script>
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
    if score_percentage >= 70:
        return {
            "style": "feedback-success", "title": "🏆 PROTOCOL MASTERED",
            "message": "EXCEPTIONAL PERFORMANCE: Neural pathways optimized for SMART goal identification.",
            "color": "#00ff7f"
        }
    elif score_percentage >= 50:
        return {
            "style": "neon-container", "title": "🎯 SYSTEM UPGRADED",
            "message": "GOOD PROGRESS: Core algorithms functioning within acceptable parameters.",
            "color": "#00ffff"
        }
    else:
        return {
            "style": "feedback-learning", "title": "🔄 RECALIBRATION REQUIRED",
            "message": "LEARNING MODE: Additional training cycles recommended for optimization.",
            "color": "#ff5050"
        }

# ---------------------------- OVERVIEW PAGE ----------------------------
st.markdown( """ <style> @media (min-width: 1300px) { .custom-spacer { height: 10vh; } } </style> <div class="custom-spacer"></div> """, unsafe_allow_html=True )

if st.session_state.current_question == 0 and not st.session_state.game_completed:
    st.markdown("""
    <div class="neon-container">
        <h2 class="cyber-title" style="margin-bottom: -5px;">Mission: SMART Possible</h1>
        <div class="cyber-text" style="text-align: center;">
            SMART goals are the blueprint for peak performance. 
            They turn wishful thinking into clear action steps, reduce procrastination, and keep your focus locked on progress. 
            By identifying the missing SMART components in this challenge, you’ll sharpen your ability to set goals that actually drive results. Ready to power up your performance?
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="neon-container">
        <h3 style="color: #00ffff; font-family: 'Orbitron', monospace; text-align: center; font-size: clamp(1rem, 1.6vw, 1.5em); margin-bottom: -5px;">
            📡 SMART PROTOCOL COMPONENTS
        </h3>
        <div class="smart-grid">
            <div class="smart-card">
                <span class="smart-letter">S</span>
                <strong style="color: #00ffff; font-size: clamp(0.9rem, 1.1vw, 1.1em);">SPECIFIC</strong><br>
                <i style="color: rgba(255,255,255,0.7); font-size: clamp(0.8rem, 1vw, 1em);">Is it well-defined?</i>
            </div>
            <div class="smart-card">
                <span class="smart-letter">M</span>
                <strong style="color: #00ffff; font-size: clamp(0.9rem, 1.1vw, 1.1em);">MEASURABLE</strong><br>
                <i style="color: rgba(255,255,255,0.7); font-size: clamp(0.8rem, 1vw, 1em);">Is it quantifiable?</i>
            </div>
            <div class="smart-card">
                <span class="smart-letter">A</span>
                <strong style="color: #00ffff; font-size: clamp(0.9rem, 1.1vw, 1.1em);">ACHIEVABLE</strong><br>
                <i style="color: rgba(255,255,255,0.7); font-size: clamp(0.8rem, 1vw, 1em);">Is it realistic?</i>
            </div>
            <div class="smart-card">
                <span class="smart-letter">R</span>
                <strong style="color: #00ffff; font-size: clamp(0.9rem, 1.1vw, 1.1em);">RELEVANT</strong><br>
                <i style="color: rgba(255,255,255,0.7); font-size: clamp(0.8rem, 1vw, 1em);">Is there a purpose?</i>
            </div>
            <div class="smart-card">
                <span class="smart-letter">T</span>
                <strong style="color: #00ffff; font-size: clamp(0.9rem, 1.1vw, 1.1em);">TIMEBOUND</strong><br>
                <i style="color: rgba(255,255,255,0.7); font-size: clamp(0.8rem, 1vw, 1em);">Is there a time horizon?</i>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="neon-container">
        <h3 style="color: #ff00ff; font-family: 'Orbitron', monospace; text-align: center; margin-bottom: -5px; font-size: clamp(1rem, 1.6vw, 1.5em);">
            ⚡ MISSION PARAMETERS
        </h3>
        <div class="cyber-text" style="text-align: center; margin-bottom: 5px;">
            Analyze each goal. Identify missing component(s). Complete all 10 challenges to succeed!
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 INITIALIZE PROTOCOL", use_container_width=True, type="primary"):
        reset_to_question(1)
        st.rerun()
    
    st.stop()

# ---------------------------- MAIN GAME ----------------------------
if not st.session_state.game_completed:
    if st.session_state.show_feedback:
        progress_percentage = (st.session_state.current_question / st.session_state.total_questions) * 100
    else:
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
        <div class="neon-container">
            <h3 style="color: #00ffff; font-family: 'Orbitron', monospace; margin-bottom: -10px; font-size: clamp(1rem, 1.2vw, 1.2em);">
                🔍 WHICH SMART COMPONENTS ARE MISSING?
            </h3>
            <div class="goal-statement" style="text-align: center;">
                <span class="goal-text">{goal['text']}</span>
            </div>
            <div class="hint-text">💡 Hint: This goal is missing <u><strong class="missing-count">{missing_count}</strong></u> SMART component{"s" if missing_count != 1 else ""}.</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div style="margin-top: 5px;">', unsafe_allow_html=True)
        
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

                if 'component_errors' not in st.session_state:
                    st.session_state.component_errors = {}

                # Track false negatives only
                for component in goal["missing"]:
                    if component not in selected_missing:  # User missed this component
                        if component not in st.session_state.component_errors:
                            st.session_state.component_errors[component] = 0
                        st.session_state.component_errors[component] += 1
                
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    elif st.session_state.show_feedback:
        goal = st.session_state.current_goal
        user_correct = set(st.session_state.user_selections) == set(goal["missing"])
        
        # Feedback styling
        feedback_class = "feedback-success" if user_correct else "feedback-learning"
        feedback_icon = "✅" if user_correct else "❌"
        feedback_title = "SUCCESS!" if user_correct else "INCORRECT!"
        title_color = "#00ff7f" if user_correct else "#ff5050"
        
        st.markdown(f"""
        <div class="{feedback_class}" style="display: flex; align-items: center; justify-content: center; gap: 8px; margin-top: 10px;">
            <span class="feedback-icon">{feedback_icon}</span>
            <h3 class="feedback-title" style="color: {title_color}; margin: 0;">{feedback_title}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Show correct answer
        st.markdown(f"""
        <div class="neon-container">
            <h3 style="color: #ffff00; font-family: 'Orbitron', monospace; margin-bottom: -20px; font-size: clamp(1.05rem, 1.35vw, 1.35em); text-align: center;">
                📊 MISSING COMPONENTS
            </h3>
            <div class="missing-components">
                {' '.join([f'<span class="component-tag">{comp}</span>' for comp in goal["missing"]])}
            </div>
            <div style="background: rgba(0,255,255,0.1); border: clamp(1px, 0.15vw, 1px) solid rgba(0,255,255,0.3); border-radius: clamp(8px, 1.2vw, 12px); padding: clamp(2px, 0.5vw, 20px); margin-top: clamp(4px, 1vw, 20px);">
                <div style="color: #00ffff; font-family: 'Orbitron', monospace; font-weight: 600; margin-bottom: clamp(6px, 1vw, 10px); font-size: clamp(0.9rem, 1.1vw, 1.1em);">
                    📝 SYSTEM ANALYSIS:
                </div>
                <div style="color: rgba(255,255,255,0.9); font-family: 'Rajdhani', sans-serif; line-height: 1.2; font-size: clamp(1.05rem, 1.25vw, 1.25em);">
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
    
    component_totals = {"Specific": 3, "Measurable": 6, "Achievable": 4, "Relevant": 6, "Timebound": 4}
    error_rates = {}
    for component, total in component_totals.items():
        errors = st.session_state.component_errors.get(component, 0)
        error_rates[component] = errors / total
    
    max_error_rate = max(error_rates.values()) if error_rates.values() else 0
    weakest_components = [comp for comp, rate in error_rates.items() if rate == max_error_rate and rate > 0]
    
    if weakest_components:
        if len(weakest_components) == 1:
            weakness_text = f"Your weakest area: <strong>{weakest_components[0]}</strong> ({max_error_rate:.0%} missed)"
            feedback_text = f"Focus on making your goals more <strong>{weakest_components[0].lower()}</strong>."
        else:
            weakness_text = f"Your weakest areas: <strong>{' & '.join(weakest_components)}</strong> ({max_error_rate:.0%} missed)"
            feedback_text = f"Focus on making your goals more <strong>{' and '.join([c.lower() for c in weakest_components])}</strong>."
    else:
        weakness_text = "Perfect component identification!"
        feedback_text = "You correctly identified all missing SMART components."
    
    st.markdown(f"""
    <div class="neon-container">
        <div class="results-container">
            <div style="color: #00ffff; font-family: 'Orbitron', monospace; font-size: clamp(1.2rem, 1.6vw, 1.6em); font-weight: 600; margin-bottom: clamp(8px, 1.2vw, 10px);">
                {weakness_text}
            </div>
            <div style="background: rgba(0,255,255,0.1); border: clamp(1px, 0.15vw, 1px) solid rgba(0,255,255,0.3); border-radius: clamp(8px, 1.2vw, 12px); padding: clamp(6px, 1vw, 10px);">
                <div style="color: rgba(255,255,255,0.9); font-family: 'Rajdhani', sans-serif; font-size: clamp(1.1rem, 1.3vw, 1.3em); line-height: 1.4;">
                    feedback_messages = {
                        "Specific": "Make your goals crystal clear. Instead of 'exercise more', say 'do 30 minutes of cardio'. Vague goals lead to vague results.",
                        "Measurable": "Add numbers to track progress. Replace 'save money' with 'save $500'. If you can't measure it, you can't manage it.",
                        "Achievable": "Set realistic targets. Don't aim to 'read 50 books tomorrow' - aim for '1 book per month'. Unrealistic goals kill motivation.",
                        "Relevant": "Connect goals to your bigger purpose. Explain WHY this goal matters to you or your future. Purpose fuels persistence.",
                        "Timebound": "Set clear deadlines. Change 'learn Spanish' to 'learn Spanish by June 2025'. Deadlines create urgency and focus."
                    }
                    
                    if weakest_components:
                        if len(weakest_components) == 1:
                            weakness_text = f"Your weakest area: <strong>{weakest_components[0]}</strong> ({max_error_rate:.0%} missed)"
                            feedback_text = feedback_messages[weakest_components[0]]
                        else:
                            weakness_text = f"Your weakest areas: <strong>{' & '.join(weakest_components)}</strong> ({max_error_rate:.0%} missed)"
                            # Combine feedback for multiple weak areas
                            combined_feedback = " ".join([feedback_messages[comp] for comp in weakest_components])
                            feedback_text = combined_feedback
                    else:
                        weakness_text = "Perfect component identification!"
                        feedback_text = "Excellent work on SMART goal mastery! You correctly identified all missing components."
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 5px;">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 TRY AGAIN", use_container_width=True):
            st.session_state.score = 0
            st.session_state.game_completed = False
            reset_to_question(1)
            st.rerun()
    with col2:
        if st.button("🏠 RETURN TO HOME", use_container_width=True):
            st.session_state.clear()
            st.switch_page("pages/Modules.py")
    st.stop()
