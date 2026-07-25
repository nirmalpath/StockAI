"""
Central logging configuration.
"""

from pathlib import Path

from loguru import logger


def setup_logger():
    """
    Configure application logging.
    """

    log_directory = Path("logs")

    log_directory.mkdir(exist_ok=True)

    logger.remove()

    logger.add(
        sink="logs/stockai.log",
        rotation="10 MB",
        retention="30 days",
        level="INFO",
        format=("{time:YYYY-MM-DD HH:mm:ss} | " "{level} | " "{message}"),
    )

    logger.add(
        sink=lambda msg: print(msg),
        level="INFO",
    )

    return logger
