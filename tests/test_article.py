import pytest

from pages.article_page import ArticlePage
from pages.main_page import MainPage
from pages.onboarding_page import OnboardingPage
from pages.search_page import SearchPage


@pytest.mark.functional
def test_open_article_from_search_results(driver):
    OnboardingPage(driver).skip_if_present()
    MainPage(driver).open_search()

    search = SearchPage(driver)
    search.search_for("Appium")
    search.open_first_result()

    title = ArticlePage(driver).title_text()
    assert title, "После открытия результата должен отображаться заголовок статьи"


@pytest.mark.regression
def test_article_can_be_saved_without_login(driver):
    OnboardingPage(driver).skip_if_present()
    MainPage(driver).open_search()

    search = SearchPage(driver)
    search.search_for("Python")
    search.open_first_result()

    article = ArticlePage(driver)
    article.save_article()

    assert article.title_text(), "После сохранения статьи пользователь должен остаться на странице статьи"
