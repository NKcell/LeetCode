package leetcode

import(
	"testing"
)

func Test(t *testing.T){
	type test struct{
		input []int
		want int
	}
	
	tests := map[string]test{
	"1": test{[]int{},0},
	"2": test{[]int{1,2}, 2},
	"3": test{[]int{1,2,3,1},4},
	"4": test{[]int{2,7,9,3,1},12},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := rob(tc.input)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkSingleNumber(b *testing.B){
	for i:=0; i<b.N; i++{
		rob([]int{2,7,9,3,1})
	}
}