# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = list()
        tmp = head
        while tmp != None:
            res.append(tmp.val)
            tmp = tmp.next
        
        big = [res.pop()]
        fin = [0]

        while res:
            tmp = res.pop()
            while big and tmp>=big[-1]:
                big.pop()
            if not big:
                fin.append(0)
            else:
                fin.append(big[-1])
            big.append(tmp)

        fin.reverse()
        return fin