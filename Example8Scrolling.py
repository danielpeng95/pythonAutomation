from selenium import webdriver
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
        self.driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
        self.driver.implicitly_wait(10)

        #Scroll down the page by pixel
        self.driver.execute_script("window.scrollBy(0, 1000)", "")
        time.sleep(3)

        #Scroll down the page until element found
        TaiwanFlag = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[79]/td[2]')
        self.driver.execute_script("arguments[0].scrollIntoView();", TaiwanFlag)
        time.sleep(3)

        #Scroll to the end of the page
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
