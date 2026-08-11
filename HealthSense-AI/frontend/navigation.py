"""
frontend/navigation.py

Navigation manager for HealthSense AI.
"""

import streamlit as st


PAGES = {
    "🏠 Home": "home",
    "💬 AI Consultation": "consultation",
    "📊 Wellness Hub": "dashboard",
    "🧮 Health Tools": "calculators",
    "📄 Report Preview": "report",
}


def initialize_navigation():
    """Initialize page state."""

    if "page" not in st.session_state:
        st.session_state.page = "home"


def get_current_page():
    """Return current page."""
    return st.session_state.page


def set_page(page: str):
    """Change page."""
    st.session_state.page = page