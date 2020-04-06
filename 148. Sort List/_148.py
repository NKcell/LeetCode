# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        tmpNode = head
        myDict = dict()
        while tmpNode:
            tmp = myDict.get(tmpNode.val, 0)
            if tmp == 0:
                myDict[tmpNode.val] = [tmpNode]
            else:
                tmp.append(tmpNode)
                myDict[tmpNode.val] = tmp
            tmpNode = tmpNode.next

        flag = 0
        for k in sorted(myDict):
            for i in myDict[k]:
                if flag == 0:
                    head = i
                    tmpNode = head
                    flag = 1
                else:
                    tmpNode.next = i
                    tmpNode =  i


        if tmpNode:
            tmpNode.next = None

        return head