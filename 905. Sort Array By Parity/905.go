package main

import (
	"fmt"
)

func main(){
	fmt.Println(sortArrayByParity([]int{1,2,3,4}))
}

func sortArrayByParity(A []int) []int {
	var oddlist []int
	for i, v := range A{
		if v%2 != 0{
			oddlist = append(oddlist, i)
		}else{
			if len(oddlist) != 0{
				A[oddlist[0]], A[i] = v, A[oddlist[0]]
				oddlist = oddlist[1:]
				oddlist = append(oddlist, i)
			}
		}
	}
	return A
}