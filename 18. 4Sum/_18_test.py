import unittest
from _18 import *

class MyTest(unittest.TestCase):
    def testFourSum(self):
        test = [[1,0,-1,0,-2,2], 0]
        so = Solution()
        got = so.fourSum(test[0], test[1])
        self.assertEqual(got, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]], "Test Failed")


if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(MyTest("testFourSum"))
    unittest.TextTestRunner(testSuite)