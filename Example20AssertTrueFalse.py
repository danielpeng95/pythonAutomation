import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        self.driver.get("https://google.com")

        title = self.driver.title

        self.assertTrue(title == "Google")

        self.assertFalse(title == "Not Google")

if __name__ == "__main__":
    unittest.main()