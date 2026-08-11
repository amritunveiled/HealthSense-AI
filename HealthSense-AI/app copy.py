"""
HealthSense AI

Main Streamlit Application
"""

# ==========================================================
# IMPORTS
# ==========================================================

import streamlit as st

# ---------------- Backend ----------------

from backend.consultation_manager import ConsultationManager
from backend.exporter import ReportExporter
from backend.formatter import format_ai_response

# ---------------- Frontend ----------------

from frontend.theme import load_theme
from frontend.home import show_home
from frontend.sidebar import show_sidebar
from frontend.dashboard import show_dashboard
from frontend.chatbot_ui import (
    consultation_header,
    quick_question_box,
    consultation_buttons,
)
from frontend.quick_topics import show_quick_topics
from frontend.followup_flow import show_follow_up
from frontend.report_view import show_report_preview
from frontend.footer import show_footer
from frontend.animations import (
    show_ai_thinking,
    celebration,
    success_message,
)
from frontend.navigation import (
    initialize_navigation,
    get_current_page,
    set_page,
)

# ---------------- Calculators ----------------

from calculators import (
    show_bmi_calculator,
    show_water_calculator,
    show_sleep_calculator,
    show_exercise_calculator,
)

# ==========================================================
# LOAD THEME
# ==========================================================

load_theme()

# ==========================================================
# INITIALIZE NAVIGATION
# ==========================================================

initialize_navigation()

# ==========================================================
# SESSION STATE
# ==========================================================

DEFAULTS = {
    "question": "",
    "response": "",
    "selected_topic": "",
    "follow_up_answers": {},
    "report_ready": False,
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ==========================================================
# BACKEND OBJECTS
# ==========================================================

consultation_manager = ConsultationManager()
report_exporter = ReportExporter()

# ==========================================================
# SIDEBAR
# ==========================================================

selected_page = show_sidebar()

PAGE_MAP = {
    "🏠 Home": "home",
    "💬 AI Consultation": "consultation",
    "📊 Wellness Dashboard": "dashboard",
    "🧮 Health Calculators": "calculators",
    "📄 Export Report": "report",
    "ℹ️ About": "about",
}

if selected_page in PAGE_MAP:
    set_page(PAGE_MAP[selected_page])

current_page = get_current_page()



# ==========================================================
# HOME PAGE
# ==========================================================

def render_home():
    """
    Render the Home page.
    """

    show_home()

    st.write("")

    show_quick_topics()

    st.write("")

    show_footer()




# ==========================================================
# CONSULTATION PAGE
# ==========================================================

def render_consultation():
    """
    Render the AI Consultation page.
    """

    consultation_header()

    st.write("")

    question = quick_question_box()

    ask_button, clear_button = consultation_buttons()

    if clear_button:
        st.session_state.question = ""
        st.session_state.response = ""
        st.session_state.follow_up_answers = {}
        st.rerun()

    if ask_button:

        if not question.strip():

            st.warning("Please enter your health question.")

            return

        st.session_state.question = question

        topic = "General"

        lower_question = question.lower()

        if "headache" in lower_question:
            topic = "Headache"

        elif "fever" in lower_question:
            topic = "Fever"

        elif "sleep" in lower_question:
            topic = "Better Sleep"

        elif (
            "nutrition" in lower_question
            or "diet" in lower_question
            or "food" in lower_question
        ):
            topic = "Nutrition"

        answers = show_follow_up(topic)

        if st.button(
            "Generate AI Response",
            use_container_width=True,
        ):
            st.session_state.follow_up_answers = answers

            show_ai_thinking()
            try:

                response = consultation_manager.get_ai_response(
                    st.session_state.question,
                    st.session_state.follow_up_answers,
                )

                response = format_ai_response(response)

                st.session_state.response = response

                st.session_state.report_ready = True

                celebration()

                success_message()

            except Exception as error:

                st.error(f"Error: {error}")

    if st.session_state.response:

        st.markdown("---")

        st.subheader("🩺 AI Health Guidance")

        st.markdown(st.session_state.response)

    show_footer()

# ==========================================================
# DASHBOARD PAGE
# ==========================================================

def render_dashboard():
    """
    Render the Wellness Dashboard.
    """
    show_dashboard()
    show_footer()


# ==========================================================
# CALCULATORS PAGE
# ==========================================================

def render_calculators():
    """
    Render all Health Calculators.
    """

    st.title("🧮 Health Calculators")

    calculator = st.selectbox(
        "Choose a Calculator",
        [
            "BMI Calculator",
            "Water Intake Calculator",
            "Sleep Recommendation",
            "Exercise Recommendation",
        ],
    )

    st.markdown("---")

    if calculator == "BMI Calculator":
        show_bmi_calculator()

    elif calculator == "Water Intake Calculator":
        show_water_calculator()

    elif calculator == "Sleep Recommendation":
        show_sleep_calculator()

    elif calculator == "Exercise Recommendation":
        show_exercise_calculator()

    show_footer()


# ==========================================================
# REPORT PAGE
# ==========================================================

def render_report():
    """
    Render Report Preview.
    """

    if (
        st.session_state.question
        and st.session_state.response
    ):

        show_report_preview(
            st.session_state.question,
            st.session_state.response,
        )

    else:

        st.info(
            "Complete an AI consultation first to generate a report."
        )

    show_footer()


# ==========================================================
# ABOUT PAGE
# ==========================================================

def render_about():
    """
    Render About page.
    """

    st.title("ℹ️ About HealthSense AI")

    st.markdown(
        """
### 🩺 HealthSense AI

HealthSense AI is an AI-powered educational health assistant designed to help users better understand health and wellness topics.

### ✨ Features

- 🤖 AI Consultation
- 📊 Wellness Dashboard
- 🧮 Health Calculators
- 📄 Report Generation
- 🌱 Healthy Lifestyle Guidance

### ⚠️ Medical Disclaimer

This application provides educational information only.

It does **not** diagnose diseases, prescribe medications, or replace professional medical advice.

Always consult a qualified healthcare professional for diagnosis and treatment.
"""
    )

    show_footer()


# ==========================================================
# APPLICATION ROUTING
# ==========================================================

if current_page == "home":

    render_home()

elif current_page == "consultation":

    render_consultation()

elif current_page == "dashboard":

    render_dashboard()

elif current_page == "calculators":

    render_calculators()

elif current_page == "report":

    render_report()

elif current_page == "about":

    render_about()

else:

    render_home()