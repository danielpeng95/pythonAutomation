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
        self.driver.get("http://newtours.demoaut.com/")
        self.driver.implicitly_wait(10)
        links = self.driver.find_element_by_tag_name("a")
        #BELOW DOESN'T WORK
        # print(len(links))
        # print("Number of links present in a page:", len(links))
        # for link in links:
        #     print(link.text)

        #clicking on the link
        self.driver.find_element(By.LINK_TEXT, "REGISTER").click()

        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
