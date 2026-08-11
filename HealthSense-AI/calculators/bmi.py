"""
calculators/bmi.py

BMI (Body Mass Index) Calculator for HealthSense AI.
"""

import streamlit as st


def show_bmi_calculator():
    """
    Display the BMI Calculator.
    """

    st.subheader("⚖️ BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI).")

    col1, col2 = st.columns(2)

    with col1:
        height = st.number_input(
            "Height (cm)",
            min_value=50.0,
            max_value=250.0,
            value=170.0,
            step=1.0,
            key="bmi_height",
        )

    with col2:
        weight = st.number_input(
            "Weight (kg)",
            min_value=10.0,
            max_value=300.0,
            value=70.0,
            step=0.5,
            key="bmi_weight",
        )

    if st.button(
        "Calculate BMI",
        use_container_width=True,
        key="bmi_button",
    ):

        height_m = height / 100
        bmi = weight / (height_m ** 2)

        st.session_state.bmi = round(bmi, 1)
        
        st.metric("Your BMI", f"{bmi:.1f}")

        if bmi < 18.5:
            st.info(
                "🔹 Underweight\n\n"
                "Consider consulting a healthcare professional for healthy weight gain advice."
            )

        elif bmi < 25:
            st.success(
                "✅ Normal Weight\n\n"
                "Great! Maintain a balanced diet and regular exercise."
            )

        elif bmi < 30:
            st.warning(
                "🟡 Overweight\n\n"
                "Regular exercise and healthy eating may help improve your BMI."
            )

        else:
            st.error(
                "🔴 Obesity\n\n"
                "Consider consulting a healthcare professional for personalized guidance."
            )

        st.markdown("---")

        st.markdown(
            """
### 📘 BMI Categories

| Category | BMI |
|----------|-----|
| Underweight | Below 18.5 |
| Normal Weight | 18.5 – 24.9 |
| Overweight | 25.0 – 29.9 |
| Obesity | 30.0 and above |
"""
        )

        st.caption(
            "BMI is a general screening tool and does not directly measure body fat or overall health."
        )