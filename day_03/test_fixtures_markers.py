import pytest
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

    assert "inventory" in driver.current_url

@pytest.mark.regression
def test_locked_out_user(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error_msg = driver.find_element(By.XPATH,"//h3[contains(text(),"
                                 "'Epic sadface: Sorry, this user has been locked out')]")
    assert error_msg.is_displayed()
    assert "user has been locked out" in error_msg.text

@pytest.mark.regression
def test_wrong_password(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_suce")
    driver.find_element(By.ID, "login-button").click()
    error = driver.find_element(By.XPATH,"//h3[contains(text(),'Epic "
                                         "sadface: Username and password do not match a')]")
    assert "password do not match" in error.text


@pytest.mark.smoke
def test_get_attribute_and_clear(driver):
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    assert username.get_attribute("value")  == "standard_user"
    username.clear()

    assert username.get_attribute("value") == ""
