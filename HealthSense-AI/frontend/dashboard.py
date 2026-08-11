"""
frontend/dashboard.py

Premium Wellness Dashboard for HealthSense AI.
"""

import streamlit as st


def _sync_habit_progress():
    """Keep the habit summary in sync with the checkbox state."""

    habit_keys = [
        "habit_drink",
        "habit_walk",
        "habit_fruits",
        "habit_sleep",
        "habit_breathing",
    ]

    completed = sum(1 for key in habit_keys if st.session_state.get(key, False))
    total = len(habit_keys)

    st.session_state.water_glasses = 8 if st.session_state.get("habit_drink", False) else 0
    st.session_state.sleep_hours = 7 if st.session_state.get("habit_sleep", False) else 0
    st.session_state.exercise_minutes = 150 if st.session_state.get("habit_walk", False) else 0

    st.session_state.habit_completed = completed
    st.session_state.habit_completion_rate = round((completed / total) * 100) if total else 0
    st.session_state.habit_score = completed * 5


def show_dashboard():
    """
    Display the Wellness Dashboard.
    """

    # =====================================================
    # Initialize habit completion state
    # =====================================================

    st.session_state.setdefault("habit_drink", False)
    st.session_state.setdefault("habit_walk", False)
    st.session_state.setdefault("habit_fruits", False)
    st.session_state.setdefault("habit_sleep", False)
    st.session_state.setdefault("habit_breathing", False)

    _sync_habit_progress()

    # =====================================================
    # Get live values from session state
    # =====================================================

    water = st.session_state.get("water_glasses", 0)
    sleep = st.session_state.get("sleep_hours", 0)
    exercise = st.session_state.get("exercise_minutes", 0)
    bmi = st.session_state.get("bmi", 0.0)

    # =====================================================
    # Calculate Wellness Score
    # =====================================================

    score = 0

    if water >= 8:
        score += 25

    if sleep >= 7:
        score += 25

    if exercise >= 150:
        score += 25

    if 18.5 <= bmi <= 24.9:
        score += 25

    score = min(100, score + st.session_state.habit_score)

    if score >= 80:
        status = "🟢 Excellent"

    elif score >= 60:
        status = "🟡 Good"

    elif score >= 40:
        status = "🟠 Fair"

    else:
        status = "🔴 Needs Attention"

    # =====================================================
    st.markdown("# 📊 Wellness Dashboard")
    st.markdown(
        "Track your daily wellness goals and healthy habits."
    )

    # =====================================================
    # Metrics
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "💧 Water Intake",
            f"{water}/8 Glasses",
            "Live",
        )

    with col2:

        st.metric(
            "😴 Sleep",
            f"{sleep} Hours",
            "Live",
        )

    with col3:

        st.metric(
            "🏃 Exercise",
            f"{exercise} mins/week",
            "Live",
        )

    with col4:

        st.metric(
            "❤️ Wellness Score",
            f"{score}/100",
            status,
        )

    with st.container(horizontal=True):
        st.metric(
            "🌿 Habit Completion",
            f"{st.session_state.habit_completed}/5",
            f"{st.session_state.habit_completion_rate}%",
            border=True,
        )

        st.metric(
            "✅ Habit Score",
            f"{st.session_state.habit_score}/25",
            "Live",
            border=True,
        )

    # =====================================================
    # Progress
    # =====================================================

    st.divider()

    st.subheader("📈 Today's Progress")

    progress = score / 100

    st.progress(
        progress,
        text=f"Overall Wellness Progress : {score}%",
    )

    # =====================================================
    # Healthy Habits
    # =====================================================

    st.divider()

    st.subheader("🌿 Today's Healthy Habits")

    drink = st.checkbox(
        "Drink at least 8 glasses of water",
        key="habit_drink",
        on_change=_sync_habit_progress,
    )

    walk = st.checkbox(
        "Walk for 30 minutes",
        key="habit_walk",
        on_change=_sync_habit_progress,
    )

    fruits = st.checkbox(
        "Eat fruits and vegetables",
        key="habit_fruits",
        on_change=_sync_habit_progress,
    )

    sleep_box = st.checkbox(
        "Sleep 7–9 hours",
        key="habit_sleep",
        on_change=_sync_habit_progress,
    )

    breathing = st.checkbox(
        "Practice deep breathing for 5 minutes",
        key="habit_breathing",
        on_change=_sync_habit_progress,
    )

    completed = st.session_state.habit_completed

    st.caption(
        "Checking a habit updates the dashboard score and completion count immediately."
    )

    # =====================================================
    # Motivation
    # =====================================================

    st.divider()

    if completed == 5:

        st.success(
            "🎉 Amazing! You completed all today's healthy habits."
        )

    elif completed >= 3:

        st.success(
            f"🌟 Great job! You completed {completed} of 5 healthy habits today."
        )

    else:

        st.info(
            "💪 Keep going! Every healthy habit contributes to your wellness."
        )

    # =====================================================
    # Health Tip
    # =====================================================

    st.divider()

    tips = [
        "💧 Drink water before meals to stay hydrated.",
        "🥗 Include fruits and vegetables in every meal.",
        "😴 Aim for consistent sleep every night.",
        "🚶 A short walk after meals improves digestion.",
        "🧘 Take a few minutes every day to relax and breathe deeply.",
    ]

    import random

    st.info(random.choice(tips))

    # =====================================================
    # Last Updated
    # =====================================================

    from datetime import datetime

    st.caption(
        f"Last Updated: {datetime.now().strftime('%d %b %Y • %I:%M %p')}"
    )