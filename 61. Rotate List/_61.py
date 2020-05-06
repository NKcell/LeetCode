# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        tmpHead = head
        linkLen = 1
        while tmpHead.next is not None:
            linkLen += 1
            tmpHead = tmpHead.next

        k = k%linkLen
        nodePointPre = linkLen - k - 1

        if nodePointPre == -1:
            return head

        tmp = 0
        tmpHead2 = head
        while tmp != nodePointPre:
            tmp += 1
            tmpHead2 = tmpHead2.next

        tmpHead.next = head
        head = tmpHead2.next
        tmpHead2.next = None

        return head

a1 = ListNode(0)
a2 = ListNode(1)
a3 = ListNode(2)
a1.next = a2
a2.next = a3
a = Solution()
newlink = a.rotateRight(a1, 4)
while newlink:
    print(newlink.val )
    newlink = newlink.next