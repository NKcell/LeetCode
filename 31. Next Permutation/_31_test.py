import unittest
from _31 import *

class myTest(unittest.TestCase):
    def testNextPermutation(self):
        so = Solution()
        test1 = [3,5,8,7,6,4]
        test2 = [1,2,3]
        test3 = [3,2,1]
        test4 = [1,1,5]
        so.nextPermutation(test1)
        so.nextPermutation(test2)
        so.nextPermutation(test3)
        so.nextPermutation(test4)
        self.assertEqual(test1, [3,6,4,5,7,8], "Test1 Error!")
        self.assertEqual(test2, [1,3,2], "Test2 Error!")
        self.assertEqual(test3, [1,2,3], "Test3 Error!")
        self.assertEqual(test4, [1,5,1], "Test4 Error!")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(myTest('testNextPermutation'))
    unittest.TextTestRunner(testSuite)