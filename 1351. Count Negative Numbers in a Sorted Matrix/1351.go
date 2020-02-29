package leetcode

func countNegatives(grid [][]int) int {
    myLen := len(grid[0])
	count := 0
	for _,v := range grid{
		for index, value := range v{
			if value<0{
				count += (myLen-index)
                break
			}
		}
	}
	return count
}