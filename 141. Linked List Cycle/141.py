# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        if head == None:
            return False
        while True:
            if fast.next == None or fast.next.next == None:
                return False
            if fast.next == slow or fast.next.next == slow:
                return True
            
            fast = fast.next.next
            slow = slow.next
