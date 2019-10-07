package leetcode

import (
	"sort"
)

func findLHS(nums []int) int {
	myDict := make(map[int]int, 0)
	for _, v := range nums{
		myDict[v]++
	}
	sort.Ints(nums)
	maxvalue := 0
	for i:=0; i<len(nums); {
		// 这里其实可以可以不用length，直接走下面的与1相等的判断就好了
		length, ok := myDict[nums[i]]
		if !ok{
			break
		}
		i += length
		if i<len(nums){
			if nums[i]-nums[i-length] == 1{
				tmp := myDict[nums[i]] + myDict[nums[i-length]]
				if maxvalue < tmp{
					maxvalue = tmp
				}
			}
		}	
	}
	return maxvalue
}

// 其实这样简单的利用hashmap去查找，效率是很高的，没必要向上面哪像
func findLHS1(nums []int) int {
    res := 0
	tmp := make(map[int]int) 
	for _, v := range nums {
		tmp[v]++
	}
    for i, v := range tmp {
        if c, ok := tmp[i+1]; ok {
            if v + c > res {
                res = v + c
            } 
        }
    }
	return res
}