import unittest

class AppTesting(unittest.TestCase):

    #this will skip/ignor this test
    @unittest.SkipTest #these are called decorator
    def test_search(self):
        print("This is search test")

    def test_advancedSearch(self):
        print("this is advanced search method")

    def test_prepaidRecharge(self):
        print("this is prepaid recharge")

    def test_postpaidRecharge(self):
        print("this is postpaid recharge")

    def test_loginByGmail(self):
        print("this is login by eamil test")

    def test_loginByTwitter(self):
        print("this is login by twitter")


if __name__ == '__main__':
    unittest
