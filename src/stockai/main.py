"""
StockAI Application Entry Point.
"""

from stockai.config import Settings
from stockai.logger import setup_logger


def main():

    logger = setup_logger()

    settings = Settings()

    logger.info("Starting StockAI")

    logger.info(f"Application: {settings.application}")

    logger.info(f"Database: {settings.database}")

    logger.info("Startup completed successfully")


if __name__ == "__main__":
    main()
