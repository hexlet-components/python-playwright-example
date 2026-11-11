import allure
from playwright.sync_api import Page, Route, expect

BOARD_URL = "https://http.hexlet.app/python-playwright"


@allure.epic("Departures")
@allure.feature("Табло")
def test_board_shows_flights(page: Page) -> None:
    page.goto(BOARD_URL)
    expect(page.get_by_test_id("flight-number")).to_have_count(4)


@allure.epic("Departures")
@allure.feature("Табло")
def test_board_without_departures(page: Page) -> None:
    def handle(route: Route) -> None:
        route.fulfill(json=[])

    page.route("**/api/departures", handle)
    page.goto(BOARD_URL)
    expect(page.get_by_text("No departures right now.")).to_be_visible()
