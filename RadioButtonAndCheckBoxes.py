from selenium import webdriver
from selenium.webdriver.common.by import By
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
        self.driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        self.driver.implicitly_wait(10)

        status = self.driver.find_element_by_xpath('(//label[@for="RESULT_RadioButton-7_0"])').is_selected()
        print("Selected: ", status)

        time.sleep(2)

        self.driver.find_element_by_xpath('(//label[@for="RESULT_RadioButton-7_0"])').click()

        time.sleep(2)

        status2 = self.driver.find_element_by_xpath('(//label[@for="RESULT_RadioButton-7_0"])').is_enabled()
        print("Selected: ", status2)

        self.driver.find_element_by_xpath('(//label[@for="RESULT_CheckBox-8_0"])').click()
        self.driver.find_element_by_xpath('(//label[@for="RESULT_CheckBox-8_6"])').click()


        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
