import streamlit as st
import json
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Chat - Mental Health Companion",
    page_icon="🤖",
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
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: flex-start;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 2rem;
    }
    .bot-message {
        background-color: #f8f9fa;
        margin-right: 2rem;
    }
    .message-content {
        margin-left: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Check if form is submitted
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

if not st.session_state.form_submitted:
    st.error("Please complete the assessment form first!")
    if st.button("Go to Assessment"):
        st.switch_page("pages/02_Assessment.py")
    st.stop()

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm your mental health companion. I'm here to listen and support you. How are you feeling today?"
        }
    ]

st.title("🤖 Chat with Your Mental Health Companion")

# Display chat messages
for message in st.session_state.messages:
    with st.container():
        if message["role"] == "assistant":
            st.markdown(f"""
                <div class="chat-message bot-message">
                    <div style="width: 30px;">🤖</div>
                    <div class="message-content">{message["content"]}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="chat-message user-message">
                    <div style="width: 30px;">👤</div>
                    <div class="message-content">{message["content"]}</div>
                </div>
            """, unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # TODO: Add actual chatbot logic here
    # For now, just echo a supportive message
    response = "I hear you. Would you like to tell me more about that?"
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Rerun to update chat display
    st.rerun()

# Add a note about privacy
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.8rem;'>
    🔒 Your conversations are private and confidential. If you're experiencing severe distress, 
    please reach out to a mental health professional or emergency services.
</div>
""", unsafe_allow_html=True) 