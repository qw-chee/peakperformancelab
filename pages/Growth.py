import streamlit as st
import openai

st.set_page_config(
    page_title="Mindset Growth Garden", 
    layout="centered",
    page_icon="🌱"
)

# Set OpenAI API key
openai.api_key = st.secrets.get("openai_api_key")

# ---------------------------- DATA ----------------------------
QUIZ_QUESTIONS = [
    {"text": "1. Math is much easier to learn if you are male or maybe come from a culture that values math.", "scores": {"Strongly Agree": 0, "Agree": 1, "Disagree": 2, "Strongly Disagree": 3}},
    {"text": "2. You can always substantially change how intelligent you are.", "scores": {"Strongly Agree": 3, "Agree": 2, "Disagree": 1, "Strongly Disagree": 0}},
    {"text": "3. All human beings without a brain injury or birth defect are capable of the same amount of learning.", "scores": {"Strongly Agree": 3, "Agree": 2, "Disagree": 1, "Strongly Disagree": 0}},
    {"text": "4. You are a certain kind of person, and there is not much that can be done to really change that.", "scores": {"Strongly Agree": 0, "Agree": 1, "Disagree": 2, "Strongly Disagree": 3}},
    {"text": "5. Music talent can be learned by anyone.", "scores": {"Strongly Agree": 3, "Agree": 2, "Disagree": 1, "Strongly Disagree": 0}},
    {"text": "6. Truly smart people don't need to try hard.", "scores": {"Strongly Agree": 0, "Agree": 1, "Disagree": 2, "Strongly Disagree": 3}},
    {"text": "7. No matter what kind of person you are, you can always change substantially.", "scores": {"Strongly Agree": 3, "Agree": 2, "Disagree": 1, "Strongly Disagree": 0}},
    {"text": "8. I often get angry when I get feedback about my performance.", "scores": {"Strongly Agree": 0, "Agree": 1, "Disagree": 2, "Strongly Disagree": 3}},
    {"text": "9. The harder you work at something, the better you will be at it.", "scores": {"Strongly Agree": 3, "Agree": 2, "Disagree": 1, "Strongly Disagree": 0}},
    {"text": "10. Your intelligence is something very basic about you that you can't change very much.", "scores": {"Strongly Agree": 0, "Agree": 1, "Disagree": 2, "Strongly Disagree": 3}},
    {"text": "11. You can always change basic things about the kind of person you are.", "scores": {"Strongly Agree": 3, "Agree": 2, "Disagree": 1, "Strongly Disagree": 0}},
    {"text": "12. Trying new things is stressful for me and I avoid it.", "scores": {"Strongly Agree": 0, "Agree": 1, "Disagree": 2, "Strongly Disagree": 3}},
    {"text": "13. Some people are good and kind, some are not – it is not often that people change.", "scores": {"Strongly Agree": 0, "Agree": 1, "Disagree": 2, "Strongly Disagree": 3}},
    {"text": "14. I appreciate when parents, coaches, teachers give me feedback about my performance.", "scores": {"Strongly Agree": 3, "Agree": 2, "Disagree": 1, "Strongly Disagree": 0}},
    {"text": "15. No matter how much intelligence you have, you can always change it quite a bit.", "scores": {"Strongly Agree": 3, "Agree": 2, "Disagree": 1, "Strongly Disagree": 0}},
    {"text": "16. You can do things differently, but the important part of who you are can't really be changed.", "scores": {"Strongly Agree": 0, "Agree": 1, "Disagree": 2, "Strongly Disagree": 3}},
    {"text": "17. Only a few people will be truly good at sports – you have to be \"born with it.\"", "scores": {"Strongly Agree": 0, "Agree": 1, "Disagree": 2, "Strongly Disagree": 3}},
    {"text": "18. Human beings are basically good, but sometimes make terrible decisions.", "scores": {"Strongly Agree": 3, "Agree": 2, "Disagree": 1, "Strongly Disagree": 0}},
    {"text": "19. You can learn new things, but you can't really change how intelligent you are.", "scores": {"Strongly Agree": 0, "Agree": 1, "Disagree": 2, "Strongly Disagree": 3}},
    {"text": "20. An important reason why I do my schoolwork is that I like to learn new things.", "scores": {"Strongly Agree": 3, "Agree": 2, "Disagree": 1, "Strongly Disagree": 0}}
]

