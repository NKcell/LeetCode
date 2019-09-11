package main

import "fmt"

func main(){
	fmt.Println(minCostClimbingStairs([]int{1, 100}))
}

func minCostClimbingStairs(cost []int) int {
    for index:=2; index<len(cost); index++{
		if cost[index-1] > cost[index-2]{
			cost[index] = cost[index-2] + cost[index]
		}else{
			cost[index] = cost[index-1] + cost[index]
		}
	}
	if cost[len(cost)-1]<cost[len(cost)-2]{
		return cost[len(cost)-1]
	}
	return cost[len(cost)-2]
}