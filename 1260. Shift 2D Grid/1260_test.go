package leetcode

import(
	"testing"
	"reflect"
)

func Test(t *testing.T){
	type test struct{
		input1 [][]int
		input2 int
		want [][]int
	}
	
	tests := map[string]test{
	"1": test{[][]int{{1,2,3},{4,5,6},{7,8,9}}, 1, [][]int{{9,1,2},{3,4,5},{6,7,8}}},
	"2": test{[][]int{{1},{2},{3},{4},{7},{6},{5}}, 23, [][]int{{6},{5},{1},{2},{3},{4},{7}}},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := shiftGrid(tc.input1, tc.input2)
			if !reflect.DeepEqual(tc.want, got){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func Benchmark(b *testing.B){
	for i:=0; i<b.N; i++{
		
	}
}