import streamlit as st


def display_thoughts(thoughts):
    st.subheader("Agent's Thought Process")
    for i, thought in enumerate(thoughts, 1):
        st.write(f"{i}. {thought}")


def display_final_plan(plan):
    st.subheader("Your Personalized Trip Plan")
    st.write(plan)

    # Display plan sections
    sections = ["Itinerary", "Accommodations", "Transportation", "Activities", "Budget Breakdown"]
    for section in sections:
        with st.expander(section):
            st.write(f"Details for {section} go here...")  # Replace with actual content


def display_budget_tracker(initial_budget, current_budget):
    st.sidebar.subheader("Budget Tracker")
    progress = (current_budget / initial_budget) * 100
    st.sidebar.progress(progress)
    st.sidebar.write(f"Remaining Budget: ${current_budget:.2f}")


def display_action_result(action, result):
    with st.expander(f"Action: {action}"):
        st.write(result)


def get_user_preferences():
    st.subheader("Travel Preferences")
    preferences = {}
    preferences['destination'] = st.text_input("Preferred destination")
    preferences['duration'] = st.number_input("Trip duration (days)", min_value=1, max_value=30, value=7)
    preferences['budget'] = st.number_input("Budget ($)", min_value=100, max_value=10000, value=2000)
    preferences['interests'] = st.multiselect(
        "Interests",
        ["Culture", "Nature", "Adventure", "Relaxation", "Food", "Shopping"]
    )
    return preferences