from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
}
options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()

products = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
print(len(products))
for product in products:
    print(product.text)

# product_1 = driver.find_element(By.XPATH,"//div[text()='Sauce Labs Bike Light']")
# product_2 = driver.find_element(By.XPATH,"//div[starts-with(text(),'Sauce Labs')]")
# product_3 = driver.find_element(By.XPATH,"//div[text()='Sauce Labs Onesie']"
#                                          "/ancestor::div[contains(@class,'inventory"
#                                          "_item_desc')]//div[contains(@class,'inventory"
#                                          "_item_price')]")
# product_4 = driver.find_element(By.XPATH,"//div[text()='Test.allTheThings() T-Shirt (Red)']"
#                                          "/ancestor::div[@class='inventory_item_description']"
#                                          "//button[text()='Add to cart']")
# product_5 = driver.find_element(By.XPATH,"//div[text()='Sauce Labs Fleece Jacket']/ancestor"
#                                          "::div[@class='inventory_item_label']//div[contains(@class"
#                                          ",'inventory_item_desc')]")
