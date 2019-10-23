from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class Challenge1(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):

        self.driver.get("https://www.google.com")
        assert 'Google' in self.driver.title
        self.assertIn("Google", self.driver.title)
        time.sleep(5)


        # self.driver.find_element_by_name('q').send_keys("Puppies")
        # self.driver.find_element_by_name("btnK").submit()
        # self.driver.find_element_by_name("btnK").send_keys(Keys.RETURN)
        #
        # assert 'Puppies' in self.driver.title


if __name__ == '__main__':
    unittest.main()

