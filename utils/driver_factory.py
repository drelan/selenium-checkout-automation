from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def build_driver(browser: str, headless: bool) -> webdriver.Remote:
    browser = browser.lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1440,1200")
        if headless:
            options.add_argument("--headless=new")
        return webdriver.Chrome(options=options)

    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1440")
        options.add_argument("--height=1200")
        if headless:
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)

    raise ValueError(f"Unsupported browser: {browser}")
