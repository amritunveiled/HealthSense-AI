"""
backend/logger.py

Logging utility for HealthSense AI.
"""

import logging
from pathlib import Path

from backend.constants import PROJECT_ROOT

LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "healthsense.log"


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Args:
        name: Logger name.

    Returns:
        logging.Logger
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    logger = get_logger("HealthSense")

    logger.info("Logger initialized successfully.")

    print("Log file created successfully.")