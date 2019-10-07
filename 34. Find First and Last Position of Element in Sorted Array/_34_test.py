import unittest
from _34 import *

class test():
    def __init__(self, input1, input2, want):
        self.input1 = input1
        self.input2 = input2
        self.want = want

class myTest(unittest.TestCase):
    def testSearchRange(self):
        so = Solution()
        test1 = test([1],1,[0,0])
        test2 = test([5,7,7,8,8,10],8,[3,4])
        test3 = test([5,7,7,8,8,10],6,[-1,-1])

        want1 = so.searchRange(test1.input1, test1.input2)
        want2 = so.searchRange(test2.input1, test2.input2)
        want3 = so.searchRange(test3.input1, test3.input2)

        self.assertEqual(want1, test1.want, "Test1 Failed!")
        self.assertEqual(want2, test2.want, "Test2 Failed!")
        self.assertEqual(want3, test3.want, "Test3 Failed!")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(myTest("testSearchRange"))
    unittest.TextTestRunner(testSuite)
