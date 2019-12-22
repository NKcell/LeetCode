package leetcode

func oddCells(n int, m int, indices [][]int) int {
	col := make([]int, n)
	row := make([]int, m)

	for _,v := range indices{
		col[v[0]]++
		row[v[1]]++
	}

	res := 0
	for i:=0; i<n; i++{
		for j:=0; j<m; j++{
			if (col[i]+row[j])%2 == 1{
				res ++
			}
		}
	}
	return res
}