package main

import (
	"fmt"
)

func main(){
	fmt.Println(isMonotonic([]int{3,3,3}))
}

func isMonotonic(A []int) bool {
	flag := 0
	pre := A[0]
	for _,v := range A{
		if v>pre{
			if flag < 0{
				return false
			}
			flag = 1
		}
		if v < pre{
			if flag > 0{
				return false
			}
			flag = -1
		}
		pre = v
	}
	return true
}