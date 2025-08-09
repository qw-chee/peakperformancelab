import streamlit as st
import openai

openai.api_key = st.secrets.get("openai_api_key")

# ---------------------------- SCENARIOS ----------------------------
SCENARIOS = {
    "Soccer Penalty Kick": {
        "icon": "⚽",
        "description": "Perfect your soccer performance through mental rehearsal"
    },
    "Public Speaking": {
        "icon": "🎤",
        "description": "Master your presentation skills through vivid mental practice"
    },
    "Exam Hall": {
        "icon": "📝",
        "description": "Prepare for exam success through mental rehearsal"
    }
}

# ---------------------------- PETTLEP ELEMENTS ----------------------------
def get_pettlep_elements(scenario):
    """Get PETTLEP elements with scenario-specific challenges"""
    
    # Define scenario-specific challenges
    challenges = {
        "Soccer Penalty Kick": {
            "🏃 Physical": {
                "question": "Which best describes the Physical element for a penalty kick?",
                "options": [
                    "I'm wearing my team jersey, soccer cleats, and shin guards, with the ball at my feet.",
                    "I hear the crowd cheering and the referee's whistle blowing.",
                    "I feel confident and focused on scoring the winning goal."
                ],
                "correct": 0
            },
            "🌟 Environment": {
                "question": "Which is most Environment-focused for a penalty kick?",
                "options": [
                    "I'm dribbling the ball past defenders with quick footwork.",
                    "I can see the green field, hear fans chanting, and smell the fresh grass.",
                    "I'm wearing my lucky cleats and team captain's armband."
                ],
                "correct": 1
            },
            "⚡ Task": {
                "question": "Which best describes the Task element in a penalty kick?",
                "options": [
                    "I'm standing on the penalty spot in my team uniform.",
                    "The stadium lights are bright and I can hear my teammates.",
                    "I take three steps back, run up, and strike the ball into the top corner."
                ],
                "correct": 2
            },
            "⏱️ Timing": {
                "question": "Which represents Timing in a penalty kick?",
                "options": [
                    "I feel pumped up and ready to dominate the game.",
                    "I control my run-up pace, then accelerate smoothly through the kick.",
                    "I'm wearing my favorite cleats on the perfectly marked field."
                ],
                "correct": 1
            },
            "📚 Learning": {
                "question": "Which shows the Learning element in a penalty kick?",
                "options": [
                    "I hear the crowd roaring as I approach the goal.",
                    "I'm sprinting at full speed down the sideline.",
                    "I focus on keeping my head up while dribbling, as coach taught me."
                ],
                "correct": 2
            },
            "💝 Emotion": {
                "question": "Which best represents Emotion in a penalty kick?",
                "options": [
                    "I'm executing a perfect through-pass to my teammate.",
                    "I feel the adrenaline and excitement, staying calm under pressure.",
                    "I'm wearing my team colors on the home field."
                ],
                "correct": 1
            },
            "👁️ Perspective": {
                "question": "Which shows the Perspective element in a penalty kick?",
                "options": [
                    "I feel nervous but channel it into focused energy.",
                    "I see through my own eyes as I line up the penalty shot.",
                    "I hear my coach shouting tactical instructions."
                ],
                "correct": 1
            }
        },
        "Public Speaking": {
            "🏃 Physical": {
                "question": "Which best describes the Physical element for public speaking?",
                "options": [
                    "I'm standing confidently at the podium, wearing my best suit, holding my notes.",
                    "I can see the audience's attentive faces and hear the microphone feedback.",
                    "I feel nervous but excited to share my important message."
                ],
                "correct": 0
            },
            "🌟 Environment": {
                "question": "Which is most Environment-focused for public speaking?",
                "options": [
                    "I'm gesturing naturally while making eye contact with the audience.",
                    "I see the conference room, hear the projector humming, and smell coffee.",
                    "I'm holding my presentation clicker and wearing professional attire."
                ],
                "correct": 1
            },
            "⚡ Task": {
                "question": "Which describes the Task element in public speaking?",
                "options": [
                    "I'm standing behind the lectern in my professional outfit.",
                    "I can see friendly faces in the audience nodding along.",
                    "I click to the next slide, pause for emphasis, and deliver my key point clearly."
                ],
                "correct": 2
            },
            "⏱️ Timing": {
                "question": "Which represents Timing in public speaking?",
                "options": [
                    "I feel confident and prepared to engage my audience.",
                    "I speak at a measured pace, pausing strategically for impact.",
                    "I'm holding my presentation remote in the well-lit room."
                ],
                "correct": 1
            },
            "📚 Learning": {
                "question": "Which shows the Learning element in public speaking?",
                "options": [
                    "I focus on maintaining eye contact, something I've been practicing.",
                    "I hear the audience laughing at my opening joke.",
                    "I'm delivering my conclusion with perfect timing."
                ],
                "correct": 0
            },
            "💝 Emotion": {
                "question": "Which best represents Emotion in public speaking?",
                "options": [
                    "I'm advancing through my slides with smooth transitions.",
                    "I'm standing tall at the podium with good posture.",
                    "I feel excited to share my ideas, managing any nerves with deep breathing."
                ],
                "correct": 2
            },
            "👁️ Perspective": {
                "question": "Which shows the Perspective element in public speaking?",
                "options": [
                    "I feel the spotlight warming my face as I speak.",
                    "I see myself from the audience's view, looking confident and engaging.",
                    "I hear applause echoing through the auditorium."
                ],
                "correct": 1
            }
        },
        "Exam Hall": {
            "🏃 Physical": {
                "question": "Which best describes the Physical element for an exam?",
                "options": [
                    "I'm sitting upright in my chair, holding my favorite pen, wearing comfortable clothes.",
                    "I can see rows of desks and hear the clock ticking on the wall.",
                    "I feel calm and confident about my preparation."
                ],
                "correct": 0
            },
            "🌟 Environment": {
                "question": "Which is most Environment-focused for an exam?",
                "options": [
                    "I'm writing my answers clearly and checking my work carefully.",
                    "I see the quiet exam hall, hear pencils scratching, and feel the cool air.",
                    "I'm holding my lucky pen and wearing my comfortable exam outfit."
                ],
                "correct": 1
            },
            "⚡ Task": {
                "question": "Which describes the Task element in an exam?",
                "options": [
                    "I'm sitting at my assigned desk with my student ID displayed.",
                    "I can see the supervising teacher walking quietly between rows.",
                    "I read each question carefully, plan my answer, then write clearly and concisely."
                ],
                "correct": 2
            },
            "⏱️ Timing": {
                "question": "Which represents Timing in an exam?",
                "options": [
                    "I feel prepared and ready to demonstrate my knowledge.",
                    "I pace myself steadily, spending appropriate time on each question.",
                    "I'm writing with my favorite pen in the silent exam room."
                ],
                "correct": 1
            },
            "📚 Learning": {
                "question": "Which shows the Learning element in exams?",
                "options": [
                    "I apply the study techniques I've been practicing all semester.",
                    "I hear the invigilator announcing time remaining.",
                    "I'm working through the multiple choice section systematically."
                ],
                "correct": 0
            },
            "💝 Emotion": {
                "question": "Which best represents Emotion in exams?",
                "options": [
                    "I'm writing my final answer and reviewing my work.",
                    "I'm sitting in the middle row of the examination hall.",
                    "I feel focused and calm, breathing deeply to stay relaxed."
                ],
                "correct": 2
            },
            "👁️ Perspective": {
                "question": "Which shows the Perspective element in exams?",
                "options": [
                    "I feel the smooth pen gliding across the paper.",
                    "I see through my own eyes as I read the questions and formulate answers.",
                    "I hear other students turning pages around me."
                ],
                "correct": 1
            }
        }
    }
    
    base_elements = [
        {
            "name": "🏃 Physical",
            "letter": "P",
            "lesson": "This element refers to the physical sensations and movements involved in the actual performance. It includes things like posture, muscle activation, breathing patterns, facial expressions, and even clothing or equipment. The idea is to replicate the physical conditions as closely as possible during imagery. Engaging these bodily details makes the mental rehearsal more lifelike and connected to real execution.",
            "example": "Example: 'I'm holding my tennis racket with both hands and bouncing slightly on the balls of my feet.'",
            "elaboration_questions": [
                "How is your body positioned?",
                "What physical sensations do you feel (weight, texture, temperature)?"
            ]
        },
        {
            "name": "🌟 Environment",
            "letter": "E",
            "lesson": "This element describes the surrounding context where the performance takes place. It involves imagining the setting’s layout, colors, lighting, temperature, sounds, and even smells. The environment could include specific objects, people, or landmarks that are usually present. Recreating the environment in detail helps your brain anchor the imagery in a familiar setting.",
            "example": "Example: 'I hear the whistle blow, smell the grass, and see the sun glare off the white lines of the field.'",
            "elaboration_questions": [
                "What do you see around you in detail?",
                "What sounds do you hear?",
                "Are there any smells or temperature sensations?",
                "Who else is present in your environment?"
            ]
        },
        {
            "name": "⚡ Task",
            "letter": "T",
            "lesson": "This element refers to the exact activity being mentally rehearsed. It involves the technical components of the skill, such as movement sequences, decisions, and required focus. The task should match what you actually needs to perform, whether it's simple or complex. This includes both the motor and cognitive demands of the action.",
            "example": "Example: 'I bounce the ball twice, bend my knees, and release the shot smoothly.'",
            "elaboration_questions": [
                "What specific actions are you performing step by step?",
                "What is the sequence of your movements?",
                "How are you executing each part of the skill?"
            ]
        },
        {
            "name": "⏱️ Timing",
            "letter": "T",
            "lesson": "This element describes the need to match the real duration and pace of the performance. It involves imagining the action in real time, with accurate rhythm, tempo, and transition speeds. Timing also includes pauses, reaction times, or sequences that are part of the performance flow. The mental timing should reflect how the task unfolds naturally.",
            "example": "Example: 'I take a slow, deliberate approach, then accelerate quickly through the swing.'",
            "elaboration_questions": [
                "How fast or slow are you moving?",
                "Is there a specific rhythm or pace to follow?",
                "Are there moments where you pause or accelerate?"
            ]
        },
        {
            "name": "📚 Learning",
            "letter": "L",
            "lesson": "This element refers to your current level of skill or stage of development. It involves adjusting the imagery content to reflect what you can actually do or are currently working on. For beginners, the focus might be on fundamental steps, while advanced individuals might include automatic or refined techniques. The imagery should evolve as you progress.",
            "example": "Example: 'I focus on keeping my follow-through consistent, which I've been working on in practice.'",
            "elaboration_questions": [
                "What specific aspect are you trying to improve?",
                "What corrections or refinements are you making?"
            ]
        },
        {
            "name": "💝 Emotion",
            "letter": "E",
            "lesson": "This element describes the emotional states typically experienced during the activity. It involves mentally recreating feelings like excitement, anxiety, frustration, determination, or confidence. The intensity and type of emotion should reflect what’s usually felt during real performance. This also includes how the body physically responds to those emotions.",
            "example": "Example: 'I feel calm and focused, with a surge of excitement as I prepare to perform.'",
            "elaboration_questions": [
                "How are you feeling during this performance?",
                "What positive emotions do you experience?",
                "How do you handle any nervousness or pressure?"
            ]
        },
        {
            "name": "👁️ Perspective",
            "letter": "P",
            "lesson": "This element refers to the viewpoint from which the imagery is experienced. It involves choosing between a first-person perspective (seeing through your own eyes) or a third-person perspective (watching yourself as if from the outside). The choice affects what details are included, such as visual angles, body awareness, or spatial relationships. It is possible to switch between perspectives depending on the focus of your imagery.",
            "example": "Example: 'I see through my own eyes as I grip the bat and watch the ball approach.'",
            "elaboration_questions": [
                "Why does this viewpoint help you?",
                "What can you see from this perspective that helps your performance?"
            ]
        }
    ]
    
    # Add scenario-specific challenge data to each element
    for element in base_elements:
        element_name = element["name"]
        if scenario in challenges and element_name in challenges[scenario]:
            challenge = challenges[scenario][element_name]
            element["challenge_question"] = challenge["question"]
            element["options"] = challenge["options"]
            element["correct_index"] = challenge["correct"]
    
    return base_elements

