from pages.login_page import LoginPage
import pytest


USERS = {
    "standard": ("standard_user", "secret_sauce"),
    "locked": ("locked_out_user", "secret_sauce"),
    "glitch": ("performance_glitch_user", "secret_sauce"),
}


@pytest.mark.critical
def test_login_page_is_shown_corretly(google_chrome_module):
    login_page = LoginPage(google_chrome_module)
    login_page.open(clean=True)
    assert login_page.find_element(LoginPage.USERNAME_INPUT)
    assert login_page.find_element(LoginPage.PASSWORD_INPUT)
    assert login_page.find_element(LoginPage.LOGIN_BUTTON)
    assert "login" in login_page.get_visible_containers()


def test_login_as_normal_user_with_correct_credentials(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    login_page.login(*USERS["standard"])
    assert "inventory" in login_page.get_visible_containers()


def test_login_as_normal_user_with_bad_credentials(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    login_page.login(USERS["standard"][0], "bad")
    assert "login" in login_page.get_visible_containers()
    assert ("Username and password do not match any user in this service"
            in login_page.get_error())


def test_login_as_locked_user_with_correct_credentials(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    login_page.login(*USERS["locked"])
    assert "login" in login_page.get_visible_containers()
    assert "Sorry, this user has been locked out" in login_page.get_error()


def test_login_as_empty_user(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    login_page.login("", "")
    assert "login" in login_page.get_visible_containers()
    assert "Username is required" in login_page.get_error()


def test_login_without_password_user(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    login_page.login("user", "")
    assert "login" in login_page.get_visible_containers()
    assert "Password is required" in login_page.get_error()


def test_login_as_glitch_user_with_correct_credentials(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    assert login_page.login(*USERS["glitch"], timeout=2)
    assert "inventory" in login_page.get_visible_containers()
