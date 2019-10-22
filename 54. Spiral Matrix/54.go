package leetcode

func spiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 || len(matrix[0]) == 0{
        return []int{}
	}
	
	res := make([]int, 0, len(matrix)*len(matrix[0]))

	for len(matrix) != 0 && len(matrix[0]) != 0{
		for _,v := range matrix[0]{
			res = append(res, v)
		}
		if len(matrix) == 0 || len(matrix[0]) == 0{
			break
		}
		matrix = matrix[1:]

		tmp := make([][]int, 0, len(matrix))
		for _,v := range matrix{
			res = append(res, v[len(matrix[0])-1])
			tmp = append(tmp, v[:len(matrix[0])-1])
		}
		if len(matrix) == 0 || len(matrix[0]) == 0{
			break
		}
		matrix = tmp

		for i:=len(matrix[0])-1; i>-1; i--{
			res = append(res, matrix[len(matrix)-1][i])
		}
		if len(matrix) == 0 || len(matrix[0]) == 0{
			break
		}
		matrix = matrix[:len(matrix)-1]

		
		for i:=len(matrix)-1; i>-1; i--{
			res = append(res, matrix[i][0])
		}
		if len(matrix) == 0 || len(matrix[0]) == 0{
			break
		}
		tmp1 := make([][]int, 0, len(matrix))
		for _,v := range matrix{
			tmp1 = append(tmp1, v[1:])
		}
		matrix = tmp1
	}
	
	return res
}

func spiralOrder1(matrix [][]int) []int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return []int{}
	}

	// right->down->left->up->right
	up, down, left, right := 0, len(matrix)-1, 0, len(matrix[0])-1
	i, j := 0, 0
	move := 0
	ret := make([]int, 0)
	processLoop:
	for {
		ret = append(ret, matrix[i][j])
		switch move%4 {
		case 0: // →
			if j == right {
				if i < down {
					i++
					move++
					up++
					continue processLoop
				} else {
					break processLoop
				}
			}
			j++

		case 1: // ↓
			if i == down {
				if j > left {
					j--
					move++
					right--
					continue processLoop
				} else {
					break processLoop
				}
			}
			i++

		case 2: // ←
			if j == left {
				if i > up {
					i--
					move++
					down--
					continue processLoop
				} else {
					break processLoop
				}
			}
			j--

		case 3: // ↑
			if i == up {
				if j < right {
					j++
					move++
					left++
					continue processLoop
				} else {
					break processLoop
				}
			}
			i--
		}
	}
	return ret
}