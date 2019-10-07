# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
            
        slow = head
        fast = head.next

        if fast:
            head = fast

        while slow and fast:
            slow.next = fast.next
            fast.next = slow
            
            fast = slow.next
            if fast and fast.next:
                slow.next = fast.next
                slow = fast
                fast = fast.next
            else:
                if not fast:
                    break
                slow = fast
                fast = fast.next

        return head

# 怎么说了感觉这个链表不难能实现，但没别人写的那么简练
# Iteratively
def swapPairs1(self, head):
    dummy = p = ListNode(0)
    dummy.next = head
    while head and head.next:
        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        p.next = tmp
        head = head.next
        p = tmp.next
    return dummy.next

# Recursively    
def swapPairs(self, head):
    if head and head.next:
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp
    return head