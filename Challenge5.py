from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
#Asserts


class Challenge5(unittest.TestCase):

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
        self.driver.find_element_by_id("input-search").send_keys("porsche")
        self.driver.find_element_by_xpath('(//button[@type="submit"])[2]').click()

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name('serverSideDataTable_length').click()

        self.driver.find_element_by_xpath('(//option[@value="100"])[1]').click()

        all_list = []
        new_list = []
        time.sleep(5)
        for i in range(1, 100):
            result = self.driver.find_element_by_xpath(f'(//span[@data-uname="lotsearchLotmodel"])[{i}]').text
            all_list.append(result)

        print("This is the list with all the cars:")
        print(all_list)
        time.sleep(5)

        for i in all_list:
            if i not in new_list:
                new_list.append(i)

        print("This is the list without any repeated cars:")
        print(new_list)

if __name__ == '__main__':
    unittest.main()
