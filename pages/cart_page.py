import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

ITEM_NAME = (By.CSS_SELECTOR, "[data-autom='bag-item-name']")
SUBTOTAL = (By.CSS_SELECTOR, "[data-autom='bagrs-summary-subtotalvalue']")
CHECKOUT_BUTTON = (
    By.CSS_SELECTOR,
    ".rs-bag-checkout-otheroptions button[data-autom='checkout']",
)


class CartPage(BasePage):
    @allure.step("Assert on the bag/cart page")
    def assert_on_page(self):
        assert "/shop/bag" in self.current_url(), (
            f"Expected to be on the bag page, got {self.current_url()}"
        )
        return self

    @allure.step("Assert bag contains item: {expected_name}")
    def assert_item_present(self, expected_name: str):
        item_text = self.wait_visible(ITEM_NAME).text.replace("\xa0", " ")
        assert expected_name in item_text, (
            f"Expected bag item to contain '{expected_name}', got '{item_text}'"
        )
        return self

    @allure.step("Assert bag subtotal matches price captured on the product page: {expected_price}")
    def assert_price_matches(self, expected_price: str):
        subtotal = self.wait_visible(SUBTOTAL).text.strip()
        assert subtotal == expected_price, (
            f"Expected bag subtotal '{expected_price}', got '{subtotal}'"
        )
        return self

    @allure.step("Click Checkout")
    def click_checkout(self):
        button = self.wait_clickable(CHECKOUT_BUTTON)
        self.scroll_into_view(button)
        button.click()
        self.wait_url_contains("signIn")
        return self
