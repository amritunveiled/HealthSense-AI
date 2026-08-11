"""
frontend/animations.py

Animations and loading effects for HealthSense AI.
"""

import random
import time

import streamlit as st

HEALTH_FACTS = [
    "💧 Staying hydrated may help reduce some headaches.",
    "😴 Adults generally need 7–9 hours of sleep every night.",
    "🥗 A balanced diet supports overall health and immunity.",
    "🚶 Walking for 30 minutes daily benefits heart health.",
    "🧘 Deep breathing exercises can help reduce stress.",
    "🍎 Fruits and vegetables provide essential vitamins and minerals.",
    "❤️ Regular exercise supports cardiovascular health.",
    "☀️ Vitamin D is important for healthy bones and muscles.",
]


def show_ai_thinking():
    """
    Premium AI thinking animation.
    """

    placeholder = st.empty()

    with placeholder.container():
        st.markdown(
            """
            <div class="glass-card">
                <h3>🤖 HealthSense AI is analyzing your question...</h3>
                <p>Please wait while we prepare a personalized educational response.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        progress = st.progress(0)

        for i in range(100):
            progress.progress(i + 1)

            if i % 25 == 0:
                st.info(random.choice(HEALTH_FACTS))

            time.sleep(0.015)

    placeholder.empty()


def celebration():
    """
    Display success animation.
    """
    st.balloons()


def success_message():
    """
    Display completion message.
    """
    st.success("✅ Consultation completed successfully!")