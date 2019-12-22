package leetcode

func dominantIndex(nums []int) int {
    if len(nums)<2{
		return 0
	}

	var(
		b int
		a int
		index int
	)
	if nums[0]<nums[1]{
		a = nums[0]
		b = nums[1]
		index = 1
	}else{
		a = nums[1]
		b = nums[0]
		index = 0
	}

	for i:=2; i<len(nums); i++{
		if nums[i]>b{
			a, b = b, nums[i]
			index = i
		}else if nums[i]>a{
			a = nums[i]
		}
	}

	if b >= 2*a{
		return index
	}
	return -1
}