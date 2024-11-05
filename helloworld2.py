from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get ("https://www.google.com/")
driver.find_element(By.ID,'APjFqb').send_keys('hola'+Keys.ENTER)
driver.find_element(By.LINK_TXT, "Actualidad").click()
#driver.close()