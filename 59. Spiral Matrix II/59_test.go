package leetcode

import(
	"testing"
	"reflect"
)

func TestGenerateMatrix(t *testing.T){
	type test struct{
		input int
		want [][]int
	}
	
	tests := map[string]test{
	"1": test{3, [][]int{{1, 2, 3}, {8, 9, 4}, {7, 6, 5}}},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := generateMatrix(tc.input)
			if !reflect.DeepEqual(got,tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkSingleNumber(b *testing.B){
	for i:=0; i<b.N; i++{
		
	}
}