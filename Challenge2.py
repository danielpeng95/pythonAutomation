from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class Challenge2(unittest.TestCase):

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
        self.driver.find_element_by_id("input-search").send_keys("exotics")
        self.driver.find_element_by_xpath('(//button[@type="submit"])[2]').click()

        self.driver.implicitly_wait(10)
        result = self.driver.find_element_by_xpath('(//span[@data-uname="lotsearchLotmake"])[1]').text

        self.driver.implicitly_wait(5)
        self.assertIn(result, "Porsche")
        self.driver.implicitly_wait(5)


if __name__ == '__main__':
    unittest.main()
