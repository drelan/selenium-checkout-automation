import allure

from pages.home_page import HomePage
from pages.shop_ipad_page import ShopIpadPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_auth_page import CheckoutAuthPage
from utils.config import PRODUCT_NAME, TARGET_COLOR


@allure.epic("Apple Store")
@allure.feature("iPad Accessories")
@allure.title("Add Smart Folio for iPad to bag and reach checkout sign-in options")
@allure.severity(allure.severity_level.CRITICAL)
def test_smart_folio_purchase_flow(driver):
    home_page = HomePage(driver)
    shop_ipad_page = ShopIpadPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    checkout_auth_page = CheckoutAuthPage(driver)

    home_page.load()
    home_page.open_ipad_store_via_store_menu()

    shop_ipad_page.assert_on_page()
    shop_ipad_page.open_smart_folio_tile()

    product_page.assert_on_page()
    product_page.select_color(TARGET_COLOR)
    base_price = product_page.get_price()
    product_page.add_to_bag()

    cart_page.assert_on_page()
    cart_page.assert_item_present(PRODUCT_NAME)
    cart_page.assert_price_matches(base_price)
    cart_page.click_checkout()

    checkout_auth_page.assert_signin_and_guest_options_visible()
