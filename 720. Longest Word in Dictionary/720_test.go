package leetcode

import(
	"testing"
)

func TestLongestWord(t *testing.T){
	type test struct{
		input []string
		want string
	}
	
	tests := map[string]test{
	"1": test{[]string{"w","wo","wor","worl", "world"}, "world"},
	"2": test{[]string{"a", "banana", "app", "appl", "ap", "apply", "apple"}, "apple"},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := longestWord(tc.input)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkLongestWord(b *testing.B){
	for i:=0; i<b.N; i++{
		longestWord([]string{"a", "banana", "app", "appl", "ap", "apply", "apple"})
	}
}

func BenchmarkLongestWord1(b *testing.B){
	for i:=0; i<b.N; i++{
		longestWord1([]string{"a", "banana", "app", "appl", "ap", "apply", "apple"})
	}
}