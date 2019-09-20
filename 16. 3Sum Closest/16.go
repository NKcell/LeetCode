package  leetcode

import(
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	numsLen := len(nums)
	tmp := isAns(nums, target, numsLen)
	if tmp{
		return target
	}
	closenum := 0
	for{
		if closenum>=0{
			closenum = -(closenum+1)
		}else{
			closenum = -(closenum-1)
		}
		target = target+closenum
		tmp = isAns(nums, target, numsLen)
		if tmp{
			return target
		}
	}
}

func isAns(nums []int, target int, numsLen int)bool{
	for i:=0; i<numsLen-2; i++{
		if i>0 && nums[i]==nums[i-1]{
			continue
		}
		l, r := i+1, numsLen-1
		for l<r{
			value := nums[i] + nums[l] +nums[r]
			if value == target{
				return true
			}else if value<target{
				l ++
				for l<r && nums[l] == nums[l-1]{
					l++
				}
			}else{
				r --
				for l<r && nums[r] == nums[r+1]{
					r --
				}
			}
		}
	}
	return false
}