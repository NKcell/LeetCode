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

func getDecimalValue(head *ListNode) int {
	tmp := 0
	for head != nil{
		tmp = tmp*2 + head.Val
		head = head.Next
	}
	return tmp
}