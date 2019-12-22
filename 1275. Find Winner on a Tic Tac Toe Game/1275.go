package leetcode

func tictactoe(moves [][]int) string {
    if len(moves)<5{
		return "Pending"
	}

	res := make([][]int, 0, 3)
	for i:=0; i<3; i++{
		res = append(res, []int{0,0,0})
	}

	for i:=0; i<len(moves); i+=2{
		res[moves[i][0]][moves[i][1]] = 1
	}

	for i:=1; i<len(moves); i+=2{
		res[moves[i][0]][moves[i][1]] = -1
	}

	for i:=0; i<3; i++{
		if res[0][i]+res[1][i]+res[2][i] == 3 || res[i][0]+res[i][1]+res[i][2] == 3{
			return "A"
		}
		if res[0][i]+res[1][i]+res[2][i] == -3 || res[i][0]+res[i][1]+res[i][2] == -3{
			return "B"
		}
	}

	if res[0][0]+res[1][1]+res[2][2] == 3 || res[0][2]+res[1][1]+res[2][0] == 3{
		return "A"
	}
	if res[0][0]+res[1][1]+res[2][2] == -3 || res[0][2]+res[1][1]+res[2][0] == -3{
		return "B"
	}

	if len(moves) == 9{
		return "Draw"
	}
	return "Pending"
}