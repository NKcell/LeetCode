# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        tmp = 0
        while head is not None:
            tmp = tmp*2+head.val
            head = head.next
        return tmp

    def getDecimalValue1(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = (ans << 1) | head.val
            head = head.next
        return ans