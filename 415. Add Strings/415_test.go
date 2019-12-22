package leetcode

import(
	"testing"
)

func TestAddStrings(t *testing.T){
	type test struct{
		input1 string
		input2 string
		want string
	}
	
	tests := map[string]test{
	"1": test{"0","0","0"},
	"2": test{"99","1","100"},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := addStrings(tc.input1, tc.input2)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func Benchmark(b *testing.B){
	for i:=0; i<b.N; i++{
		
	}
}