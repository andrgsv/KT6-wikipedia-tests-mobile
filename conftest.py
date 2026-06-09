import json
import os
from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_CAPS_FILE = PROJECT_ROOT / "capabilities.example.json"


def load_capabilities() -> dict:
    """Загрузка capabilities из JSON-файла.

    По умолчанию используется capabilities.example.json.
    Можно указать свой файл через переменную окружения APPIUM_CAPS_FILE.
    """
    caps_file = Path(os.getenv("APPIUM_CAPS_FILE", DEFAULT_CAPS_FILE))
    with caps_file.open("r", encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture
def driver():
    server_url = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
    options = UiAutomator2Options().load_capabilities(load_capabilities())
    app_driver = webdriver.Remote(command_executor=server_url, options=options)
    app_driver.implicitly_wait(0)
    yield app_driver
    app_driver.quit()
