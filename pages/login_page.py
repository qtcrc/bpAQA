import time
from pages.common import SauceDemo
from selenium.webdriver.common.by import By


class LoginPage(SauceDemo):
    URL = "https://www.saucedemo.com/"

    # locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, r'[data-test="error"]')

    def open(self, clean=True):
        if clean:
            self.driver.delete_all_cookies()

        self.driver.get(self.URL)

    def enter_username(self, username):
        elm = self.driver.find_element(*self.USERNAME_INPUT)
        elm.send_keys(username)

    def enter_password(self, password):
        elm = self.driver.find_element(*self.PASSWORD_INPUT)
        elm.send_keys(password)

    def press_login(self):
        elm = self.driver.find_element(*self.LOGIN_BUTTON)
        elm.click()

    def login(self, username, password, timeout=1):
        login_start_time = time.time()
        self.enter_username(username)
        self.enter_password(password)
        self.press_login()
        login_end_time = time.time()

        # (REDO) login button press hangs whole tab... This will not work.
        #
        # self.wait_until(
        #     lambda d:
        #         (self.get_error() != "" or
        #          "inventory" in self.get_visible_containers()),
        #     timeout
        # )

        # (TEMP)
        assert (login_end_time - login_start_time) <= timeout

    def get_error(self):
        elm = self.find_element(self.ERROR_MSG, timeout=0)
        return elm.text if elm else ""

    def is_visible(self):
        return ("login" in self.get_visible_containers() and
                self.has_element(self.USERNAME_INPUT) and
                self.has_element(self.PASSWORD_INPUT) and
                self.has_element(self.LOGIN_BUTTON))
