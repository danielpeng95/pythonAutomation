import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        self.assertIsNotNone(self.driver)

        self.driver = None
        self.assertIsNone(self.driver)

if __name__ == "__main__":
    unittest.main()