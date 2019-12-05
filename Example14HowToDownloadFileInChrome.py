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

    def test_example(self):
        self.driver.get("http://demo.automationtesting.in/FileDownload.html")
        self.driver.implicitly_wait(10)

        #download text file
        self.driver.find_element_by_xpath('//textarea[@id="textbox"]').send_keys("Testing")
        self.driver.find_element_by_xpath('//button[@id="createTxt"]').click() #generate file button
        self.driver.find_element_by_xpath('//a[@download="info.txt"]').click() #download link

        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
