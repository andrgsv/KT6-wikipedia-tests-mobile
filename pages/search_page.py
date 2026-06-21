from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_CARD = (AppiumBy.ID, "org.wikipedia:id/search_card")

    SEARCH_INPUTS = [
        (AppiumBy.ID, "org.wikipedia:id/search_src_text"),
        (AppiumBy.CLASS_NAME, "android.widget.AutoCompleteTextView"),
        (AppiumBy.CLASS_NAME, "android.widget.EditText"),
    ]

    # В установленной версии Wikipedia результаты отрисовываются через Jetpack Compose.
    # У строк результатов нет resource-id; первая строка — первый clickable View
    # внутри fragment_search_results.
    FIRST_RESULT_ROW = (
        AppiumBy.XPATH,
        "(//*[@resource-id='org.wikipedia:id/fragment_search_results']"
        "//android.view.View[@clickable='true'])[1]",
    )

    FIRST_RESULT_TITLE = (
        AppiumBy.XPATH,
        "(//*[@resource-id='org.wikipedia:id/fragment_search_results']"
        "//android.view.View[@clickable='true']"
        "/android.widget.TextView[1])[1]",
    )

    def _get_input(self):
        try:
            return self.find_first(self.SEARCH_INPUTS, timeout=2)
        except TimeoutException:
            self.click(self.SEARCH_CARD, timeout=10)
            return self.find_first(self.SEARCH_INPUTS, timeout=15)

    def search_for(self, query: str) -> None:
        input_field = self._get_input()
        input_field.clear()
        if query:
            input_field.send_keys(query)

    def first_result_title(self) -> str:
        return self.wait_visible(self.FIRST_RESULT_TITLE, timeout=30).text.strip()

    def open_first_result(self) -> None:
        self.click(self.FIRST_RESULT_ROW, timeout=30)

    def is_input_visible(self) -> bool:
        try:
            self._get_input()
            return True
        except TimeoutException:
            return False
