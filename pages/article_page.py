from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ArticlePage(BasePage):
    TITLE = (By.ID, "org.wikipedia:id/view_page_title_text")
    SAVE_BUTTONS = [
        (By.ID, "org.wikipedia:id/page_save"),
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Save")'),
        (By.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Сохранить")'),
    ]
    MORE_OPTIONS = [
        (By.ACCESSIBILITY_ID, "More options"),
        (By.ACCESSIBILITY_ID, "Ещё"),
    ]

    def title_text(self) -> str:
        return self.wait_visible(self.TITLE, timeout=15).text

    def save_article(self) -> None:
        self.click_first(self.SAVE_BUTTONS, timeout=10)
