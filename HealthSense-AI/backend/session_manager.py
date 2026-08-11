"""
backend/session_manager.py

Maintains the conversation history and manages
personalized follow-up interactions.
"""


class SessionManager:
    """
    Stores conversation history during the current session.
    """

    def __init__(self):
        self.chat_history = []
        self.follow_up_answers = {}

    def add_user_message(self, message: str):
        self.chat_history.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_ai_message(self, message: str):
        self.chat_history.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def save_follow_up(self, question: str, answer: str):
        self.follow_up_answers[question] = answer

    def get_follow_up_answers(self):
        return self.follow_up_answers

    def get_chat_history(self):
        return self.chat_history

    def clear_session(self):
        self.chat_history.clear()
        self.follow_up_answers.clear()

    def conversation_length(self):
        return len(self.chat_history)


if __name__ == "__main__":
    session = SessionManager()

    session.add_user_message("I have a headache.")
    session.add_ai_message("How long have you had it?")

    session.save_follow_up(
        "How long have you had it?",
        "Two days",
    )

    print(session.get_chat_history())
    print(session.get_follow_up_answers())