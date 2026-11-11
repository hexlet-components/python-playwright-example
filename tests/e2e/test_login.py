import allure
import pytest
from playwright.sync_api import Page

from tests.pages.login_page import LoginPage


@allure.epic("Departures")
@allure.feature("Вход")
@allure.story("Успешный вход пассажира")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://http.hexlet.app/python-playwright/login", name="Страница входа")
def test_login_passenger(page: Page) -> None:
    login_page = LoginPage(page)
    with allure.step("Открыть страницу входа"):
        login_page.open()
    with allure.step("Войти пассажиром"):
        # Учётка стенда напечатана на его странице входа и в уроках.
        trips_page = login_page.login("passenger", "flight123")  # betterleaks:allow
    with allure.step("Проверить раздел поездок"):
        trips_page.expect_opened()
        trips_page.expect_trip("SK 204")


@allure.epic("Departures")
@allure.feature("Вход")
@pytest.mark.parametrize(
    ("username", "password", "error"),
    [
        ("blocked", "flight123", "locked"),
        ("", "flight123", "Username is required"),
        ("passenger", "", "Password is required"),
    ],
)
def test_login_errors(page: Page, username: str, password: str, error: str) -> None:
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    login_page.expect_error_contains(error)
