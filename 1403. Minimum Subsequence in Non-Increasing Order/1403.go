package leetcode

import(
	"sort"
)

func minSubsequence(nums []int) []int {
	sort.Ints(nums)
	index := len(nums)-1

	res := make([]int, 0)

	sumValue := 0
	for _,v := range nums{
		sumValue += v
	}
	tmpValue := 0

	for index >= 0{
		tmp := nums[index]
		res = append(res, tmp)
		tmpValue += tmp
		sumValue -= tmp

		if tmpValue>sumValue{
			break
		}
		index --
	}
	return res
}