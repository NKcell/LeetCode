package main

import (
	"fmt"
)

func main(){
	fmt.Println(checkPossibility([]int{2,3,3,2,4}))
}

func checkPossibility(nums []int) bool {
	count := 0
    for i:=0; i<len(nums)-1; i++{
		if nums[i]>nums[i+1]{
			count++
			if i != 0{
				if nums[i+1]<nums[i-1]{
					nums[i+1] = nums[i]
				}
			}
		}

		if count>1{
			return false
		}
	}
	return true
}