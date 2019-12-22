package leetcode

import(
	"testing"
)

func TestCountServers(t *testing.T){
	type test struct{
		input [][]int
		want int
	}
	
	tests := map[string]test{
	"1": test{[][]int{{1,0},{0,1}}, 0},
	"2": test{[][]int{{1,1,0,0},{0,0,1,0},{0,0,1,0},{0,0,0,1}}, 4},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := countServers(tc.input)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkSingleNumber(b *testing.B){
	for i:=0; i<b.N; i++{
		
	}
}