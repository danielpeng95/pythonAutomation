import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        title = self.driver.title

        #assertEqual
        self.assertEqual("Google", title, "Web page title is not same")

        #this will give you an error
        #self.assertEqual("notGoogle", title, "Web page title is not the same")

        #assertNotEqual
        self.assertNotEqual("notGoogle", title, "Web page title is not the same")

if __name__ == "__main__":
    unittest.main