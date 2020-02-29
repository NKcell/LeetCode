# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def numComponents(self, head: ListNode, G) -> int:
        myList = list()
        while head:
            myList.append(head.val)
            head = head.next

        count = 0
        flag = 0
        for i in myList:
            if i in G and flag == 0:
                count+=1
                flag = 1
            elif i in G and flag != 0:
                continue
            else:
                flag = 0

        return count

    def numComponents1(self, head, G):
        setG = set(G)
        res = 0
        while head:
            if head.val in setG and (head.next == None or head.next.val not in setG):
                res += 1
            head = head.next
        return res

    def numComponents2(self, head, G):
        p, prev, count, G = head, False, 0, set(G)
        while p:
            if p.val in G and not prev:
                count += 1
            prev, p = p.val in G, p.next
        
        return count