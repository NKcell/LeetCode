package leetcode

import(
	"math"
)

func grayCode(n int) []int {
	res := make([]int, 0, int(math.Pow(2, float64(n))))
	res = append(res, 0)

	for i:=0; i<n; i++{
		tmp := len(res) 
		for j:=tmp-1; j>=0; j--{
			res = append(res, res[j]+tmp)
		}
	}

	return res
}