class ListNode:
    def __init__(self, x):
       self.val = x
       self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l1list = []
    if l1 is not None:
        while l1.next != None:
            l1list.append(l1.val)
            l1 = l1.next
        l1list.append(l1.val)

    if l2 is not None:
        l2list = []
        while l2.next != None:
            l2list.append(l2.val)
            l2 = l2.next
        l2list.append(l2.val)

    l3list = l1list + l2list
    l3list.sort()

    l3 = ListNode(0)
    rl3 = l3
    for i in l3list:
        l3.next = ListNode(i)
        l3 = l3.next

    return rl3.next