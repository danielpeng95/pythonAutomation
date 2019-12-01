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
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.implicitly_wait(10)

        #sign into the website
        self.driver.find_element_by_xpath('//input[@name="txtUsername"]').send_keys("Admin")
        self.driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("admin123")
        self.driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

        admin = self.driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
        usermgnt = self.driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
        users = self.driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

        #mouseover/mousehover action
        actions = ActionChains(self.driver)
        actions.move_to_element(admin).move_to_element(usermgnt).move_to_element(users).click().perform()





        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
