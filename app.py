import streamlit as st
import json
from pathlib import Path
import requests
from PIL import Image
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Mental Health Chatbot",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern design
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #2E4057;
        font-size: 3rem !important;
        font-weight: 700 !important;
        margin-bottom: 2rem !important;
    }
    .stMarkdown {
        font-size: 1.2rem;
    }
    .css-1d391kg {
        padding: 3rem 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Function to load hero image
def load_hero_image():
    try:
        url = "https://images.unsplash.com/photo-1516302752625-fcc3c50ae61f?q=80&w=1200"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except:
        return None

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.title("🧠 Mental Health Companion")
    st.markdown("""
    Welcome to your personal mental health companion. We're here to support your journey 
    towards better mental well-being in this digital age.
    
    ### How it works:
    1. 📝 Fill out a brief questionnaire
    2. 💭 Get personalized support
    3. 💬 Chat with our AI companion
    
    > "Mental health is not a destination, but a journey."
    """)
    
    # Call-to-action button
    if st.button("Start Your Journey", type="primary", key="start_journey"):
        st.session_state['start_journey'] = True
        st.switch_page("pages/02_Assessment.py")

with col2:
    hero_image = load_hero_image()
    if hero_image:
        st.image(hero_image, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    Made with ❤️ for better mental health<br>
    © 2024 Mental Health Companion
</div>
""", unsafe_allow_html=True)
