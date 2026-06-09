from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NavigationPage(BasePage):
    MORE_TAB_LOCATORS = [
        (By.ID, "org.wikipedia:id/nav_tab_more"),
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("More")'),
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Ещё")'),
    ]
    SETTINGS_LOCATORS = [
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Settings")'),
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Настройки")'),
    ]
    SETTINGS_TITLE_LOCATORS = [
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Settings")'),
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Настройки")'),
    ]

    def open_more(self) -> None:
        self.click_first(self.MORE_TAB_LOCATORS, timeout=10)

    def open_settings(self) -> None:
        self.click_first(self.SETTINGS_LOCATORS, timeout=10)

    def settings_is_opened(self) -> bool:
        return any(self.is_visible(locator, timeout=3) for locator in self.SETTINGS_TITLE_LOCATORS)
