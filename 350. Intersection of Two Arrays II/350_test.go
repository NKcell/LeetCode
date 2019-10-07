package leetcode

import(
	"testing"
	"reflect"
)

func TestIntersect(t *testing.T){
	type test struct{
		input1 []int
		input2 []int
		want []int
	}
	
	tests := map[string]test{
	"1": test{[]int{1,2,2,1}, []int{2,2}, []int{2,2}},
	"2": test{[]int{4,9,5}, []int{9,4,9,8,4}, []int{9, 4}},
	}
	
	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := intersect(tc.input1, tc.input2)
			if !reflect.DeepEqual(got, tc.want){
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkIntersect(b *testing.B){
	for i:=0; i<b.N; i++{
		intersect([]int{4,9,5}, []int{9,4,9,8,4})
	}
}