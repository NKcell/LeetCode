package leetcode

func rotate(matrix [][]int)  {
	myLen := len(matrix)-1
	endLen := len(matrix)-1
	flag := len(matrix)
	start := 0

	for flag>1{
		for i:=start; i<endLen; i++{
			x := start
			y := i
			tmp := matrix[x][y]
			for j:=0; j<4; j++{
				now := matrix[y][myLen-x]
				matrix[y][myLen-x] = tmp
				tmp = now
				x, y = y, myLen-x
			}
		}
		start ++
		flag -= 2
		endLen --
	}
}