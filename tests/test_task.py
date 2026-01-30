from pages.login_page import LoginPage
import pytest
import allure
import tests.allure_helpers as AH


USERS = {
    "standard": ("standard_user", "secret_sauce"),
    "locked": ("locked_out_user", "secret_sauce"),
    "glitch": ("performance_glitch_user", "secret_sauce"),
}


@allure.feature("Login")
@allure.tag("ui", "login")
@allure.title("Проверка страницы авторизации")
@allure.story("Страница пригодна для проведения тестов")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.critical
def test_login_page_is_shown_correctly(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    AH.take_screenshot(
        google_chrome_module,
        name="LoginPage"
    )

    assert login_page.find_element(LoginPage.USERNAME_INPUT), \
        "Не найдено поле для ввода имени"
    assert login_page.find_element(LoginPage.PASSWORD_INPUT), \
        "Не найдено поле для ввода пароля"
    assert login_page.find_element(LoginPage.LOGIN_BUTTON), \
        "Кнопка входа не найдена"
    assert "login" in login_page.get_visible_containers(), \
        "Login контейнер не найден"


@allure.feature("Login")
@allure.tag("ui", "login")
@allure.title("Авторизация с корректными данными")
@allure.story("Успешный логин")
@allure.story("Redirect на страницу с инвентарём")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_as_normal_user_with_correct_credentials(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    login_page.login(*USERS["standard"])

    assert login_page.get_error() == "", \
        "Отображается ошибка"
    assert "inventory" in login_page.get_visible_containers(), \
        "Инвентарь не отображается"


@allure.feature("Login")
@allure.tag("ui", "login")
@allure.title("Авторизация с некорректными данными")
@allure.story("Ошибка авторизации")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_as_normal_user_with_bad_credentials(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    login_page.login(USERS["standard"][0], "bad")

    assert "login" in login_page.get_visible_containers(), \
        "Покинута страница аутентификации"
    assert ("Username and password do not match any user in this service"
            in login_page.get_error()), \
        "Ошибка об пустом имени пользователя не получена"


@allure.feature("Login")
@allure.tag("ui", "login")
@allure.title("Авторизация заблокированного пользователя с корректными данными")
@allure.story("Ошибка авторизации")
@allure.story("Уведомление о блокировке")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_as_locked_user_with_correct_credentials(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    login_page.login(*USERS["locked"])

    assert "login" in login_page.get_visible_containers(), \
        "Покинута страница аутентификации"
    assert ("Sorry, this user has been locked out"
            in login_page.get_error()), \
        "Ошибка о блокировки не получина"


@allure.feature("Login")
@allure.tag("ui", "login")
@allure.title("Авторизация с пустыми данными")
@allure.story("Ошибка авторизации")
@allure.story("Уведомление об отсутствие имени пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_as_empty_user(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    login_page.login("", "")

    assert "login" in login_page.get_visible_containers(), \
        "Покинута страница аутентификации"
    assert "Username is required" in login_page.get_error(), \
        "Ошибка об отсутствие имени не получена"


@allure.feature("Login")
@allure.tag("ui", "login")
@allure.title("Авторизация без пароля")
@allure.story("Ошибка авторизации")
@allure.story("Уведомление об необходимости пароля")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_without_password_user(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    login_page.login("user", "")

    assert "login" in login_page.get_visible_containers(), \
        "Покинута страница аутентификации"
    assert "Password is required" in login_page.get_error(), \
        "Ошибка об отсутствие пароля не получена"


@allure.feature("Login")
@allure.tag("ui", "login")
@allure.title("Авторизация glitch пользователя")
@allure.story("Успешная авторизация")
@allure.story("Авторизация заняла меньше 2 секунд")
@allure.severity(allure.severity_level.NORMAL)
def test_login_as_glitch_user_with_correct_credentials(google_chrome_module):
    login_page = LoginPage(google_chrome_module)

    login_page.open(clean=True)
    login_page.login(*USERS["glitch"], timeout=2)

    assert "inventory" in login_page.get_visible_containers(), \
        "Инвентарь не отображён"
