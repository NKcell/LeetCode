package leetcode

func countServers(grid [][]int) int {
	col := make([]int, len(grid))
	row := make([]int, len(grid[0]))

	for i:=0; i<len(grid); i++{
		count := 0
		for j:=0; j<len(grid[0]); j++{
			if grid[i][j] == 1{
				count++
			}
		}
		if count>1{
			col[i] = 1
		}
	}

	for i:=0; i<len(grid[0]); i++{
		count := 0
		for j:=0; j<len(grid); j++{
			if grid[j][i] == 1{
				count++
			}
		}
		if count>1{
			row[i] = 1
		}
	}

	count := 0
	for i:=0; i<len(grid); i++{
		for j:=0; j<len(grid[0]); j++{
			if grid[i][j] == 1{
				if col[i] == 1 || row[j] == 1{
					count++
				}
			}
		}
	}
	return count
}