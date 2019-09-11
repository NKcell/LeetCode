class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


# def addTwoNumbers(l1, l2):
#     """
#     :type l1: ListNode
#     :type l2: ListNode
#     :rtype: ListNode
#     """
#     link1 = []
#     link1.append(l1.val)
#     l1cur = l1.next
#     while l1cur is not None:
#         link1.append(l1cur.val)
#         l1cur = l1cur.next
#     lival = 0
#     for i in range(len(link1)):
#         lival += link1[i]*(10**i)
#
#     link2 = []
#     link2.append(l2.val)
#     l2cur = l2.next
#     while l2cur is not None:
#         link2.append(l2cur.val)
#         l2cur = l2cur.next
#     lival2 = 0
#     for i in range(len(link2)):
#         lival2 += link2[i] * (10 ** i)
#
#     lival3 = lival + lival2
#     print(lival3)
#
#     link3 = []
#     if lival3 == 0:
#         link3.append(0)
#     else:
#         while lival3 != 0:
#             link3.append(lival3%10)
#             lival3 = lival3 // 10
#
#     print(link3)
#
#     new = ListNode(link3[0])
#     for i in range(len(link3)-1):
#         newnode = ListNode(link3[i+1])
#         cur = new
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = newnode
#
#     return new


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l3 = ListNode(0)
    dummy = l3
    carry = 0
    while l1 != None or l2 != None or carry != 0:
        sum = carry
        if l1 != None:
            sum += l1.val
            l1 = l1.next
        if l2 != None:
            sum += l2.val
            l2 = l2.next
        carry = int(sum / 10)
        l3.next = ListNode(sum % 10)
        l3 = l3.next
    return dummy.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l3 = addTwoNumbers(l1, l2)

print(l3.val)
print(l3.next.val)
print(l3.next.next.val)
