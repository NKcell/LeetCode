package main

import "fmt"

func main(){
	fmt.Println(maxProfit([]int{7,6,4,3,1}))
}

func maxProfit(prices []int) int {
    if len(prices) == 0{
		return 0
	}
	minprice := prices[0]
	maxvalue := 0

	for _,value := range prices{
		if minprice>value{
			minprice = value
		}else{
			if value-minprice > maxvalue{
				maxvalue = value-minprice
			}
		}
	}
	return maxvalue
}

