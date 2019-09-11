package main

import "fmt"

func main(){
	fmt.Println(findLengthOfLCIS([]int{1,1,1,1,1}))
}

func findLengthOfLCIS(nums []int) int {
	max_incerasing_length, tmp_max := 0, 1
	if len(nums) == 0{
		return max_incerasing_length
	}
	for i:=0; i<len(nums)-1; i++{
		if nums[i] < nums[i+1]{
			tmp_max ++
		}else{
			if max_incerasing_length<tmp_max{
				max_incerasing_length = tmp_max
			}
			tmp_max = 1
		}
	}
	if max_incerasing_length<tmp_max{
		max_incerasing_length = tmp_max
	}
	return max_incerasing_length
}