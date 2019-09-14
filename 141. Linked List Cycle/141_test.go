package leetcode

import(
	"testing"
)

func TestHasCycle(t *testing.T){
	type test struct{
		input *ListNode
		want bool
	}

	a := [4]*ListNode{}
	a[0] = &ListNode{3, nil}
	a[1] = &ListNode{2, nil}
	a[2] = &ListNode{0, nil}
	a[3] = &ListNode{-4, nil}
	a[0].Next = a[1]
	a[1].Next = a[2]
	a[2].Next = a[3]
	a[3].Next = a[1]

	b := [2]*ListNode{}
	b[0] = &ListNode{1, nil}
	b[1] = &ListNode{0, nil}
	b[0].Next = b[1]
	b[1].Next = b[0]

	c := [1]*ListNode{}
	c[0] =  &ListNode{1, nil}
	c[0].Next = nil

	d := [2]*ListNode{}
	d[0] = &ListNode{1, nil}
	d[1] = &ListNode{0, nil}
	d[0].Next = d[1]
	d[1].Next = nil

	tests := map[string]test{
		"1": test{a[0], true},
		"2": test{b[0], true},
		"3": test{c[0], false},
		"4": test{d[0], false},
		"5": test{nil, false},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := hasCycle(tc.input)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkHasCycle(b *testing.B){
	a := [4]*ListNode{}
	a[0] = &ListNode{3, nil}
	a[1] = &ListNode{2, nil}
	a[2] = &ListNode{0, nil}
	a[3] = &ListNode{-4, nil}
	a[0].Next = a[1]
	a[1].Next = a[2]
	a[2].Next = a[3]
	a[3].Next = a[1]

	for i:=0; i<b.N; i++{
		hasCycle(a[0])
	}
}