# ---------------------------- SESSION STATE INIT ----------------------------
def init_session_state():
    defaults = {
        'current_step': 0,  # 0 = overview, 1-7 = PETTLEP elements, 8 = final script
        'selected_scenario': None,
        'responses': {},
        'gpt_approved': {},
        'gpt_feedback': {},
        'challenge_passed': {},
        'selected_option': {},
        'elaboration_mode': {},  # New: track if in elaboration mode
        'background_loaded': False,
        'script_generated': False,
        'complete_script': "",
        'generating_script': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

# ---------------------------- GPT FUNCTIONS ----------------------------
def get_gpt_feedback(element_name, user_response, scenario):
    """Get GPT feedback on user's imagery description"""
    try:
        # Get the elaboration questions for this element
        element_data = None
        for elem in get_pettlep_elements(scenario):
            if elem['name'] == element_name:
                element_data = elem
                break
        
        questions_text = ""
        if element_data and 'elaboration_questions' in element_data:
            questions_text = "\n".join([f"- {q}" for q in element_data['elaboration_questions']])
        
        prompt = f"""You are a sports psychology expert evaluating a user's mental imagery description for the {element_name} element of PETTLEP imagery.
        
        Scenario: {scenario}
        Element Questions to Address:
        {questions_text}
        
        User's Response: "{user_response}"
        
        APPROVE the response if it addresses the key questions above with specific details, even if brief. ONLY reject if the response is too vague, doesn't address the questions, or lacks vivid imagery details.
        
        Provide feedback in this exact format:
        
        APPROVED: [YES/NO]
        FEEDBACK: [If NO, explain what questions weren't addressed in around 40 words. If YES, provide brief positive reinforcement in around 40 words.]"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a sports psychology expert specializing in PETTLEP imagery training. Provide constructive feedback to help users create vivid, detailed mental rehearsals."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        content = response.choices[0].message.content.strip()
        
        # Parse response
        approved = "YES" in content.split("APPROVED:")[1].split("FEEDBACK:")[0].strip()
        feedback_text = content.split("FEEDBACK:")[1].strip()
        
        return approved, feedback_text
        
    except Exception as e:
        st.error(f"Error getting feedback: {str(e)}")
        return False, "Unable to provide feedback at this time. Please continue with your description."

def generate_complete_script(scenario, selected_options, user_responses):
    """Generate a complete PETTLEP imagery script using GPT"""
    try:
        # Build the prompt with all user data
        prompt = f"""You are a sports psychology expert creating a complete PETTLEP imagery script for mental rehearsal.

Scenario: {scenario}

The user has completed all 7 PETTLEP elements with the following information:

"""
        
        PETTLEP_ELEMENTS = get_pettlep_elements(scenario)
        for element in PETTLEP_ELEMENTS:
            element_name = element['name']
            selected_option = selected_options.get(element_name, "")
            user_elaboration = user_responses.get(element_name, "")
            
            prompt += f"{element_name}:\n"
            prompt += f"- Base answer: {selected_option}\n"
            prompt += f"- User elaboration: {user_elaboration}\n\n"

        prompt += """Create a complete, flowing imagery script that integrates all these elements into one cohesive mental rehearsal. The script should:

1. Be written in first person ("I")
2. Be vivid and detailed
3. Include all PETTLEP elements seamlessly woven together
4. Be specific to the scenario

Write the script as one continuous narrative without section headers. Make it feel like a mental rehearsal that the user can follow. Use simple words and language. Write in 200 words or less."""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a sports psychology expert who creates vivid, detailed PETTLEP imagery scripts for mental rehearsal training."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        st.error(f"Error generating script: {str(e)}")
        return f"Unable to generate complete script at this time. Please use your individual responses for mental rehearsal.\n\nScenario: {scenario}\n\nYour responses:\n" + "\n".join([f"{k}: {v}" for k, v in user_responses.items()])

# ---------------------------- STYLES ----------------------------
def get_movie_styles():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sigmar&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
    
    .stApp {
        background-image: url('https://www.dropbox.com/scl/fi/1ltb3xhk32nr1rp08qm30/imagery-1.jpg?rlkey=5encz1ynf5p9o96ndyd5j9e8o&st=ehpd3unf&raw=1');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        min-height: 100vh;
    }
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.7) 0%, rgba(139, 69, 19, 0.3) 25%, rgba(255, 215, 0, 0.2) 50%, rgba(255, 0, 0, 0.3) 75%, rgba(0, 0, 0, 0.8) 100%);
        z-index: -1;
        pointer-events: none;
    }
    
    .movie-container {
        background: rgba(0, 0, 0, 0.85);
        border: 3px solid #FFD700;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.3), inset 0 0 30px rgba(255, 215, 0, 0.1);
    }
      
    .movie-text {
        font-family: 'Lato', sans-serif;
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1em;
        line-height: 1.4;
        margin-bottom: 5px;
        font-weight: 300;
    }
    
    .element-title {
        font-family: 'Sigmar', cursive;
        font-size: 2.5em;
        color: #FFD700 !important;
        text-align: center;
        margin-bottom: 20px;
        letter-spacing: 2px;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
    }
    
    .example-text {
        font-style: italic;
        font-size: 1.1em;
        color: rgba(255, 255, 255, 0.8);
        background: rgba(255, 215, 0, 0.1);
        padding: 10px;
        border-left: 3px solid #FFD700;
        border-radius: 5px;
        margin: 15px 0;
    }
      
    .challenge-title {
        font-family: 'Sigmar', cursive;
        color: white !important;
        font-size: 1.5em;
        margin-top: 5px;
        margin-bottom: 10px;
        text-align: center;
    }
    
    .elaboration-container {
        background: black;
        border: 3px solid #32CD32;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        margin-bottom: -20px;
    }
    
    .elaboration-title {
        font-family: 'Sigmar', cursive;
        color: #32CD32;
        font-size: 1.3em;
        margin-bottom: 5px;
    }
    
    .feedback-container {
        background: rgba(255, 215, 0, 0.1);
        border: 2px solid #FFD700;
        border-radius: 12px;
        padding: 20px;
        margin: 5px 0;
        backdrop-filter: blur(5px);
    }
    
    .feedback-approved {
        border-color: #32CD32;
        background: rgba(50, 205, 50, 0.1);
    }
    
    .feedback-needs-work {
        border-color: #FF6347;
        background: rgba(255, 99, 71, 0.1);
    }
    
    .script-container {
        background: rgba(0, 0, 0, 0.9);
        border: 3px solid #FFD700;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 40px rgba(255, 215, 0, 0.3);
    }
    

    .script-text {
        font-family: 'Lato', sans-serif;
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.2;
        font-size: 1.2em;
        text-align: justify;
    }

    /* Text area styling */
    div[data-testid="stTextArea"] textarea {
        background: white !important;
        border: 2px solid #FFD700 !important;
        border-radius: 10px !important;
        color: #000000 !important;
        font-family: 'Lato', sans-serif !important;
        font-size: 1.1em !important;
    }
    
    div[data-testid="stTextArea"] textarea:focus {
        border-color: #FF6347 !important;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.4) !important;
    }
    
    /* Radio button styling */
    .stRadio * {
        color: rgba(255, 255, 255, 0.9) !important;
        font-family: 'Lato', sans-serif !important;
        font-size: 1em !important;
    }

    /* Button styling */
    div[data-testid="stButton"] > button[kind="primary"] {
        background: linear-gradient(135deg, #FFD700 0%, #FF6347 50%, #FFD700 100%) !important;
        border: 2px solid #FFD700 !important;
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 1.2em !important;
        font-family: 'Sigmar', cursive !important;
        padding: 15px 30px !important;
        border-radius: 25px !important;
        box-shadow: 0 5px 20px rgba(255, 215, 0, 0.4) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
    }

    div[data-testid="stButton"] > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #FF6347 0%, #FFD700 50%, #FF6347 100%) !important;
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 8px 30px rgba(255, 215, 0, 0.6) !important;
        border-color: #FF6347 !important;
    }

    div[data-testid="stButton"] > button {
        background: black !important;
        border: 3px solid rgba(255, 215, 0) !important;
        color: white !important;
        font-weight: 1000 !important;
        font-family: 'Lato', sans-serif !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stButton"] > button:hover {
        background: black !important;
        border-color: #FFD700 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(255, 215, 0, 0.3) !important;
    }

    /* Download button specific styling */
    div[data-testid="stDownloadButton"] > button {
        background: linear-gradient(135deg, #32CD32 0%, #228B22 100%) !important;
        border: 2px solid #32CD32 !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.2em !important;
        font-family: 'Sigmar', cursive !important;
    }

    div[data-testid="stDownloadButton"] > button:hover {
        background: linear-gradient(135deg, #228B22 0%, #32CD32 100%) !important;
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 5px 20px rgba(50, 205, 50, 0.4) !important;
    }

    .stSpinner > div {
        color: white !important;
    }

    .stAlert {
        background-color: white !important;
        color: black !important; /* Optional: ensure text stays readable */
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """

st.markdown(get_movie_styles(), unsafe_allow_html=True)

# ---------------------------- LOADING OVERLAY ----------------------------
if not st.session_state.background_loaded:
    st.markdown("""
    <div id="loading-overlay">
        <div class="loading-content">
            <div class="loading-title">🎬 Setting Up Stage...</div>
            <div class="loading-bar-container">
                <div class="loading-bar"></div>
            </div>
            <div class="loading-subtitle">Preparing your imagery rehearsal experience</div>
        </div>
    </div>

    <style>
    #loading-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #000000 0%, #8B4513 50%, #000000 100%);
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
        font-family: 'Sigmar', cursive;
        font-size: 3.5em;
        color: #FFD700;
        margin-bottom: 20px;
        text-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
        letter-spacing: 3px;
        animation: title-glow 2s ease-in-out infinite alternate;
    }

    .loading-bar-container {
        width: 300px;
        height: 8px;
        background: rgba(255, 215, 0, 0.3);
        border-radius: 4px;
        overflow: hidden;
        position: relative;
        margin: 0 auto;
        border: 1px solid #FFD700;
    }

    .loading-bar {
        width: 40%;
        height: 100%;
        background: linear-gradient(90deg, #FFD700, #FF6347);
        border-radius: 4px;
        animation: loading-bar 2s ease-in-out infinite;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.8);
    }

    .loading-subtitle {
        font-family: 'Lato', sans-serif;
        color: rgba(255, 255, 255, 0.9);
        margin-top: 15px;
        font-size: 1.3em;
        font-weight: 300;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
    }

    @keyframes title-glow {
        0% { text-shadow: 0 0 30px rgba(255, 215, 0, 0.5); }
        100% { text-shadow: 0 0 50px rgba(255, 215, 0, 0.8); }
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
    st.session_state.background_loaded = True

# ---------------------------- NAVIGATION FUNCTIONS ----------------------------
def next_step():
    """Move to next step"""
    if st.session_state.current_step < 8:
        st.session_state.current_step += 1
        st.rerun()

# ---------------------------- OVERVIEW PAGE ----------------------------
if st.session_state.current_step == 0:
    st.markdown("""
    <div class="movie-container">
        <h3 style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 2em; text-align: center; margin-bottom: 0px; letter-spacing: 1px;">
            🎬 Lights, Camera, Mental Action!
        </h3>
        <div class="movie-text">
            Welcome to your personal theatre stage where you're the director, star, and audience all in one! 
            Mental imagery is like filming the perfect performance in your mind - you get to rehearse, 
            perfect, and replay your success before it happens in real life.
        </div>
        <div class="movie-text">
           This activity will guide you through the creation of a detailed mental script for your chosen scenario, 
            with feedback to ensure that every scene is vivid and impactful.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="movie-container">
        <h3 style="color: #FF6347; font-family: 'Sigmar', cursive; font-size: 2em; text-align: center; margin-bottom: 0px; letter-spacing: 1px;">
            🎪 The PETTLEP Method
        </h3>
        <div class="movie-text">
            You will be using the <strong>PETTLEP</strong> framework - seven essential elements that make 
            mental imagery incredibly effective. Think of each element as a different camera angle or lighting 
            setup that makes your mental movie more realistic and powerful.
        </div>
        <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 3px; margin: 10px 0; max-width: 800px; margin: 15px auto;">
            <div style="background: rgba(255, 215, 0, 0.1); border: 1px solid rgba(255, 215, 0, 0.3); border-radius: 8px; padding: 0px; text-align: center; display: flex; flex-direction: column; justify-content: center; aspect-ratio: 1;">
                <div style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 2em; font-weight: bold; margin-bottom: 10px;">P</div>
                <div style="color: rgba(255, 255, 255, 0.9); font-size: 1em;">Physical</div>
            </div>
            <div style="background: rgba(255, 215, 0, 0.1); border: 1px solid rgba(255, 215, 0, 0.3); border-radius: 8px; padding: 0px; text-align: center; display: flex; flex-direction: column; justify-content: center; aspect-ratio: 1;">
                <div style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 2em; font-weight: bold; margin-bottom: 10px;">E</div>
                <div style="color: rgba(255, 255, 255, 0.9); font-size: 1em;">Environment</div>
            </div>
            <div style="background: rgba(255, 215, 0, 0.1); border: 1px solid rgba(255, 215, 0, 0.3); border-radius: 8px; padding: 0px; text-align: center; display: flex; flex-direction: column; justify-content: center; aspect-ratio: 1;">
                <div style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 2em; font-weight: bold; margin-bottom: 10px;">T</div>
                <div style="color: rgba(255, 255, 255, 0.9); font-size: 1em;">Task</div>
            </div>
            <div style="background: rgba(255, 215, 0, 0.1); border: 1px solid rgba(255, 215, 0, 0.3); border-radius: 8px; padding: 0px; text-align: center; display: flex; flex-direction: column; justify-content: center; aspect-ratio: 1;">
                <div style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 2em; font-weight: bold; margin-bottom: 10px;">T</div>
                <div style="color: rgba(255, 255, 255, 0.9); font-size: 1em;">Timing</div>
            </div>
            <div style="background: rgba(255, 215, 0, 0.1); border: 1px solid rgba(255, 215, 0, 0.3); border-radius: 8px; padding: 0px; text-align: center; display: flex; flex-direction: column; justify-content: center; aspect-ratio: 1;">
                <div style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 2em; font-weight: bold; margin-bottom: 10px;">L</div>
                <div style="color: rgba(255, 255, 255, 0.9); font-size: 1em;">Learning</div>
            </div>
            <div style="background: rgba(255, 215, 0, 0.1); border: 1px solid rgba(255, 215, 0, 0.3); border-radius: 8px; padding: 0px; text-align: center; display: flex; flex-direction: column; justify-content: center; aspect-ratio: 1;">
                <div style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 2em; font-weight: bold; margin-bottom: 10px;">E</div>
                <div style="color: rgba(255, 255, 255, 0.9); font-size: 1em;">Emotion</div>
            </div>
            <div style="background: rgba(255, 215, 0, 0.1); border: 1px solid rgba(255, 215, 0, 0.3); border-radius: 8px; padding: 0px; text-align: center; display: flex; flex-direction: column; justify-content: center; aspect-ratio: 1;">
                <div style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 2em; font-weight: bold; margin-bottom: 10px;">P</div>
                <div style="color: rgba(255, 255, 255, 0.9); font-size: 1em;">Perspective</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h3 style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 2em; text-align: center; margin-top: 10px; letter-spacing: 1px;">
            🎬 Choose Your Scenario
        </h3>
        """, unsafe_allow_html=True)
    
    # Put the actual buttons here
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button(f"{SCENARIOS['Soccer Penalty Kick']['icon']} Soccer Penalty Kick", key="scenario_Soccer Penalty Kick", use_container_width=True):
            st.session_state.selected_scenario = "Soccer Penalty Kick"
            next_step()
    
    with col2:
        if st.button(f"{SCENARIOS['Public Speaking']['icon']} Public Speaking", key="scenario_Public Speaking", use_container_width=True):
            st.session_state.selected_scenario = "Public Speaking"
            next_step()
    
    with col3:
        if st.button(f"{SCENARIOS['Exam Hall']['icon']} Exam Hall", key="scenario_Exam Hall", use_container_width=True):
            st.session_state.selected_scenario = "Exam Hall"
            next_step()
    
    st.stop()

# ---------------------------- PETTLEP ELEMENTS (STEPS 1-7) ----------------------------
if 1 <= st.session_state.current_step <= 7:
    element_index = st.session_state.current_step - 1
    PETTLEP_ELEMENTS = get_pettlep_elements(st.session_state.selected_scenario)
    element = PETTLEP_ELEMENTS[element_index]
    
    # Display selected scenario at the top
    st.markdown(f"""
    <div>
        <h3 style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 2em; text-align: center; margin-bottom: -20px; margin-top: 10px; letter-spacing: 1px;">
            {SCENARIOS[st.session_state.selected_scenario]['icon']} Scenario: {st.session_state.selected_scenario}
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Check if we're in elaboration mode for this element
    if not st.session_state.elaboration_mode.get(element['name'], False):
        # MINI CHALLENGE MODE
        st.markdown(f"""
        <div class="movie-container">
            <h1 class="element-title">{element['name']}</h1>
            <div class="movie-text">{element['lesson']}</div>
            <div class="example-text">{element['example']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div>
            <div class="challenge-title">🧩 Mini Challenge</div>
        """, unsafe_allow_html=True)
        
        user_answer = st.radio(
            element['challenge_question'], 
            element['options'], 
            key=f"challenge_{element['name']}"
        )

        if st.button("Check Answer", key=f"check_{element['name']}"):
            if element['options'].index(user_answer) == element['correct_index']:
                st.success("✅ Correct! Moving to elaboration...")
                st.session_state.challenge_passed[element['name']] = True
                st.session_state.selected_option[element['name']] = user_answer
                st.session_state.elaboration_mode[element['name']] = True
                st.rerun()
            else:
                st.error("❌ That's not quite right. Try again!")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        # ELABORATION MODE (NEW PAGE AFTER CORRECT ANSWER)        
        # Build the questions list as a single string
        questions_html = ""
        for question in element['elaboration_questions']:
            questions_html += f"<li>{question}</li>"
    
        st.markdown(f"""
        <div class="elaboration-container">
            <div class="elaboration-title">✨ Now Elaborate Further</div>
            <div class="movie-text">Great! You correctly identified the key aspects of this element.</div>
            <div class="movie-text">You chose: <strong>"{st.session_state.selected_option.get(element['name'], '')}"</strong> Please elaborate on your answer by addressing these questions:</div>
            <div style="margin-top: 10px; margin-bottom: -15px;">
                <ul style="color: rgba(255, 255, 255, 0.9); font-family: 'Lato', sans-serif;">
                    {questions_html}
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Text area for elaboration
        current_response = st.session_state.responses.get(element['name'], "")
        user_input = st.text_area(
            label="",
            value=current_response,
            height=100,
            key=f"input_{element['name']}",
            placeholder=f"Based on your answer, elaborate with specific details."
        )
        
        # Submit button - trigger feedback immediately
        if st.button("📝 Submit for Feedback", key=f"submit_{element['name']}", type="primary"):
            if user_input.strip():
                st.session_state.responses[element['name']] = user_input
                
                # Get feedback immediately
                with st.spinner("🎬 Getting feedback..."):
                    approved, feedback = get_gpt_feedback(
                        element['name'], 
                        user_input, 
                        st.session_state.selected_scenario
                    )
                    
                    st.session_state.gpt_feedback[element['name']] = feedback
                    st.session_state.gpt_approved[element['name']] = approved  # Add this line
                    st.rerun()  # Refresh to show feedback
        
        # Display existing feedback if available
        if element['name'] in st.session_state.gpt_feedback:
            feedback_text = st.session_state.gpt_feedback[element['name']]
            # Determine if it was approved
            is_approved = st.session_state.gpt_approved.get(element['name'], False)
            
            feedback_class = "feedback-approved" if is_approved else "feedback-needs-work"
            feedback_icon = "✅" if is_approved else "🎬"
            feedback_title = "Great work!" if is_approved else "Needs more detail"
            
            st.markdown(f"""
            <div class="feedback-container {feedback_class}">
                <h4 style="color: {'#32CD32' if is_approved else '#FF6347'}; font-family: 'Sigmar', cursive; margin-bottom: -10px;">
                    {feedback_icon} {feedback_title}
                </h4>
                <div class="movie-text">{feedback_text}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if is_approved:
                st.markdown("<div style='text-align: center; margin-top: -5px;'>", unsafe_allow_html=True)
                # Check if this is the last element (step 7)
                button_text = "🎬 Generate Script" if st.session_state.current_step == 7 else "➡️ Next Element"
                if st.button(button_text, key=f"next_{element['name']}", type="primary"):
                    next_step()
                st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------- FINAL SCRIPT (STEP 8) ----------------------------
elif st.session_state.current_step == 8:
    # LOADING SCRIPT PAGE
    if not st.session_state.script_generated and not st.session_state.generating_script:
        # Start generating
        st.session_state.generating_script = True
        st.rerun()
    
    elif st.session_state.generating_script and not st.session_state.script_generated:
        # Show loading overlay
        st.markdown("""
        <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0, 0, 0, 0.95); z-index: 1000; display: flex; align-items: center; justify-content: center;">
            <div class="movie-container" style="margin: 0; padding: 40px; text-align: center;">
                <div style="font-family: 'Sigmar', cursive; font-size: 2.5em; color: #FFD700; margin-bottom: 20px;">
                    🎬 Generating Your Complete Script...
                </div>
                <div class="spinner" style="border: 4px solid #f3f3f3; border-top: 4px solid #FFD700; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 0 auto 15px auto;"></div>
                <div style="font-family: 'Lato', sans-serif; color: rgba(255, 255, 255, 0.9); font-size: 1.1em;">
                    Creating your personalized imagery rehearsal experience...
                </div>
            </div>
        </div>
        
        <style>
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Generate the script
        complete_script = generate_complete_script(
            st.session_state.selected_scenario,
            st.session_state.selected_option,
            st.session_state.responses
        )
        
        st.session_state.complete_script = complete_script
        st.session_state.script_generated = True
        st.session_state.generating_script = False
        st.rerun()
    
    else:
        # SHOW RESULTS PAGE
        complete_script = st.session_state.complete_script
        
        st.markdown("""
        <div class="movie-container">
            <h2 style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 2em; text-align: center; margin-bottom: 0px; letter-spacing: 1px;">
                🎉 That's A Wrap!
            </h2>
            <div class="movie-text">
                Congratulations! You've created a complete PETTLEP imagery script. This is your personal 
                mental rehearsal tool - use it regularly to train your mind for peak performance.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Handle case where script generation failed
        if complete_script is None:
            complete_script = f"Unable to generate complete script at this time. Please use your individual responses for mental rehearsal.\n\nScenario: {st.session_state.selected_scenario}\n\nYour responses:\n" + "\n".join([f"{k}: {v}" for k, v in st.session_state.responses.items()])
        
        st.markdown(f"""
        <div class="script-container">
            <h3 style="color: #FF6347; font-family: 'Sigmar', cursive; font-size: 2em; text-align: center; margin-bottom: 0px; letter-spacing: 1px;">
                📜 Your Complete Imagery Script
            </h3>
            <div style="text-align: center; margin-bottom: 20px; color: #FF6347; font-family: 'Lato', sans-serif; font-size: 1.2em;">
                Scenario: {st.session_state.selected_scenario}
            </div>
            <div class="script-text">
            {complete_script.replace(chr(10), '<br>') if complete_script else 'Error loading script.'}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Usage instructions
        st.markdown("""
        <div class="movie-container">
            <h3 style="color: #FFD700; font-family: 'Sigmar', cursive; font-size: 1.8em; text-align: center; margin-bottom: 15px;">
                🎯 How to Use Your Script
            </h3>
            <div class="movie-text">
                <strong>🕐 Practice regularly:</strong> Use this script 3-5 times per week, spending 5-10 minutes each session.
            </div>
            <div class="movie-text">
                <strong>🧘 Find a quiet space:</strong> Choose a comfortable, distraction-free environment for your mental rehearsal.
            </div>
            <div class="movie-text">
                <strong>🎬 Engage all senses:</strong> Make each element as vivid as possible - see, hear, feel, and experience every detail.
            </div>
            <div class="movie-text">
                <strong>🔄 Update as needed:</strong> Modify your script as your skills improve or circumstances change.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Download button and reset options
        col1, col2 = st.columns([1, 1])
        
        with col1:
            if st.button("🔄 Create Another Script", use_container_width=True):
                # Reset everything
                for key in ['current_step', 'selected_scenario', 'responses', 'gpt_feedback', 'challenge_passed', 'selected_option', 'elaboration_mode', 'script_generated', 'complete_script', 'generating_script']:
                    if key == 'current_step':
                        st.session_state[key] = 0
                    elif key == 'selected_scenario':
                        st.session_state[key] = None
                    elif key in ['script_generated', 'generating_script']:
                        st.session_state[key] = False
                    elif key in ['complete_script']:
                        st.session_state[key] = ""
                    else:
                        st.session_state[key] = {}
                st.rerun()
        
        with col2:
            if st.button("🎭 Different Scenario", use_container_width=True):
                # Keep some progress but change scenario
                for key in ['current_step', 'selected_scenario', 'responses', 'gpt_feedback', 'challenge_passed', 'selected_option', 'elaboration_mode', 'script_generated', 'complete_script', 'generating_script']:
                    if key == 'current_step':
                        st.session_state[key] = 0
                    elif key == 'selected_scenario':
                        st.session_state[key] = None
                    elif key in ['script_generated', 'generating_script']:
                        st.session_state[key] = False
                    elif key in ['complete_script']:
                        st.session_state[key] = ""
                    else:
                        st.session_state[key] = {}
                st.rerun()