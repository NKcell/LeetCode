package leetcode

func setZeroes(matrix [][]int)  {
	row := make([]int, 0)
	col := make([]int, 0)

	for colindex,v := range matrix{
		for rowindex, value := range v{
			if value == 0{
				col = append(col, colindex)
				row = append(row, rowindex)
			}
		}
	}

	for _,v := range row{
		for i:=0; i<len(matrix); i++{
			matrix[i][v] = 0
		}
	}
	for _,v := range col{
		for i:=0; i<len(matrix[0]); i++{
			matrix[v][i] = 0
		}
	}
}