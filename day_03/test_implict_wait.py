import time
from selenium.webdriver.common.by import By

def test_dynamic_loading_fail(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.XPATH,"//button[normalize-space()='Start']").click()
    print(driver.find_element(By.ID, "finish").text)   # Hello World!

def test_dynamic_loading_with_sleep(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.XPATH,"//button[normalize-space()='Start']").click()
    time.sleep(5)
    print(driver.find_element(By.ID, "finish").text)   # Hello World!

def test_dynamic_loading_implicit_wait(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    message = driver.find_element(By.ID, "finish")
    assert message.text == "Hello World!"

def test_dynamic_loading_hidden_vs_missing(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    message = driver.find_element(By.ID, "finish")
    print("Text immediately after find:", repr(message.text))

