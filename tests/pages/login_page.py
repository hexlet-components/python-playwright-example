from playwright.sync_api import Page, expect

from tests.pages.base_page import BasePage
from tests.pages.trips_page import TripsPage


class LoginPage(BasePage):
    """Страница входа Departures."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Log in")
        self.error_message = page.locator("#flash")

    def open(self, path: str = "/login") -> None:
        super().open(path)

    def login(self, username: str, password: str) -> TripsPage:
        """Войти и вернуть страницу, которая открывается после входа."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return TripsPage(self.page)

    def expect_error_contains(self, text: str) -> None:
        expect(self.error_message).to_contain_text(text)
