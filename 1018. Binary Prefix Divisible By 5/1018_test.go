package leetcode

import(
	"testing"
	"reflect"
)

func TestPrefixesDivBy5(t *testing.T){
	type test struct{
		input []int
		want []bool
	}

	tests := map[string]test{
		"1": test{[]int{0,1,1}, []bool{true,false,false}},
		"2": test{[]int{1,1,1}, []bool{false,false,false}},
		"3": test{[]int{0,1,1,1,1,1}, []bool{true,false,false,false,true,false}},
		"4": test{[]int{1,1,1,0,1}, []bool{false,false,false,false,false}},
		"5": test{[]int{1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0}, []bool{false,false,true,false,false,false,false,false,false,false,true,true,true,true,true,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,true,false,false,false,true,false,false,true,false,false,true,true,true,true,true,true,true,false,false,true,false,false,false,false,true,true}},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			if !reflect.DeepEqual(tc.want, prefixesDivBy5(tc.input)){
				t.Errorf("测试失败！ want:%#v got:%#v", tc.want, prefixesDivBy5(tc.input))
			}
		})
	}
}

func BenchmarkPrefixesDivBy5(b *testing.B){
	for i:=0; i<b.N; i++{
		prefixesDivBy5([]int{0,1,1,1,1,1})
	}
}