package leetcode

import(
	"sort"
)

func merge(intervals [][]int) [][]int {
	if len(intervals) < 2{
		return intervals
	}
    sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	res := [][]int{intervals[0]}
	for _, v := range intervals{
		if v[0]>res[len(res)-1][1]{
			res = append(res, v)
		}else{
			tmpmax := 0
			if res[len(res)-1][1]>v[1]{
				tmpmax = res[len(res)-1][1]
			}else{
				tmpmax = v[1]
			}
			res[len(res)-1] = []int{res[len(res)-1][0], tmpmax}
		}
	}
	return res
}