from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import BASE_URL

STORE_NAV_LINK = (By.CSS_SELECTOR, "a.globalnav-link-store")
STORE_FLYOUT_IPAD_LINK = (
    By.XPATH,
    "//a[contains(@class,'globalnav-submenu-link') and normalize-space(text())='iPad']",
)


class HomePage(BasePage):
    def load(self):
        self.driver.get(BASE_URL)
        self.wait_visible(STORE_NAV_LINK)
        return self

    def open_ipad_store_via_store_menu(self):
        store_link = self.wait_visible(STORE_NAV_LINK)
        self.hover(store_link)
        ipad_link = self.wait_visible(STORE_FLYOUT_IPAD_LINK)
        ipad_link.click()
        self.wait_url_contains("buy-ipad")
        return self
