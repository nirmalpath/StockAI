"""
Environment variable loader.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Environment:
    """
    Provides access to environment variables.
    """

    @staticmethod
    def get(key: str, default=None):
        return os.getenv(key, default)
