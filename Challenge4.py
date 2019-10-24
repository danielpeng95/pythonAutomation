import inflect
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

#Fibonacci

class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\benpe\\DevMountain\\testing-resources\\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        p = inflect.engine()

        #Recursive function to print Fibonacci sequence
        def recur_fibo(n):

           if n <= 1:
               return n
           else:
               return(recur_fibo(n-1) + recur_fibo(n-2))

        nterms = 9

        if nterms <= 0:
           print("Enter a positive integer")
        else:
           print("Fibonacci sequence:")
           for i in range(nterms):
               print(str(recur_fibo(i)) + ' ' + p.number_to_words(recur_fibo(i)))


if __name__ == '__main__':
    unittest.main()