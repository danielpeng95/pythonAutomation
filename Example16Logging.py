from selenium import webdriver
import unittest
import time
import logging

class Example(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_challenge(self):
        #self.driver.get("")
        self.driver.implicitly_wait(10)

        #it logs it into a file
        logging.basicConfig(filename="C://Users/benpe/PycharmProjects/firstExample/test.log")

        logging.debug("This is debug message")
        logging.info("This is info message")
        logging.warning("This is warning message")
        logging.error("This is error message")
        logging.critical("This is critical message")

        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
