package leetcode

import(
	"testing"
)

func TestRemoveNthFromEnd(t *testing.T){
	type test struct{
		input1 *ListNode
		input2 int
		want *ListNode
	}
	a5 := ListNode{5, nil}
	a4 := ListNode{4, &a5}
	a3 := ListNode{3, &a4}
	a2 := ListNode{2, &a3}
	a1 := ListNode{1, &a2}

	b2 := ListNode{2, nil}
	b1 := ListNode{1, &b2}

	tests := map[string]test{
		"1": test{&a1, 2, &a1},
		"2": test{&b1, 2, &b2},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := removeNthFromEnd(tc.input1, tc.input2)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkRemoveNthFromEnd(b *testing.B){
	for i:=0; i<b.N; i++{
		a5 := ListNode{5, nil}
		a4 := ListNode{4, &a5}
		a3 := ListNode{3, &a4}
		a2 := ListNode{2, &a3}
		a1 := ListNode{1, &a2}

		removeNthFromEnd(&a1, 2)
	}
}

func BenchmarkRemoveNthFromEnd1(b *testing.B){
	for i:=0; i<b.N; i++{
		a5 := ListNode{5, nil}
		a4 := ListNode{4, &a5}
		a3 := ListNode{3, &a4}
		a2 := ListNode{2, &a3}
		a1 := ListNode{1, &a2}

		removeNthFromEnd1(&a1, 2)
	}
}