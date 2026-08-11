"""
calculators/sleep.py

Sleep Recommendation Calculator for HealthSense AI.
"""

import streamlit as st


def show_sleep_calculator():
    """
    Display sleep recommendation calculator.
    """

    st.subheader("😴 Sleep Recommendation")

    age = st.number_input(
        "Enter your age",
        min_value=1,
        max_value=100,
        value=25,
        step=1,
        key="sleep_age",
    )

    if st.button(
        "Get Sleep Recommendation",
        use_container_width=True,
        key="sleep_button",
    ):

        if age <= 5:
            hours = "10–13 hours"
        elif age <= 12:
            hours = "9–12 hours"
        elif age <= 18:
            hours = "8–10 hours"
        elif age <= 64:
            hours = "7–9 hours"
        else:
            hours = "7–8 hours"

        
        sleep_hours = int(hours.split("–")[0])
        st.session_state.sleep_hours = sleep_hours
        
        st.metric("Recommended Sleep", hours)

        st.success(
            "💤 Maintaining a regular sleep schedule helps improve your overall health."
        )

        st.info(
            "Avoid screens, caffeine, and heavy meals before bedtime for better sleep quality."
        )