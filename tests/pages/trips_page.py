from playwright.sync_api import Page, expect

from tests.pages.base_page import BasePage


class TripsPage(BasePage):
    """Раздел с поездками пассажира после входа."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page_title = page.get_by_role("heading", name="My trips")
        self.trips = page.locator(".trip")

    def expect_opened(self) -> None:
        expect(self.page_title).to_be_visible()

    def expect_trip(self, text: str) -> None:
        expect(self.trips.filter(has_text=text)).to_have_count(1)
