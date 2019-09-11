package leetcode

import "sort"

func heightChecker(heights []int) int {
	heightsSort := make([]int, len(heights))
	copy(heightsSort, heights)
	sort.Ints(heightsSort)
	var count int
	for i, v := range heights{
		if v != heightsSort[i]{
			count ++
		}
	}
	return count
}