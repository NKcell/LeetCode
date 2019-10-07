import unittest
from _136 import *

class MyTest(unittest.TestCase):
    def testSingleNumber(self):
        test1 = [2,2,1]
        want1 = 1
        test2 = [4,1,2,1,2]
        want2 = 4

        so = Solution()
        got1 = so.singleNumber(test1)
        got2 = so.singleNumber(test2)

        self.assertEqual(got1, want1, "test1 failed!")
        self.assertEqual(got2, want2, "test2 failed!")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(MyTest("testSingleNumber"))
    unittest.TextTestRunner(testSuite)