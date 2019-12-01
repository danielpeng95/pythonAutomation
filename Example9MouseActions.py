from selenium import webdriver
import unittest
import time
from selenium.webdriver import ActionChains


class Example(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_challenge(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath('//*[@id="divUsername"]/span').send_keys("Admin")
        self.driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("admin123")
        self.driver.find_element_by_xpath('//*[@id="btnLogin"]').click()


        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
