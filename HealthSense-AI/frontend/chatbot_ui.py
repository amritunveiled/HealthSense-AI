"""
frontend/chatbot_ui.py

Premium AI Consultation Interface.
"""

import streamlit as st


def consultation_header():
    """Display the consultation hero."""

    st.markdown(
        """
        <div class="glass-card">

        <h1 style="color:#0F766E;text-align:center;">
        🩺 Guided AI Health Consultation
        </h1>

        <p style="
        text-align:center;
        font-size:18px;
        color:#475569;
        ">

        Tell us what's bothering you.

        Our AI will ask a few simple follow-up questions
        before providing educational health guidance.

        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


def quick_question_box():
    """Question input."""

    question = st.text_area(
        "Describe your health concern",
        height=140,
        placeholder="Example: I have had a headache since yesterday...",
    )

    return question


def consultation_buttons():

    col1, col2 = st.columns([4, 1])

    with col1:

        ask = st.button(
            "🚀 Start AI Consultation",
            use_container_width=True,
        )

    with col2:

        clear = st.button(
            "🗑",
            use_container_width=True,
        )

    return ask, clear


def loading_animation():

    with st.spinner("🩺 AI is analyzing your health question..."):

        pass


def show_typing():

    st.info(
        "🤖 HealthSense AI is preparing your personalized educational response..."
    )


def show_response(response: str):

    st.markdown("## 🩺 Consultation Result")

    st.markdown(
        f"""
        <div class="glass-card">

        {response}

        </div>
        """,
        unsafe_allow_html=True,
    )


def follow_up_box(question: str):

    st.markdown("### 🤖 Follow-up Question")

    answer = st.radio(

        question,

        ["Yes", "No"],

        horizontal=True,

    )

    return answer