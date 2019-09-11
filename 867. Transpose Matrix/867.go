package main

import (
	"fmt"
)

func main(){
	fmt.Println(transpose([][]int{{1,2,3},{4,5,6}}))
}

func transpose(A [][]int) [][]int {
	var B [][]int
    for collength:=0; collength<len(A[0]); collength++{
		var tmplist []int
		for rowlength:=0; rowlength<len(A); rowlength++{
			tmplist = append(tmplist, A[rowlength][collength])
		}
		B = append(B, tmplist)
	}
	return B
}