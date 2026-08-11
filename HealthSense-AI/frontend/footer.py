"""
frontend/footer.py

Professional footer for HealthSense AI.
"""

import streamlit as st


def show_footer():
    """
    Display the application footer.
    """

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center;padding:20px;">

        <h4 style="color:#0F766E;">
        🩺 HealthSense AI
        </h4>

        <p>
        Empowering Health Decisions Through Responsible AI
        </p>

        <p style="color:gray;font-size:14px;">

        Built with ❤️ using

        Python • Streamlit • Groq • Llama 3.1

        </p>

        <p style="color:gray;font-size:13px;">
        Educational Purposes Only • Not a Substitute for Professional Medical Advice
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )