"""
frontend/quick_topics.py

Beautiful Quick Health Topics section.
"""

import streamlit as st


TOPICS = [
    ("🤕", "Headache", "Common causes and prevention"),
    ("🤒", "Fever", "Understand fever and self-care"),
    ("😴", "Better Sleep", "Improve your sleep quality"),
    ("💧", "Hydration", "Stay hydrated every day"),
    ("🥗", "Nutrition", "Healthy eating habits"),
    ("❤️", "Heart Health", "Lifestyle for a healthy heart"),
    ("🧘", "Mental Wellness", "Stress management tips"),
    ("🏃", "Fitness", "Daily exercise guidance"),
]


TOPIC_PROMPTS = {
    "Headache": "I have a headache and would like advice.",
    "Fever": "I have a fever and would like advice.",
    "Better Sleep": "I want help improving my sleep.",
    "Hydration": "I want help staying hydrated.",
    "Nutrition": "I want guidance on healthy eating.",
    "Heart Health": "I want tips for better heart health.",
    "Mental Wellness": "I want support with stress and mental wellness.",
    "Fitness": "I want guidance for daily exercise and fitness.",
}


def show_quick_topics():
    """
    Display clickable health topic cards.
    """

    st.markdown("## ✨ Explore Popular Health Topics")

    cols = st.columns(4)

    for index, topic in enumerate(TOPICS):

        icon, title, subtitle = topic

        with cols[index % 4]:

            st.markdown(
                f"""
                <div class="glass-card">

                <h2 style="text-align:center;">
                {icon}
                </h2>

                <h3 style="text-align:center;">
                {title}
                </h3>

                <p style="text-align:center;">
                {subtitle}
                </p>

                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                f"Explore {title}",
                key=title,
                use_container_width=True,
            ):
                st.session_state.selected_topic = title
                st.session_state.question = TOPIC_PROMPTS.get(
                    title,
                    f"I would like advice about {title.lower()}.",
                )
                st.session_state.show_followups = True
                st.session_state.page = "consultation"