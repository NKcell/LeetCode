package leetcode

import(
	"testing"
)

func TestIsPalindrome(t *testing.T){
	type test struct{
		input string
		want bool
	}
	
	tests := map[string]test{
	"1": test{"A man, a plan, a canal: Panama", true},
	"2": test{"race a car", false},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := isPalindrome(tc.input)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkIsPalindrome(b *testing.B){
	for i:=0; i<b.N; i++{
		isPalindrome("A man, a plan, a canal: Panama")
	}
}