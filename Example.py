from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ExampleInputBox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def Example(self):
        self.driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        self.driver.implicitly_wait(10)

        inputboxes = self.driver.find_elements(By.CLASS_NAME, 'text_field')
        print(len(inputboxes))

        self.driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Daniel")
        self.driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("Peng")
        self.driver.find_element_by_id("RESULT_TextField-3").send_keys("1234567890")



        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
