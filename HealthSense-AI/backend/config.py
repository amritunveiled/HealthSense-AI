"""
backend/config.py

Configuration manager for HealthSense AI.

Responsible for:
- Loading the Groq API key
- Providing the default model
- Validating application configuration
"""

from backend.constants import API_KEY_FILE, DEFAULT_MODEL


def load_groq_api_key() -> str:
    """
    Load the Groq API key from the key-vault.

    Returns:
        str: The Groq API key.

    Raises:
        FileNotFoundError:
            If the API key file does not exist.

        ValueError:
            If the API key file is empty.
    """

    if not API_KEY_FILE.exists():
        raise FileNotFoundError(
            f"Groq API key file was not found.\n"
            f"Expected location:\n{API_KEY_FILE}"
        )

    api_key = API_KEY_FILE.read_text(
        encoding="utf-8"
    ).strip()

    if not api_key:
        raise ValueError(
            "The Groq API key file exists but is empty."
        )

    return api_key


def get_model_name() -> str:
    """
    Return the default Groq model.
    """

    return DEFAULT_MODEL


def validate_configuration() -> bool:
    """
    Validate that the application configuration is correct.

    Returns:
        bool: True if configuration is valid.
    """

    load_groq_api_key()

    return True


if __name__ == "__main__":

    print("=" * 50)
    print("HealthSense AI Configuration Check")
    print("=" * 50)

    try:

        validate_configuration()

        print("✅ Configuration Status : OK")
        print(f"📁 API Key File        : {API_KEY_FILE}")
        print(f"🤖 Model              : {get_model_name()}")

    except Exception as error:

        print("\n❌ Configuration Error\n")
        print(error)