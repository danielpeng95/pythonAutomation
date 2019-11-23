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
        self.driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
        self.driver.implicitly_wait(10)

        #1st frame
        self.driver.switch_to_frame("packageListFrame")
        self.driver.find_element_by_link_text("org.openqa.selenium").click()
        #we need this to work
        self.driver.switch_to.default_content()

        #2nd frame
        self.driver.switch_to_frame("packageFrame")
        self.driver.find_element_by_link_text("WebDriver").click()
        self.driver.switch_to_default_content()

        #3rd frame
        self.driver.switch_to_frame("classFrame")
        #link text didn't work so I swtiched to Xpath
        self.driver.find_element_by_xpath('(//a[@href="package-summary.html"])[1]').click()





        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
