from collections.abc import Generator

import allure
import pytest
from playwright.sync_api import APIRequestContext, Playwright


@pytest.fixture(scope="session")
def api(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    """API-клиент с токеном пассажира, браузер не поднимается."""
    anonymous = playwright.request.new_context(
        base_url="https://http.hexlet.app/python-playwright/"
    )
    token = anonymous.post(
        "api/login", data={"username": "passenger", "password": "flight123"}
    ).json()["token"]
    anonymous.dispose()

    context = playwright.request.new_context(
        base_url="https://http.hexlet.app/python-playwright/",
        extra_http_headers={"Authorization": f"Bearer {token}"},
    )
    yield context
    context.dispose()


@allure.epic("Departures")
@allure.feature("API бронирований")
def test_list_bookings(api: APIRequestContext) -> None:
    response = api.get("api/bookings")
    assert response.ok
    assert [booking["flight"] for booking in response.json()] == ["SK 204", "SK 318"]


@allure.epic("Departures")
@allure.feature("API бронирований")
def test_create_booking(api: APIRequestContext) -> None:
    response = api.post(
        "api/bookings", data={"flight": "SK 527", "passenger": "Ivan Petrov"}
    )
    assert response.status == 201
    assert response.json()["status"] == "confirmed"


@allure.epic("Departures")
@allure.feature("API бронирований")
def test_bookings_require_token(playwright: Playwright) -> None:
    context = playwright.request.new_context(
        base_url="https://http.hexlet.app/python-playwright/"
    )
    assert context.get("api/bookings").status == 401
    context.dispose()
