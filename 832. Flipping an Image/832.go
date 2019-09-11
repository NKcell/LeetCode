package  main

import "fmt"

func main(){
	fmt.Println(flipAndInvertImage([][]int{{1,1,0,0},{1,0,0,1},{0,1,1,1},{1,0,1,0}}))
}

func flipAndInvertImage(A [][]int) [][]int {
    for index, value := range A{
		A[index] = reverse(value)
	}
	for i:=0; i<len(A); i++{
		for j:=0; j<len(A[0]); j++{
			A[i][j] = (A[i][j]+1)%2
		}
	}
	return A
}

func reverse(value []int) []int{
	for i:=0; i<len(value)-1-i; i++{
		value[i], value[len(value)-1-i] = value[len(value)-1-i], value[i]
	}
	return value
}