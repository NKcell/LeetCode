package leetcode

func search(nums []int, target int) bool {
	l, r := 0, len(nums)-1
	
	for l<=r{
		mid := (l+r)/2
		if nums[mid] == target{
			return true
		}
		for l<mid && nums[l] == nums[mid]{
			l++
		}

		if nums[mid]>=nums[l]{
			if nums[l]<=target && nums[mid]>target{
				r = mid-1
			}else{
				l = mid+1
			}
		}else{
			if nums[mid] < target && target <= nums[r]{
				l = mid + 1
			}else{
				r = mid - 1
			}
		}
	}
	return false
}