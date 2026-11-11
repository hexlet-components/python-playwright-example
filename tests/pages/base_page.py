from playwright.sync_api import Page


class BasePage:
    """Базовый класс для всех Page Objects."""

    BASE_URL = "https://http.hexlet.app/python-playwright"

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, path: str = "") -> None:
        """Открыть страницу по относительному пути."""
        self.page.goto(f"{self.BASE_URL}{path}")
