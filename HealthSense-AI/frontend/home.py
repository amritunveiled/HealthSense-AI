"""
frontend/home.py

Premium landing page for HealthSense AI.
"""

import streamlit as st


def _go_to(page: str):
    """Navigate to one of the app pages."""

    st.session_state.page = page


def show_home():
    """Render the landing page."""

    st.markdown(
        """
        <div class="main-title float">
            🩺 HealthSense AI
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="subtitle">
            Your Personal AI-Powered Health & Wellness Companion
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### 🩺 AI Health Consultation")
            st.write(
                "Ask health and wellness questions and receive structured educational guidance powered by Groq AI."
            )
            st.button(
                "Open consultation",
                key="home_consultation_link",
                on_click=_go_to,
                args=("consultation",),
                width="stretch",
            )

    with col2:
        with st.container(border=True):
            st.markdown("### 📊 Wellness Dashboard")
            st.write(
                "Track BMI, water intake, sleep goals and healthy lifestyle recommendations in one place."
            )
            st.button(
                "Open dashboard",
                key="home_dashboard_link",
                on_click=_go_to,
                args=("dashboard",),
                width="stretch",
            )

    with col3:
        with st.container(border=True):
            st.markdown("### 📄 Smart Health Reports")
            st.write(
                "Export beautifully formatted reports of every consultation for future reference."
            )
            st.button(
                "Open report export",
                key="home_report_link",
                on_click=_go_to,
                args=("report",),
                width="stretch",
            )

    st.write("")

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center;font-size:24px;font-weight:600;">
            🌱 Small healthy choices today create a healthier tomorrow.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")

    if st.button("🚀 Start Health Consultation"):
        st.session_state.page = "consultation"