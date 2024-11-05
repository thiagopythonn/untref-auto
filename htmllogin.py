import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test1(unittest.TestCase):
    def setUP(self) -> None:
        self.driver =webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.saucedemo.com/")
        
if __name__ == "__main__":
    unittest.main()