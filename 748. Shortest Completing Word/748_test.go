package leetcode

import(
	"testing"
)

func TestShortestCompletingWord(t *testing.T){
	type test struct{
		input1 string
		input2 []string
		want string
	}
	
	tests := map[string]test{
	"1": test{"1s3 PSt", []string{"step", "steps", "stripe", "stepple"}, "steps"},
	"2": test{"1s3 456", []string{"looks", "pest", "stew", "show"}, "pest"},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := shortestCompletingWord(tc.input1, tc.input2)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkShortestCompletingWord(b *testing.B){
	for i:=0; i<b.N; i++{
		shortestCompletingWord("1s3 456", []string{"looks", "pest", "stew", "show"})
	}
}

func BenchmarkShortestCompletingWord1(b *testing.B){
	for i:=0; i<b.N; i++{
		shortestCompletingWord1("1s3 456", []string{"looks", "pest", "stew", "show"})
	}
}