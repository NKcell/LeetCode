package leetcode

import(
	"testing"
	"reflect"
)

func TestMinimumAbsDifference(t *testing.T){
	type test struct{
		input []int
		want [][]int
	}
	
	tests := map[string]test{
	"1": test{[]int{4,2,1,3}, [][]int{{1,2},{2,3},{3,4}}},
	"2": test{[]int{1,3,6,10,15}, [][]int{{1,3}}},
	"3": test{[]int{3,8,-10,23,19,-4,-14,27}, [][]int{{-14,-10},{19,23},{23,27}}},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := minimumAbsDifference(tc.input)
			if !reflect.DeepEqual(got, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkSingleNumber(b *testing.B){
	for i:=0; i<b.N; i++{
		minimumAbsDifference([]int{3,8,-10,23,19,-4,-14,27})
	}
}