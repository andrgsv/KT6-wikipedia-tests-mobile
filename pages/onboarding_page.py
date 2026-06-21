from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class OnboardingPage(BasePage):
    SKIP_BUTTONS = [
        (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button"),
        (AppiumBy.ID, "org.wikipedia:id/onboarding_skip_button"),
        (AppiumBy.ACCESSIBILITY_ID, "Skip"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textMatches("(?i)(skip|пропустить)")',
        ),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().descriptionMatches("(?i)(skip|пропустить)")',
        ),
    ]

    def skip_if_present(self, timeout: float = 6) -> bool:
        try:
            self.click_first(self.SKIP_BUTTONS, timeout)
            return True
        except TimeoutException:
            return False

    def skip(self) -> None:
        self.click_first(self.SKIP_BUTTONS, timeout=10)
