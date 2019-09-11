package main

import "fmt"

func main(){
	fmt.Println(containsNearbyDuplicate([]int{1,2,3,1,2,3}, 2))
}

func containsNearbyDuplicate(nums []int, k int) bool {
	dict_map := make(map[int]int)
    for index,value := range nums{
		last_index, ok := dict_map[value]
		if ok{
			if index-last_index<=k{
				return true
			}
		}
		dict_map[value] = index
	}
	return false
}

//这个if语句写法写的好
func containsNearbyDuplicate1(nums []int, k int) bool {
    exist := make(map[int]int, len(nums))
    for i, v := range nums{
        if pos, ok := exist[v]; ok && i - pos <= k{
            return true
        }
        exist[v] = i
    }
    return false
}