package leetcode

import (
	"testing"
	"reflect"
)

func TestDuplicateZeros(t *testing.T){
	type test struct{
		input []int;
		want []int;
	}

	tests := map[string]test{
		"1": test{[]int{1,0,2,3,0,4,5,0}, []int{1,0,0,2,3,0,0,4}},
		"2": test{[]int{1,2,3}, []int{1,2,3}},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			duplicateZeros(tc.input)
			if !reflect.DeepEqual(tc.input, tc.want){
				t.Errorf("测试失败！got:%#v want:%#v", tc.input, tc.want)
			}
		})
	}
}

func BenchmarkDuplicateZeros1(b *testing.B){
	for i:=0; i<b.N; i++{
		duplicateZeros1([]int{1,0,2,3,0,4,5,0})
	}
}

func BenchmarkDuplicateZeros(b *testing.B){
	for i:=0; i<b.N; i++{
		duplicateZeros([]int{1,0,2,3,0,4,5,0})
	}
}