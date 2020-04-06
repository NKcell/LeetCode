package leetcode

import(
	"sort"
)

func smallerNumbersThanCurrent(nums []int) []int {
	nums2 := make([]int, len(nums), len(nums))
	copy(nums2,nums)

	sort.Ints(nums2)

	myDict := make(map[int]int, 0)

	for i,v := range nums2{
		if _, ok := myDict[v]; !ok{
			myDict[v] = i
		}
	}
	
	res := make([]int, 0, len(nums))

	for _,v := range nums{
		value,_ := myDict[v]
		res = append(res, value)
	}

	return res
}