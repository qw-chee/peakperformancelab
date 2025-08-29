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
        goal_type = goal.get("type", "multiple_choice")
        
        if goal_type == "multiple_choice":
            missing_count = len(goal["missing"])
                  
            st.markdown(f"""
            <div class="neon-container">
                <h3 style="color: #00ffff; font-family: 'Orbitron', monospace; margin-bottom: -10px; font-size: clamp(1rem, 1.4vw, 1.4em);">
                    🔍 WHICH SMART COMPONENTS ARE MISSING?
                </h3>
                <div class="goal-statement" style="text-align: center;">
                    <span class="goal-text">{goal['text']}</span>
                </div>
                <div class="hint-text">💡 Hint: This goal is missing <strong>{missing_count}</strong> SMART component{"s" if missing_count != 1 else ""}.</div>
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
                    
                    st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)
            
        else:  # GPT evaluation type
            st.markdown(f"""
            <div class="neon-container">
                <h3 style="color: #00ffff; font-family: 'Orbitron', monospace; margin-bottom: -10px; font-size: clamp(1rem, 1.4vw, 1.4em);">
                    ✍️ REWRITE THIS GOAL TO BE SMART
                </h3>
                <div class="goal-statement" style="text-align: center;">
                    <span class="goal-text">{goal['text']}</span>
                </div>
                <div class="hint-text">💡 Rewrite this goal to include all SMART components: Specific, Measurable, Achievable, Relevant, and Timebound.</div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown('<div style="margin-top: 5px;">', unsafe_allow_html=True)
            
            with st.form("smart_rewrite_form", clear_on_submit=False):
                user_rewrite = st.text_input(
                    "Your SMART Goal:",
                    value=st.session_state.user_rewrite,
                    placeholder="Rewrite the goal to make it SMART...",
                    help="Make sure your goal is Specific, Measurable, Achievable, Relevant, and Timebound"
                )
                
                submitted = st.form_submit_button("🤖 ANALYZE WITH AI", use_container_width=True, type="primary")
                
                if submitted and user_rewrite.strip():
                    st.session_state.user_rewrite = user_rewrite
                    st.session_state.awaiting_response = False
                    st.session_state.evaluating = True
                    st.rerun()
                elif submitted and not user_rewrite.strip():
                    st.error("Please enter a rewritten goal before submitting.")
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    elif st.session_state.evaluating:
        # Show loading state while GPT evaluates
        st.markdown(f"""
        <div class="neon-container">
            <div style="text-align: center; padding: clamp(15px, 2.5vw, 25px);">
                <div class="loading-spinner"></div>
                <div style="color: #00ffff; font-family: 'Orbitron', monospace; font-size: clamp(1.2rem, 1.6vw, 1.6em); font-weight: 600;">
                    AI ANALYZING YOUR GOAL...
                </div>
                <div style="color: rgba(255,255,255,0.7); font-family: 'Rajdhani', sans-serif; margin-top: clamp(5px, 0.8vw, 8px);">
                    Evaluating SMART components...
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Perform GPT evaluation
        goal = st.session_state.current_goal
        evaluation_result = evaluate_goal_with_gpt(
            goal['text'], 
            st.session_state.user_rewrite, 
            goal['feedback']
        )
        
        st.session_state.gpt_evaluation = evaluation_result
        st.session_state.evaluating = False
        st.session_state.show_feedback = True
        
        # Award score based on GPT evaluation
        parsed_eval = parse_gpt_evaluation(evaluation_result)
        if parsed_eval['score'] >= 70:  # Threshold for success
            st.session_state.score += 1
            
        st.rerun()
    
    elif st.session_state.show_feedback:
        goal = st.session_state.current_goal
        goal_type = goal.get("type", "multiple_choice")
        
        if goal_type == "multiple_choice":
            # Original multiple choice feedback
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
                <h3 style="color: #ffff00; font-family: 'Orbitron', monospace; margin-bottom: -20px; font-size: clamp(1rem, 1.3vw, 1.3em); text-align: center;">
                    📊 MISSING COMPONENTS DETECTED
                </h3>
                <div class="missing-components">
                    {' '.join([f'<span class="component-tag">{comp}</span>' for comp in goal["missing"]])}
                </div>
                <div style="background: rgba(0,255,255,0.1); border: clamp(1px, 0.15vw, 1px) solid rgba(0,255,255,0.3); border-radius: clamp(8px, 1.2vw, 12px); padding: clamp(2px, 0.5vw, 20px); margin-top: clamp(4px, 1vw, 20px);">
                    <div style="color: #00ffff; font-family: 'Orbitron', monospace; font-weight: 600; margin-bottom: clamp(6px, 1vw, 10px); font-size: clamp(0.9rem, 1.1vw, 1.1em);">
                        📝 SYSTEM ANALYSIS:
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-family: 'Rajdhani', sans-serif; line-height: 1.2; font-size: clamp(1rem, 1.2vw, 1.2em);">
                        {goal["feedback"]}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        else:  # GPT evaluation feedback
            parsed_eval = parse_gpt_evaluation(st.session_state.gpt_evaluation)
            score = parsed_eval['score']
            
            # Determine score class and feedback
            if score >= 80:
                score_class = "score-excellent"
                feedback_class = "feedback-success"
                feedback_icon = "🏆"
                feedback_title = "EXCELLENT!"
            elif score >= 60:
                score_class = "score-good"
                feedback_class = "feedback-success"
                feedback_icon = "✅"
                feedback_title = "GOOD WORK!"
            elif score >= 40:
                score_class = "score-needs-work"
                feedback_class = "neon-container"
                feedback_icon = "⚠️"
                feedback_title = "NEEDS IMPROVEMENT"
            else:
                score_class = "score-poor"
                feedback_class = "feedback-learning"
                feedback_icon = "❌"
                feedback_title = "NEEDS WORK"
            
            st.markdown(f"""
            <div class="{feedback_class}" style="display: flex; align-items: center; justify-content: center; gap: 8px; margin-top: 10px;">
                <span class="feedback-icon">{feedback_icon}</span>
                <h3 class="feedback-title" style="margin: 0;">{feedback_title}</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Show GPT evaluation
            st.markdown(f"""
            <div class="gpt-evaluation">
                <div class="evaluation-score {score_class}">
                    AI SCORE: {score}/100
                </div>
                
                <div style="margin-bottom: clamp(8px, 1.2vw, 15px);">
                    <div style="color: #00ffff; font-family: 'Orbitron', monospace; font-weight: 600; margin-bottom: clamp(4px, 0.6vw, 6px); font-size: clamp(0.9rem, 1.1vw, 1.1em);">
                        🎯 YOUR REWRITTEN GOAL:
                    </div>
                    <div style="background: rgba(0,255,255,0.1); border: clamp(1px, 0.15vw, 1px) solid rgba(0,255,255,0.3); border-radius: clamp(6px, 1vw, 10px); padding: clamp(8px, 1.2vw, 12px); color: rgba(255,255,255,0.95); font-family: 'Rajdhani', sans-serif; font-style: italic;">
                        "{st.session_state.user_rewrite}"
                    </div>
                </div>
                
                {f'''
                <div style="margin-bottom: clamp(8px, 1.2vw, 15px);">
                    <div style="color: #00ff7f; font-family: 'Orbitron', monospace; font-weight: 600; margin-bottom: clamp(4px, 0.6vw, 6px); font-size: clamp(0.9rem, 1.1vw, 1.1em);">
                        ✅ SMART COMPONENTS PRESENT:
                    </div>
                    <div class="missing-components" style="justify-content: flex-start;">
                        {' '.join([f'<span class="component-tag" style="background: rgba(0,255,127,0.2); color: #00ff7f; border-color: rgba(0,255,127,0.5);">{comp}</span>' for comp in parsed_eval['present']]) if parsed_eval['present'] else '<span style="color: rgba(255,255,255,0.6);">None identified</span>'}
                    </div>
                </div>
                ''' if parsed_eval['present'] else ''}
                
                {f'''
                <div style="margin-bottom: clamp(8px, 1.2vw, 15px);">
                    <div style="color: #ffff00; font-family: 'Orbitron', monospace; font-weight: 600; margin-bottom: clamp(4px, 0.6vw, 6px); font-size: clamp(0.9rem, 1.1vw, 1.1em);">
                        ⚠️ COMPONENTS NEEDING WORK:
                    </div>
                    <div class="missing-components" style="justify-content: flex-start;">
                        {' '.join([f'<span class="component-tag">{comp}</span>' for comp in parsed_eval['missing']]) if parsed_eval['missing'] else '<span style="color: rgba(255,255,255,0.6);">All components addressed!</span>'}
                    </div>
                </div>
                ''' if parsed_eval['missing'] else ''}
                
                <div style="background: rgba(0,255,255,0.1); border: clamp(1px, 0.15vw, 1px) solid rgba(0,255,255,0.3); border-radius: clamp(8px, 1.2vw, 12px); padding: clamp(8px, 1.2vw, 12px);">
                    <div style="color: #00ffff; font-family: 'Orbitron', monospace; font-weight: 600; margin-bottom: clamp(6px, 1vw, 10px); font-size: clamp(0.9rem, 1.1vw, 1.1em);">
                        🤖 AI FEEDBACK:
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-family: 'Rajdhani', sans-serif; line-height: 1.4; font-size: clamp(1rem, 1.2vw, 1.2em);">
                        {parsed_eval['feedback']}
                    </div>
                    
                    {f'''
                    <div style="margin-top: clamp(8px, 1.2vw, 15px); padding-top: clamp(8px, 1.2vw, 15px); border-top: clamp(1px, 0.15vw, 1px) solid rgba(0,255,255,0.2);">
                        <div style="color: #ffff00; font-family: 'Orbitron', monospace; font-weight: 600; margin-bottom: clamp(4px, 0.6vw, 6px); font-size: clamp(0.9rem, 1.1vw, 1.1em);">
                            💡 SUGGESTIONS FOR IMPROVEMENT:
                        </div>
                        <div style="color: rgba(255,255,255,0.9); font-family: 'Rajdhani', sans-serif; line-height: 1.4; font-size: clamp(1rem, 1.2vw, 1.2import streamlit as st
import random
import openai

st.set_page_config(
    page_title="Mission: SMART Possible", 
    layout="centered",
    page_icon="🎯"
)

# Set up OpenAI API
openai.api_key = st.secrets.get("openai_api_key")

# ---------------------------- GOALS DATABASE ----------------------------
GOALS_DATABASE = [
    # Missing 1 element
    {
        "text": "I will aim to improve my GPA by 0.2 for better career prospects.",
        "missing": ["Timebound"],
        "feedback": "This goal isn't <strong>Timebound</strong> - there's no deadline specified. There should be a timeframe like 'by the end of this semester' or 'within one academic year'.<br><br><strong>SMART Version:</strong> 'I will improve my GPA by 0.5 points by the end of this academic year through consistent study habits to enhance my career prospects.'",
        "type": "multiple_choice"
    },
    {
        "text": "To manage time, I will write some of my TMA every evening.",
        "missing": ["Measurable"],
        "feedback": "This goal isn't <strong>Measurable</strong> - 'some' is vague. How much work should be specified, like '2 pages' or '500 words' or '1 hour of writing'.<br><br><strong>SMART Version:</strong> 'To manage time effectively, I will write 300 words of my TMA every evening until completion.'",
        "type": "multiple_choice"
    },
    {
        "text": "I will finish reading 10 books to improve my writing by tomorrow.",
        "missing": ["Achievable"],
        "feedback": "This goal isn't <strong>Achievable</strong> - reading 10 books in one day is unrealistic. A more achievable timeline would be several months.<br><br><strong>SMART Version:</strong> 'I will finish reading 10 books over the next 6 months to improve my writing skills by expanding my vocabulary and understanding different writing styles.'",
        "type": "multiple_choice"
    },
    {
        "text": "I will volunteer twice at the foodbank each month.",
        "missing": ["Relevant"],
        "feedback": "This goal lacks clear <strong>Relevance</strong> - it doesn't explain how volunteering connects to any goals.<br><br><strong>SMART Version:</strong> 'I will volunteer twice at the foodbank each month for 6 months to develop my leadership skills and give back to my community.'",
        "type": "multiple_choice"
    },
    
    # Missing 2 elements
    {
        "text": "I want to save 10 million dollars by the end of this year.",
        "missing": ["Achievable", "Relevant"],
        "feedback": "This goal isn't <strong>Achievable</strong> (10 million in one year is unrealistic for most people) and lacks <strong>Relevance</strong> (why this specific amount? What's the purpose?).<br><br><strong>SMART Version:</strong> 'I will save $5,000 by the end of this year to build an emergency fund for my family's financial security.'",
        "type": "multiple_choice"
    },
    {
        "text": "I will arrive earlier for class starting next week.",
        "missing": ["Measurable", "Relevant"],
        "feedback": "This goal isn't <strong>Measurable</strong> (how much earlier?) and lacks <strong>Relevance</strong> (why is arriving earlier important for your academic success?).<br><br><strong>SMART Version:</strong> 'I will arrive 15 minutes earlier for each class starting next week to review notes and improve my academic performance.'",
        "type": "multiple_choice"
    },
    
    # Missing 3 elements
    {
        "text": "I will start exploring other types of exercise next week.",
        "missing": ["Specific", "Measurable", "Relevant"],
        "feedback": "This goal isn't <strong>Specific</strong> (which types of exercise?), isn't <strong>Measurable</strong> (how much exploration?), and lacks <strong>Relevance</strong> (why explore new exercises?).<br><br><strong>SMART Version:</strong> 'I will try 3 new types of exercise (yoga, swimming, and cycling) for 30 minutes each next week to find enjoyable activities that will help me maintain long-term fitness.'",
        "type": "multiple_choice"
    },  
    # Missing 4 elements
    {
        "text": "I will launch a successful online business by next week.",
        "missing": ["Specific", "Measurable", "Achievable", "Relevant"],
        "feedback": "This goal isn't <strong>Specific</strong> (what type of business?), isn't <strong>Measurable</strong> (what defines success?), isn't <strong>Achievable</strong> (one week is unrealistic), and lacks <strong>Relevance</strong> (why this business?).<br><br><strong>SMART Version:</strong> 'I will launch a graphic design website with 5 portfolio pieces within 6 months to generate $1,000 monthly income.'",
        "type": "multiple_choice"
    },
    # Test - GPT Evaluated
    {
        "text": "I want to build better habits.",
        "missing": ["Specific", "Measurable", "Relevant", "Timebound"],
        "feedback": "This goal lacks <strong>Specificity</strong> (which habits?), isn't <strong>Measurable</strong> (how will you track progress?), lacks <strong>Relevance</strong> (why these habits?), and has no <strong>Timebound</strong> deadline.<br><br><strong>SMART Version:</strong> 'I will establish a morning routine of 30 minutes of reading and 10 minutes of meditation daily for the next 30 days to improve my focus and productivity at work.'",
        "type": "gpt_evaluation"
    },
    {
        "text": "I want to eat healthier.",
        "missing": ["Specific", "Measurable", "Relevant", "Timebound"],
        "feedback": "This goal lacks <strong>Specificity</strong> (what does healthier mean?), isn't <strong>Measurable</strong> (how will you track it?), lacks <strong>Relevance</strong> (why is this important to you?), and has no <strong>Timebound</strong> deadline.<br><br><strong>SMART Version:</strong> 'I will eat 5 servings of fruits and vegetables daily for the next 3 months to improve my energy levels and overall health.'",
        "type": "gpt_evaluation"
    }
]

# ---------------------------- SESSION STATE INIT ----------------------------
def init_game_state():
    defaults = {
        'current_question': 0, 'score': 0, 'total_questions': len(GOALS_DATABASE),
        'current_goal': None, 'awaiting_response': False, 'show_feedback': False,
        'user_selections': [], 'game_completed': False, 'user_rewrite': '',
        'gpt_evaluation': None, 'evaluating': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_game_state()

# ---------------------------- GPT EVALUATION FUNCTION ----------------------------
def evaluate_goal_with_gpt(original_goal, user_rewrite, expected_feedback):
    """Evaluate user's rewritten goal using GPT"""
    try:
        prompt = f"""
You are evaluating a student's rewritten SMART goal. 

SMART Criteria:
- Specific: Well-defined and clear
- Measurable: Quantifiable with specific metrics
- Achievable: Realistic and attainable
- Relevant: Has a clear purpose and reason
- Timebound: Has a specific deadline or timeframe

Original Goal: "{original_goal}"
Student's Rewritten Goal: "{user_rewrite}"

Expected Issues in Original Goal: {expected_feedback}

Evaluate the student's rewritten goal and provide:
1. Score out of 100
2. Which SMART components are now present (if any)
3. Which SMART components are still missing (if any)
4. Specific feedback on improvements made
5. Suggestions for further improvement (if needed)

Format your response as:
SCORE: [0-100]
PRESENT: [List components that are now adequate]
MISSING: [List components still missing or inadequate]
FEEDBACK: [Detailed feedback on what the student did well and what needs improvement]
SUGGESTIONS: [Specific suggestions for improvement if score < 80]
"""

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.3,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        return response.choices[0].text.strip()
    
    except Exception as e:
        return f"Error evaluating goal: {str(e)}"

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
            border-radius: clamp(12px, 1.8vw, 18px);
            padding: clamp(1px, 0.2vw, 2px);
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
            font-size: clamp(1.2rem, 1.4vw, 1.3em);
            color: rgba(255, 255, 255, 0.95);
            font-style: italic;
            font-weight: 700;
            line-height: 1.5;
            margin: 0;
            text-shadow: 0 0 clamp(3px, 0.5vw, 5px) rgba(255, 255, 255, 0.7);
        }
        
        .hint-text {
            color: rgba(0, 255, 127, 0.9);
            font-family: 'Rajdhani', sans-serif;
            font-weight: 500;
            font-size: clamp(1rem, 1.2vw, 1.1em);
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
            font-size: clamp(0.7rem, 0.9vw, 0.9em);
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
        
        .stTextInput > div > div > input {
            background: rgba(15, 15, 35, 0.9) !important;
            border: clamp(1px, 0.15vw, 1px) solid rgba(0, 255, 255, 0.3) !important;
            color: white !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-size: clamp(1rem, 1.2vw, 1.2em) !important;
            border-radius: clamp(5px, 0.8vw, 8px) !important;
            padding: clamp(8px, 1.2vw, 12px) !important;
            backdrop-filter: blur(10px) !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: rgba(0, 255, 255, 0.6) !important;
            box-shadow: 0 0 clamp(10px, 1.5vw, 15px) rgba(0, 255, 255, 0.3) !important;
        }
        
        .stTextInput label {
            color: rgba(0, 255, 255, 0.9) !important;
            font-family: 'Orbitron', monospace !important;
            font-weight: 600 !important;
            font-size: clamp(0.9rem, 1.1vw, 1.1em) !important;
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
        
        .loading-spinner {
            border: clamp(2px, 0.3vw, 4px) solid rgba(0, 255, 255, 0.3);
            border-radius: 50%;
            border-top: clamp(2px, 0.3vw, 4px) solid #00ffff;
            width: clamp(20px, 3vw, 40px);
            height: clamp(20px, 3vw, 40px);
            animation: spin 1s linear infinite;
            display: inline-block;
            margin-right: clamp(8px, 1.2vw, 15px);
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .gpt-evaluation {
            background: rgba(15, 15, 35, 0.95);
            border: clamp(1px, 0.2vw, 2px) solid rgba(0, 255, 127, 0.4);
            border-radius: clamp(8px, 1.2vw, 12px);
            padding: clamp(8px, 1.5vw, 15px);
            margin: clamp(8px, 1.5vw, 15px) 0;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 clamp(15px, 2.5vw, 25px) rgba(0, 255, 127, 0.2);
        }
        
        .evaluation-score {
            font-family: 'Orbitron', monospace;
            font-size: clamp(1.5rem, 2.2vw, 2.5em);
            font-weight: 900;
            text-align: center;
            margin-bottom: clamp(8px, 1.2vw, 15px);
        }
        
        .score-excellent { color: #00ff7f; }
        .score-good { color: #00ffff; }
        .score-needs-work { color: #ffff00; }
        .score-poor { color: #ff5050; }
    }
    </style>
    """
