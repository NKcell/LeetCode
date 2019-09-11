package main

import "fmt"

func main(){
	fmt.Println(missingNumber1([]int{9,6,4,2,3,5,7,0,1}))
}

func missingNumber(nums []int) int {
	var sum1,sum2 int
	for index,value := range nums{
		sum1 += value
		sum2 += index
	}
	return sum2-sum1+len(nums)
}

func missingNumber1(nums []int) int {
	var sum int
	for index,value := range nums{
		sum ^= value
		sum ^= index
	}
	return sum ^ len(nums)
}