package leetcode

import (
	"sort"
)

type IntSlice [][]int

func (s IntSlice) Len() int { return len(s) }
func (s IntSlice) Swap(i, j int){ s[i], s[j] = s[j], s[i] }
func (s IntSlice) Less(i, j int) bool {
	if s[i][1] < s[j][1]{
		return false
	}else if s[i][1] > s[j][1]{
		return true
	}else{
		if s[i][0] < s[j][0]{
			return false
		}else {
			return true
		}
	} 
}


func filterRestaurants(restaurants [][]int, veganFriendly int, maxPrice int, maxDistance int) []int {
	res := make([][]int, 0)
	
	for _,v := range restaurants{
		if veganFriendly==1{
			if v[2] == 1 && v[3]<=maxPrice && v[4]<=maxDistance{
				tmp := []int{v[0], v[1]}
				res = append(res, tmp)
			}
		}else{
			if v[3]<=maxPrice && v[4]<=maxDistance{
				tmp := []int{v[0], v[1]}
				res = append(res, tmp)
			}
		}
	}

	sort.Sort(IntSlice(res))

	l := make([]int, 0, len(res))
	for _, v := range res{
		l = append(l, v[0])
	}

	return l
}