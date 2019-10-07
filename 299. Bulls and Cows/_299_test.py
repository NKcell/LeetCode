import unittest
from _299 import *

class test():
    def __init__(self, input1, input2, want):
        self.input1 = input1
        self.input2 = input2
        self.want = want

class myTest(unittest.TestCase):
    def testGetHint(self):
        so = Solution()

        test1 = test("1807", "7810", "1A3B")
        test2 = test("1123", "0111", "1A1B")

        got1 = so.getHint(test1.input1, test1.input2)
        got2 = so.getHint(test2.input1, test2.input2)

        self.assertEqual(got1, test1.want, "Test1 Failed!")
        self.assertEqual(got2, test2.want, "Test1 Failed!")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(myTest("testGetHint"))
    unittest.TextTestRunner(testSuite)