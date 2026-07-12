from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_DIR = BASE_DIR / "config"
DATA_DIR = BASE_DIR / "data"
DATABASE_DIR = BASE_DIR / "database"
LOG_DIR = BASE_DIR / "logs"

CONFIG_FILE = CONFIG_DIR / "config.yaml"
WATCHLIST_FILE = CONFIG_DIR / "stocks.csv"

DATA_DIR.mkdir(exist_ok=True)
DATABASE_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

with open(CONFIG_FILE, "r") as f:
    SETTINGS = yaml.safe_load(f)