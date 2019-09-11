package main

import "fmt"

func main(){
	fmt.Println(findPairs([]int{1, 2, 3, 4, 5}, 1))
}

func findPairs(nums []int, k int) int {
	nummap := make(map[int]int)
	for _,value := range nums{
		mapvalue, ok := nummap[value]
		if (ok){
			nummap[value] = mapvalue+1
		}else{
			nummap[value] = 1
		}
	}

	res := 0
	for key := range nummap{
		_, ok := nummap[key+k]
		if (k==0 && nummap[key] > 1) || (k>0 && ok){
			res ++
		}
	}
	return res
}