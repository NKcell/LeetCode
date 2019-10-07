package leetcode

import(
	"testing"
	"reflect"
)

func Test(t *testing.T){
	type test struct{
		input1 []int
		input2 int
		want [][]int
	}
	
	tests := map[string]test{
	"1": test{[]int{7,3,2}, 18, [][]int{{2,2,2,2,2,2,2,2,2},{2,2,2,2,2,2,3,3},{2,2,2,2,3,7},{2,2,2,3,3,3,3},{2,2,7,7},{2,3,3,3,7},{3,3,3,3,3,3}}},
	"2": test{[]int{2,3,6,7}, 7, [][]int{{2,2,3},{7}}},
	"3": test{[]int{2,3,5}, 8, [][]int{{2,2,2,2},{2,3,3},{3,5}}},
}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := combinationSum(tc.input1, tc.input2)
			if !reflect.DeepEqual(got, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkSingleNumber(b *testing.B){
	for i:=0; i<b.N; i++{
		combinationSum([]int{7,3,2}, 18)
	}
}