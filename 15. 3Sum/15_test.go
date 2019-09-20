package leetcode

import (
	"testing"
	"reflect"
)

func TestThreeSum(t *testing.T){
	type test struct{
		input []int
		want [][]int
	}

	tests := map[string]test{
		"1": test{[]int{0,0,0}, [][]int{[]int{0,0,0}}},
		"2": test{[]int{-1, 0, 1, 2, -1, -4}, [][]int{[]int{-1,-1,2}, []int{-1,0,1}}},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := threeSum(tc.input)
			if !reflect.DeepEqual(got, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkThreeSum(b *testing.B){
	for i:=0; i<b.N; i++{
		threeSum([]int{-1, 0, 1, 2, -1, -4})
	}
}