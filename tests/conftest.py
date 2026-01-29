import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser_module():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# critical test
def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "critical: marks a test as critical; \
        failure stops remaining tests in the module"
    )


_failed_critical_modules = set()


def pytest_runtest_setup(item):
    if item.module in _failed_critical_modules:
        pytest.skip("Skipped due to critical failure in this module")


def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo:
        if item.get_closest_marker("critical"):
            _failed_critical_modules.add(item.module)
