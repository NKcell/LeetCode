package main

import "fmt"

func main(){
	fmt.Println(pivotIndex([]int{1,1,-1,0,-1}))
}

func pivotIndex(nums []int) int {
	total := 0
    for _, value := range nums{
		total += value
	}
	left := 0
	for index, value := range nums{
		if total-value == left*2{
			return index
		}
		left += value
	}
	return -1
}