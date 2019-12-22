package leetcode

func maxAreaOfIsland(grid [][]int) int {
	max := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				tmp := getarea(&grid, i, j)
				if tmp > max {
					max = tmp
				}
			}
		}
	}
	return max
}

func getarea(grid *[][]int, i, j int) int {
	if (i >= 0 && i < len(*grid)) && (j >= 0 && j < len((*grid)[0])) && (*grid)[i][j] == 1 {
		(*grid)[i][j] = 0
		return 1 + getarea(grid, i-1, j) + getarea(grid, i+1, j) + getarea(grid, i, j-1) + getarea(grid, i, j+1)
	}
	return 0
}
