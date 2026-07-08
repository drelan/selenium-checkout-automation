from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import PRODUCT_URL_FRAGMENT

SMART_FOLIO_TILE = (By.CSS_SELECTOR, f"a[href*='{PRODUCT_URL_FRAGMENT}-a16-sky']")


class ShopIpadPage(BasePage):
    def assert_on_page(self):
        assert "buy-ipad" in self.current_url(), (
            f"Expected to be on the iPad store page, got {self.current_url()}"
        )
        return self

    def open_smart_folio_tile(self):
        self.scroll_to_bottom()
        tile = self.wait_visible(SMART_FOLIO_TILE)
        self.scroll_into_view(tile)
        tile.click()
        self.wait_url_contains(PRODUCT_URL_FRAGMENT)
        return self
