from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OnboardingPage(BasePage):
    SKIP_BUTTONS = [
        (By.ID, "org.wikipedia:id/fragment_onboarding_skip_button"),
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Skip")'),
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Пропустить")'),
    ]

    def skip_if_present(self) -> None:
        try:
            self.click_first(self.SKIP_BUTTONS, timeout=5)
        except Exception:
            # Экран онбординга может не появляться, если приложение уже запускалось.
            pass
