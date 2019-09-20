package leetcode

import(
	"testing"
	"reflect"
)

func TestMiddleNode(t *testing.T){
	type test struct{
		input *ListNode
		want *ListNode
	}

	a1 := ListNode{5, nil}
	a2 := ListNode{4, &a1}
	a3 := ListNode{3, &a2}
	a4 := ListNode{2, &a3}
	a5 := ListNode{1, &a4}

	b0 := ListNode{6, nil}
	b1 := ListNode{5, &b0}
	b2 := ListNode{4, &b1}
	b3 := ListNode{3, &b2}
	b4 := ListNode{2, &b3}
	b5 := ListNode{1, &b4}

	tests := map[string]test{
		"1": test{&a5, &a3},
		"2": test{&b5, &b2},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := middleNode(tc.input)
			if !reflect.DeepEqual(got, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkMiddleNode(b *testing.B){
	a1 := ListNode{5, nil}
	a2 := ListNode{4, &a1}
	a3 := ListNode{3, &a2}
	a4 := ListNode{2, &a3}
	a5 := ListNode{1, &a4}
	for i:=0; i<b.N; i++{
		middleNode(&a5)
	}
}

func BenchmarkMiddleNode1(b *testing.B){
	a1 := ListNode{5, nil}
	a2 := ListNode{4, &a1}
	a3 := ListNode{3, &a2}
	a4 := ListNode{2, &a3}
	a5 := ListNode{1, &a4}
	for i:=0; i<b.N; i++{
		middleNode1(&a5)
	}
}