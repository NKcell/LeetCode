package main

import (
	"fmt";
	"strconv";
	"strings"
)

func main(){
	fmt.Println(numMagicSquaresInside([][]int{{4,3,8,4},{9,5,1,9},{2,7,6,2}}))
}

func numMagicSquaresInside(grid [][]int) int {
	var count int
	var str1 = "43816729" + "43816729"
	var str2 = "92761834" + "92761834"
    for i:=1; i<len(grid)-1; i++{
		for j:=1; j<len(grid[0])-1; j++{
			if grid[i][j] == 5{
				tmpstr := strconv.Itoa(grid[i-1][j-1])+strconv.Itoa(grid[i-1][j])+strconv.Itoa(grid[i-1][j+1])+strconv.Itoa(grid[i][j+1])+strconv.Itoa(grid[i+1][j+1])+strconv.Itoa(grid[i+1][j])+strconv.Itoa(grid[i+1][j-1])+strconv.Itoa(grid[i][j-1])
				if strings.Index(str1, tmpstr) != -1 || strings.Index(str2, tmpstr) != -1{
					count ++
				}
			}
		}
	}
	return count
}