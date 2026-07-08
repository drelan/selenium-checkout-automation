from selenium.webdriver.common.by import By

from pages.base_page import BasePage

SIGNIN_WIDGET_IFRAME = (By.ID, "aid-auth-widget-iFrame")
CONTINUE_AS_GUEST_BUTTON = (
    By.XPATH,
    "//button[.//*[contains(text(),'Continue as Guest')] or contains(text(),'Continue as Guest')]",
)


class CheckoutAuthPage(BasePage):
    def assert_signin_and_guest_options_visible(self):
        assert "signIn" in self.current_url(), (
            f"Expected to be on the sign-in/guest checkout page, got {self.current_url()}"
        )
        # The Apple Account sign-in form is a cross-origin idmsa.apple.com widget
        # embedded in an iframe, so we assert its presence rather than switching
        # into it to reach the email/phone field.
        self.wait_visible(SIGNIN_WIDGET_IFRAME)
        self.wait_visible(CONTINUE_AS_GUEST_BUTTON)
        return self
