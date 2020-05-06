package leetcode


//Definition for singly-linked list.
type ListNode struct {
	Val int
	Next *ListNode
}


func partition(head *ListNode, x int) *ListNode {
	head1 := head
	head1 = nil
	head2 := head
	head2 = nil
	tmp1 := head
	tmp1 = nil
	tmp2 := head
	tmp2 = nil
	flag1 := 0
	flag2 := 0

	for(head != nil){
		if head.Val<x{
			if flag1 == 0{
				flag1 = 1
				head1 = head
				tmp1 = head
			}else{
				tmp1.Next = head
				tmp1 = head
			}
		}else{
			if flag2 == 0{
				flag2 = 1
				head2 = head
				tmp2 = head
			}else{
				tmp2.Next = head
				tmp2 = head
			}
		}
		head = head.Next
	}

	if tmp1 != nil{
		tmp1.Next = head2
	}
	if tmp2 != nil{
		tmp2.Next = nil
	}

	if head1 != nil{
		return head1
	}
	return head2
}