import streamlit as st
import os
from dotenv import load_dotenv
from orchestrator import route_to_agent

# Load environment variables
load_dotenv()

# Set page config with a wider layout and custom theme
st.set_page_config(
    page_title="NLP Multi-Agent Education Tutor",
    page_icon="\U0001F4D8",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: none;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .css-1d391kg {
        padding: 1rem;
        border-radius: 5px;
        background-color: #f0f2f6;
    }
    h1 {
        color: #1E88E5;
        padding-bottom: 1rem;
        border-bottom: 2px solid #1E88E5;
    }
    .stSelectbox {
        background-color: white;
    }
    .output-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        margin-top: 1rem;
    }
    .stSelectbox label {
        margin-top: -1rem; /* Adjust this value as needed */
        display: block; /* Important for margin to work correctly */
    }
    </style>
    """, unsafe_allow_html=True)

# Check for required API keys
required_keys = {
    "TOGETHER_API_KEY": "Story Tutor (Together API)",
    "GROQ_API_KEY": "Quiz Tutor (Groq API)",
    "GOOGLE_API_KEY": "Visual Tutor (Gemini API)"
}

missing_keys = [key for key, name in required_keys.items() if not os.getenv(key)]
if missing_keys:
    st.error("⚠️ Missing API Keys!")
    st.markdown("""
        <div style='background-color: #fff3cd; padding: 1rem; border-radius: 5px; border: 1px solid #ffeeba;'>
            <h4 style='color: #856404; margin: 0;'>Please add the following API keys to your .env file:</h4>
        </div>
    """, unsafe_allow_html=True)
    for key in missing_keys:
        st.markdown(f"<div style='margin-left: 1rem;'>• {key} (for {required_keys[key]})</div>", unsafe_allow_html=True)
    st.stop()

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.title("\U0001F4D8 NLP Multi-Agent Education Tutor")
    st.markdown("""
        <div style='font-size: 1.2rem; color: #666; margin-bottom: 2rem;'>
            Learn any topic in your preferred style! Our AI tutors adapt to your learning preferences.
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='background-color: #e3f2fd; padding: 1rem; border-radius: 10px; margin-bottom: 1rem;'>
            <h4 style='color: #1565C0; margin: 0;'>Available Learning Styles:</h4>
            <ul style='margin: 0.5rem 0; color: black;'>
                <li>\U0001F9E0 Logical - Step-by-step explanations</li>
                <li>\U0001F3A8 Visual - Analogies and diagrams</li>
                <li>\U0001F3AD Story - Learning through stories</li>
                <li>\U0001F4CA Quiz - Test your knowledge</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Input section with better styling
st.markdown("---")
st.markdown("### \U0001F4D6 Start Learning")

# Create two columns for input fields
input_col1, input_col2 = st.columns([3, 2])

with input_col1:
    topic = st.text_input(
        "Enter a topic you want to learn about:",
        placeholder="e.g., Photosynthesis, Quantum Physics, World War II...",
        help="Type any topic you'd like to learn about"
    )

with input_col2:
    style = st.selectbox(
        "Choose your learning style:",
        ("logical", "visual", "story", "quiz", "story_quiz", "visual_quiz", "visual_story"),
        format_func=lambda x: {
            "logical": "\U0001F9E0 Logical (step-by-step)",
            "visual": "\U0001F3A8 Visual (analogies/diagrams)",
            "story": "\U0001F3AD Story (via stories)",
            "quiz": "\U0001F4CA Quiz (questions)",
            "story_quiz": "\U0001F3AD Story + \U0001F4CA Quiz (story with questions)",
            "visual_quiz": "\U0001F3A8 Visual + \U0001F4CA Quiz (visual with questions)",
            "visual_story": "\U0001F3A8 Visual + \U0001F3AD Story (visual with story)"
        }[x],
        help="Select how you'd like to learn this topic"
    )

# Center the button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("Teach Me! \U0001F4DA", use_container_width=True):
        if not topic:
            st.warning("Please enter a topic to begin learning.")
        else:
            try:
                with st.spinner("Generating your lesson..."):
                    st.markdown("""
                        <div style='text-align: center;'>
                            <div style='font-size: 1.2rem; margin-bottom: 0.5rem;'>Generating your lesson...</div>
                            <div style='color: #666;'>This may take a few moments</div>
                        </div>
                    """, unsafe_allow_html=True)
                    result = route_to_agent(topic, style)
                
                st.markdown("---")
                st.markdown("""
                    <div class='output-box'>
                        <h3 style='color: #1E88E5; margin-top: 0;'>\U0001F393 Your Tailored Learning Output</h3>
                """, unsafe_allow_html=True)
                st.markdown(result)
                st.markdown("</div>", unsafe_allow_html=True)
                
            except Exception as e:
                st.error("""
                    <div style='background-color: #fde8e8; padding: 1rem; border-radius: 5px; border: 1px solid #fbd5d5;'>
                        <h4 style='color: #c53030; margin: 0;'>An error occurred</h4>
                        <p style='color: #742a2a; margin: 0.5rem 0;'>{}</p>
                        <p style='color: #742a2a; margin: 0;'>Please check your API keys and internet connection.</p>
                    </div>
                """.format(str(e)), unsafe_allow_html=True)

# Add a footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9rem;'>
        Powered by AI Education Tutors | Made with \U0001F49A
    </div>
""", unsafe_allow_html=True) 