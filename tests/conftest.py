import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser_module():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
