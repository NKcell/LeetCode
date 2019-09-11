package main

import (
	"fmt"
)

func main(){
	fmt.Println(validMountainArray([]int{1,3, 5}))
}

func validMountainArray(A []int) bool {
	if len(A)<3 || A[0]>A[1]{
		return false
	}
	flag := 1
	start := A[0]
	for i:=1; i<len(A); i++{
		if A[i] == start{
			return false
		}
		if A[i]<start && flag == 1{
			flag = 2
		}
		if A[i]>start && flag == 2{
			return false
		}
		start = A[i]
	}
	if flag == 2{
		return true
	}
	return false
}