package leetcode

import (
	"sort"
)

func nextPermutation(nums []int)  {
	loc := -1
	for i:=len(nums)-1; i>0; i--{
		if nums[i] > nums[i-1]{
			loc = i-1
			break
		}
	}

	if loc == -1{
		sort.Ints(nums)
	}else{
		for i:=len(nums)-1; i>loc; i--{
			if nums[i] > nums[loc]{
				nums[i], nums[loc] = nums[loc], nums[i]
				break
			}
		}

		for i:=loc+1; i<len(nums)-1; i++{
			for j:=len(nums)-1; j>i; j--{
				if nums[j]<nums[j-1]{
					nums[j], nums[j-1] = nums[j-1], nums[j]
				}
			}
		} 
	}
}

// 这种采用反转的方法就比排序好很多
func nextPermutation1(nums []int)  {
	length := len(nums)
	// test if nums[i] < nums[i-1] true
	for i := length-2; i >= 0; i-- {
		if nums[i] < nums[i + 1] {
			// i < swapIndex < length && nums[swapIndex] > nums[i] && nearest
			swapIndex := i + 1
			for j := i+2; j < length; j++ {
				if nums[j] > nums[i] {
					swapIndex = j
				} else {
					break
				}
			}
			// swap nums[i], nums[swapIndex]
			nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
			// reverse nums[i+1:]
			for j := i+1; j < i+1+(length-i-1)/2; j++ {
				nums[j], nums[length-j+i] = nums[length-j+i], nums[j]
			}
			return
		}
	}
	// just reverse it
	for i := 0; i < length/2; i++ {
		nums[i], nums[length-1-i] = nums[length-1-i], nums[i]
	}
}