package leetcode

import(
	//"fmt"
)

func shiftGrid(grid [][]int, k int) [][]int {
	res := make([]int,0 ,len(grid)*len(grid[0]))
	
	k = k%(len(grid)*len(grid[0]))

	for i:=0; i<len(grid); i++{
		for j:=0; j<len(grid[0]); j++{
			res = append(res, grid[i][j])
		}
	}

	s := make([][]int, len(grid))
    for i := 0; i < len(grid); i++ {
        s[i] = make([]int, len(grid[0]))
	}

	res1 := make([]int, len(grid)*len(grid[0]))
	for i, v := range res[len(res)-k:len(res)]{
		res1[i] = v
	}

	for i,v := range res[:len(res)-k]{
		res1[i+k] = v
	}

	for i:=0; i<len(grid); i++{
		//fmt.Println(s)
		for j:=0; j<len(grid[0]); j++{
			s[i][j] = res1[i*len(grid[0])+j]
		}
	}

	return s
}