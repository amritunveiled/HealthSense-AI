"""
frontend/theme.py

Loads the premium UI theme for HealthSense AI.
"""

from pathlib import Path

import streamlit as st


def load_theme() -> None:
    """
    Configure the Streamlit page and load custom CSS.
    """

    st.set_page_config(
        page_title="HealthSense AI",
        page_icon="🩺",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    css_path = Path(__file__).parent.parent / "assets" / "styles.css"

    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as css_file:
            st.markdown(
                f"<style>{css_file.read()}</style>",
                unsafe_allow_html=True,
            )