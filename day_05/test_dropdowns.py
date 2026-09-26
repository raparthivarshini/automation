
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_dropdown_by_text(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = driver.find_element(By.XPATH,"//select[@id='dropdown']")
    select = Select(dropdown)
    select.select_by_visible_text("Option 1")

    assert select.first_selected_option.text == "Option 1"
    for item in select.options:
        print(item.text)
    assert len(select.options) == 3

def test_dropdown_by_index(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = driver.find_element(By.XPATH,"//select[@id='dropdown']")
    select = Select(dropdown)
    select.select_by_index(0)

def test_dropdown_by_value(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = driver.find_element(By.XPATH,"//select[@id='dropdown']")
    select = Select(dropdown)
    select.select_by_value("2")

def test_standard_multi_select(driver):
    driver.get("https://demoqa.com/select-menu")
    options = driver.find_element(By.ID,"cars")
    select = Select(options)
    if select.is_multiple:
        select.select_by_value("saab")
        select.select_by_value("volvo")

def test_select_value(driver):
    driver.get("https://demoqa.com/select-menu")
    driver.find_element(By.XPATH,"//div[@id='withOptGroup']").click()
    driver.find_element(By.XPATH,"//div[contains(text(),'Group 1, option 2')]").click()
    selected_text = driver.find_element(By.CSS_SELECTOR,
                                        "div[id='withOptGroup'] div[class*='singleValue']").text
    assert selected_text == "Group 1, option 2"

def test_select_one(driver):
    driver.get("https://demoqa.com/select-menu")
    driver.find_element(By.XPATH,"//div[@id='selectOne']").click()
    driver.find_element(By.XPATH,"//div[contains(text(),'Mr.')]").click()
    selected_text = driver.find_element(By.CSS_SELECTOR,"div[id='selectOne'] div[class='css-1dimb5e-singleValue']").text
    assert selected_text == "Mr."
