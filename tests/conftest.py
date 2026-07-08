import os

import pytest

from utils.driver_factory import build_driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless") or os.environ.get("HEADLESS") == "true"

    drv = build_driver(browser, headless)
    drv.implicitly_wait(0)
    yield drv
    drv.quit()
