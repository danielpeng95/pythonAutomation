import unittest


class Test(unittest.TestCase):
    def testName(self):
        my_list = {"python", "selenium", "java"}
        self.assertIn("python", my_list)
        self.assertNotIn("JavaScript", my_list)


if __name__ == "__main__":
    unittest.main()
