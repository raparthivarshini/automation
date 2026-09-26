
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_multi_tabs(driver):
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.find_element(By.LINK_TEXT,"Click Here").click()
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    assert "New Window" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print(driver.title)
    driver.switch_to.new_window('tab')
    driver.get("https://the-internet.herokuapp.com/")
    print(driver.title)
