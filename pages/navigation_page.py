from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class NavigationPage(BasePage):
    MORE_BUTTONS = [
        (AppiumBy.ID, "org.wikipedia:id/nav_more"),
        (AppiumBy.ID, "org.wikipedia:id/bottom_nav_more"),
        (AppiumBy.ACCESSIBILITY_ID, "More"),
        (AppiumBy.ACCESSIBILITY_ID, "Ещё"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textMatches("(?i)(more|ещё)")',
        ),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().descriptionMatches("(?i)^(more|ещё)$")',
        ),
    ]

    SETTINGS_BUTTONS = [
        (AppiumBy.ID, "org.wikipedia:id/settings"),
        (AppiumBy.ID, "org.wikipedia:id/menu_settings"),
        (AppiumBy.ACCESSIBILITY_ID, "Settings"),
        (AppiumBy.ACCESSIBILITY_ID, "Настройки"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textMatches("(?i)(settings|настройки)")',
        ),
    ]

    SETTINGS_TITLES = [
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Настройки")'),
        (AppiumBy.ACCESSIBILITY_ID, "Settings"),
        (AppiumBy.ACCESSIBILITY_ID, "Настройки"),
    ]

    def open_more(self) -> None:
        self.click_first(self.MORE_BUTTONS, timeout=15)

    def open_settings(self) -> None:
        self.click_first(self.SETTINGS_BUTTONS, timeout=15)

    def settings_is_opened(self) -> bool:
        if self.any_visible(self.SETTINGS_TITLES, timeout=10):
            return True
        activity = (self.driver.current_activity or "").lower()
        return "setting" in activity or "preference" in activity
