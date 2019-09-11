package main

import (
	"fmt"
)

func main(){
	fmt.Println(sumEvenAfterQueries([]int{1,2,3,4}, [][]int{{1,0},{-3,1},{-4,0},{2,3}}))
}

func sumEvenAfterQueries(A []int, queries [][]int) []int {
	var sum int
	for _, v := range A{
		if v%2 == 0{
			sum+=v
		}
	}

	var relist []int
	for _, v := range queries{
		if A[v[1]]%2 == 0{
			if v[0]%2 == 0{
				sum += v[0]
			}else{
				sum -= A[v[1]]
			}
			A[v[1]] += v[0]
		}else{
			A[v[1]] += v[0]
			if v[0]%2 != 0{
				sum += A[v[1]]
			}
		}
		relist = append(relist, sum)
	}

	return relist
}