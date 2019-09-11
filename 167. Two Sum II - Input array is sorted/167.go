package main

import "fmt"

func main(){
	fmt.Println(twoSum([]int{1,4,7,13}, 17))
}

func twoSum(numbers []int, target int) []int {
	pre := 0
	fin := len(numbers)-1
	for{
		if numbers[pre]+numbers[fin]==target{
			return []int{pre+1, fin+1}
		}else if numbers[pre]+numbers[fin]<target{
			pre ++
		}else{
			fin --
		}
	}
}