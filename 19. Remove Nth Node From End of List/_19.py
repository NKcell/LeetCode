# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head
        nodeLen = 0
        myPre = head
        while myPre:
            nodeLen += 1
            myPre = myPre.next

        if nodeLen == 1:
            return None
        
        if nodeLen == 0:
            return head
        
        if nodeLen == n:
            return head.next
        
        myPre = head
        for _ in range(nodeLen-n-1):
            myPre = myPre.next
        
        myPre.next = myPre.next.next
        return head

    # 这个递归的方法效率并不高
    def removeNthFromEnd1(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next

    # 这个没用递归用的双指针的方法真的不错我很喜欢，这种快慢指针的应用真的是在链表中常用，多练习，遇到链表多思考下快慢指针的可能性
    def removeNthFromEnd2(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    # 这个真的是只用了一次遍历，相当于用空间换了时间， 这个self用的很骚气啊
    def removeNthFromEnd3(self, head, n):
        self.next, nodelist  = head, [self]
        while head.next:
            if len(nodelist) == n:
                nodelist.pop(0)
            nodelist += head,
            head = head.next
        nodelist[0].next = nodelist[0].next.next 
        return self.next