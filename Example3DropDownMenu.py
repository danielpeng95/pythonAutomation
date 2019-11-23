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
        self.driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        self.driver.implicitly_wait(10)

        element = self.driver.find_element_by_id("RESULT_RadioButton-9")
        drp = Select(element)
        #select by visible text
        drp.select_by_visible_text('Morning')
        time.sleep(2)

        #select by index number
        drp.select_by_index(1) #Afternoon
        time.sleep(2)

        #select by value
        drp.select_by_value("Radio-2") #Evening
        time.sleep(2)

        print(len(drp.options))


        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
