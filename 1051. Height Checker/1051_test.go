package leetcode

import(
	"testing"
)

func TestHeightChecker(t *testing.T){
	type test struct{
		input []int;
		want int;
	}

	tests := map[string]test{
		"1" : test{[]int{1,1,4,2,1,3}, 3},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			if heightChecker(tc.input) != tc.want{
				t.Errorf("测试失败！wand:%#v got:%#v", tc.want, heightChecker(tc.input))
			}
		})
	}
}

func BenchmarkHeightChecker(b *testing.B){
	for i:=0; i<b.N; i++{
		heightChecker([]int{1,1,4,2,1,3})
	}
}