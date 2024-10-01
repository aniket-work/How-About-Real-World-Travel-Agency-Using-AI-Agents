import streamlit as st
import yaml
import json
from agent import TravelAgent
from loguru import logger


def load_config():
    with open('config/config.json') as f:
        return json.load(f)


def load_settings():
    with open('config/settings.yaml') as f:
        return yaml.safe_load(f)


def display_travel_plan(plan):
    st.markdown(f"```\n{plan}\n```")


def main():
    st.set_page_config(page_title="AI Agent Travel Planner", page_icon="✈️", layout="wide")

    # Custom CSS for a more professional look
    st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 2rem;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1 {
        color: #2c3e50;
        font-weight: 700;
    }
    .stTextInput, .stTextArea {
        background-color: white;
        border-radius: 5px;
        border: 1px solid #bdc3c7;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        font-weight: 600;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    .css-1v0mbdj.etr89bj1 {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("img/logo.png", width=150)
        st.title("AI Agent Travel Agency")
        st.write("Welcome to our professional travel planning service. Let us help you create your perfect trip.")

    config = load_config()
    settings = load_settings()

    agent = TravelAgent(config['system_prompt'], settings['initial_budget'])

    user_input = st.text_area("Describe your ideal trip:")
    if st.button("Plan My Trip"):
        if user_input:
            with st.spinner("Planning your perfect journey..."):
                result = agent.plan_trip(user_input)

                with st.expander("View Agent's Thought Process"):
                    for i, thought in enumerate(agent.get_thoughts(), 1):
                        st.write(f"{i}. {thought}")

                st.subheader("Your Customized Travel Itinerary")
                display_travel_plan(result)

                col1, col2 = st.columns(2)
                with col1:
                    st.download_button("Download Itinerary (TXT)", result, "trip_itinerary.txt")
                with col2:
                    st.download_button("Download Itinerary (PDF)", result, "trip_itinerary.pdf")
        else:
            st.warning("Please provide some details about your desired trip.")

    st.markdown("---")
    st.markdown("© 2024 AI Agent Travel Planner. All rights reserved.")


if __name__ == "__main__":
    logger.info("Launching AI Agent Travel Planner application")
    main()