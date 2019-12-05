from selenium import webdriver
import unittest
import time

#This is an example of how unittest framework order work

def setUpModule(): #will be executed before executing any class or any method present in test class
    print("setUpModule")

def tearDownModule(): #will be executed after completing everything present in the python module
    print("tearDownModule")

#This is how UnitTest Framework work
class Example(unittest.TestCase):

    @classmethod #Execute before all test methods
    def setUp(self):
        print("this is login test")
        # self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        # self.driver.implicitly_wait(20)
        # self.driver.set_page_load_timeout(20)
        # self.driver.maximize_window()

    @classmethod #Execute after all test methods
    def tearDown(self):
        print("this is logout test")
        # self.driver.close()

    @classmethod #will execute once before the class has started
    def setUpClass(cls):
        print("Open Application")

    @classmethod #will execute once after the class has completed
    def tearDownClass(cls):
        print("Close Application")

    def test_search(self):
        print("############this is a search test")

    def test_advancedsearch(self):
        print("###############this is advanced search")

    def test_prepaidRecharge(self):
        print("#############this is prepaid recharge test")

if __name__ == '__main__':
    unittest.main()
