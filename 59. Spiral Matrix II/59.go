package leetcode

import(
	"fmt"
)

func generateMatrix(n int) [][]int {
	res := make([][]int, n)
	for i := range res{
		res[i] = make([]int, n)
	}

	myLen := n
	flag := 0
	x, y := 0, 0

	for i:=y; i<y+myLen; i++{
		flag ++
		res[x][i] = flag
	}
	myLen --
	y = myLen

	for myLen>0{
		for i:=x+1; i<x+1+myLen; i++{
			flag ++
			res[i][y] = flag
		}
		x = x+myLen

		fmt.Println(res)

		for i:=y-1; i>y-1-myLen; i--{
			flag ++
			res[x][i] = flag
		}
		y = y-myLen
		myLen --

		fmt.Println(res)

		if myLen<=0{
			break
		}

		for i:=x-1; i>x-1-myLen; i--{
			flag ++
			res[i][y] = flag
		}
		x = x-myLen

		

		for i:=y+1; i<y+1+myLen; i++{
			fmt.Println(x, i)
			flag ++
			res[x][i] = flag
		}
		y = y+myLen
		myLen --

		fmt.Println(res)
	}

	return res
}