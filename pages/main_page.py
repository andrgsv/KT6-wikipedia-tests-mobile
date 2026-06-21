from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_TAB = (AppiumBy.ID, "org.wikipedia:id/nav_tab_search")
    SEARCH_CARD = (AppiumBy.ID, "org.wikipedia:id/search_card")

    SEARCH_INPUTS = [
        (AppiumBy.ID, "org.wikipedia:id/search_src_text"),
        (AppiumBy.CLASS_NAME, "android.widget.EditText"),
    ]

    def open_search(self) -> None:
        # Если поле уже открыто — ничего не делаем.
        if self.any_visible(self.SEARCH_INPUTS, timeout=1):
            return

        # В текущей версии Wikipedia поиск открывается в два шага:
        # вкладка Search -> карточка Search Wikipedia.
        if not self.is_visible(self.SEARCH_CARD, timeout=1):
            self.click(self.SEARCH_TAB, timeout=10)

        self.click(self.SEARCH_CARD, timeout=10)
        self.find_first(self.SEARCH_INPUTS, timeout=15)

    def is_loaded(self) -> bool:
        return self.driver.current_package == "org.wikipedia"
