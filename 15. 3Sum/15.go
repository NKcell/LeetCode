package leetcode

import(
	"sort"
)

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	numsLen := len(nums)
	myAns := make([][]int,0)
	for i:=0; i<numsLen-2; i++{
		if nums[i]>0{
			break
		}
		if i>0 && nums[i] == nums[i-1]{
			continue
		}

		l, r := i+1, numsLen-1
		for l<r{
			value := nums[i] + nums[l] + nums[r]
			if value > 0{
				r --
				for l<r && nums[r] == nums[r+1]{
					r --
				}
			}else if value < 0{
				l ++
				for l<r && nums[l] == nums[l-1]{
					l++
				}
			}else{
				myAns = append(myAns, []int{nums[i], nums[l], nums[r]})
				r --
				l ++
				for l<r && nums[r] == nums[r+1]{
					r --
				}
				for l<r && nums[l] == nums[l-1]{
					l++
				}
			}
		}
	}
	return myAns
}