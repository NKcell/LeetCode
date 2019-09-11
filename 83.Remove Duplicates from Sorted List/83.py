class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return  head

    l = head
    while l.next is not None:
        if l.val == l.next.val:
            l.next = l.next.next
        else:
            l = l.next

    return head


l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(2)

l1 = deleteDuplicates(l1)

while l1 is not None:
    print(l1.val)
    l1 = l1.next