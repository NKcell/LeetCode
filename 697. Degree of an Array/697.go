package main

import "fmt"

func main(){
	fmt.Println(findShortestSubArray([]int{1,2,3,4,2,1}))
}

func findShortestSubArray(nums []int) int {
	count := make(map[int]int)
	start_index := make(map[int]int)
	degree, res := 0, len(nums)
	for index,value := range nums{
		_, ok := start_index[value]
		if !ok{
			start_index[value] = index
		}
		count_value, count_ok := count[value]
		if count_ok{
			count[value] = count_value+1
		}else{
			count[value] = 1
		}
		if degree<count[value]{
			degree = count[value]
			res = index - start_index[value]+1
		}
		if degree == count[value]{
			tmp := index - start_index[value]+1
			if res > tmp{
				res = tmp
			}
		}
	}
	return res
}