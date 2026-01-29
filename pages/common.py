from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class SauceDemo:
    DEFAULT_TIMEOUT = 2

    CONTAINERS = {
        "login": (By.CSS_SELECTOR, "#root > .login_container"),
        "header": (By.ID, "header_container"),
        "inventory": (By.ID, "inventory_container"),
        "cart_contents": (By.ID, "cart_contents_container"),
    }

    @classmethod
    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def wait_until(self, method, timeout=DEFAULT_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(method, timeout)
        except TimeoutException:
            return False

        return True

    @classmethod
    def find_element(self, selector_tuple, timeout=DEFAULT_TIMEOUT):
        if timeout > 0:
            try:
                WebDriverWait(self.driver, timeout).until(
                    lambda d: d.find_elements(*selector_tuple)
                )
            except TimeoutException:
                pass

        elements = self.driver.find_elements(*selector_tuple)
        return elements[0] if elements else None

    @classmethod
    def get_visible_containers(self):
        visible = []
        for c in self.CONTAINERS:
            elm = self.find_element(self.CONTAINERS[c], timeout=0)
            if elm:
                visible.append(c)

        return visible

    @classmethod
    def has_element(self, selector_tuple):
        return self.driver.find_elemnts(*selector_tuple)

    # @classmethod
    # def get_login_cookie(self):
    # todo?
