"""
backend/validators.py

Validation utilities for HealthSense AI.
"""

import re

from backend.constants import (
    EMERGENCY_KEYWORDS,
    MAX_QUESTION_LENGTH,
)


def validate_question(question: str) -> tuple[bool, str]:
    """
    Validate the user's health question.

    Returns:
        (is_valid, message)
    """

    if not question:
        return False, "Please enter a question."

    question = question.strip()

    if len(question) == 0:
        return False, "Question cannot be empty."

    if len(question) > MAX_QUESTION_LENGTH:
        return (
            False,
            f"Question cannot exceed {MAX_QUESTION_LENGTH} characters.",
        )

    return True, "Valid question."


def contains_emergency_keywords(question: str) -> bool:
    """
    Check whether the question contains emergency-related keywords.
    """

    question = question.lower()

    return any(keyword in question for keyword in EMERGENCY_KEYWORDS)


def sanitize_input(question: str) -> str:
    """
    Clean unnecessary spaces from the input.
    """

    question = re.sub(r"\s+", " ", question)

    return question.strip()


if __name__ == "__main__":
    sample = "   I have severe chest pain   "

    print("Original :", sample)
    print("Sanitized:", sanitize_input(sample))
    print("Valid    :", validate_question(sample))
    print("Emergency:", contains_emergency_keywords(sample))