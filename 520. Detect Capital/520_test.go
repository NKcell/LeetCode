package leetcode

import(
	"testing"
)

func TestDetectCapitalUse(t *testing.T){
	type test struct{
		input string
		want bool
	}
	
	tests := map[string]test{
	"1": test{"Leetcode", true},
	"2": test{"FlAG", false},
	"3": test{"ffffffffffffffffffffF", false},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := detectCapitalUse(tc.input)
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