from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_dynamic_loading_fail(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))).click()
    msg = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    assert msg.text == "Hello World!"


def test_dynamic_controls(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    wait = WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                           "button[onclick='swapCheckbox()']"))).click()
    message = wait.until(EC.visibility_of_element_located((By.ID,"message"))).text
    assert message == "It's gone!"

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                           "button[onclick='swapInput()']"))).click()
    msg = wait.until(EC.visibility_of_element_located((By.ID,"message"))).text
    assert msg == "It's enabled!"