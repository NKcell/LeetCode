import unittest
from _19 import *

class myTest(unittest.TestCase):
    def testRemoveNthFromEnd(self):
        a1 = ListNode(1)
        a2 = ListNode(2)
        a3 = ListNode(3)
        a4 = ListNode(4)
        a5 = ListNode(5)
        a1.next = a2
        a2.next = a3
        a3.next = a4
        a4.next = a5

        b1 = ListNode(1)
        b2 = ListNode(2)
        b1.next = b2

        test1 = [a1, 2, a5] 
        test2 = [b1, 2, b2]

        so = Solution()
        got1 = so.removeNthFromEnd(test1[0], test1[1])
        got2 = so.removeNthFromEnd(test2[0], test2[1])
        self.assertEqual(got1.next.next.next, test1[2], "Test1 Failed")
        self.assertEqual(got2, test2[2])