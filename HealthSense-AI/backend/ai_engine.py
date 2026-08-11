"""
backend/ai_engine.py

Handles communication with the Groq LLM.
"""

from groq import Groq

from backend.config import load_groq_api_key, get_model_name
from backend.prompts import SYSTEM_PROMPT, build_user_prompt


class AIEngine:
    """
    Handles all AI interactions.
    """

    def __init__(self):
        self.client = Groq(api_key=load_groq_api_key())
        self.model = get_model_name()

    def ask(self, question: str) -> str:
        """
        Send a health question to the Groq model and
        return the AI-generated response.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": build_user_prompt(question),
                },
            ],
            temperature=0.4,
            max_tokens=1024,
        )

        return response.choices[0].message.content


if __name__ == "__main__":
    engine = AIEngine()

    question = input("Ask a health question: ")

    print("\nGenerating response...\n")

    answer = engine.ask(question)

    print(answer)