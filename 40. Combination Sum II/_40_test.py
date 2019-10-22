import unittest
from _40 import *


class test():
    def __init__(self, input1, input2, want):
        self.input1 = input1
        self.input2 = input2
        self.want = want


class myTest(unittest.TestCase):
    def testCombinationSum2(self):
        so = Solution()

        test1 = test([10,1,2,7,6,1,5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
        test2 = test([2,5,2,1,2], 5, [[1,2,2],[5]])

        got1 = so.combinationSum2(test1.input1, test1.input2)
        got2 = so.combinationSum2(test2.input1, test2.input2)

        self.assertEqual(test1.want, got1, "Test1 Failed!")
        self.assertEqual(test2.want, got2, "Test2 Failed!")