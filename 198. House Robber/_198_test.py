import unittest
from _198 import *


class test():
    def __init__(self, input, want):
        self.input = input
        self.want = want

class myTest(unittest.TestCase):
    def testRob(self):
        so = Solution()

        test1 = test([], 0)
        test2 = test([1,2], 2)
        test3 = test([1,2,3,1], 4)
        test4 = test([2,7,9,3,1], 12)

        got1 = so.rob(test1.input)
        got2 = so.rob(test2.input)
        got3 = so.rob(test3.input)
        got4 = so.rob(test4.input)

        self.assertEqual(test1.want, got1, "Test1 Failed!")
        self.assertEqual(test2.want, got2, "Test2 Failed!")
        self.assertEqual(test3.want, got3, "Test3 Failed!")
        self.assertEqual(test4.want, got4, "Test4 Failed!")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(myTest("testRob"))
    unittest.TextTestRunner(testSuite)