package  main

import (
	"fmt"
	"sort"
)

func majorityElement(nums []int) int {
	mymap := make(map[int]int)
	flag := len(nums)/2

	for _,value := range nums{
		count,ok := mymap[value]
		if !(ok){
			count = 0
		}
		count++
		if count > flag{
			return value
		}
		mymap[value] = count
	}
	return 0
}

func majorityElement1(nums []int) int{
	sort.Ints(nums)
	return nums[len(nums)/2]
}

//============================================================================

func majorityElement2(nums []int) int {
    m := make(map[int]int)
	for _, v := range nums {
		m[v]++
		if m[v] > len(nums) / 2 {
			return v
		}
	}
	return 0
}


func main(){
	a := []int{2,2,1,1,1,2,2}
	fmt.Println(majorityElement(a))
}

/*
这里主要可以看到go map的使用
对于不存在的键，会使用默认值，int类型就默认为0, 这样使用++操作是可以的
value,ok = map[i]  i不存在ok为false，存在为true

切片可以导入sort包来进行排序操作
*/