MINDSET_RESULTS = {
    "Strong Growth Mindset": {"range": (45, 60), "icon": "🌳", "title": "The Mighty Oak", "subtitle": "Strong Growth Mindset", "description": "Like a strong oak tree with reaching branches, you have embraced growth! You understand that abilities can flourish through effort.", "color": "#59250e"},
    "Growth Mindset with some Fixed Ideas": {"range": (34, 44), "icon": "🌿", "title": "The Growing Sapling", "subtitle": "Growth Mindset with some Fixed Ideas", "description": "Like a sapling reaching toward the sun, you have many growth-oriented beliefs but have some areas where you have a fixed view of ability.", "color": "#59250e"},
    "Fixed Mindset with some Growth Ideas": {"range": (21, 33), "icon": "🌱", "title": "The Sprouting Seed", "subtitle": "Fixed Mindset with some Growth Ideas", "description": "Like a sprouting seed, you currently lean toward a fixed view of ability, but you're starting to develop some growth-oriented beliefs!", "color": "#59250e"},
    "Strong Fixed Mindset": {"range": (0, 20), "icon": "🌰", "title": "The Dormant Seed", "subtitle": "Strong Fixed Mindset", "description": "Your current beliefs lean toward a fixed view of ability, but remember - growth is always possible when the conditions are right.", "color": "#59250e"}
}

RESPONSE_OPTIONS = ["Strongly Disagree", "Disagree", "Agree", "Strongly Agree"]

