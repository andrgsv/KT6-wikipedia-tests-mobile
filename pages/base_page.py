from __future__ import annotations

from typing import Iterable, Tuple

from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def wait_visible(self, locator: Locator, timeout: int | None = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator: Locator, timeout: int | None = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator: Locator, timeout: int | None = None):
        element = self.wait_clickable(locator, timeout)
        element.click()
        return element

    def type_text(self, locator: Locator, text: str, timeout: int | None = None):
        element = self.wait_visible(locator, timeout)
        element.clear()
        element.send_keys(text)
        return element

    def is_visible(self, locator: Locator, timeout: int = 3) -> bool:
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def find_first(self, locators: Iterable[Locator], timeout: int | None = None):
        last_error: Exception | None = None
        for locator in locators:
            try:
                return self.wait_visible(locator, timeout or 3)
            except Exception as error:  # noqa: BLE001 - для fallback-локаторов
                last_error = error
        raise NoSuchElementException(f"Не найден ни один локатор: {list(locators)}") from last_error

    def click_first(self, locators: Iterable[Locator], timeout: int | None = None):
        element = self.find_first(locators, timeout)
        element.click()
        return element

    @staticmethod
    def text_contains(text: str) -> Locator:
        return (By.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{text}")')
