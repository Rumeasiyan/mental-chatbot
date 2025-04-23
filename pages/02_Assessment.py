import streamlit as st
import json
from pathlib import Path
import uuid
import pandas as pd

# Page config
st.set_page_config(
    page_title="Assessment - Mental Health Companion",
    page_icon="📝",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #2E4057;
    }
    .form-section {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton > button {
        width: 100%;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

def load_questions():
    try:
        with open('data/questions.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading questions: {str(e)}")
        return None

def save_responses(responses):
    try:
        Path("data/responses").mkdir(exist_ok=True)
        # Generate a unique ID for the response file
        response_id = str(uuid.uuid4())
        response_data = {
            "user_id": st.session_state.user_id,
            "timestamp": str(pd.Timestamp.now()),
            "responses": responses
        }
        with open(f'data/responses/{response_id}.json', 'w') as f:
            json.dump(response_data, f, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving responses: {str(e)}")
        return False

# Initialize session state
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

if 'responses' not in st.session_state:
    st.session_state.responses = {}

st.title("📝 Mental Health Assessment")
st.markdown("""
Before we begin our conversation, please help us understand you better by filling out this brief assessment.
Your responses will help us provide more personalized support.
""")

# Load questions
questions = load_questions()
if not questions:
    st.error("Unable to load the questionnaire. Please try again later.")
    st.stop()

# Form
with st.form("mental_health_assessment", clear_on_submit=False):
    for section, section_questions in questions.items():
        st.subheader(section.replace('_', ' ').title())
        
        for field_id, field_data in section_questions.items():
            field_key = f"{section}_{field_id}"
            
            if field_data['type'] == 'select':
                response = st.selectbox(
                    field_data['label'],
                    options=field_data['options'],
                    key=field_key
                )
                if response:
                    st.session_state.responses[field_key] = response
                    
            elif field_data['type'] == 'slider':
                response = st.slider(
                    field_data['label'],
                    min_value=field_data['min'],
                    max_value=field_data['max'],
                    key=field_key
                )
                st.session_state.responses[field_key] = response
                
            elif field_data['type'] == 'multiselect':
                response = st.multiselect(
                    field_data['label'],
                    options=field_data['options'],
                    key=field_key
                )
                if response:
                    st.session_state.responses[field_key] = response
                    
            elif field_data['type'] == 'text_area':
                response = st.text_area(
                    field_data['label'],
                    key=field_key
                )
                if response:
                    st.session_state.responses[field_key] = response
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    submit_button = st.form_submit_button("Submit Assessment", use_container_width=True)

if submit_button:
    # Validate responses
    is_valid = True
    missing_fields = []
    
    for section, section_questions in questions.items():
        for field_id, field_data in section_questions.items():
            field_key = f"{section}_{field_id}"
            if field_data.get('required', False):
                if field_key not in st.session_state.responses or not st.session_state.responses[field_key]:
                    is_valid = False
                    missing_fields.append(field_data['label'])
    
    if not is_valid:
        st.error("Please answer all required questions:")
        for field in missing_fields:
            st.warning(f"- {field}")
    else:
        if save_responses(st.session_state.responses):
            st.session_state.form_submitted = True
            st.success("Thank you for completing the assessment! Redirecting to chat...")
            st.balloons()
            st.switch_page("pages/03_Chat.py")
        else:
            st.error("There was an error saving your responses. Please try again.") 