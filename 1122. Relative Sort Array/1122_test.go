package leetcode

import (
	"testing"
	"reflect"
)

func TestRelativeSortArray(t *testing.T){
	type test struct{
		input1 []int;
		input2 []int;
		want []int;
	}

	tests := map[string]test{
		"1" : test{[]int{28,6,22,8,44,17},[]int{22,28,8,6},[]int{22,28,8,6,17,44}},
		"2" : test{[]int{2,3,1,3,2,4,6,7,9,2,19},[]int{2,1,4,3,9,6},[]int{2,2,2,1,4,3,3,9,6,7,19}},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			if !reflect.DeepEqual(relativeSortArray(tc.input1, tc.input2),tc.want){
				t.Errorf("测试失败！ want:%#v got:%#v",tc.want,relativeSortArray(tc.input1, tc.input2))
			}
		})
	}
}

func BenchmarkRelativeSortArray(b *testing.B){
	for i:=0; i<b.N; i++{
		relativeSortArray([]int{2,3,1,3,2,4,6,7,9,2,19},[]int{2,1,4,3,9,6})
	}
}

func BenchmarkRelativeSortArray1(b *testing.B){
	for i:=0; i<b.N; i++{
		relativeSortArray1([]int{2,3,1,3,2,4,6,7,9,2,19},[]int{2,1,4,3,9,6})
	}
}