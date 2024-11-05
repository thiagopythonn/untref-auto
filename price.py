from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.implicitly_wait(8)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,'user-name').send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").send_keys(Keys.ENTER)
driver.find_element(By.CLASS_NAME, "product_sort_container").click()
driver.find_element(By.value,"lohi").click()
driver.find_element(By.CSS_SELECTOR, value=("lohi"))