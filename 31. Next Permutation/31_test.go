package leetcode

import(
	"testing"
	"reflect"
)

func TestNextPermutation(t *testing.T){
	type test struct{
		input []int
		want []int
	}

	tests := map[string]test{
		"1": test{[]int{3,5,8,7,6,4}, []int{3,6,4,5,7,8}},
		"2": test{[]int{1,2,3}, []int{1,3,2}},
		"3": test{[]int{3,2,1}, []int{1,2,3}},
		"4": test{[]int{1,1,5}, []int{1,5,1}},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			nextPermutation(tc.input)
			if !reflect.DeepEqual(tc.input, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, tc.input)
			}
		})
	}
}

func BenchmarkNextPermutation(b *testing.B){
	for i:=0; i<b.N; i++{
		nextPermutation([]int{3,5,8,7,6,4})
	}
}

// 这个方法会明显好于上面
func BenchmarkNextPermutation1(b *testing.B){
	for i:=0; i<b.N; i++{
		nextPermutation1([]int{3,5,8,7,6,4})
	}
}