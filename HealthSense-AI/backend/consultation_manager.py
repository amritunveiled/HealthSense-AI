"""
backend/consultation_manager.py

Manages the complete AI consultation workflow.
"""

from backend.ai_engine import AIEngine


class ConsultationManager:
    """
    Handles the end-to-end consultation flow.
    """

    def __init__(self):
        self.ai = AIEngine()

    def build_consultation_prompt(
        self,
        question: str,
        follow_up_answers: dict,
    ) -> str:
        """
        Combine the user's question and follow-up answers into
        a single prompt for the AI.
        """

        prompt = f"Health Question:\n{question}\n\n"

        if follow_up_answers:
            prompt += "Additional Information:\n"

            for key, value in follow_up_answers.items():
                prompt += f"- {key}: {value}\n"

        return prompt

    def get_ai_response(
        self,
        question: str,
        follow_up_answers: dict,
    ) -> str:

        prompt = self.build_consultation_prompt(
            question,
            follow_up_answers,
        )

        return self.ai.ask(prompt)