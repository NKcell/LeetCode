package leetcode

type ListNode struct {
	Val int
	Next *ListNode
	}

func middleNode(head *ListNode) *ListNode {
	var lenNode int
	tmp := head

	for tmp != nil{
		tmp = tmp.Next
		lenNode++
	}

	midloc := lenNode/2
	for i:=0; i<midloc; i++{
		head = head.Next
	}

	return head
}

func middleNode1(head *ListNode) *ListNode {
    fast := head
    slow := head
    
    for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next 
    }
    
    return slow
}