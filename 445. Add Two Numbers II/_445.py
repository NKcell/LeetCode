# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1 = 0
        v2 = 0
        while l1 != None:
            v1 = v1*10 + l1.val
            l1 = l1.next
        while l2 != None:
            v2 = v2*10 + l2.val
            l2 = l2.next
        
        v = v1+v2
        v = str(v)
        tmp = None
        for i in range(len(v)-1, -1, -1):
            node = ListNode(int(v[i]))
            node.next = tmp
            tmp = node
        return tmp

