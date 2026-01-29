import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def google_chrome_module():
    opt = Options()

    opt.add_argument("--disable-save-password-bubble")
    opt.add_argument("--disable-infobars")
    opt.add_argument("--disable-notifications")
    opt.add_argument("--disable-popup-blocking")
    opt.add_argument("--incognito")

    driver = webdriver.Chrome(options=opt)
    yield driver

    driver.quit()


# critical tests

_failed_critical_modules = set()


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "critical: marks a test as critical; \
        failure stops remaining tests in the module"
    )


def pytest_runtest_setup(item):
    if item.module in _failed_critical_modules:
        pytest.skip("Skipped due to critical failure in this module")


def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo:
        if item.get_closest_marker("critical"):
            _failed_critical_modules.add(item.module)
