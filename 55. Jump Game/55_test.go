package leetcode

import(
	"testing"
)

func TestCanJump(t *testing.T){
	type test struct{
		input []int
		want bool
	}
	
	tests := map[string]test{
	"1": test{[]int{2,3,1,1,4}, true},
	"2": test{[]int{3,2,1,0,4}, false},
	"3": test{[]int{0}, true},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := canJump(tc.input)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkSingleNumber(b *testing.B){
	for i:=0; i<b.N; i++{
		canJump([]int{3,2,1,0,4})
	}
}


func BenchmarkSingleNumber1(b *testing.B){
	for i:=0; i<b.N; i++{
		canJump1([]int{3,2,1,0,4})
	}
}