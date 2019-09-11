"""
2324
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


"""
def isPalindrome(self, head):

    if head is None:
        return True
    val = []
    while True:
        val.append(head.val)
        if head.next is None:
            break
        head = head.next

    while True:
        if val[0] != val[-1]:
            return False
        else:
            if len(val) == 2 or len(val) == 1:
                return True
            else:
                val = val[1:-1]
"""


def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    pre = None
    while slow is not None:
        temp = slow
        slow = slow.next
        #temp.next.next = temp
        temp.next = pre
        pre = temp

    head2 = pre

    while head2 is not None:
        if head2.val != head.val:
            return False

        head2 = head2.next
        head = head.next

    return True



















