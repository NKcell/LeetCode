import unittest
from _876 import *

class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMiddleNode(self):
        a1 = ListNode(5)
        a1.next = None
        a2 = ListNode(4)
        a2.next = a1
        a3 = ListNode(3)
        a3.next = a2
        a4 = ListNode(2)
        a4.next = a3
        a5 = ListNode(1)
        a5.next = a4
        
        a = Solution()
        self.assertEqual(a.middleNode(a5), a3, "Test1 Failed")

        a0 = ListNode(6)
        a0.next = None
        a1.next = a0
        self.assertEqual(a.middleNode(a5), a2, "Test2 Failed")

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(MyTest('testMiddleNode'))
    unittest.TextTestRunner(test_suite)