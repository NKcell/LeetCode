import unittest
from _33 import *

class test():
    def __init__(self, input1, input2, want):
        self.input1 = input1
        self.input2 = input2
        self.want = want

class myTest(unittest.TestCase):
    def testSearch(self):
        so = Solution()

        test1 = test([], 1, -1)
        test2 = test([1,3], 1, 0)
        test3 = test([5,1,3], 1, 1)
        test4 = test([4,5,6,7,0,1,2], 0, 4)
        test5 = test([4,5,6,7,0,1,2], 3, -1)

        got1 = so.search(test1.input1, test1.input2)
        got2 = so.search(test2.input1, test2.input2)
        got3 = so.search(test3.input1, test3.input2)
        got4 = so.search(test4.input1, test4.input2)
        got5 = so.search(test5.input1, test5.input2)

        self.assertEqual(test1.want, got1, "Test1 Failed!")
        self.assertEqual(test2.want, got2, "Test2 Failed!")
        self.assertEqual(test3.want, got3, "Test3 Failed!")
        self.assertEqual(test4.want, got4, "Test4 Failed!")
        self.assertEqual(test5.want, got5, "Test5 Failed!")

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(myTest('testSearch'))
    unittest.TextTestRunner(testSuite)