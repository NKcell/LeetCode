package leetcode

import(
	"sort"
)

func minimumAbsDifference(arr []int) [][]int {
	sort.Ints(arr)
	absolute := 100000000
	for i:=0; i<len(arr)-1; i++{
		v := arr[i+1]-arr[i]
		if v<absolute{
			absolute = v
			if absolute == 1{
				break
			}
		}
	}

	relist := make([][]int, 0)
	for i:=0; i<len(arr)-1; i++{
		if arr[i+1]-arr[i] == absolute{
			relist = append(relist, []int{arr[i], arr[i+1]})
		}
	}
	return relist
}