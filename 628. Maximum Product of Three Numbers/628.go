package  main

import (
	"fmt"
	"sort"
)

func main(){
	fmt.Println(maximumProduct([]int{1,2,3}))
}

func maximumProduct(nums []int) int {
	maxint := int(^uint(0) >> 1)
	minint := ^maxint
	max1, max2, max3, min1, min2 := minint, minint, minint, maxint, maxint
	for _,value := range nums{
		if value > max1{
			max1, max2, max3 = value, max1, max2
		}else if value>max2{
			max2, max3 = value, max2
		}else if value>max3{
			max3 = value
		}else{

		}

		if value < min1{
			min1, min2 = value, min1
		}else if value < min2{
			min2 = value
		}else{

		}
	}

	if max1*max2*max3 > max1*min1*min2{
		return max1*max2*max3
	}
	return max1*min1*min2
}

// go的int最大值最小值
//maxint := int(^uint(0) >> 1)
//minint := ^maxint

//这个和python中用到的方法一样，这里导入了sort
func maximumProduct2(nums []int) int {
	sort.Ints(nums)
	lennums := len(nums)

	a := nums[0] * nums[1] * nums[lennums-1]
	b := nums[lennums-3] * nums[lennums-2] * nums[lennums-1]

	if a > b {
		return a
	}
	return b
}