/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
package leetcode

type ListNode struct {
	Val int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
    if head == nil{
		return false
	}
	fast := head
	slow := head

	for {
		if fast.Next == nil || fast.Next.Next == nil{
			return false
		}
		if fast.Next == slow || fast.Next.Next == slow{
			return true
		}
		fast = fast.Next.Next
		slow = slow.Next
	}
}