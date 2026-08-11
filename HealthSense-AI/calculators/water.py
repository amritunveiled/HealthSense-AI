"""
calculators/water.py

Daily Water Intake Calculator for HealthSense AI.
"""

import streamlit as st


def show_water_calculator():
    """
    Display the daily water intake calculator.
    """

    st.subheader("💧 Daily Water Intake Calculator")
    st.write("Estimate your recommended daily water intake.")

    weight = st.number_input(
        "Enter your weight (kg)",
        min_value=10.0,
        max_value=300.0,
        value=70.0,
        step=0.5,
        key="water_weight",
    )

    activity = st.selectbox(
        "Activity Level",
        [
            "Low",
            "Moderate",
            "High",
        ],
        key="water_activity",
    )

    if st.button(
        "Calculate Water Intake",
        use_container_width=True,
        key="water_button",
    ):

        water_ml = weight * 35

        if activity == "Moderate":
            water_ml += 500
        elif activity == "High":
            water_ml += 1000

        liters = water_ml / 1000
        glasses = round(water_ml / 250)

        st.session_state.water_glasses = glasses

        st.metric(
            "Recommended Water Intake",
            f"{liters:.1f} L/day",
        )

        st.success(
            f"🥤 Approximately {glasses} glasses of water per day."
        )

        st.info(
            "💡 Your water needs may increase in hot weather, during exercise, or if you're unwell."
        )