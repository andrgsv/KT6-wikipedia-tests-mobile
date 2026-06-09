from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_INPUTS = [
        (By.ID, "org.wikipedia:id/search_src_text"),
        (By.CLASS_NAME, "android.widget.EditText"),
    ]
    FIRST_RESULT = (By.ID, "org.wikipedia:id/page_list_item_title")
    RESULT_TITLES = [FIRST_RESULT]

    def search_for(self, query: str) -> None:
        input_field = self.find_first(self.SEARCH_INPUTS, timeout=10)
        input_field.clear()
        input_field.send_keys(query)

    def first_result_title(self) -> str:
        return self.wait_visible(self.FIRST_RESULT, timeout=15).text

    def open_first_result(self) -> None:
        self.click(self.FIRST_RESULT, timeout=15)

    def is_input_visible(self) -> bool:
        return self.is_visible(self.SEARCH_INPUTS[0], timeout=5) or self.is_visible(self.SEARCH_INPUTS[1], timeout=5)
