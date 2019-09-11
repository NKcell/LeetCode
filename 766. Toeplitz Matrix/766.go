package main

import "fmt"

func main(){
	fmt.Println(isToeplitzMatrix([][]int{{1,2,3,4},{5,1,2,3},{9,5,1,2}}))
}

func isToeplitzMatrix(matrix [][]int) bool {
	mymap := make(map[int]int)
	for index_row, col := range matrix{
		for index_col, value := range col{
			getvalue,ok := mymap[index_row-index_col]
			if ok{
				if getvalue != value{
					return false
				}
			}else{
				mymap[index_row-index_col] = value
			}
		}
	}
	return true
}