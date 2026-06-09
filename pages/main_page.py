from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_ENTRY_POINTS = [
        (By.ID, "org.wikipedia:id/search_container"),
        (By.ID, "org.wikipedia:id/main_toolbar_wordmark"),
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Search Wikipedia")'),
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Искать в Википедии")'),
    ]
    EXPLORE_TEXTS = [
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Explore")'),
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Обзор")'),
    ]

    def open_search(self) -> None:
        self.click_first(self.SEARCH_ENTRY_POINTS, timeout=10)

    def is_loaded(self) -> bool:
        return self.is_visible(self.SEARCH_ENTRY_POINTS[0], timeout=5) or self.is_visible(self.EXPLORE_TEXTS[0], timeout=3)
