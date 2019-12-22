package leetcode

func minPathSum(grid [][]int) int {
    if len(grid[0]) == 0{
		return 0
	}

	for i:=1;i<len(grid);i++{
		grid[i][0] += grid[i-1][0]
	}
	for i:=1;i<len(grid[0]);i++{
		grid[0][i] += grid[0][i-1]
	}

	for i:=1;i<len(grid);i++{
		for j:=1;j<len(grid[0]);j++{
			var tmp int
			if grid[i-1][j]<grid[i][j-1]{
				tmp = grid[i-1][j]
			}else{
				tmp = grid[i][j-1]
			}

			grid[i][j] += tmp
		}
	}
	return grid[len(grid)-1][len(grid[0])-1]
}