package leetcode

import (
	"sort"
)

func subsets(nums []int) [][]int {
	sort.Ints(nums)
	res := make([][]int, 0)
	tmp := make([][]int, 0)
	myLen := len(nums)

	for _, v := range nums{
		res = append(res, []int{v})
		tmp = append(tmp, []int{v})
	}

	for i:=2; i<=myLen; i++{
		newtmp := make([][]int, 0)
		for _, v := range tmp{
			for j := sort.SearchInts(nums, v[len(v)-1])+1; j<myLen; j++{
				realtmp := make([]int, 0, len(v)+1)
				realtmp = append(realtmp, v...)
				realtmp = append(realtmp, nums[j])
				res = append(res, realtmp)
				newtmp = append(newtmp, realtmp)
			}
		}
		tmp = newtmp
	}

	res = append(res, []int{})
	return res
}