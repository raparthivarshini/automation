from selenium.webdriver.common.by import By


def test_tick_checkboxes(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    check_boxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    for check_box in check_boxes:
        if not check_box.is_selected():
            check_box.click()
        assert check_box.is_selected()
def test_un_tick_checkboxes(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    check_boxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    for check_box in check_boxes:
        if check_box.is_selected():
            check_box.click()
        assert not check_box.is_selected()

def test_yes_radio_button(driver):
    driver.get("https://demoqa.com/radio-button")
    driver.find_element(By.ID,"yesRadio").click()
    msg = driver.find_element(By.XPATH,"//p[@class='mt-3']").text
    assert msg == "You have selected Yes"


def test_impressive_radio_button(driver):
    driver.get("https://demoqa.com/radio-button")
    driver.find_element(By.ID, "impressiveRadio").click()
    msg = driver.find_element(By.XPATH, "//p[@class='mt-3']").text
    assert msg == "You have selected Impressive"
    assert not driver.find_element(By.ID,"yesRadio").is_selected()
#
def test_no_radio_button(driver):
    driver.get("https://demoqa.com/radio-button")
    assert not driver.find_element(By.XPATH,"//input[@id='noRadio']").is_enabled()