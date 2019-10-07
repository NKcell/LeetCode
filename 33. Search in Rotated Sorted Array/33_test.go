package leetcode

import(
	"testing"
)

func Test(t *testing.T){
	type test struct{
		input1 []int
		input2 int
		want int
	}
	
	tests := map[string]test{
	"1": test{[]int{}, 1, -1},
	"2": test{[]int{1,3}, 1, 0},
	"3": test{[]int{5,1,3}, 1, 1},
	"4": test{[]int{4,5,6,7,0,1,2}, 0, 4},
	"5": test{[]int{4,5,6,7,0,1,2}, 3, -1},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := search(tc.input1, tc.input2)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkSingleNumber(b *testing.B){
	for i:=0; i<b.N; i++{
		search([]int{4,5,6,7,0,1,2}, 3)
	}
}