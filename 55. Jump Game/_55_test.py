import unittest
from _55 import *

class test():
    def __init__(self, input, want):
        self.input = input
        self.want = want

class myTest(unittest.TestCase):
    def testCanJump(self):
        so = Solution()
        test1 = test([2,3,1,1,4], True)
        test2 = test([3,2,1,0,4], False)
        test3 = test([0], True)

        got1 = so.canJump1(test1.input)
        got2 = so.canJump1(test2.input)
        got3 = so.canJump1(test3.input)

        self.assertEqual(test1.want, got1, "Test1 Failed!")
        self.assertEqual(test2.want, got2, "Test2 Failed!")
        self.assertEqual(test3.want, got3, "Test3 Failed!")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(myTest("testCanJump"))        
    unittest.TextTestRunner(testSuite)