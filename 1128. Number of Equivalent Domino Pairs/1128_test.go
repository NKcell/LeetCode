package leetcode

import (
	"testing"
)

func TestNumEquivDominoPairs(t *testing.T){
	type test struct{
		input [][]int
		want int
	}

	tests := map[string]test{
		"1": test{[][]int{{1,2},{2,1},{3,4},{5,6}}, 1},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			if tc.want != numEquivDominoPairs(tc.input){
				t.Errorf("测试失败！want: %#v got: %#v", tc.want, numEquivDominoPairs(tc.input))
			}
		})
	}
}

func BenchmarkNumEquivDominoPairs(b *testing.B){
	for i:=0; i<b.N; i++{
		numEquivDominoPairs([][]int{{1,2},{2,1},{3,4},{5,6}})
	}
}

func BenchmarkNumEquivDominoPairs1(b *testing.B){
	for i:=0; i<b.N; i++{
		numEquivDominoPairs1([][]int{{1,2},{2,1},{3,4},{5,6}})
	}
}