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

        inputboxes = self.driver.find_elements(By.CLASS_NAME, 'text_field')
        print(len(inputboxes))

        status = self.driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
        print("Displayed: ", status)

        status2 = self.driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
        print("Enabled: ", status2)

        self.driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Daniel")
        self.driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("Peng")
        self.driver.find_element_by_id("RESULT_TextField-3").send_keys("1234567890")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
