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
        self.driver.get("http://newtours.demoaut.com/mercurywelcome.php")
        self.driver.implicitly_wait(10)

        self.driver.save_screenshot("C:\PycharmProjects\ScreenShots\homePage.jpeg")

        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
