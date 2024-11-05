import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test1(unittest.TestCase):
    def setUP(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
        
    def login(self, usuario, password):
        self.driver.find_element(By.ID,'user-name').send_keys(usuario)
        self.driver.find_element(By.ID,"password").send_keys(password)
        self.driver.find_element(By.ID,"login-button").click()
        
    def checkout(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID,"checkout").click()
        self.driver.find_element(By.ID,"first-name").send_keys(first_name)
        self.driver.find_element(By.ID,"last-name").send_keys(last_name)
        self.driver.find_element(By.ID,"postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID,"continue").click()
        
    def finish(self):
        self.driver.find_element(By.ID,"finish").click()
        
    def go_to_car(self):
        self.driver.find_element(By.ID,"shopping_cart_container").click()
    
    def select_element(self, element):
        elements = {"pepa":"add-to-cart-sauce-labs-backpack","pepe":"remove-sauce-labs-backpack","pepo":"continue-shopping","pepi":"add-to-cart-sauce-labs-bike-light","pepu":"add-to-cart-sauce-labs-bolt-t-shirt"}
        self.driver.find_element(By.ID,elements[element]).click()
    
    def get_final_check_articles(self, order):
        return self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")(order).text
   
    def get_final_menssage(self):
        return self.driver.find_element(By.CLASS_NAME,"complete-header").text
   
    def test_caso1(self):
        self.login("standard_user","secret_sauce")
        self.select_element("pepa")
        self.go_to_car()
        self.select_element("pepe")
        self.select_element("pepo")
        self.select_element("pepi")
        self.select_element("pepu")
        self.go_to_car()
        self.checkout("thiago","thiago","50000")
        self.driver.find_element(By.ID,"continue").click()
        self.finish()
        messange = self.get_final_menssage()
        self.assertEqual("thank you for you order!",messange)
if __name__ == "__main__":
    unittest.main()