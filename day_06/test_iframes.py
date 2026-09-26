
from selenium.webdriver.common.by import By

def test_iframes(driver):
    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.find_element(By.CSS_SELECTOR,"div[aria-label='Close'] svg").click()
    iframe = driver.find_element(By.ID,"mce_0_ifr")
    driver.switch_to.frame(iframe)
    iframe_content = driver.find_element(By.TAG_NAME,"p").text
    assert "Your content goes here." in iframe_content
    driver.switch_to.default_content()

def test_nested_frames(driver):
    driver.get("https://the-internet.herokuapp.com/nested_frames")
    #Top frames
    driver.switch_to.frame("frame-top")

     ##Frame left
    driver.switch_to.frame("frame-left")
    assert "LEFT" in driver.find_element(By.TAG_NAME,"body").text
    driver.switch_to.parent_frame()
     ##Frame middle
    driver.switch_to.frame("frame-middle")
    assert "MIDDLE" in driver.find_element(By.ID,"content").text
    driver.switch_to.parent_frame()
     ##Frame right
    driver.switch_to.frame("frame-right")
    assert "RIGHT" in driver.find_element(By.TAG_NAME, "body").text
    driver.switch_to.default_content()
    #Bottom frames
    driver.switch_to.frame("frame-bottom")
    assert "BOTTOM" in driver.find_element(By.TAG_NAME, "body").text
