package leetcode

func islandPerimeter(grid [][]int) int {
	res := 0
	for col, v1 := range grid{
		for row, v := range v1{
			if v == 1{
				if col == 0 || grid[col-1][row] == 0{
					res++
				}
				if col == len(grid)-1 || grid[col+1][row] == 0{
					res++
				}
				if row == 0 || grid[col][row-1] == 0{
					res++
				}
				if row == len(grid[0])-1 || grid[col][row+1] == 0{
					res++
				}
			}
		}
	}
	return res
}