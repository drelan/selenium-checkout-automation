import os
import platform

import allure
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


@pytest.fixture(scope="session", autouse=True)
def allure_environment(request):
    results_dir = request.config.getoption("--alluredir")
    if results_dir:
        os.makedirs(results_dir, exist_ok=True)
        with open(os.path.join(results_dir, "environment.properties"), "w") as f:
            f.write(f"Browser={request.config.getoption('--browser')}\n")
            f.write(f"Headless={request.config.getoption('--headless')}\n")
            f.write(f"OS={platform.system()} {platform.release()}\n")
            f.write("BaseURL=https://www.apple.com\n")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv is not None:
            allure.attach(
                drv.get_screenshot_as_png(),
                name="screenshot-on-failure",
                attachment_type=allure.attachment_type.PNG,
            )
            allure.attach(
                drv.page_source,
                name="page-source-on-failure",
                attachment_type=allure.attachment_type.HTML,
            )
