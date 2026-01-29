from pages.login_page import LoginPage
import pytest


@pytest.mark.critical
def test_login_page_is_shown_corretly(browser_module):
    login_page = LoginPage(browser_module)
    login_page.open(clean=True)
    assert login_page.find_element(LoginPage.USERNAME_INPUT)
    assert login_page.find_element(LoginPage.PASSWORD_INPUT)
    assert login_page.find_element(LoginPage.LOGIN_BUTTON)
    assert "login" in login_page.get_visible_containers()


def test_login_with_correct_credentials(browser_module):
    login_page = LoginPage(browser_module)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in login_page.get_visible_containers()
    assert login_page.get_error() == ""
