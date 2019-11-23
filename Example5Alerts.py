from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import time


class Example(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_challenge(self):
        self.driver.get("https://testautomationpractice.blogspot.com")
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath('//button[@onclick="myFunction()"]').click()
        time.sleep(3)

        #closes alert window using OK button
        self.driver.switch_to_alert().accept()

        self.driver.find_element_by_xpath('//button[@onclick="myFunction()"]').click()
        time.sleep(3)

        #closes alert window by using Cancel button
        self.driver.switch_to_alert().dismiss()

        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
