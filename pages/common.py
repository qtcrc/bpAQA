from selenium.webdriver.common.by import By


class SauceDemo:
    URL = "https://www.saucedemo.com/"

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
    def get_visible_containers(self):
        visible = []
        for c in self.CONTAINERS:
            elm = self.driver.find_elements(*(self.CONTAINERS[c]))
            if elm:
                visible.append(c)

        return visible

    # @classmethod
    # def get_login_cookie(self):
    # todo?
