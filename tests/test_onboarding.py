import pytest

from pages.main_page import MainPage
from pages.onboarding_page import OnboardingPage


@pytest.mark.smoke
def test_first_launch_can_skip_onboarding(driver):
    onboarding = OnboardingPage(driver)
    onboarding.skip_if_present()

    main_page = MainPage(driver)
    assert main_page.is_loaded(), "После пропуска онбординга должна открыться главная страница"
