import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

# Set page configuration with a custom icon and wider layout
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="centered")

# Custom CSS for improved styling
st.markdown("""
    <style>
    .main-title {
        color: #2E86C1;
        font-size: 2.5em;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subtitle {
        color: #34495E;
        font-size: 1.2em;
        text-align: center;
        margin-bottom: 1.5em;
    }
    .stButton>button {
        background-color: #2E86C1;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1B4F72;
        color: white;
    }
    .stTextInput>div>input {
        border: 2px solid #D5DBDB;
        border-radius: 8px;
    }
    .itinerary-box {
        background-color: #000000;
        padding: 1.5em;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Header with improved styling
st.markdown('<div class="main-title">AI Travel Itinerary Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Plan your perfect day trip by entering your city and interests</div>', unsafe_allow_html=True)

# Environment setup
load_dotenv()

# Form with improved layout and placeholders
with st.form("planner_form"):
    st.markdown("### Plan Your Trip")
    city = st.text_input("City", placeholder="e.g., Paris, New York", help="Enter the city you want to visit")
    interests = st.text_input("Interests", placeholder="e.g., art, food, history", help="Enter your interests, separated by commas")
    submitted = st.form_submit_button("Generate Itinerary")

    if submitted:
        if city and interests:
            with st.spinner("Generating your itinerary..."):
                planner = TravelPlanner()
                planner.set_city(city)
                planner.set_interests(interests)
                itinerary = planner.create_itineary()  # Keeping original method name

            st.subheader("📍 Your Day Trip Itinerary")
            st.markdown(f'<div class="itinerary-box">{itinerary}</div>', unsafe_allow_html=True)
        else:
            st.error("Please fill in both City and Interests to proceed.")
