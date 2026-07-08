from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.config import PRODUCT_URL_FRAGMENT, SHORT_TIMEOUT

PRICE = (By.CSS_SELECTOR, "[data-autom='full-price']")
ADD_TO_BAG_BUTTON = (
    By.XPATH,
    "//button[@data-autom='add-to-cart' and normalize-space(text())='Add to Bag']",
)


def color_swatch_locator(color: str):
    return (By.CSS_SELECTOR, f"[data-autom='colornav-{color.lower()}']")


class ProductPage(BasePage):
    def assert_on_page(self):
        assert PRODUCT_URL_FRAGMENT in self.current_url(), (
            f"Expected to be on the Smart Folio product page, got {self.current_url()}"
        )
        return self

    def select_color(self, color: str):
        swatch = self.wait_clickable(color_swatch_locator(color))
        swatch.click()
        self.wait_url_contains(color.lower())
        self.wait_visible(PRICE)
        return self

    def get_price(self) -> str:
        return self.wait_visible(PRICE).text.strip()

    def add_to_bag(self):
        for _ in range(3):
            button = self.wait_clickable(ADD_TO_BAG_BUTTON)
            button.click()
            try:
                WebDriverWait(self.driver, SHORT_TIMEOUT).until(EC.url_contains("/shop/bag"))
                return self
            except Exception:
                continue
        raise AssertionError("Add to Bag did not navigate to the bag page after 3 attempts")
