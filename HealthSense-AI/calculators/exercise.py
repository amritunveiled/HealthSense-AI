"""
calculators/exercise.py

Exercise Recommendation Calculator for HealthSense AI.
"""

import streamlit as st


def show_exercise_calculator():
    """
    Display personalized exercise recommendations.
    """

    st.subheader("🏃 Exercise Recommendation")

    age = st.number_input(
        "Enter your age",
        min_value=1,
        max_value=100,
        value=25,
        step=1,
        key="exercise_age",
    )

    goal = st.selectbox(
        "Select Your Goal",
        [
            "Stay Healthy",
            "Weight Loss",
            "Build Muscle",
            "Improve Fitness",
        ],
        key="exercise_goal",
    )

    if st.button(
        "Get Exercise Plan",
        use_container_width=True,
        key="exercise_button",
    ):

        if goal == "Stay Healthy":
            recommendation = (
                "• 30 minutes brisk walking\n"
                "• Light stretching\n"
                "• 5 days per week"
            )

        elif goal == "Weight Loss":
            recommendation = (
                "• 45–60 minutes cardio\n"
                "• Strength training 3 days/week\n"
                "• Stay hydrated"
            )

        elif goal == "Build Muscle":
            recommendation = (
                "• Strength training 4–5 days/week\n"
                "• Progressive overload\n"
                "• Adequate protein intake"
            )

        else:
            recommendation = (
                "• Mix cardio and strength training\n"
                "• Improve flexibility\n"
                "• Stay consistent"
            )

        if goal == "Stay Healthy":
            st.session_state.exercise_minutes = 150
        elif goal == "Weight Loss":
            st.session_state.exercise_minutes = 300
        elif goal == "Build Muscle":
            st.session_state.exercise_minutes = 240
        else:
            st.session_state.exercise_minutes = 180


        st.metric(
            "Recommended Weekly Exercise",
            "150–300 mins",
        )

        st.success(recommendation)

        st.info(
            f"💪 At age {age}, consistency, proper recovery, and good nutrition are key to long-term fitness."
        )