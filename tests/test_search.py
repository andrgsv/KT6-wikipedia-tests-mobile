import pytest

from pages.main_page import MainPage
from pages.onboarding_page import OnboardingPage
from pages.search_page import SearchPage


@pytest.mark.functional
def test_search_article_returns_relevant_results(driver):
    OnboardingPage(driver).skip_if_present()
    MainPage(driver).open_search()

    search = SearchPage(driver)
    search.search_for("Selenium")

    first_title = search.first_result_title()
    assert "Selenium" in first_title, f"Первый результат должен быть связан с Selenium, получено: {first_title}"


@pytest.mark.functional
def test_empty_search_field_does_not_crash_app(driver):
    OnboardingPage(driver).skip_if_present()
    MainPage(driver).open_search()

    search = SearchPage(driver)
    search.search_for("")

    assert search.is_input_visible(), "При пустом поиске поле ввода должно остаться доступным"
