"""
Configuration management for StockAI.

Loads application settings from config/config.yaml
"""

from pathlib import Path
from typing import Any

import yaml


class Settings:
    """
    Loads and provides access to application configuration.
    """

    def __init__(self, config_file: str = "config/config.yaml"):
        self.base_dir = Path.cwd()
        self.config_file = self.base_dir / config_file

        self._config = self._load_config()

    def _load_config(self) -> dict[str, Any]:
        """
        Load YAML configuration file.
        """

        if not self.config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

        with open(self.config_file, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def get(self, key: str, default=None):
        """
        Retrieve configuration value.
        """

        return self._config.get(key, default)

    @property
    def application(self):
        return self._config.get("application", {})

    @property
    def database(self):
        return self._config.get("database", {})

    @property
    def logging(self):
        return self._config.get("logging", {})

    @property
    def download(self):
        return self._config.get("download", {})
