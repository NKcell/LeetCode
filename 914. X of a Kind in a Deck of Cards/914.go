package main

import (
	"fmt"
)

func main(){
	fmt.Println(hasGroupsSizeX([]int{1,1,1,2,2,2,3,3}))
}

func hasGroupsSizeX(deck []int) bool {
	mymap := make(map[int]int)
	for _,v := range deck{
		value,ok := mymap[v]
		if !ok{
			mymap[v] = 1
		}else{
			mymap[v] = value+1
		}
	}
	
	var count []int
	for i := range mymap{
		count = append(count, mymap[i])
	}
	
	gcdvalue := count[0]
	for _,v := range count{
		gcdvalue = gcd(gcdvalue, v)
		if gcdvalue == 1{
			return false
		}
	}
	return true
}

func gcd(a,b int)int{
	for a!=0{
		a,b = b%a, a
	}
	return b
}