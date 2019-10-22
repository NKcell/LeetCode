package leetcode

import(
	"testing"
	"reflect"
)

func TestSpiralOrder(t *testing.T){
	type test struct{
		input [][]int
		want []int
	}
	
	tests := map[string]test{
	"1": test{[][]int{{1,2,3,4}}, []int{1,2,3,4}},
	"2": test{[][]int{{1, 2, 3, 4},{5, 6, 7, 8},{9,10,11,12}}, []int{1,2,3,4,8,12,11,10,9,5,6,7}},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := spiralOrder(tc.input)
			if !reflect.DeepEqual(got, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkSingleNumber(b *testing.B){
	for i:=0; i<b.N; i++{
		spiralOrder([][]int{{1, 2, 3, 4},{5, 6, 7, 8},{9,10,11,12}})
	}
}

func BenchmarkSingleNumber1(b *testing.B){
	for i:=0; i<b.N; i++{
		spiralOrder1([][]int{{1, 2, 3, 4},{5, 6, 7, 8},{9,10,11,12}})
	}
}