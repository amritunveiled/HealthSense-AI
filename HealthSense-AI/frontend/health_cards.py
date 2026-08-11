"""
frontend/health_cards.py

Premium response cards for HealthSense AI.
"""

import streamlit as st


def health_card(title: str, icon: str, content: str):
    """Displays a premium health information card."""

    st.markdown(
        f"""
        <div class="glass-card">
            <h3>{icon} {title}</h3>
            <div style="line-height:1.8;font-size:16px;">
                {content}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_response_sections(response_sections: dict):
    """
    Display all AI response sections beautifully.

    Example:
    {
        "Explanation": "...",
        "Possible Causes": "...",
        "Healthy Habits": "...",
        ...
    }
    """

    icons = {
        "Explanation": "🩺",
        "Possible Causes": "⚠️",
        "Prevention Tips": "🛡️",
        "Healthy Habits": "🌱",
        "Nutrition Tips": "🥗",
        "Hydration Advice": "💧",
        "Sleep Suggestions": "😴",
        "When to Consult a Doctor": "👨‍⚕️",
        "Disclaimer": "📌",
    }

    for title, content in response_sections.items():
        health_card(
            title,
            icons.get(title, "✨"),
            content,
        )