"""
frontend/components.py

Reusable premium UI components for HealthSense AI.
"""

import streamlit as st


def hero_section():
    """Display the main hero section."""

    st.markdown(
        """
        <div style='text-align:center;padding:25px;'>

        <h1 class='main-title'>
        🩺 HealthSense AI
        </h1>

        <p class='subtitle'>
        Empowering Health Decisions Through Responsible AI
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


def section_heading(title: str, icon: str = "✨"):
    """Display a section heading."""

    st.markdown(
        f"""
        <h2 style="
            color:#0F766E;
            margin-top:20px;
            margin-bottom:20px;
            font-weight:700;">
            {icon} {title}
        </h2>
        """,
        unsafe_allow_html=True,
    )


def glass_card(title: str, description: str, emoji: str):
    """Premium glass card."""

    st.markdown(
        f"""
        <div class="glass-card">

        <h3>{emoji} {title}</h3>

        <p>{description}</p>

        </div>
        """,
        unsafe_allow_html=True,
    )


def response_card(title: str, content: str):
    """Card for AI responses."""

    st.markdown(
        f"""
        <div class="glass-card">

        <h3 style="color:#0F766E;">
        {title}
        </h3>

        <p style="
        font-size:16px;
        line-height:1.8;">
        {content}
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_card(title: str, value: str, emoji: str):
    """Display a metric card."""

    st.markdown(
        f"""
        <div class="metric-card">

        <h2>{emoji}</h2>

        <h3>{value}</h3>

        <p>{title}</p>

        </div>
        """,
        unsafe_allow_html=True,
    )


def wellness_tip(tip: str):
    """Display today's wellness tip."""

    st.info(f"💡 **Today's Wellness Tip:** {tip}")


def disclaimer():
    """Medical disclaimer."""

    st.warning(
        """
        **Medical Disclaimer**

        HealthSense AI is designed for educational purposes only.

        It does not diagnose diseases or replace professional medical advice.

        Always consult a qualified healthcare professional for medical concerns.
        """
    )