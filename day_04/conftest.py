import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(0)
    yield driver

    driver.quit()