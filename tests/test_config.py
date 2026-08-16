from stockai.core.config import Settings


def test_config_load():

    settings = Settings()

    assert settings.application["name"] == "StockAI"
