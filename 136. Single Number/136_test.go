package leetcode

import(
	"testing"
)

func TestSingleNumber(t *testing.T){
	type test struct{
		input []int
		want int
	}

	tests := map[string]test{
		"1": test{[]int{1,2,2}, 1},
		"2": test{[]int{4,1,2,1,2}, 4},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := singleNumber(tc.input)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkSingleNumber(b *testing.B){
	for i:=0; i<b.N; i++{
		singleNumber([]int{4,1,2,1,2})
	}
}

func BenchmarkSingleNumber1(b *testing.B){
	for i:=0; i<b.N; i++{
		singleNumber1([]int{4,1,2,1,2})
	}
}