package leetcode

import(
	"sort"
)

func permuteUnique(nums []int) [][]int {
	sort.Ints(nums)
	res := make([][]int, 0)
	dfs(&res, nums, []int{})
	return res
}

func dfs(res *[][]int, nums []int, tmp []int){
	if len(nums) == 0{
		*res = append(*res, tmp)
	}

	var pre int
	for i,v := range nums{
		newtmp := make([]int, 0, len(tmp)+1)
		newnums := make([]int, 0, len(nums)-1)
		if i == 0{
			pre = nums[0]			
			newtmp = append(newtmp, tmp...)
			newtmp = append(newtmp, v)
			newnums = append(newnums, nums[1:]...)
			dfs(res, newnums, newtmp)
		}else{
			if v == pre{
				continue
			}else{
				pre = v
				newtmp = append(newtmp, tmp...)
				newtmp = append(newtmp, v)
				newnums = append(newnums, nums[:i]...)
				newnums = append(newnums, nums[i+1:]...)
				dfs(res, newnums, newtmp)
			}
		}
	}
}