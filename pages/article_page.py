import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class ArticlePage(BasePage):
    TITLE_LOCATORS = [
        (AppiumBy.ID, "org.wikipedia:id/view_page_title_text"),
        (AppiumBy.ID, "org.wikipedia:id/page_title"),
        (AppiumBy.ID, "org.wikipedia:id/article_title"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceIdMatches(".*(page|article).*title.*")',
        ),
    ]

    SAVE_BUTTONS = [
        (AppiumBy.ID, "org.wikipedia:id/page_save"),
        (AppiumBy.ID, "org.wikipedia:id/menu_page_save"),
        (AppiumBy.ACCESSIBILITY_ID, "Save"),
        (AppiumBy.ACCESSIBILITY_ID, "Add to reading list"),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().descriptionMatches("(?i)(save|add to reading list|сохранить|добавить в список для чтения)")',
        ),
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textMatches("(?i)(save|add to reading list|сохранить|добавить в список для чтения)")',
        ),
    ]

    def title_text(self) -> str:
        try:
            return self.find_first(self.TITLE_LOCATORS, timeout=12).text.strip()
        except TimeoutException:
            pass

        # В разных версиях Wikipedia заголовок статьи может не иметь
        # стабильного resource-id. Берём первый содержательный видимый текст.
        ignored = {
            "search", "more", "saved", "home", "explore", "share",
            "save", "back", "settings", "поиск", "ещё", "сохранить",
        }
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            elements = self.driver.find_elements(
                AppiumBy.XPATH,
                "//*[@text!='' or @content-desc!='']",
            )
            for element in elements:
                text = (element.text or element.get_attribute("content-desc") or "").strip()
                if len(text) >= 3 and text.lower() not in ignored:
                    return text
            time.sleep(0.3)
        return ""

    def save_article(self) -> None:
        self.click_first(self.SAVE_BUTTONS, timeout=15)

    def click_save(self) -> None:
        self.save_article()
