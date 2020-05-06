# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1 = None
        tmp1 = None
        flag1 = 0
        head2 = None
        tmp2 = None
        flag2 = 0
        while head != None:
            if head.val < x:
                if flag1 == 0:
                    flag1 = 1
                    head1 = head
                    tmp1 = head
                else:
                    tmp1.next = head
                    tmp1 = tmp1.next
            else:
                if flag2 == 0:
                    flag2 = 1
                    head2 = head
                    tmp2 = head
                else:
                    tmp2.next = head
                    tmp2 = tmp2.next

            head = head.next

        if tmp1:
            tmp1.next = head2
        if tmp2:
            tmp2.next = None

        if head1:
            return head1
        return head2