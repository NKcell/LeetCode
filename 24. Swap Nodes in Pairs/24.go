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

func swapPairs(head *ListNode) *ListNode {
    dummy := &ListNode{0, head}
    reli := dummy
    for head != nil && head.Next != nil{
        tmp := head.Next
        head.Next = tmp.Next
        tmp.Next = head
        reli.Next = tmp
        head = head.Next
        reli = tmp.Next
    }
    return dummy.Next
}