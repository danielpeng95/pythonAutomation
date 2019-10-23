from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.copart.com")

        self.driver.implicitly_wait(10)
        for i in range(1, 6):
            locator = self.driver.find_element_by_xpath(f'(//li[@ng-repeat="popularSearch in popularSearches | limitTo: 5"])[{i}]')
            print(locator.text)

        for i in range(1, 6):
            locator = self.driver.find_element_by_xpath(f'(//li[@ng-repeat="popularSearch in popularSearches | limitTo: 5 : 5"])[{i}]')
            print(locator.text)

if __name__ == '__main__':
    unittest.main()
