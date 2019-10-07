import unittest
from _349 import *

class test():
    def __init__(self, input1, input2, want):
        self.input1 = input1
        self.input2 = input2
        self.want = want

class myTest(unittest.TestCase):
    def testIntersection(self):
        so = Solution()

        test1 = test([1,2,2,1], [2,2], [2])
        test2 = test([4,9,5], [9,4,9,8,4], [9,4])

        got1 = so.intersection(test1.input1, test1.input2)
        got2 = so.intersection(test2.input1, test2.input2)

        self.assertEqual(got1, test1.want, "Test1 Failed!")
        self.assertEqual(got2, test2.want, "Test2 Failed!")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(myTest("testIntersection"))
    unittest.TextTestRunner(testSuite)