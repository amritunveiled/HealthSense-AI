"""
backend/constants.py

Application-wide constants used throughout HealthSense AI.
Keeping all constant values in one place makes the project
clean, maintainable, and easy to update.
"""

from pathlib import Path

# ==========================================================
# APPLICATION INFORMATION
# ==========================================================

APP_NAME: str = "HealthSense AI"

APP_VERSION: str = "1.0.0"

APP_TAGLINE: str = (
    "Your AI-Powered Health & Wellness Companion"
)

APP_DESCRIPTION: str = (
    "An AI-powered educational health assistant "
    "that provides responsible wellness guidance."
)

# ==========================================================
# AI MODEL CONFIGURATION
# ==========================================================

DEFAULT_MODEL: str = "llama-3.1-8b-instant"

AI_TEMPERATURE: float = 0.4

MAX_RESPONSE_TOKENS: int = 1024

# ==========================================================
# FILE & DIRECTORY PATHS
# ==========================================================

PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent

KEY_VAULT_DIR: Path = PROJECT_ROOT / "key-vault"

API_KEY_FILE: Path = KEY_VAULT_DIR / "groq-api.key"

EXPORTS_DIR: Path = PROJECT_ROOT / "exports"

ASSETS_DIR: Path = PROJECT_ROOT / "assets"

# ==========================================================
# CHAT SETTINGS
# ==========================================================

MAX_QUESTION_LENGTH: int = 1000

MAX_CHAT_HISTORY: int = 20

# ==========================================================
# EXPORT SETTINGS
# ==========================================================

EXPORT_FILE_NAME: str = "HealthSense_Report.md"

# ==========================================================
# UI SETTINGS
# ==========================================================

PRIMARY_COLOR = "#0F766E"

SECONDARY_COLOR = "#14B8A6"

BACKGROUND_COLOR = "#F8FAFC"

CARD_BORDER_RADIUS = 18

# ==========================================================
# DISCLAIMER
# ==========================================================

MEDICAL_DISCLAIMER: str = (
    "This application is intended for educational purposes only. "
    "It does not diagnose diseases or replace professional medical advice. "
    "Always consult a qualified healthcare professional for medical concerns."
)

# ==========================================================
# EMERGENCY KEYWORDS
# ==========================================================

EMERGENCY_KEYWORDS = [
    "chest pain",
    "difficulty breathing",
    "severe bleeding",
    "stroke",
    "heart attack",
    "loss of consciousness",
]

# ==========================================================
# WELLNESS HABITS
# ==========================================================

DEFAULT_WELLNESS_ACTIONS = [
    "💧 Drink enough water",
    "🥗 Eat balanced meals",
    "😴 Sleep 7–9 hours",
    "🏃 Exercise for at least 30 minutes",
    "🧘 Practice stress management",
]

# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    print("=" * 50)
    print(f"{APP_NAME} v{APP_VERSION}")
    print("=" * 50)

    print(f"Project Root : {PROJECT_ROOT}")
    print(f"Model        : {DEFAULT_MODEL}")
    print(f"API Key      : {API_KEY_FILE}")