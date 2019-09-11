package leetcode

import (
	"testing"
	"reflect"
)

func TestNumSmallerByFrequency(t *testing.T){
	type test struct{
		input1 []string
		input2 []string
		want []int
	}

	tests := map[string]test{
		"1": test{[]string{"cbd"}, []string{"zaaaz"}, []int{1}},
		"2": test{[]string{"bbb", "cc"}, []string{"a","aa","aaa","aaaa"}, []int{1, 2}},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := numSmallerByFrequency(tc.input1, tc.input2)
			if !reflect.DeepEqual(got, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkNumSmallerByFrequency(b *testing.B){
	for i:=0; i<b.N; i++{
		numSmallerByFrequency([]string{"bbb", "cc"}, []string{"a","aa","aaa","aaaa"})
	}
}

func BenchmarkNumSmallerByFrequency1(b *testing.B){
	for i:=0; i<b.N; i++{
		numSmallerByFrequency1([]string{"bbb", "cc"}, []string{"a","aa","aaa","aaaa"})
	}
}