# ---------------------------- SESSION STATE ----------------------------
def init_session_state():
    defaults = {
        'current_question': 0,
        'total_questions': len(QUIZ_QUESTIONS),
        'responses': {},
        'quiz_completed': False,
        'background_loaded': False,
        'show_results': False,
        'gpt_feedback': None,
        'generating_feedback': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

# ---------------------------- GPT-4 FEEDBACK FUNCTION ----------------------------
def generate_personalized_feedback(responses, mindset_category, total_score):
    """Generate personalized feedback using GPT-4 based on user responses"""
    try:
        # Create a summary of responses for GPT-4
        response_summary = []
        for q_num, response in responses.items():
            question_text = QUIZ_QUESTIONS[q_num - 1]["text"]
            response_summary.append(f"Q{q_num}: {question_text}\nResponse: {response}")
        
        responses_text = "\n\n".join(response_summary)
        
        prompt = f"""
Based on the following growth mindset assessment responses, provide a maximum of 5 specific, actionable recommendations to help nurture a growth mindset. The user scored {total_score}/60 and falls into the category: {mindset_category}.

Assessment Responses:
{responses_text}

Please provide recommendations in the following format:
- Each recommendation should be a complete sentence starting with an action verb, in less than 12 words
- Focus on specific behaviors and mindset shifts
- Make recommendations relevant to their specific responses but don't mention question numbers
- Keep each point concise but actionable
- Use encouraging and supportive language
- Use simple and understandable laymen language

Format your response as a simple list with each recommendation on a new line, starting with a dash (-). Give a maximum of 4 recommendations with a maximum of 9 words each.
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an educational psychologist specializing in growth mindset development. Provide personalized, actionable advice based on assessment responses."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        feedback = response.choices[0].message.content.strip()
        
        # Convert GPT response to HTML list items
        lines = feedback.split('\n')
        html_items = []
        for line in lines:
            line = line.strip()
            if line.startswith('- '):
                html_items.append(f"<li><strong>{line[2:]}</strong></li>")
            elif line and not line.startswith('-'):
                html_items.append(f"<li><strong>{line}</strong></li>")
        
        return "\n".join(html_items)
        
    except Exception as e:
        st.error(f"Error generating personalized feedback: {str(e)}")
        # Fallback to generic recommendations
        return """
        <li><strong>View mistakes as learning opportunities rather than failures</strong></li>
        <li><strong>Focus on the process of learning rather than just the outcome</strong></li>
        <li><strong>Embrace challenges as chances to grow and improve</strong></li>
        <li><strong>Seek feedback actively and use it constructively</strong></li>
        <li><strong>Practice positive self-talk that emphasizes effort and progress</strong></li>
        <li><strong>Celebrate small wins and incremental improvements</strong></li>
        """

# ---------------------------- STYLES ----------------------------
def get_styles():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300;400;500;600;700&family=Comfortaa:wght@300;400;500;600;700&display=swap');

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
        
        /* Full screen background */
        .stApp {
            background-image: url('https://raw.githubusercontent.com/qw-chee/peakperformancelab/main/assets/Growth.gif');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            min-height: 100vh;
            position: relative;
        }
          
        .nature-container {
            background: rgba(255, 255, 255, 0.95);
            border: clamp(2px, 0.3vw, 3px) solid #59250e;
            border-radius: clamp(15px, 2vw, 20px);
            padding: clamp(7px, 0.9vw, 9px);
            margin: clamp(9px, 1.4vh, 14px) 0;
            position: relative;
            backdrop-filter: blur(8px);
            box-shadow: 0 8px 32px rgba(255, 161, 102, 0.2), inset 0 0 20px rgba(255, 161, 102, 0.1);
        }
        
        .nature-container::before {
            content: '';
            position: absolute;
            top: -5px;
            left: -5px;
            right: -5px;
            bottom: -5px;
            background: white;
            border-radius: clamp(18px, 2.3vw, 23px);
            z-index: -1;
            opacity: 0.3;
        }
        
        .growth-title {
            font-family: 'Fredoka', cursive;
            font-weight: 700;
            font-size: clamp(2rem, 4vw, 5rem);
            color: #59250e;
            text-align: center;
            margin-bottom: clamp(5px, 1vh, 10px);
            text-shadow: 2px 2px 4px rgba(255, 161, 102, 0.2);
            line-height: 1.1;
        }
        
        .leaf-subtitle {
            font-family: 'Comfortaa', cursive;
            font-size: clamp(1rem, 1.8vw, 3rem);
            color: #32CD32;
            text-align: center;
            margin-bottom: clamp(15px, 2vh, 20px);
            font-weight: 500;
            text-shadow: 1px 1px 2px rgba(50, 205, 50, 0.2);
        }
        
        .nature-text {
            font-family: 'Comfortaa', cursive;
            display: block;
            color: #08692d;
            font-size: clamp(0.8rem, 1.1vw, 1.2rem);
            line-height: 1.1;
            text-align: center;
            margin-bottom: 0.8em;
        }
        
        .question-container {
            background: rgba(255, 255, 255, 0.9);
            border: clamp(2px, 0.3vw, 3px) solid #9ACD32;
            border-radius: clamp(15px, 2vw, 20px);
            padding: clamp(20px, 3vh, 30px);
            margin: clamp(20px, 2.5vh, 25px) 0;
            position: relative;
            box-shadow: 0 8px 25px rgba(154, 205, 50, 0.2);
        }
        
        .question-text {
            font-family: 'Comfortaa', cursive;
            font-size: clamp(1rem, 1.5vw, 1.3rem);
            color: #2E8B57;
            line-height: 1.6;
            margin: 0;
            text-align: center;
            font-weight: 500;
        }
        
        .response-grid {
            display: grid !important;
            grid-template-columns: 1fr 1fr !important;
            gap: clamp(10px, 1.5vw, 15px) !important;
            margin: clamp(20px, 2.5vh, 25px) 0 !important;
            width: 100% !important;
        }
        
        .response-option {
            background: rgba(255, 255, 255, 0.8);
            border: clamp(2px, 0.3vw, 3px) solid #32CD32;
            border-radius: clamp(12px, 1.5vw, 15px);
            padding: clamp(15px, 2vh, 20px);
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Fredoka', cursive;
            font-weight: 500;
            font-size: clamp(0.9rem, 1.2vw, 2rem);
            color: #59250e;
            position: relative;
            overflow: hidden;
        }
        
        .response-option::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(124, 252, 0, 0.3), transparent);
            transition: left 0.5s ease;
        }
        
        .response-option:hover {
            background: rgba(124, 252, 0, 0.2);
            border-color: #7CFC00;
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 8px 25px rgba(124, 252, 0, 0.3);
        }
        
        .response-option:hover::before {
            left: 100%;
        }
        
        .results-container {
            text-align: center;
            padding: clamp(8px, 1vw, 10px);
        }
        
        .result-icon {
            font-size: clamp(0.8rem, 2.5vw, 4rem);
            margin-bottom: clamp(-8px, -1vh, -10px);
            display: block;
            animation: bounce-grow 2s ease-in-out infinite;
        }
        
        @keyframes bounce-grow {
            0%, 100% { transform: scale(1) rotate(0deg); }
            50% { transform: scale(1.1) rotate(5deg); }
        }
        
        .result-title {
            font-family: 'Fredoka' !important;
            font-weight: 700;
            font-size: clamp(0.6rem, 1.5vw, 4rem);
            margin-bottom: clamp(-40px, -2.5vh, -20px);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .result-description {
            font-family: 'Comfortaa', cursive;
            font-size: clamp(0.9rem, 1.2vw, 1.1rem);
            line-height: 1.2;
            margin-bottom: 0px;
            text-align: left;
            font-weight: 400;
        }
        
        .loading-feedback {
            text-align: center;
            padding: clamp(15px, 2vh, 20px);
            font-family: 'Comfortaa', cursive;
            color: #2E8B57;
            font-size: clamp(0.9rem, 1.2vw, 2rem);
        }
        
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #32CD32;
            border-radius: 50%;
            width: clamp(30px, 4vw, 40px);
            height: clamp(30px, 4vw, 40px);
            animation: spin 1s linear infinite;
            margin: 0 auto clamp(12px, 1.5vh, 15px) auto;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Main buttons (not radio options) */
        div[data-testid="stButton"] > button:not([data-testid*="response_"]) {
            background: linear-gradient(135deg, #e6733c 0%, #f2a93b 50%, #f6d860 100%) !important;
            border: clamp(2px, 0.3vw, 3px) solid #FF6347 !important;
            color: white !important;
            font-weight: 600 !important;
            font-size: clamp(1rem, 1.2vw, 1.4rem) !important;
            font-family: 'Fredoka', cursive !important;
            padding: clamp(12px, 1.5vh, 15px) clamp(25px, 3vw, 30px) !important;
            border-radius: clamp(20px, 2.5vw, 25px) !important;
            box-shadow: 0 6px 20px rgba(34, 139, 34, 0.3) !important;
            transition: all 0.3s ease !important;
            text-transform: none !important;
            letter-spacing: 0.5px !important;
            width: 100% !important;
        }

        div[data-testid="stButton"] > button:not([data-testid*="response_"]):hover {
            background: linear-gradient(135deg, #FF8C00 0%, #FFD700 50%, #FFFF00 100%) !important;
            transform: translateY(-3px) scale(1.05) !important;
            box-shadow: 0 8px 30px rgba(50, 205, 50, 0.4) !important;
            border-color: #FF8C00 !important;
        }

        div[data-testid="stButton"] > button[kind="primary"] {
            background: linear-gradient(135deg, #e6733c 0%, #f2a93b 50%, #f6d860 100%) !important;
            border-color: #FF6347 !important;
            animation: sunny-glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes sunny-glow {
            0% { box-shadow: 0 6px 20px rgba(255, 99, 71, 0.3); }
            100% { box-shadow: 0 8px 30px rgba(255, 140, 0, 0.5); }
        }

        div[data-testid="stButton"] > button[kind="primary"]:hover {
            background: linear-gradient(135deg, #FF8C00 0%, #FFD700 50%, #FFFF00 100%) !important;
            border-color: #FF8C00 !important;
        }
             
        div[data-testid="stRadio"] > div[role="radiogroup"] {
            display: grid !important;
            grid-template-columns: 1fr 1fr !important;
            gap: 15px !important;
            margin: 25px 0 !important;
        }
        
        div[data-testid="stRadio"] > div[role="radiogroup"] > label {
            border-radius: 15px !important;
            padding: 5px !important;
            margin: 0 !important;
            display: flex !important;  /* Add this */
            align-items: center !important;
            justify-content: center !important;
            cursor: pointer !important;
            transition: all 0.3s ease !important;
            font-family: 'Fredoka', cursive !important;
            font-weight: 600 !important;
            font-size: clamp(0.9rem, 1.2vw, 1.4rem) !important;
            color: white !important;
            text-align: center !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
            border: 2px solid !important;
            width: 100% !important;  /* Add this */
            min-width: 0 !important;  /* Add this */
            flex-grow: 1 !important;  /* Add this */
            box-sizing: border-box !important;  /* Add this */
        }
        
        div[data-testid="stRadio"] > div[role="radiogroup"] > label:nth-child(1) {
            background: rgba(153, 21, 21, 0.9) !important;
            border-color: #FF6347 !important;
        }
        
        div[data-testid="stRadio"] > div[role="radiogroup"] > label:nth-child(2) {
            background: rgba(255, 157, 0, 0.9) !important;
            border-color: #FFA500 !important;
        }
        
        div[data-testid="stRadio"] > div[role="radiogroup"] > label:nth-child(3) {
            background: rgba(11, 176, 90, 0.9) !important;
            border-color: #1bf282 !important;
        }
        
        div[data-testid="stRadio"] > div[role="radiogroup"] > label:nth-child(4) {
            background: rgba(7, 135, 61, 0.9) !important;
            border-color: #0bb05a !important;
        }
        
        div[data-testid="stRadio"] > div[role="radiogroup"] > label:hover {
            transform: translateY(-2px) scale(1.02) !important;
            box-shadow: 0 6px 20px rgba(0,0,0,0.3) !important;
        }
        
        div[data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) {
            transform: scale(1.05) !important;
            box-shadow: 0 8px 25px rgba(0,0,0,0.4) !important;
            opacity: 1 !important;
            font-weight: 700 !important;
        }
        
        div[data-testid="stRadio"] > div[role="radiogroup"] > label > div:first-child {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            position: absolute !important;
            left: -9999px !important;
        }
        
        div[data-testid="stRadio"] > div[role="radiogroup"] > label > div:last-child,
        div[data-testid="stRadio"] > div[role="radiogroup"] > label > div:last-child > *,
        div[data-testid="stRadio"] > div[role="radiogroup"] > label * {
            color: white !important;
            font-family: 'Fredoka', cursive !important;
            font-weight: 600 !important;
            font-size: 1.1em !important;
            text-align: center !important;
        }
        
        div[data-testid="stRadio"] input[type="radio"] {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
        }
        
        ::-webkit-scrollbar {
            width: clamp(8px, 1vw, 12px);
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(34, 139, 34, 0.1);
            border-radius: 6px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, #59250e, #32CD32);
            border-radius: 6px;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(45deg, #32CD32, #7CFC00);
        }
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
    </style>
    """

st.markdown(get_styles(), unsafe_allow_html=True)

# ---------------------------- HELPER FUNCTIONS ----------------------------
def calculate_total_score():
    total = 0
    for q_num, response in st.session_state.responses.items():
        total += QUIZ_QUESTIONS[q_num - 1]["scores"][response]
    return total

def get_mindset_result(score):
    for category, data in MINDSET_RESULTS.items():
        if data["range"][0] <= score <= data["range"][1]:
            return category, data
    return "Unknown", {}

def reset_quiz(to_start=False):
    keys_to_reset = ['current_question', 'responses', 'quiz_completed', 'show_results', 'gpt_feedback', 'generating_feedback']
    for key in keys_to_reset:
        if key in st.session_state:
            del st.session_state[key]
    st.session_state.current_question = 1 if to_start else 0
    st.session_state.responses = {}
    st.session_state.quiz_completed = False
    st.session_state.show_results = False
    st.session_state.gpt_feedback = None
    st.session_state.generating_feedback = False

# ---------------------------- LOADING OVERLAY ----------------------------
st.markdown("""
    <div id="loading-overlay">
        <div class="loading-content">
            <div class="loading-title">🌱 Planting Your Garden...</div>
            <div class="loading-bar-container">
                <div class="loading-bar"></div>
            </div>
            <div class="loading-subtitle">Growing your mindset discovery experience</div>
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
            background: linear-gradient(135deg, #539429 0%, #3b7a12 50%, #265706 100%);
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
            font-family: 'Fredoka', cursive;
            font-size: clamp(2rem, 4vw, 3.5rem);
            font-weight: 700;
            color: white;
            margin-bottom: clamp(15px, 2vh, 20px);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            animation: grow-bounce 2s ease-in-out infinite;
        }

        .loading-bar-container {
            width: clamp(250px, 30vw, 300px);
            height: clamp(6px, 1vh, 8px);
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
            background: linear-gradient(90deg, white, #FFFF00);
            border-radius: 4px;
            animation: loading-bar 2s ease-in-out infinite;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.8);
        }

        .loading-subtitle {
            font-family: 'Comfortaa', cursive;
            color: rgba(255, 255, 255, 0.9);
            margin-top: clamp(12px, 1.5vh, 15px);
            font-size: clamp(1rem, 1.5vw, 1.3rem);
            font-weight: 500;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }

        @keyframes grow-bounce {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
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
            document.body.innerHTML = '<div style="display: flex; justify-content: center; align-items: center; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: linear-gradient(135deg, #539429 0%, #3b7a12 50%, #265706 100%); color: white; font-size: 1.5rem; text-align: center; font-family: Fredoka, cursive;">This application is designed for desktop and laptop screens only.</div>';
        }
    });
}
</script>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
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

# ---------------------------- MAIN APP LOGIC ----------------------------
# OVERVIEW PAGE
if st.session_state.current_question == 0 and not st.session_state.quiz_completed:
    st.markdown("""
    <div class="nature-container">
        <h3 style="color: #59250e; font-family: 'Fredoka', cursive; font-size: 1.5em; margin-bottom: -5px; text-align: center;">
            🌱 Mindset Growth Garden
        </h3>
        <div class="nature-text">
            A <strong>growth mindset</strong> is the belief that your abilities and talents can bloom and flourish through dedication, hard work, and learning from mistakes. 
        </div>
        <div class="nature-text">
            In contrast, a <strong>fixed mindset</strong> is like believing a seed can never become a flower - that our intelligence, creativity, and character cannot change. 
            <br>
        </div>
        <div class="nature-text">
            This questionnaire will help you explore your current beliefs about ability, learning, and personal development. Your responses will help reveal your current mindset and show you the path toward even more growth.
        </div>
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("""
    <div class="nature-container">
        <h3 style="color: #59250e; font-family: 'Fredoka', cursive; font-size: 1.5em; margin-bottom: -5px; text-align: center;">
            ✨ How to Respond
        </h3>
        <div class="nature-text">
            You'll read 20 statements about learning and ability. Take your time for each statement, then click on the option that best matches how you truly feel:
        </div>
        <div style="margin: -10px 0 -20px 0;">
            <div class="response-grid">
                <div style="background: rgba(153, 21, 21, 0.8); border: 2px solid #FF6347; border-radius: 15px; padding: 5px; text-align: center; font-family: 'Fredoka', cursive; font-weight: 600; color: white;">
                    Strongly Disagree
                </div>
                <div style="background: rgba(255, 157, 0, 0.8); border: 2px solid #FFA500; border-radius: 15px; padding: 5px; text-align: center; font-family: 'Fredoka', cursive; font-weight: 600; color: white;">
                    Disagree
                </div>
                <div style="background: rgba(11, 176, 90, 0.8); border: 2px solid #1bf282; border-radius: 15px; padding: 5px; text-align: center; font-family: 'Fredoka', cursive; font-weight: 600; color: white; margin-top: -5px;">
                    Agree
                </div>
                <div style="background: rgba(7, 135, 61, 0.8); border: 2px solid #0bb05a; border-radius: 15px; padding: 5px; text-align: center; font-family: 'Fredoka', cursive; font-weight: 600; color: white; margin-top: -5px;">
                    Strongly Agree
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🌱 Start Growing Your Garden!", use_container_width=True, type="primary"):
        st.session_state.current_question = 1
        st.rerun()

# QUIZ QUESTIONS
elif 1 <= st.session_state.current_question <= st.session_state.total_questions and not st.session_state.quiz_completed:
    st.markdown("<div style='height: 10vh;'></div>", unsafe_allow_html=True)
    
    current_question = QUIZ_QUESTIONS[st.session_state.current_question - 1]
    
    st.markdown(f"""
    <div class="question-container">
        <div class="question-text">{current_question['text']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    selected_response = st.radio(
        "Choose your response:",
        RESPONSE_OPTIONS,
        index=None,
        label_visibility="collapsed",
        key=f"radio_{st.session_state.current_question}"
    )
    
    if selected_response:
        st.session_state.responses[st.session_state.current_question] = selected_response
        
        if st.session_state.current_question < st.session_state.total_questions:
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.session_state.quiz_completed = True
            st.session_state.show_results = False  # Don't show results yet
            st.session_state.current_question = 999  # Clear question state
            st.rerun()

# LOADING FEEDBACK PAGE
elif st.session_state.quiz_completed and not st.session_state.show_results:
    # Clear screen with full viewport container
    st.markdown("""
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(255, 255, 255, 0.98); z-index: 1000; display: flex; align-items: center; justify-content: center;">
        <div class="nature-container" style="margin: 0; padding: 40px;">
            <div class="loading-feedback">
                <div class="spinner"></div>
                Generating your personalized growth recommendations...
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate feedback
    total_score = calculate_total_score()
    mindset_category, result_data = get_mindset_result(total_score)
    feedback = generate_personalized_feedback(st.session_state.responses, mindset_category, total_score)
    st.session_state.gpt_feedback = feedback
    st.session_state.show_results = True
    st.rerun()
    
# RESULTS PAGE
elif st.session_state.quiz_completed and st.session_state.show_results:
    total_score = calculate_total_score()
    mindset_category, result_data = get_mindset_result(total_score)
    
    st.markdown(f"""
    <div class="nature-container">
        <div class="results-container">
            <span class="result-icon">{result_data['icon']}</span>
            <h3 class="result-title" style="color: {result_data['color']}; margin-bottom: -15px;">{result_data['title']}</h2>
            <h4 class="result-title" style="color: {result_data['color']};">{result_data['subtitle']}</h3>
            <div class="result-description" style="color: #6e3f09;">
                {result_data['description']}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="nature-container">
        <div class="result-description" style="color: #6e3f09; padding: 10px 15px 10px 10px;">
            Based on your responses, here are some ways you can nurture your growth mindset:
        </div>
        <div class="result-description" style="color: #2E8B57; padding: 0 15px 5px 10px;">
            <ul style="padding-left: 10px; margin: 10px 0;">
                {st.session_state.gpt_feedback}
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Try Again", use_container_width=True):
            reset_quiz(to_start=True)
            st.rerun()
    
    with col2:
        if st.button("🏡 Return to Home", use_container_width=True):
            st.switch_page("pages/Modules.py")

st.markdown(
    """
    <style>
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
