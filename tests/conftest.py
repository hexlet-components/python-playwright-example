from collections.abc import Generator
from pathlib import Path

import allure
import pytest
from playwright.sync_api import Page


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(
    item: pytest.Item, call: pytest.CallInfo[None]
) -> Generator[None, pytest.TestReport, pytest.TestReport]:
    """Скриншот упавшего теста, пока страница ещё открыта."""
    report = yield
    if report.when == "call" and report.failed:
        page = getattr(item, "funcargs", {}).get("page")
        if isinstance(page, Page):
            allure.attach(
                page.screenshot(),
                name="screenshot-on-failure",
                attachment_type=allure.attachment_type.PNG,
            )
    return report


@pytest.hookimpl(wrapper=True)
def pytest_runtest_teardown(item: pytest.Item) -> Generator[None, None, None]:
    """Видео и трейс появляются после закрытия контекста браузера."""
    yield
    output_path = getattr(item, "funcargs", {}).get("output_path")
    if not output_path:
        return
    for file in Path(output_path).glob("*"):
        if file.suffix == ".webm":
            allure.attach.file(
                file, name="video", attachment_type=allure.attachment_type.WEBM
            )
        elif file.suffix == ".zip":
            allure.attach.file(file, name="trace", extension="zip")
