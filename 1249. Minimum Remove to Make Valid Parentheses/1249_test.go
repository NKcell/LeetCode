package leetcode

import(
	"testing"
)

func Test(t *testing.T){
	type test struct{
		input string
		want string
	}
	
	tests := map[string]test{
	"1": test{"(t(e)y))d(()(e(", "(t(e)y)d()e"},
	"2": test{"(a(b(c)d)", "a(b(c)d)"},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := minRemoveToMakeValid(tc.input)
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