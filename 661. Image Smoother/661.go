package  main

import(
	"fmt"
)

func imageSmoother(M [][]int) [][]int {
	row := len(M[0])
	col := len(M)
	revalue := make([][]int, col)
	for i:=0; i<col ;i++{
		revalue[i] = make([]int, row)
	}

	for i:=0; i<col; i++{
		for j:=0; j<row; j++{
			tmp := 0
			count := 0
			for a:=-1; a<2; a++{
				for b:=-1; b<2; b++{
					if (i+a)<col && (i+a)>=0 && (j+b)>=0 && (j+b)<row{
						tmp += M[i+a][j+b]
						count++
					} 
				}
			}
			revalue[i][j] = tmp / count
		}
	}
	return revalue
}

func main(){
	t := [][]int{{2,3,4},{5,6,7},{8,9,10},{11,12,13},{14,15,16},}
	fmt.Println(imageSmoother(t))
}

/*
	数组初始化，里面只能是数字，不能是变量， x := [n]int这里是会报错的
	二维切片的初始化：
	revalue := make([][]int, col)
	for i:=0; i<col ;i++{
		revalue[i] = make([]int, row)
	}
*/