from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_js_alert(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.CSS_SELECTOR,"button[onclick='jsAlert()']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert"
    alert.accept()
    display_text = driver.find_element(By.XPATH,"//p[@id='result']").text
    assert display_text == "You successfully clicked an alert"

def test_js_confirm_accept(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
    alert = driver.switch_to.alert
    # assert alert.text == "I am a JS Confirm"
    alert.accept()
    display_text = driver.find_element(By.XPATH,"//p[@id='result']").text
    assert display_text == "You clicked: Ok"

def test_js_confirm_dismiss(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
    alert = driver.switch_to.alert
    alert.dismiss()
    display_text = driver.find_element(By.XPATH, "//p[@id='result']").text
    assert display_text == "You clicked: Cancel"

def test_js_prompt(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.CSS_SELECTOR,
                        "button[onclick='jsPrompt()']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS prompt"
    prompt = "This is an alert!"
    alert.send_keys(prompt)
    alert.accept()
    display_text = driver.find_element(By.XPATH, "//p[@id='result']").text
    assert display_text == f"You entered: {prompt}"

def test_EC_switch(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']"
                        ).click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.send_keys("Hello")
    alert.accept()
    assert "Hello" in driver.find_element(By.ID, "result").text