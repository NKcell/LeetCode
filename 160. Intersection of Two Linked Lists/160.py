# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 这个思路真的是很棒，包括可能出现的循环也可以通过最小公倍数出去
    # 这个一个尾连另一个的首这个想法太tm让人**了， 666
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headB is None or headA is None:
            return None

        a = headA
        b = headB

        while a is not b :
            a= a.next if a else headB
            b= b.next if b else headA

        return a