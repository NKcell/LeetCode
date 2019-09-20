# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p = head
        nodeLen = 0
        while p != None:
            nodeLen += 1
            p = p.next
        midloc = nodeLen//2
        ansNode = head
        for _ in range(midloc):
            ansNode = ansNode.next

        return ansNode

    # 这种双指针的方法很巧妙啊，而且用的也很多啊
    def middleNode1(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        # 这样还可以少一个变量，但可读性感觉不如上面
        # tmp = head
        # while tmp and tmp.next:
        #     head = head.next
        #     tmp = tmp.next.next
        # return head