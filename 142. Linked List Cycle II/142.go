package leetcode

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
    fast := head
    slow := head
    flag := 0

    for fast!=nil && fast.Next !=nil{
        fast = fast.Next.Next
        slow = slow.Next

        if fast == slow{
            flag = 1
            break
        }
    }

    if flag == 0{
        return nil
	}

	for head!=slow{
		head = head.Next
		slow = slow.Next
	}
	return head
}