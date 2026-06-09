import pytest

from pages.navigation_page import NavigationPage
from pages.onboarding_page import OnboardingPage


@pytest.mark.functional
def test_open_settings_from_more_menu(driver):
    OnboardingPage(driver).skip_if_present()

    navigation = NavigationPage(driver)
    navigation.open_more()
    navigation.open_settings()

    assert navigation.settings_is_opened(), "Экран настроек должен открываться из меню More/Ещё"
