# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        res = list()
        flag = 0
        while head:
            if not res:
                res.append(head.val)
                head = head.next
                continue

            if res[-1] == head.val:
                flag = 1
            else:
                if flag == 1:
                    flag = 0
                    res.pop()
                    res.append(head.val)
                else:
                    res.append(head.val)
            head = head.next

        if flag == 1:
            res.pop()
        if not res:
            return None
        head = ListNode(res[0])
        tmp = head
        for i in range(1, len(res)):
            tmpnode = ListNode(res[i])
            tmp.next = tmpnode
            tmp = tmpnode
        
        tmp.next = None
        return head


a1 = ListNode(1)
a2 = ListNode(1)
a3 = ListNode(1)
a4 = ListNode(2)
a5 = ListNode(3)
a6 = ListNode(4)
a7 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
# a5.next = a6
# a6.next = a7

a = Solution()
x = a.deleteDuplicates(None)
while(x):
    print(x.val)
    x = x.next