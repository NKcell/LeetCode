package leetcode

import(
	"testing"
)

func TestFractionToDecimal(t *testing.T){
	type test struct{
		input1 int
		input2 int
		want string
	}
	
	tests := map[string]test{
	"1": test{2,3,"0.(6)"},
	"2": test{10,3,"3.(3)"},
	"3": test{1,6,"0.1(6)"},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := fractionToDecimal(tc.input1, tc.input2)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkFractionToDecimal(b *testing.B){
	for i:=0; i<b.N; i++{
		fractionToDecimal(10,3)
	}
}