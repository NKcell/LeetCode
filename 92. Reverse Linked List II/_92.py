# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        tmp = head
        pre = head
        for _ in range(m-1):
            pre = tmp
            tmp = tmp.next

        tail = self.reversenode(tmp, n-m+1)
        if m==1:
            return tail
        else:
            pre.next = tail
            return head

    def reversenode(self, head: ListNode, num:int) :
        if num < 2:
            return head
        tmp = list()
        for _ in range(num):
            tmp.append(head.val)
            head = head.next

        tmp.reverse()

        newhead = ListNode(1)
        tmphead = newhead
        for i,v in enumerate(tmp):
            if i==0:
                newhead = ListNode(v)
                tmphead = newhead
            else:
                tmp.next = ListNode(v)
                tmphead = tmphead.next
        tmphead.next = head
        return newhead


            




