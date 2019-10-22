package leetcode

import(
	"testing"
	"reflect"
)

func TestCombinationSum2(t *testing.T){
	type test struct{
		input1 []int
		input2 int
		want [][]int
	}
	
	tests := map[string]test{
	"1": test{[]int{10,1,2,7,6,1,5}, 8,[][]int{{1, 1, 6}, {1, 2, 5}, {1, 7}, {2, 6}}},
	"2": test{[]int{2,5,2,1,2}, 5,[][]int{{1,2,2},{5}}},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := combinationSum2(tc.input1, tc.input2)
			if !reflect.DeepEqual(got, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkCombinationSum2(b *testing.B){
	for i:=0; i<b.N; i++{
		combinationSum2([]int{10,1,2,7,6,1,5}, 8)
	}
}

func BenchmarkCombinationSum2_1(b *testing.B){
	for i:=0; i<b.N; i++{
		combinationSum2_1([]int{10,1,2,7,6,1,5}, 8)
	}
}