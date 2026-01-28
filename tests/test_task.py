from pages.login_page import LoginPage


def test_login_with_correct_credentials(browser_module):
    login_page = LoginPage(browser_module)

    login_page.open(clean=True)
    login_page.login("standard_user", "secret_sauce")
    print(login_page.get_error)

    # assert "inventory" in login_page.get_visible_containers()
    assert not login_page.is_visible()
