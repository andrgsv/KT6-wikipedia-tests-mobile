from __future__ import annotations

from collections.abc import Sequence

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


Locator = tuple[str, str]


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator: Locator, timeout: float = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_visible(self, locator: Locator, timeout: float = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator: Locator, timeout: float = 10) -> None:
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator: Locator, text: str, timeout: float = 10) -> None:
        element = self.wait_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    def find_first(self, locators: Sequence[Locator], timeout: float = 10):
        """Возвращает первый отображаемый элемент из списка локаторов."""

        def locate(_driver):
            for locator in locators:
                try:
                    element = _driver.find_element(*locator)
                    if element.is_displayed():
                        return element
                except (NoSuchElementException, StaleElementReferenceException):
                    continue
            return False

        return WebDriverWait(self.driver, timeout, poll_frequency=0.25).until(locate)

    def click_first(self, locators: Sequence[Locator], timeout: float = 10) -> None:
        element = self.find_first(locators, timeout)
        WebDriverWait(self.driver, timeout).until(
            lambda _driver: element.is_displayed() and element.is_enabled()
        )
        element.click()

    def is_visible(self, locator: Locator, timeout: float = 3) -> bool:
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def any_visible(self, locators: Sequence[Locator], timeout: float = 3) -> bool:
        try:
            self.find_first(locators, timeout)
            return True
        except TimeoutException:
            return False

    @staticmethod
    def by_id(value: str) -> Locator:
        return AppiumBy.ID, value

    @staticmethod
    def by_xpath(value: str) -> Locator:
        return AppiumBy.XPATH, value

    @staticmethod
    def by_accessibility(value: str) -> Locator:
        return AppiumBy.ACCESSIBILITY_ID, value

    @staticmethod
    def by_android_text(text: str) -> Locator:
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().textContains("{text}")',
        )

    @staticmethod
    def by_android_desc(text: str) -> Locator:
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().descriptionContains("{text}")',
        )
