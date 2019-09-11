package main

import (
	"fmt"
)

func main(){
	nums := []int{0,0,2,1,0,1,0,3,12,1,0}
	moveZeroes(nums)
	fmt.Println(nums)
}

func moveZeroes(nums []int)  {
    for i:=len(nums)-1; i>=0; i--{
		if nums[i] == 0{
			nums = append(nums[:i], nums[i+1:]...)
			nums = append(nums, 0)
		}
	}
}
/////////////////////////////////////////////////////////////////////////////////
// 下面这个方法还是很好的，没有复杂的内存操作（切片操作）
func moveZeroes2(nums []int) {
	if len(nums) == 0 {
		return
	}

	insertIndex := 0
	for _, e := range nums {
		if e != 0 {
			nums[insertIndex] = e
			insertIndex++
		}
	}

	for ; insertIndex < len(nums); insertIndex++ {
		nums[insertIndex] = 0
	}
}