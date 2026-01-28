from pages.common import SauceDemo
from selenium.webdriver.common.by import By


class LoginPage(SauceDemo):
    # locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, r'[data-test="error"]')

    def open(self, clean=False):
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

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.press_login()

    def get_error(self):
        elm = self.driver.find_element(*self.ERROR_MSG)
        return elm.text

    def is_visible(self):
        return ("login" in self.get_visible_containers() and
                self.driver.find_elemnts(*self.USERNAME_INPUT))
