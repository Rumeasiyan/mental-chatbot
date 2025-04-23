import streamlit as st

st.set_page_config(
    page_title="About Us - Mental Health Companion",
    page_icon="🧠",
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
    </style>
""", unsafe_allow_html=True)

st.title("About Our Mental Health Companion")

# Project Overview
st.header("🎯 Project Overview")
st.markdown("""
In today's digital age, mental health challenges have become increasingly complex, 
especially with the prevalence of social media and digital connectivity. Our Mental 
Health Companion aims to provide personalized support and guidance for individuals 
navigating these challenges.
""")

# Key Features
st.header("✨ Key Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 📊 Personalized Assessment
    - Comprehensive questionnaire
    - Individual need analysis
    - Tailored recommendations
    """)

with col2:
    st.markdown("""
    ### 🤖 AI Companion
    - 24/7 supportive chat
    - Evidence-based guidance
    - Emotional support
    """)

with col3:
    st.markdown("""
    ### 🎯 Goal Tracking
    - Progress monitoring
    - Customized strategies
    - Regular check-ins
    """)

# Project Goals
st.header("🎯 Project Goals")
st.markdown("""
1. Conduct in-depth analysis of social media's impact on mental health
2. Identify patterns in digital behavior affecting well-being
3. Provide targeted interventions and support
4. Create a safe space for mental health discussions
5. Offer practical tools for emotional resilience
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    Your mental health matters. Let us help you on your journey to well-being.
</div>
""", unsafe_allow_html=True) 