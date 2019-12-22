package leetcode

import(
	"sort"
)

func findDuplicates(nums []int) []int {
	sort.Ints(nums)
	res := make([]int, 0)
	for i:=0; i<len(nums)-1; i++{
		if nums[i] == nums[i+1]{
			res = append(res, nums[i])
		}
	}
	return res
}