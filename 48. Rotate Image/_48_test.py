import unittest
from _48 import *


class test():
    def __init__(self, input, want):
        self.input = input
        self.want = want

class myTest(unittest.TestCase):
    def testRotate(self):
        so = Solution()

        test1 = test([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]])
        test2 = test([[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]], [[15,13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7,10,11]])

        so.rotate(test1.input)
        so.rotate(test2.input)

        self.assertEqual(test1.input, test1.want, "Test1 Failed!")
        self.assertEqual(test2.input, test2.want, "Test2 Failed!")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(myTest("testRotate"))
    unittest.TextTestRunner(testSuite)