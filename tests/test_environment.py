from stockai.config import Environment


def test_environment_default():

    value = Environment.get(
        "NON_EXISTING_VALUE",
        "default"
    )

    assert value == "default"