from selenium import webdriver
from selenium.webdriver.common.by import By


def test_commands():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")

    driver.find_element(By.LINK_TEXT,"Checkboxes").click()
    assert "checkboxes" in driver.current_url
    driver.back()
    assert "herokuapp.com" in driver.current_url

    driver.forward()
    assert "checkboxes" in driver.current_url


    driver.refresh()
    assert "checkboxes" in driver.current_url
    print(driver.title)
    print(driver.current_url)
    driver.quit()

def test_window_size():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    driver.maximize_window()
    viewports = [(375,812),(1920,1080)]
    for width, height in viewports:
        driver.set_window_size(width,height)
        assert driver.find_element(By.LINK_TEXT, "Checkboxes").is_displayed()

def test_screenshot():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    saved = driver.save_screenshot("screenshot/home.png")
    assert saved is True
    driver.quit()

def test_new_tab():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    original_window = driver.current_window_handle
    driver.switch_to.new_window()
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    all_windows = driver.window_handles
    assert len(all_windows) == 2

    print(driver.title)