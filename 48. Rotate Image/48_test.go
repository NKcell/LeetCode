package leetcode

import(
	"testing"
	"reflect"		
)

func Test(t *testing.T){
	type test struct{
		input [][]int
		want [][]int
	}
	
	tests := map[string]test{
	"1": test{[][]int{{1,2,3},{4,5,6},{7,8,9}}, [][]int{{7,4,1},{8,5,2},{9,6,3}}},
	"2": test{[][]int{{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}}, [][]int{{15,13,2,5},{14,3,4,1},{12,6,8,9},{16,7,10,11}}},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			rotate(tc.input)
			if !reflect.DeepEqual(tc.input, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, tc.input)
			}
		})
	}
}

func BenchmarkSingleNumber(b *testing.B){
	for i:=0; i<b.N; i++{
		rotate([][]int{{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}})
	}
}