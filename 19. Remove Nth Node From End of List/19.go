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

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	if n == 0{
		return head
	}
	var nodeLen int
	myPre := head
	for myPre != nil{
		nodeLen ++
		myPre = myPre.Next
	}
	if nodeLen == 1{
		return nil
	}
	if nodeLen == 0{
		return head
	}
	if nodeLen == n{
		return head.Next
	}
	myPre = head
	for i:=0; i<nodeLen-n-1; i++{
		myPre = myPre.Next
	}
	myPre.Next = myPre.Next.Next
	return head
}

// 这个空间消耗还是很大的，但确实是只遍历了一次，而且要动态申请内存，效率也不高...
func removeNthFromEnd1(head *ListNode, n int) *ListNode {
	nodes := make(map[int]*ListNode)

	for i := 0; head != nil; i++ {
		nodes[i] = head
		head = head.Next
	}

	lenght := len(nodes)
	nth := lenght - n
	if nth > 0 {
		head = nodes[0]
		nodes[nth-1].Next = nodes[nth].Next
	} else if lenght > 1 {
		head = nodes[1]
	} else {
		head = nil
	}

	return head
}