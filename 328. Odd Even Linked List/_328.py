# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        even = head.next
        tmpeven = even
        odd = head
        tmpodd = odd
        flag = 1

        count = 0
        while head:
            if count<2:
                count+=1
                head = head.next
                continue
            if flag:
                odd.next = head
                odd = odd.next
                head = head.next
                flag = 0
            else:
                even.next = head
                even = even.next
                head = head.next
                flag = 1
        
        even.next = None
        odd.next = tmpeven

        return tmpodd

    def oddEvenList1(self, head):
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next

