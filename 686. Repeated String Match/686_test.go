package leetcode

import(
	"testing"
)

func TestRepeatedStringMatch(t *testing.T){
	type test struct{
		input1 string
		input2 string
		want int
	}
	
	tests := map[string]test{
	"1": test{"abab", "aba", 1},
	"2": test{"abc", "cabcabca", 4},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := repeatedStringMatch(tc.input1, tc.input2)
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