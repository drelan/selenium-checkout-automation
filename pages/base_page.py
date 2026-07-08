from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_url_contains(self, fragment, timeout=None):
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        wait.until(EC.url_contains(fragment))

    def hover(self, element):
        body = self.driver.find_element("tag name", "body")
        ActionChains(self.driver).move_to_element(body).move_to_element(element).perform()

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def current_url(self):
        return self.driver.current_url
