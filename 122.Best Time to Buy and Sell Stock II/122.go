package main

import "fmt"

func main(){
	fmt.Println(maxProfit([]int{7,6,4,3,1}))
}

func maxProfit(prices []int) int {
    if len(prices) < 2{
		return 0
	}
	start := prices[0]
	profit := 0
	for _,value := range prices{
		if value>start{
			profit += (value-start)
		}
		start = value
	}
	return profit
}

func maxProfit2(prices []int) int {

	var ret int
	
	for i := 1; i < len(prices); i++ {
		if(prices[i] > prices[i-1]) {
			ret += prices[i] - prices[i-1]
		}
	}
	
	return ret
	}