package leetcode

import(
	"testing"
	"reflect"
)

func TestGetIntersectionNode(t *testing.T){
	type test struct{
		input1 *ListNode
		input2 *ListNode
		want *ListNode
	}

	a1 := ListNode{3, nil}
	a2 := ListNode{2, nil}
	a3 := ListNode{4, nil}
	b1 := ListNode{0, nil}
	b2 := ListNode{9, nil}
	b3 := ListNode{1, nil}
	a2.Next = &a3
	a1.Next = &a2
	b1.Next = &a2
	b2.Next = &b1
	b3.Next = &b2

	c1 := ListNode{3, nil}
	c2 := ListNode{2, nil}
	c3 := ListNode{4, nil}
	d1 := ListNode{0, nil}
	d2 := ListNode{9, nil}
	d3 := ListNode{1, nil}
	c2.Next = &c3
	c1.Next = &c2
	d2.Next = &d3
	d1.Next = &d2

	tests := map[string]test{
		"1":test{&a1, &b3, &a2},
		"2":test{&c1, &d1, nil},		
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := getIntersectionNode(tc.input1, tc.input2)
			if !reflect.DeepEqual(got, tc.want){
				t.Errorf("Test Failed! got: %#v want: %#v", got, tc.want)
			}
		})
	}
}

func BenchmarkGetIntersectionNode(b *testing.B){
	a1 := ListNode{3, nil}
	a2 := ListNode{2, nil}
	a3 := ListNode{4, nil}
	b1 := ListNode{0, nil}
	b2 := ListNode{9, nil}
	b3 := ListNode{1, nil}
	a2.Next = &a3
	a1.Next = &a2
	b1.Next = &a2
	b2.Next = &b1
	b3.Next = &b2
	for i:=0; i<b.N; i++{
		getIntersectionNode(&a1, &b3)
	}
}