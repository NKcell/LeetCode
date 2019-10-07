package leetcode

func searchRange(nums []int, target int) []int {
	l, r, goal := 0, len(nums)-1, -1
	for l<=r{
		mid := (l+r)/2
		if nums[mid] == target{
			goal = mid
			break
		}else if nums[mid]>target{
			r = mid-1
		}else{
			l = mid+1
		}
	}
	if goal == -1{
		return []int{-1, -1}
	}
	l, r = goal, goal

	for l>=0 && nums[l] == target{
		l--
	}
	for r<len(nums) && nums[r] == target{
		r++
	}

	return []int{l+1, r-1}
}