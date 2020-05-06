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

func rotateRight(head *ListNode, k int) *ListNode {
    if head == nil || head.Next == nil{
		return head	
	}

	headTmp := head
	linkLen := 1
	for(headTmp.Next != nil){
		linkLen ++
		headTmp = headTmp.Next
	}

	k = k%linkLen
	nodePointPre := linkLen - k - 1
	if nodePointPre == -1{
		return head
	}

	headTmp2 := head
	tmp := 0
	for (tmp != nodePointPre){
		tmp ++
		headTmp2 = headTmp2.Next
	}

	headTmp.Next = head
	head = headTmp2.Next
	headTmp2.Next = nil

	return head
}