import streamlit as st

FOLLOW_UPS = {
    "Headache": [
        "How long have you had the headache?",
        "Is the pain mild, moderate, or severe?",
        "Do you have a fever?",
        "Have you been drinking enough water?"
    ],
    "Fever": [
        "When did the fever start?",
        "Have you checked your temperature?",
        "Do you have chills or body pain?",
        "Are you staying hydrated?"
    ],
    "Better Sleep": [
        "How many hours do you usually sleep?",
        "Do you use your phone before bedtime?",
        "Do you consume caffeine at night?"
    ],
    "Nutrition": [
        "How many meals do you eat daily?",
        "Do you eat fruits and vegetables regularly?",
        "How much water do you drink every day?"
    ]
}


def show_follow_up(topic: str):

    questions = FOLLOW_UPS.get(
        topic,
        [
            "Can you tell us more about your concern?",
            "How long have you noticed this?",
            "Have you tried anything to improve it?"
        ]
    )

    st.subheader("🤖 AI Guided Questions")

    answers = {}

    for question in questions:
        answers[question] = st.text_input(question)

    submitted = st.button(
        "✅ Submit Answers",
        use_container_width=True
    )

    return submitted, answers