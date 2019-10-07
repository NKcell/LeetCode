package leetcode

import(
	"testing"
	"reflect"
)

func TestSearchRange(t *testing.T){
	type test struct{
		input1 []int
		input2 int
		want []int
	}

	tests := map[string]test{
		"1": test{[]int{1}, 1, []int{0,0}},
		"2": test{[]int{5,7,7,8,8,10}, 8, []int{3,4}},
		"3": test{[]int{5,7,7,8,8,10}, 6, []int{-1,-1}},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := searchRange(tc.input1, tc.input2)
			if !reflect.DeepEqual(got, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkSearchRange(b *testing.B){
	for i:=0; i<b.N; i++{
		searchRange([]int{5,7,7,8,8,10}, 8)
	}
}