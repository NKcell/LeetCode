package leetcode

import(
	"testing"
	//"reflect"
)
func TestCanThreePartsEqualSum(t *testing.T){
	type test struct{
		input []int
		want bool
	}

	tests := map[string]test{
		"1" : {[]int{0,2,1,-6,6,-7,9,1,2,0,1}, true},
		"2" : {[]int{0,2,1,-6,6,7,9,-1,2,0,1}, false},
		"3" : {[]int{3,3,6,5,-2,2,5,1,-9,4}, true},
	}

	for name, testcell := range tests{
		t.Run(name, func(t *testing.T){
			got := canThreePartsEqualSum(testcell.input)
			if got != testcell.want{
				t.Errorf("测试失败！want: %v, got: %v", testcell.want, got)
			}else{
				t.Logf("第%v测试通过！", name)
			}
		})
	}
}

func BenchmarkCanThreePartsEqualSum(b *testing.B){
	for i:=0; i<b.N; i++{
		canThreePartsEqualSum([]int{3,3,6,5,-2,2,5,1,-9,4})
	}
}