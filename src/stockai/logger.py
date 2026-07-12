from loguru import logger

logger.add(
    "logs/stockai.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO"
)   

from src.stockai.logger import logger

logger.info("Application started")
logger.warning("Downloading prices")
logger.error("Unable to fetch data")
