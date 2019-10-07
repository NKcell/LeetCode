import unittest
from _39 import *


class test():
    def __init__(self, input1, input2, want):
        self.input1 = input1
        self.input2 = input2
        self.want = want


class myTest(unittest.TestCase):
    def testCombinationSum(self):
        so = Solution()

        test1 = test([2,3,6,7], 7, [[2,2,3], [7]])
        test2 = test([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]])
        test3 = test([7,3,2], 18, [[2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,3,3],[2,2,2,2,3,7],[2,2,2,3,3,3,3],[2,2,7,7],[2,3,3,3,7],[3,3,3,3,3,3]])

        got1 = so.combinationSum(test1.input1, test1.input2)
        got2 = so.combinationSum(test2.input1, test2.input2)
        got3 = so.combinationSum(test3.input1, test3.input2)

        self.assertEqual(test1.want, got1, "Test1 Failed!")
        self.assertEqual(test2.want, got2, "Test1 Failed!")
        self.assertEqual(test3.want, got3, "Test1 Failed!")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(myTest("testCombinationSum"))
    unittest.TextTestRunner(testSuite)