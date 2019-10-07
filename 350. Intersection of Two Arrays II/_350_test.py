import unittest
from _350 import *

class test():
    def __init__(self, input1, input2, want):
        self.input1 = input1
        self.input2 = input2
        self.want = want


class myTest(unittest.TestCase):
    def testIntersect(self):
        so = Solution()

        test1 = test([1,2,2,1], [2,2], [2,2])
        test2 = test([4,9,5], [9,4,9,8,4], [9,4])

        got1 = so.intersect(test1.input1, test1.input2)
        got2 = so.intersect(test2.input1, test2.input2)

        self.assertEqual(test1.want, got1, "Test1 Failed!")
        self.assertEqual(test2.want, got2, "Test2 Failed!")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(myTest("testIntersect"))
    unittest.TextTestRunner(testSuite)