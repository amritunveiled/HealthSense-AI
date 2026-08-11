"""
frontend/sidebar.py

Professional sidebar navigation for HealthSense AI.
"""

import streamlit as st


def show_sidebar():
    """Render the application sidebar."""

    pages = [
        "🏠 Home",
        "💬 AI Consultation",
        "📊 Wellness Dashboard",
        "🧮 Health Calculators",
        "📄 Export Report",
        "ℹ️ About",
    ]

    current_page = st.session_state.get("page", "home")
    current_page_to_label = {
        "home": "🏠 Home",
        "consultation": "💬 AI Consultation",
        "dashboard": "📊 Wellness Dashboard",
        "calculators": "🧮 Health Calculators",
        "report": "📄 Export Report",
        "about": "ℹ️ About",
    }

    default_label = current_page_to_label.get(current_page, "🏠 Home")
    default_index = pages.index(default_label)

    with st.sidebar:

        st.markdown("# 🩺 HealthSense AI")

        st.caption("AI-Powered Health & Wellness")

        st.divider()

        page = st.radio(
            "Navigation",
            pages,
            index=default_index,
        )

        st.divider()

        st.markdown("### 🌿 Healthy Habit Today")

        st.success(
            "Drink at least 8 glasses of water and take a 20-minute walk."
        )

        st.divider()

        st.info(
            "⚠️ HealthSense AI provides educational information only and is not a substitute for professional medical advice."
        )

        return page