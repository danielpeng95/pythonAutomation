from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
#Loops

class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get("https://www.copart.com")

        self.driver.implicitly_wait(10)
        # for i in range(1, 6):
        #     locator = self.driver.find_element_by_xpath(f'(//li[@ng-repeat="popularSearch in popularSearches | limitTo: 5"])[{i}]')
        #     print(locator.text)

        for i in range(1, 5):
            locator = self.driver.find_element_by_xpath(f'(//div[@class="col-lg-3 col-sm-3 col-md-3 col-xs-6 col-xs-ext-sm"])[{i}]')
            print(locator.text)

        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
