import unittest
from _1200 import *

class test():
    def __init__(self, input, want):
        self.input = input
        self.want = want

class myTest(unittest.TestCase):
    def testMinimumAbsDifference(self):
        so = Solution()
        test1 = test([4,2,1,3], [[1,2],[2,3],[3,4]])
        test2 = test([1,3,6,10,15], [[1,3]])
        test3 = test([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]])
        got1 = so.minimumAbsDifference(test1.input)
        got2 = so.minimumAbsDifference(test2.input)
        got3 = so.minimumAbsDifference(test3.input)
        self.assertEqual(got1, test1.want, "Test1 Failed")
        self.assertEqual(got2, test2.want, "Test2 Failed")
        self.assertEqual(got3, test3.want, "Test3 Failed")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(myTest("testMinimumAbsDifference"))
    unittest.TextTestRunner(testSuite)