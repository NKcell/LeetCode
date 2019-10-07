package leetcode

import(
	"testing"
)

func TestGetHint(t *testing.T){
	type test struct{
		input1 string
		input2 string
		want string
	}
	
	tests := map[string]test{
	"1": test{"1807","7810","1A3B"},
	"2": test{"1123","0111","1A1B"},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := getHint(tc.input1, tc.input2)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkSingleNumber(b *testing.B){
	for i:=0; i<b.N; i++{
		getHint("1807","7810")
	}
}