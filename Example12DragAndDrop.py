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
        self.driver.get("https://testautomationpractice.blogspot.com")
        self.driver.implicitly_wait(10)

        source = self.driver.find_element_by_xpath('//*[@id="draggable"]')
        target = self.driver.find_element_by_xpath('//div[@id="droppable"]')

        #drag and drop element
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform() #make sure to add a perform at the end


        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
