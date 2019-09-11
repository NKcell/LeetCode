package main

import(
	"fmt";
	"math";
	"sort"
)

func main(){
	fmt.Println(sortedSquares([]int{-7,-3,2,3,11}))
}

func sortedSquares(A []int) []int {
	l, r := 0, len(A)-1
	var B []int
	for l<=r{
		if math.Abs(float64(A[l]))>math.Abs(float64(A[r])){
			B = append([]int{A[l]*A[l]}, B...)
			l++
		} else{
			B = append([]int{A[r]*A[r]}, B...)
			r--
		}
	}
	return B
}

func sortedSquares1(A []int) []int {
    B := []int{}
    for _,v := range(A){
        B = append(B,v*v)
    }
    sort.Ints(B)
    return B
}