# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 写的很不python...
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        if head == None: # if not head
            return False
        while True:
            if fast.next == None or fast.next.next == None:
                return False
            if fast.next == slow or fast.next.next == slow:
                return True
            
            fast = fast.next.next
            slow = slow.next

    # 这个写法要好很多
    def hasCycle1(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast and fast.next and slow:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False