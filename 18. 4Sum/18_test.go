package leetcode

import(
	"testing"
	"reflect"
)

func TestFourSum(t *testing.T){
	type test struct{
		input1 []int
		input2 int
		want [][]int
	}

	tests := map[string]test{
		"1": test{[]int{1,0,-1,0,-2,2}, 0, [][]int{{-2,-1,1,2},{-2,0,0,2},{-1,0,0,1}}},
		"2": test{[]int{-1,2,2,-5,0,-1,4}, 3, [][]int{{-5,2,2,4},{-1,0,2,2}}},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := fourSum1(tc.input1, tc.input2)
			if !reflect.DeepEqual(got, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkFourSum(b *testing.B){
	for i:=0; i<b.N; i++{
		fourSum([]int{1,0,-1,0,-2,2}, 0)
	}
}

func BenchmarkFourSum1(b *testing.B){
	for i:=0; i<b.N; i++{
		fourSum1([]int{1,0,-1,0,-2,2}, 0)
	}
}